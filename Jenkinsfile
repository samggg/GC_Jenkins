pipeline {
    agent any

    stages {
        stage('Clone do GitHub') {
            steps {
                git branch: 'main', url: 'https://github.com/samggg/GC_Jenkins.git'
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
                    docker.build("temp_test", "-f Dockerfile.test .").inside {
                        sh 'python -m unittest -v test_temperature.py'
                    }
                }
            }
        }
    }
}
