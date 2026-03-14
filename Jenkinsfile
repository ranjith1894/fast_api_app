pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git 'https://github.com/ranjith1894/fast_api_app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t voting-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker rm -f voting-container || true'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 8000:8000 --name voting-container voting-app'
            }
        }

    }
}