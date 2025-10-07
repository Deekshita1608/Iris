pipeline{
    agent any
    stages{
        stage('Checkout Code') {
            steps {
                git branch: 'master', url: 'https://github.com/Deekshita1608/Iris.git'
            }
        }
        stage('Show workspace'){
            steps{
                bat 'cd'
            }
        }
        stage('Build Images'){
            steps{
                bat 'docker-compose build'
            }
        }
        stage('Run Containers'){
            steps{
                bat 'docker-compose up -d'
            }
        }
    }
}