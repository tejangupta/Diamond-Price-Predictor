# Diamond Price Predictor

This project is a web application
that predicts the price of a diamond based on various features and characteristics of a diamond.
Users can input the carat, depth, table, dimensions, cut, color, and clarity of the diamond,
and the application will provide an estimated price based on the best model chosen from linear regression,
lasso regression, ridge regression, and elastic net regression

## Table of Contents

- [Features](#features)
- [Workflows](#workflows)
- [Installation](#installation)
- [MLflow](#mlflow)
- [DagsHub](#dagshub)
- [AWS CI/CD deployment with GitHub Actions](#deplpyment)
- [Usage](#usage)
- [Technologies](#technologies)
- [Contributing](#contributing)
- [License](#license)

## Features

- Input form for users to enter diamond details such as carat, depth, table, dimensions, cut, color, and clarity.
- Validation to ensure all required fields are filled and have valid input.
- Prediction model that estimates the price of the diamond based on the provided inputs.
- Display of the estimated price to the user.
- Error handling for server communication and invalid input.

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py

## Installation

To run the Diamond Price Prediction application locally, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/tejangupta/Diamond-Price-Predictor.git
 ````
or
```bash
git clone git@github.com:tejangupta/Diamond-Price-Predictor.git
```

2. Navigate to the project directory:

```bash
cd Diamond-Price-Predictor 
```

3. Create a conda anvironment after opening the repository

```bash
conda create -n diamond python=3.8 -y
```

```bash
conda activate diamond
```

4. Install the required libraries or dependencies from requirements.txt

```bash
pip install -r requirements.txt
```

5. Start the flask server: 

```bash
flask run
```

6. Open your web browser and visit `http://localhost:8080` to access the application.

## MLflow

MLflow is an open-source platform for the complete machine learning lifecycle. It allows you to manage your machine learning experiments, track and compare metrics, and share and deploy models.

[Official Documentation](https://mlflow.org/docs/latest/index.html)

### Starting MLflow UI

To start the MLflow user interface, run the following command:

```bash
mlflow ui
```

### DagsHub Integration

[DagsHub](https://dagshub.com/) is a collaborative platform for managing and sharing data science projects. Here's how to integrate DagsHub with your MLflow project:

```angular2html
MLFLOW_TRACKING_URI=https://dagshub.com/tejangupta/Diamond-Price-Predictor.mlflow \
MLFLOW_TRACKING_USERNAME=tejangupta \
MLFLOW_TRACKING_PASSWORD=<YOUR_PASSWORD> \
python script.py
```

To use these values as environment variables, run the following commands:

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/tejangupta/Diamond-Price-Predictor.mlflow
export MLFLOW_TRACKING_USERNAME=tejangupta
export MLFLOW_TRACKING_PASSWORD=<YOUR_PASSWORD>
```

Make sure to replace the values with your own DagsHub project details.

## AWS CI/CD deployment with GitHub Actions

1. Login to AWS console
2. Create IAM user for deployment

```angular2html
# With specific access

1. EC2 access: It is virtual machine
2. ECR: Elastic Container registry to save your docker image in aws

# Description: About the deployment

1. Build docker image of the source code
2. Push your docker image to ECR
3. Launch Your EC2
4. Pull Your image from ECR in EC2
5. Lauch your docker image in EC2

# Policy

1. AmazonEC2ContainerRegistryFullAccess
2. AmazonEC2FullAccess
```

3. Create ECR repo to store/save docker image

```angular2html
- Save the URI: <YOUR_URI>
```

4. Create EC2 machine (Ubuntu) 
5. Open EC2 and Install docker in EC2 Machine:

```angular2html
# Optinal

sudo apt-get update -y
sudo apt-get upgrade

# Required

curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

6. Configure EC2 as self-hosted runner:

```angular2html
setting>actions>runner>new self hosted runner>choose os>then run command one by one
```

7.  Setup GitHub secrets:

```angular2html
AWS_ACCESS_KEY_ID=<Your AWS access key ID>
AWS_SECRET_ACCESS_KEY=<Your AWS secret access key>
AWS_REGION=<Your AWS region>
AWS_ECR_LOGIN_URI=<Your AWS ECR login URI>
ECR_REPOSITORY_NAME=<Name of your ECR repository> 
```

## Usage 

1. Fill out the form with the details of the diamond you want to predict the price for.
2. Click the "Submit" button to initiate the prediction.
3. Wait for the estimated price to be displayed on the screen.
4. If any errors occur, such as missing fields or invalid input, appropriate error messages will be shown.

## Technologies 

The Diamond Price Prediction application is built using the following technologies:

- HTML, CSS, and JavaScript for the front-end user interface
- Flask for the server-side application
- Linear Regression (My Best Model) for predicting diamond prices
- MLflow to track my experiments
- Fetch API for communicating with the server
- Bootstrap for styling and responsive design

## Contribution 

Contributions to the Diamond Price Prediction project are welcome!
If you have any suggestions, bug reports, or feature requests, please open an issue on the project repository.
If you would like to contribute code, you can follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:

```bash
git checkout -b feature/new-feature
```

3. Make your changes and commit them:

```bash
git commit -m "Add new feature"
```

4. Push the changes to your forked repository:

```bash
git push origin feature/new-feature
```

5. Open a pull request on the main repository, describing your changes and referencing the related issue if applicable.

## License

This project is licensed under the MIT License.

```arduino
Feel free to customize and modify this template to suit the specific details and requirements of your project. Provide detailed information about installation, usage, technologies used, and how others can contribute. Also, consider adding sections on troubleshooting, frequently asked questions, or any additional information that might be useful for users and contributors.
```
