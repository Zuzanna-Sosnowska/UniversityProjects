import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import pearsonr, spearmanr
import scipy.stats as stats
import seaborn as sns


polish_labels = {
    'city': 'Miasto',
    'type': 'Typ nieruchomości',
    'ownership': 'Forma własności',
    'buildingMaterial': 'Materiał budynku',
    'condition': 'Stan wykończenia',
    'hasParkingSpace': 'Miejsce parkingowe',
    'hasBalcony': 'Balkon',
    'hasElevator': 'Winda',
    'hasSecurity': 'Ochrona',
    'hasStorageRoom': 'Komórka lokatorska',

    'rooms': 'Liczba pokoi',
    'floor': 'Piętro',
    'floorCount': 'Liczba pięter budynku',

    'squareMeters': 'Powierzchnia (m²)',
    'buildYear': 'Rok budowy',
    'latitude': 'Szerokość geograficzna',
    'longitude': 'Długość geograficzna',
    'centreDistance': 'Odległość od centrum (km)',
    'poiCount': 'Liczba punktów POI',
    'schoolDistance': 'Odległość do szkoły (km)',
    'clinicDistance': 'Odległość do szpitala (km)',
    'postOfficeDistance': 'Odległość do poczty (km)',
    'kindergartenDistance': 'Odległość do przedszkola (km)',
    'restaurantDistance': 'Odległość do restauracji (km)',
    'collegeDistance': 'Odległość do uczelni (km)',
    'pharmacyDistance': 'Odległość do apteki (km)',
    'price': 'Cena',
    'price_per_m2': 'Cena za m²'
}

column_names_in_polish = {'id': 'Id', 'city': 'Miasto', 'type': 'Rodzaj mieszkania', 'squareMeters': r'Powierzchnia w m²',
                          'rooms': 'Liczba pokoi', 'floor': 'Piętro', 'floorCount': 'Liczba pięter w budynku',
                          'buildYear': 'Rok budowy', 'latitude': 'Szerokość geograficzna', 'longitude': 'Długość geograficzna',
                          'centreDistance': 'Odległość od centrum w km', 'poiCount': 'Liczba "Points Of Interest"',
                          'schoolDistance': 'Odległość do szkoły w km', 'clinicDistance': 'Odległość do przychodni w km',
                          'postOfficeDistance': 'Odległość do poczty w km', 'kindergartenDistance': 'Odległość do przedszkola w km',
                        'restaurantDistance': 'Odległość do restauracji w km', 'collegeDistance': 'Odległość do uczelni w km',
                        'pharmacyDistance': 'Odległość do apteki w km', 'ownership': 'Forma własności', 'buildingMaterial': 'Materiał budynku',
                        'condition': 'Stan mieszkania', 'hasParkingSpace': 'Miejsce parkingowe', 'hasBalcony': 'Balkon',
                        'hasElevator': 'Winda', 'hasSecurity': 'Ochrona', 'hasStorageRoom': 'Komórka lokatorska', 'price': 'Cena mieszkania',
                        'price_per_m2': 'Cena za m²'}


def generate_correlation_heatmap(
        df,
        numeric_cols=None,
        method: str = 'spearman'
):
    if numeric_cols is None:
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

    matrix = df[numeric_cols].corr(method=method)

    plt.figure(figsize=(12, 9))
    ax = sns.heatmap(matrix, annot=True, fmt=".2f", linewidths=0.5, cmap='YlGnBu')

    ax.set_xticklabels([polish_labels.get(col, col) for col in matrix.columns],
                       rotation=90)
    ax.set_yticklabels([polish_labels.get(col, col) for col in matrix.columns],
                       rotation=0)

    plt.title("Macierz korelacji", size=16, pad=12)
    plt.show()


def corr_test(
        df: pd.DataFrame,
        column_list: list,
        column
) -> pd.DataFrame:
    data  = {
    ('Pearson', 'statystyka'): [],
    ('Pearson', 'p-wartość'):  [],
    ('Spearman', 'statystyka'): [],
    ('Spearman', 'p-wartość'):  []
    }
    percent_of_missing_values = df.isna().sum() / df.shape[0]
    for col in column_list:
        if percent_of_missing_values[col] < 0.4:
            corr, p_value = pearsonr(df[column], df[col])
            data[('Pearson', 'statystyka')].append(corr)
            data[('Pearson', 'p-wartość')].append(p_value)
            corr, p_value = spearmanr(df[column], df[col])
            data[('Spearman', 'statystyka')].append(corr)
            data[('Spearman', 'p-wartość')].append(p_value)
        else:
            continue
    output_df = pd.DataFrame(data, index=column_list)
    return output_df


def joint_distribution(
    df,
    labels,
    target="price_per_m2",
    distributions=None,
    cdf=True,
    return_info=False
):
    if distributions is None:
        distributions = {'lognorm': stats.lognorm, 'gamma': stats.gamma, 'chi2': stats.chi2, 't': stats.t,
                         'norm': stats.norm}
    total_size = len(df)
    components = []
    info = {}

    for label in labels.unique():
        sub_df = df[labels == label]
        data = sub_df[target].dropna().values

        best_dist = None
        best_params = None
        best_pvalue = -np.inf
        best_name = None

        for name, dist in distributions.items():
            try:
                params = dist.fit(data)
                _, p_value = stats.kstest(data, dist.cdf, args=params)

                if p_value > best_pvalue:
                    best_pvalue = p_value
                    best_dist = dist
                    best_params = params
                    best_name = name

            except Exception as e:
                print(f'Błąd dla rozkładu {name}: {e}')

        weight = len(data) / total_size
        components.append((best_dist, best_params, weight))

        info[label] = {
            'distribution': best_name,
            'params': best_params,
            'p_value': best_pvalue,
            'weight': weight,
            'n_obs': len(data)
        }

    mixture = (
        (lambda x: sum(w * d.cdf(x, *p) for d, p, w in components))
        if cdf else
        (lambda x: sum(w * d.pdf(x, *p) for d, p, w in components))
    )

    if return_info:
        return mixture, info

    return mixture