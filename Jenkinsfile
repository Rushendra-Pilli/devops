pipeline{
    agent any
    stages{
        stage('checkout the github branch'){
            steps{
                checkout scm
            }
        }
        stage('Build python requirements'){
            steps{
                powershell '''
                    python -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Tests'){
            steps{
                powershell '''
                    . venv/bin/activate
                    python -m pytest -v junitxml=report.xml
                '''
            }
        }
    }
}