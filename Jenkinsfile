pipeline {
    agent {
        docker {
            image 'python:3.14.6-alpine3.24'
        }
    }

    tools {
        dockerTool 'default'
    }

    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}