pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/thanhvhv/e-commerce.git'
            }
        }
        stage('Build') {
            steps {
                // This step should not normally be used in your script. Consult the inline help for details.
                withDockerRegistry(credentialsId: 'docker-hub', url: 'https://index.docker.io/v1/')  {
                    sh 'docker login -u thanhvhv -p 0868269806'
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
