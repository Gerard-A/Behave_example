pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Start building...'
                echo 'Build...'
                echo 'Finished building'
            }
        }
        stage('Test') {
            steps {
                echo 'Prepare virtualenv and run Behave Tests'
                bat """
                   python -m venv venv
                   call venv\\Scripts\\activate.bat
                   pip install -r requirements.txt
                   runTest.bat
                """
                echo 'Finished Behave Tests'
            }  finally {
            junit 'test_results/*.xml'  // (1)
            }
        }
    }
}