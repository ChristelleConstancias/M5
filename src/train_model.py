# src/train_model.py


import os
import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, auc, recall_score, f1_score, roc_auc_score, confusion_matrix, classification_report
from imblearn.pipeline import Pipeline
from imblearn.under_sampling import RandomUnderSampler
import joblib


import mlflow
import mlflow.sklearn

FEATURES = [
    "pregnancies", 
    "glucose", 
    "blood_pressure", 
    "skin_thickness",
    "insulin", 
    "bmi", 
    "diabetes_pedigree", 
    "age"
]


def split_train(df):
    X = df[FEATURES]
    y = df["outcome"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    X_train.shape, X_test.shape
    return X_train, X_test, y_train, y_test

def train_the_model():

    # configuraton du ML Flow
    mlflow.set_experiment("DiabetesPrediction")

    # Charger les données
    df = pd.read_csv("./data/raw/diabetes_train.csv")

    # Split train/test
    X_train, X_test, y_train, y_test = split_train(df)


    with mlflow.start_run(run_name="RandomForest_Undersampling"):

        # Pipeline
        pipeline = Pipeline(steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
            ("undersampler", RandomUnderSampler(random_state=42)),
            ("model", RandomForestClassifier(random_state=42)),
        ])


        # Hyperparamètres
        param_grid = {
            "model__n_estimators": [200, 300, 400],
            "model__max_depth": [4, 6, 8, None],
            "model__min_samples_leaf": [1, 3, 5],
        }

        # Validation croisée
        cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)


        # Recherche des meilleurs paramètres
        search = GridSearchCV(pipeline, param_grid=param_grid, scoring="recall", cv=cv, n_jobs=-1)

        search.fit(X_train, y_train)


        print("\nMeilleurs paramètres :")
        print(search.best_params_)

        print("Meilleur recall CV :",round(search.best_score_, 4))

        # Meilleur modèle
        best_pipeline = search.best_estimator_

        # Évaluation sur le jeu de test
        y_pred = best_pipeline.predict(X_test)
        y_proba = best_pipeline.predict_proba(X_test)[:, 1]

        # Métriques
        accuracy = accuracy_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        auc = roc_auc_score(y_test, y_proba)

        print("accuracy:", round(accuracy, 4))
        print("recall: ", round(recall, 4))
        print("f1: ", round(f1, 4))
        print("auc: ", round(auc, 4))
        print("confusion matrix:\n", confusion_matrix(y_test, y_pred))
        print(classification_report(y_test, y_pred))

        # =====================
        # Logging MLflow
        # =====================

        # Paramètres du run
        mlflow.log_param("scoring", "recall")
        mlflow.log_param("cv_folds", 5)
        mlflow.log_param("train_size", len(X_train))
        mlflow.log_param("test_size", len(X_test))

        # Meilleurs hyperparamètres
        mlflow.log_params(search.best_params_)

        # Métriques
        mlflow.log_metric("cv_best_recall", search.best_score_)
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("recall", recall)
        mlflow.log_metric("f1", f1)
        mlflow.log_metric("auc", auc)


        # Sauvegarde du modèle
        joblib.dump(
            {
                "model": best_pipeline,
                "features": FEATURES,
            },
            "diabetes_risk_model.pkl",
        )


        # Modèle dans MLflow
        trusted_types = [
            "imblearn.pipeline.Pipeline",
            "imblearn.under_sampling._prototype_selection._random_under_sampler.RandomUnderSampler",
            "numpy.dtype",
        ]

        mlflow.sklearn.log_model(
            sk_model=best_pipeline,
            name="model",
            skops_trusted_types=trusted_types,
        )

        print("\nModèle sauvegardé : diabetes_risk_model.pkl")

        print(
            "\nRun MLflow enregistré avec succès"
        )

    return best_pipeline, FEATURES


if __name__ == "__main__":
    train_the_model()