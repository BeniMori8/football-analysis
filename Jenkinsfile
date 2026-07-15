pipeline {
    agent { docker { image 'python:3.14.6-alpine3.24' } }
    stages {
        stage('Check Environment') {
            steps {
                echo '--- Starting environment checks inside the container ---'
                sh 'python --version'
                sh 'pip --version'
                echo '--- All checks passed successfully! ---'
            }
        }
    }
}