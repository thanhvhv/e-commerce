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
                withDockerRegistry(credentialsId: 'docker-hubb', url: 'https://index.docker.io/v1/')  {
                    sh 'docker build -t thanhvhv/jenkins .'
                    sh 'docker push thanhvhv/jenkins'
                }
            }
        }
        stage('Deploy') {
            steps {
                ansiblePlaybook becomeUser: 'ubuntu', credentialsId: 'ssh', disableHostKeyChecking: true, inventory: './ansible/inventory', playbook: './ansible/run_django.yml'
            }
        }
    }
}
