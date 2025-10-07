pipeline{
    agent{
        node{
            label 'local'
        }
    }
    stages{
        stage('Checkout Code') {
            steps {
                git branch: 'master', url: 'file:///C:/Users/deeks/Desktop/MLOPs/jenkins/microservices_docker_compose'
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