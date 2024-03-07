pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/thanhvhv/e-commerce.git'
            }
        }
        stage('Deploy') {
            steps {
                ansiblePlaybook become: true, credentialsId: 'ssh', installation: 'Ansible', inventory: './ansible/inventory', playbook: './ansible/install_docker.yml', sudo: true

            }
        }
    }
}
