pipeline{
    agent{
        node{
            label 'local'
            customWorkspace 'C:\\Users\\deeks\\Desktop\\MLOPs\\jenkins\\microservices_docker_compose'
        }
    }
    stages{
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