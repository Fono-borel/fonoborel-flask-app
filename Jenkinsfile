pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
        IMAGE_NAME = 'bobo2003/fonoborel-flask-app'
    }

    stages {
        stage('Clonage') {
            steps {
                echo 'Clonage du dépôt GitHub...'
                git branch: 'main',
                    url: 'https://github.com/Fono-borel/fonoborel-flask-app.git'
            }
        }

        stage('Image') {
            steps {
                echo 'Construction de l image Docker...'
                sh 'docker build -t ${IMAGE_NAME}:latest .'
            }
        }

        stage('Publication') {
            steps {
                echo 'Publication sur DockerHub...'
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                sh 'docker push ${IMAGE_NAME}:latest'
            }
        }
    }

    post {
        success {
            echo 'Pipeline exécuté avec succès !'
        }
        failure {
            echo 'Echec du pipeline.'
        }
    }
}
