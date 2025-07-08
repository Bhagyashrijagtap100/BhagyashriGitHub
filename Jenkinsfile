pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/Bhagyashrijagtap100/BhagyashriGitHub.git'
            }
        }

        stage('Run Python Script') {
            steps {
                bat '"C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" csvcode.py'
            }
        }

        stage('Archive Output') {
            steps {
                archiveArtifacts artifacts: 'output/*.csv', fingerprint: true
            }
        }
    }
}
