pipeline {
    agent any

    stages {
        

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t autodeploy-python .'
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                docker rm -f autodeploy-container || true
                docker run -d -p 5000:5000 --name autodeploy-container autodeploy-python
                '''
            }
        }
    }
}
