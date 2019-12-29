pipeline {
   agent any

   stages {
      stage('Build') {
         steps {
            // Get some code from a GitHub repository
            git 'https://github.com/archick12/python_automation.git'

            // Install libraries
            sh '''
                    /Library/Frameworks/Python.framework/Versions/3.7/bin/python3 -m venv venv
                    . venv/bin/activate
                    python3 -m pip install --ignore-installed -r requirements.txt
                    python3 -m pytest -v
               '''
         }
      }

      stage('Smoke') {
          steps {
             //Run only smoke test group
             sh '''
                   python -m pytest -m smoke -v
                '''

         }
       }
      stage('Regression') {
           steps {
              //Run only regression group
              sh '''
                    pytest -m regression -v
                 '''
           }
      }

    }
}