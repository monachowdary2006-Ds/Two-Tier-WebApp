pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Build Docker Images') {
            steps {
                echo 'Building Flask application image...'
                sh 'docker build -t two-tier-webapp-jenkins ./app'
            }
        }

        stage('Validate Docker Compose') {
            steps {
                echo 'Validating Docker Compose configuration...'
                sh 'docker compose -p two-tier-webapp config'
            }
        }

        stage('Deploy Application') {
            steps {
                echo 'Deploying Flask application...'
                sh 'docker compose -p two-tier-webapp up -d --build --no-deps flask-app'
            }
        }
    }

    post {
        success {
            echo 'Two-Tier Web Application deployed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check console output.'
        }
    }
}