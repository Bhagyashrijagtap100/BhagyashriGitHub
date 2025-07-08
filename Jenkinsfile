pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/Bhagyashrijagtap100/BhagyashriGitHub.git'
            }
        }

        stage('Run Python Script') {
            steps {
                bat 'python myscript.py'
            }
        }
    }
}
