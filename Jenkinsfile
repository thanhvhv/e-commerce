pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/thanhvhv/e-commerce.git'
            }
        }

        stage('SSH') {
            steps {
                sshagent(['remote_server_43']) {
                    sh 'ssh -o StrictHostKeyChecking=no thanhvhv@192.168.3.43 mkdir jenkinsss'
                }
            }
        }
    }
}
