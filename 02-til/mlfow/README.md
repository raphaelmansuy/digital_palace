# An In-Depth Guide to MLflow for Machine Learning Model Management

## Information

| Author         | Created    | Updated    | Version |
| -------------- | ---------- | ---------- | ------- |
| Raphaël MANSUY | 28/09/2023 | 28/09/2023 | 1.0.0   |

MLflow is an open source platform for managing the end-to-end machine learning lifecycle, including experimentation, reproducibility, deployment, and a central model registry. In this comprehensive tutorial, we'll walk through how to use MLflow's key components to track experiments, log metrics and artifacts, deploy models, and more.

## Overview of MLflow

MLflow consists of four main components:

- **MLflow Tracking**: Records and tracks experiments, including code, data, config, and results.
- **MLflow Projects**: Packages code and dependencies as reproducible runs.
- **MLflow Models**: Packages models for deployment and serving.
- **Model Registry**: Centralized model store, model lineage, model versioning, and stage transitions.

The tracking component is useful during development and testing, while the projects, models, and model registry components help package, validate, and deploy models to production.

MLflow works with any machine learning library or framework like TensorFlow, PyTorch, XGBoost, and scikit-learn, and integrates with tools like Docker, Kubernetes, and AWS SageMaker. It can be used for projects both small and large.

## Experiment Tracking with MLflow Tracking

The core functionality of MLflow centers around its tracking component. This allows you to log metrics, parameters, and artifacts for each run of your machine learning code and visualize results.

### Starting an MLflow run

To use MLflow tracking, wrap your code in an `mlflow.start_run()` block:

```python
import mlflow

with mlflow.start_run() as run:
  
  # ML code goes here
  
mlflow.end_run()
```

This starts a new run with a unique ID that all metrics and parameters will be logged to.

### Logging metrics and parameters

Within each run, log metrics like accuracy scores, loss values, or any other numeric values from your model training and evaluation:

```python 
mlflow.log_metric("accuracy", 0.91)
mlflow.log_metric("loss", 1.83)
```

Log key/value pairs of parameters using `log_param`:

```python
mlflow.log_param("learning_rate", 0.01)
mlflow.log_param("architecture", "ResNet50") 
```

Metrics and parameters are automatically logged to MLflow Tracking Server or a local SQLite database.

### Logging artifacts

Artifacts allow you to log files like images, models, and data files. Use `log_artifact` and provide a local file path:

```python
mlflow.log_artifact("images/profile.jpg") 
mlflow.log_artifact("models/keras_model.h5")
```

Artifacts are logged to an artifact repository like S3 or Azure Blob Storage.

### Visualizing runs

The MLflow Tracking UI provides a central place to visualize, compare, and search runs using metrics, parameters, tags, and artifacts:

MLflow Tracking UI

This makes it easy to compare runs side-by-side to determine the best model.

You can run the UI via `mlflow ui` or access it at http://localhost:5000.

## Packaging Code with MLflow Projects

While MLflow Tracking lets you log specific runs, MLflow Projects packages code and configurations so you can reproduce runs on any platform.

Projects define the full computing environment required to run your code, including:

- **Entry point**: Main executable code to run.
- **Parameters**: Key/value parameters for the entry point.  
- **Dependencies**: Local Python dependencies or Conda environment file.
- **Docker container**: Optional Docker image dependencies.

Define projects with a simple YAML format:

```yaml
name: My Project

conda_env: conda.yaml

entry_point: train.py

parameters:
  alpha: {type: float, default: 0.4}
  epochs: 10
``` 

Then run projects locally via `mlflow run` to launch the entry point:

```bash
mlflow run . -P alpha=0.5
```

This launches `train.py` with the Conda environment defined in `conda.yaml` and passes `alpha=0.5`.

You can also run projects remotely on Databricks, Kubernetes, or AWS SageMaker backends. The project contains all the info needed to replicate the run.

## Packaging and Distributing Models with MLflow Models

Once you've trained a model, you'll want to package it so it can be deployed for real-time serving.

MLflow Models provides a standard unit for packaging and reusing models with different flavors:

- **Python Function**: Deploy Python models locally.  
- **Docker**: Build a Docker image to containerize the model.
- **AWS SageMaker**: Deploy on SageMaker for real-time predictions.
- **Apache Spark**: Load PySpark models for batch predictions.

To save a model:

```python
import mlflow.sklearn

mlflow.sklearn.log_model(sk_learn_model, "model") 
```

This logs a model artifact that can be consumed from different platforms.

You can also associate the model with metadata like name, version, description, and stage.

To load and use a model:

```python
model = mlflow.pyfunc.load_model("runs:/96771d77ec124f2587b8a013f4da8c16/model")

model.predict(input_data)
```

The `mlflow.pyfunc` package loads models in a consistent way for local Python deployment.

## Managing Models with the Model Registry

For larger teams and applications, it's important to have a central model registry for discovering, versioning, and managing models.

Key features of the MLflow Model Registry:

- **Model lineage**: Visualize model history and compare versions.
- **Model versioning**: Register new model versions over time.
- **Stage transitions**: Mark models as staging vs production.
- **Annotations**: Take notes on model experiments.
- **Access control**: Limit model access to certain users.

You can associate a model with the registry when logging:

```python
mlflow.sklearn.log_model(model, "model", registered_model_name="Ecommerce Model")
``` 

This registers the model under the "Ecommerce Model" name. 

You can add new versions over time, update descriptions, transition to staging or production, and annotate experiments for easier model reproducibility and governance.

The registry provides a central hub for discovering, documenting, and managing models.

## Deploying Models to Production with MLflow

Once you've trained a performant model, you'll want to deploy it to production for real-time serving. 

MLflow provides a few options for scalable, robust deployments:

### Deploy locally

For small-scale or testing purposes, you can deploy models locally via REST API or batch inference:

```python
import mlflow.pyfunc 

model = mlflow.pyfunc.load_model("model")

mlflow.pyfunc.serve_model(model)
```

This starts a local REST API endpoint you can send requests to for real-time predictions.

### Deploy to Docker

Containerize models as Docker images for reproducible, portable deployments using the `mlflow models build-docker` CLI:

```bash
mlflow models build-docker -m runs:/<run-id>/model --no-conda -n model
```

This packages the model as a Docker image for easy deployment to hosts running Docker.

### Deploy to Kubernetes

For robust model deployment, Kubernetes is a popular open source platform. Deploy MLflow models to Kubernetes using the [MLflow KServe project](https://github.com/kubeflow/kfserving/tree/master/docs/samples/mlflow).

This provides performant, resilient serving backed by Kubernetes.

### Deploy to AWS SageMaker

For a fully-managed environment, AWS SageMaker is a good option. Deploy models to SageMaker endpoints via:

```python
import sagemaker

model = mlflow.sagemaker.deploy(app_name="model", model_uri="runs:/...") 

predictor = sagemaker.RealTimePredictor(endpoint=model.endpoint_name)
```

SageMaker handles provisioning servers, scaling, load balancing, A/B testing, and more.

## Conclusion

In this guide, we covered how to use MLflow Tracking, Projects, Models, and the Model Registry to manage experiments, package reproducible runs, save and deploy models, and centralize model lineage and lifecycle management.

MLflow provides a powerful, flexible toolkit for the end-to-end machine learning lifecycle, from initial prototyping to full production deployment. Its modular components let you incorporate MLflow into your existing workflows.

To learn more and see additional examples, refer to the [official MLflow documentation](https://www.mlflow.org/docs/latest/index.html).
