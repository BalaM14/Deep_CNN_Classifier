# deep classifier project


## workflow

1.  Update config.yaml
2.  Update secrets.yaml [Optional]
3.  Update params.yaml
4.  Update the entity
5.  Update the configuration manager in src config.
6.  Update the components
7.  Update the pipeline
8.  Test run pipeline stage
9.  run tox for testing your package
10. Update the dvc.yaml
11. run "dvc repro" for running all the stages in pipeline

![image](https://raw.githubusercontent.com/BalaM14/Deep_CNN_Classifier/main/docs/images/Data%20Ingestion%402x%20(1).png)


STEP 1: Set the env variable | Get it from dagshub -> remote tab -> mlflow tab

MLFLOW_TRACKING_URI=https://dagshub.com/BalaM14/Deep_CNN_Classifier.mlflow
MLFLOW_TRACKING_USERNAME=BalaM14
MLFLOW_TRACKING_PASSWORD=<> \

STEP 2: install mlflow

STEP 3: Set remote URI

STEP 4: Use context manager of mlflow to start run and then log metrics, params and model