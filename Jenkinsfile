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
                    python3 -m venv venv
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
                    python3 -m pytest -v junitxml=report.xml
                '''
            }
        }
    }
}