pipeline {
    agent {
        docker { image 'python:3.14.6-alpine3.24' }
    }

    environment {
        PROJECT_OWNER = 'Ben Mor'
        APP_ENV       = 'Development'
    }

    stages {
        stage('Print Env Variables') {
            steps {
                echo "Running Build number: ${env.BUILD_NUMBER}"
                echo "This project belongs to: ${env.PROJECT_OWNER}"
                sh "echo Running in environment: \$APP_ENV"
            }
        }
    }
}