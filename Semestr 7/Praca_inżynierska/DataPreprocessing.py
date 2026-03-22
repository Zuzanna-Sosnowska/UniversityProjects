import warnings

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer, KNNImputer
import geopandas as gpd


def smart_imputer(
        df: pd.DataFrame,
        numeric_cols:list=None,
        categorical_cols:list=None
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Imputes missing values in a DataFrame using different strategies based on the percentage of missing data:
    - For numeric columns:
        - <5% missing: drop rows with missing values
        - 5%-20% missing: median imputation
        - 20%-40% missing: KNN imputation
        - >40% missing: skip imputation and issue a warning
    - For categorical columns:
        - <5% missing: drop rows with missing values
        - 5%-40% missing: mode imputation
        - >40% missing: skip imputation and issue a warning
    Generates a report of the imputation methods used for each column.
    :param df: DataFrame to be imputed
    :param numeric_cols: Numeric columns to consider for imputation. If None, all numeric columns will be used.
    :param categorical_cols: Categorical columns to consider for imputation. If None, all non-numeric columns will be used.
    :return: DataFrame with imputed values and a report DataFrame.
    """

    df = df.copy()

    if numeric_cols is None:
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if categorical_cols is None:
        categorical_cols = df.select_dtypes(exclude=[np.number]).columns.tolist()

    report = []

    def median_imput(dataframe, column):
        imputer = SimpleImputer(strategy="median")
        dataframe[column] = imputer.fit_transform(dataframe[[column]]).ravel()
        return "median"

    def mode_imput(dataframe, column):
        imputer = SimpleImputer(strategy="most_frequent")
        dataframe[column] = imputer.fit_transform(dataframe[[column]]).ravel()
        return "mode"

    def knn_imput(dataframe, col_list):
        imputer = KNNImputer(n_neighbors=5)
        dataframe[col_list] = imputer.fit_transform(dataframe[col_list])
        return "knn"

    knn_candidates = []

    columns_to_drop = []

    missing_values = {column: df[column].isna().mean() for column in numeric_cols}

    for column, missing in missing_values.items():

        if missing == 0:
            method = "none"

        elif missing < 0.05:
            columns_to_drop.append(column)
            method = "drop"

        elif missing < 0.20:
            method = median_imput(df, column)

        elif missing < 0.40:
            knn_candidates.append(column)
            method = "knn (queued)"

        else:
            warnings.warn(f'Kolumna "{column}" ma >40% braków → NIE imputuję.')
            method = "skipped"

        report.append([column, "numeric", missing, method])

    if len(knn_candidates) >= 1:
        knn_imput(df, knn_candidates)
        for r in report:
            if r[0] in knn_candidates:
                r[3] = "knn"

    missing_values = {column: df[column].isna().mean() for column in categorical_cols}

    for column, missing in missing_values.items():

        if missing == 0:
            method = "none"

        elif missing < 0.05:
            columns_to_drop.append(column)
            method = "drop"

        elif missing < 0.40:
            method = mode_imput(df, column)

        else:
            warnings.warn(f'Kolumna "{column}" (kategoryczna) ma >40% braków → pomijam.')
            method = "skipped"

        report.append([column, "categorical", missing, method])

    df = df.dropna(subset=columns_to_drop)
    report_df = pd.DataFrame(report,
                             columns=["column", "type", "missing_ratio", "method"])

    return df, report_df


def df_aggregating(
        df: pd.DataFrame,
        grouped_by: list[str],
        aggregation: dict[str, str]
) -> gpd.GeoDataFrame:
    """
    Aggregates a DataFrame by specified columns and aggregation methods, then converts it to a GeoDataFrame with a specified CRS.
    :param df: DataFrame to be aggregated
    :param grouped_by: list of columns to group by
    :param aggregation: dictionary specifying aggregation methods for each column
    :return: GeoDataFrame with aggregated data and specified CRS
    """
    gdf_aggregated = df.groupby(grouped_by).agg(aggregation).reset_index()
    gdf_aggregated = gpd.GeoDataFrame(
        gdf_aggregated,
        geometry=gpd.points_from_xy(x=gdf_aggregated['longitude'], y=gdf_aggregated['latitude']),
        crs="EPSG:4326"
    )
    gdf_aggregated = gdf_aggregated.to_crs("EPSG:2180")
    return gdf_aggregated


def smart_jitter(
        df,
        x_col='x',
        y_col='y',
        scale=1.0,
        max_attempts=10
) -> gpd.GeoDataFrame:
    """
    Applies jitter to duplicate geographic points in a GeoDataFrame to ensure uniqueness.
    :param df: DataFrame or GeoDataFrame containing geographic points
    :param x_col: Name of the column representing x-coordinates
    :param y_col: Name of the column representing y-coordinates
    :param scale: Standard deviation of the normal distribution used for jitter
    :param max_attempts: Maximum number of attempts to resolve duplicates
    :return: GeoDataFrame with unique geographic points
    """
    df = gpd.GeoDataFrame(
        df,
        geometry=gpd.points_from_xy(x=df['longitude'], y=df['latitude']),
        crs="EPSG:4326"
    )

    df = df.to_crs("EPSG:2180")  # Transformacja do układu w metrach

    if 'geometry' in df.columns:
        df[x_col] = df.geometry.x
        df[y_col] = df.geometry.y

    for attempt in range(max_attempts):
        duplicates_mask = df.duplicated(subset=[x_col, y_col], keep=False)

        n_dupes = duplicates_mask.sum()

        if n_dupes == 0:
            break

        noise_x = np.random.normal(0, scale, size=n_dupes)
        noise_y = np.random.normal(0, scale, size=n_dupes)

        df.loc[duplicates_mask, x_col] += noise_x
        df.loc[duplicates_mask, y_col] += noise_y

    else:
        print("Ostrzeżenie: Nie udało się rozwiązać wszystkich kolizji w zadanej liczbie prób.")

    if 'geometry' in df.columns:
        df['geometry'] = gpd.points_from_xy(df[x_col], df[y_col])

    return df
