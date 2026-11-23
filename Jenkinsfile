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
                bat 'docker build -t two-tier-webapp-jenkins ./app'
            }
        }

        stage('Validate Docker Compose') {
            steps {
                echo 'Validating Docker Compose configuration...'
                bat 'docker compose config'
            }
        }

        stage('Deploy Application') {
            steps {
                echo 'Starting Flask and MySQL containers...'
                bat 'docker compose up -d'
            }
        }
    }

    post {
        success {
            echo 'Two-Tier Web Application deployed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}