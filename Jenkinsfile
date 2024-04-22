pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/thanhvhv/e-commerce.git'
            }
        }

        stage('Slack 1'){
            steps{
                slackSend channel: '#general', message: 'The server will be unavailable during the restart process. \nWe expect this to take only a few minutes, but the actual time may differ slightly.'
            }
        }

        // stage('SSH') {
        //     steps {
        //         sshagent(['remote_server_43']) {
        //             // Execute a single SSH command with multiple shell commands combined
        //             sh """
        //                 ssh -o StrictHostKeyChecking=no thanhvhv@192.168.3.43 /bin/bash << EOF
        //                 mkdir jenkins
        //                 cd jenkins
        //                 echo 'Hello World' > text
        //                 cat text
        //             """
        //         }
        //     }
        // }

        stage('Slack 2'){
            steps{
                slackSend channel: '#general', message: 'The server is now back online and functioning normally.'
            }
        }
    }
}
