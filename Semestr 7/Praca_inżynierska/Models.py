import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, RegressorMixin
from sklearn.model_selection import KFold, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, root_mean_squared_error
from mgwr.gwr import GWR
from mgwr.sel_bw import Sel_BW
import tensorflow as tf


class SklearnGWR(BaseEstimator, RegressorMixin):
    """
    A scikit-learn compatible wrapper for Geographically Weighted Regression (GWR) using the mgwr library.
    """
    def __init__(self, bw=None, fixed=False, kernel='bisquare'):
        self.bw = bw
        self.fixed = fixed
        self.kernel = kernel
        self.model_ = None
        self.results_ = None
        self.coords_ = None

    def fit(self, X, y):

        X_vars = X[:, :-2]
        self.coords_ = X[:, -2:]

        y = y.reshape(-1, 1)

        current_bw = self.bw
        if current_bw is None:
            selector = Sel_BW(self.coords_, y, X_vars, fixed=self.fixed, kernel=self.kernel)
            current_bw = selector.search()

        self.model_ = GWR(self.coords_, y, X_vars, bw=current_bw, fixed=self.fixed, kernel=self.kernel)
        self.results_ = self.model_.fit()

        return self

    def predict(self, X):
        X_vars = X[:, :-2]
        coords_new = X[:, -2:]

        scale = self.results_.scale
        residuals = self.results_.resid_response

        return self.model_.predict(coords_new, X_vars, scale, residuals).predictions.flatten()


def cross_validate_models(
        X: np.ndarray,
        y: np.ndarray,
        coords: list[tuple],
        models: dict[str, BaseEstimator],
        n_splits: int=5
):
    """
    Cross-validate multiple models using K-Fold cross-validation.
    :param X: Explanatory variables
    :param y: Target variable
    :param coords: Geographic coordinates to be included as features
    :param models: Dictionary of model names and their corresponding scikit-learn estimators
    :param n_splits: Number of folds for K-Fold cross-validation
    :return:
    """
    results = {}
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)

    X_with_coords = np.hstack((X, coords))

    for name, model in models.items():
        pipe = Pipeline([('scaler', StandardScaler()), ('model', model)])
        scores = cross_val_score(pipe, X_with_coords, y, cv=kf, scoring='r2')
        results[name] = np.mean(scores)

    return pd.DataFrame(results, index=['R2'])


def evaluate_model(
        X: np.ndarray,
        y: np.ndarray,
        coords: list[tuple] = None,
        models: dict[str, BaseEstimator] = None,
        random_state: int=42
):
    """
    Evaluate multiple models on a train-test split and compute performance metrics.
    :param X: Explanatory variables
    :param y: Target variable
    :param coords: Coordinates to be included as features
    :param models: Dictionary of model names and their corresponding scikit-learn estimators
    :param random_state: Random state for reproducibility
    :return: DataFrame with performance metrics for each model: R2, MSE, RMSE, MAE
    """
    results_train = {'R2': [], 'MSE': [], 'RMSE': [], 'MAE': []}
    results_test = {'R2': [], 'MSE': [], 'RMSE': [], 'MAE': []}
    if coords is not None:
        X = np.hstack((X, coords))
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_state)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    for name, model in models.items():
        model = model.fit(X_train_scaled, y_train)
        y_pred_train = model.predict(X_train_scaled)
        y_pred_test = model.predict(X_test_scaled)

        results_test['R2'].append(r2_score(y_test, y_pred_test))
        results_test['MSE'].append(mean_squared_error(y_test, y_pred_test))
        results_test['RMSE'].append(root_mean_squared_error(y_test, y_pred_test))
        results_test['MAE'].append(mean_absolute_error(y_test, y_pred_test))

        results_train['R2'].append(r2_score(y_train, y_pred_train))
        results_train['MSE'].append(mean_squared_error(y_train, y_pred_train))
        results_train['RMSE'].append(root_mean_squared_error(y_train, y_pred_train))
        results_train['MAE'].append(mean_absolute_error(y_train, y_pred_train))

    results_train = pd.DataFrame(results_train, index=models.keys())
    results_test = pd.DataFrame(results_test, index=models.keys())
    results = pd.concat({'Train': results_train, 'Test': results_test}, axis=1)
    return results

