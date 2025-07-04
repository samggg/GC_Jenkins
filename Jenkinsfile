pipeline {
    agent any

    stages {
        stage('Clone do GitHub') {
            steps {
                git 'https://github.com/samggg/GC_Jenkins.git'
            }
        }

        stage('Build em container') {
            steps {
                script {
                    docker.build("temp_build", "-f Dockerfile.build .")
                }
            }
        }

        stage('Testes em container') {
            steps {
                script {
                    docker.build("temp_test", "-f Dockerfile.test .").run()
                }
            }
        }
    }
}
