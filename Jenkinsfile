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
                // Combine all commands into a single string
                def commands = """
                cd jenkinsss
                echo 'Hello' > choe
                cat choe
                """

                // Execute the combined commands on the remote host
                sh "ssh -o StrictHostKeyChecking=no thanhvhv@192.168.3.43 '${commands}'"
            }
        }
    }
}
