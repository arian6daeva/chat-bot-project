node {
    stage('Clone repository') {
        checkout scm
    }

    stage('Start container') {
        steps {
            sh 'docker compose up -d --no-color --wait'
            sh 'docker compose ps'
        }
    }
}
