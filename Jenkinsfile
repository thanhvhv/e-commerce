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
                    // Execute a single SSH command with multiple shell commands combined
                    sh """
                        ssh -o StrictHostKeyChecking=no thanhvhv@192.168.3.43 << EOF
                        mkdir jenkins
                        cd jenkins
                        echo 'Hello' > text
                        cat text
                    EOF
                    """
                }
            }
        }
    }
}
