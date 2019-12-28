pipeline {
   agent any

//    tools {
      // Install the Maven version configured as "M3" and add it to the path.
//       maven "maven 3"
//    }

   stages {
      stage('Build') {
         steps {
            // Get some code from a GitHub repository
            git 'https://github.com/archick12/python_automation.git'

            // Install libraries
            sh '''
                    /Library/Frameworks/Python.framework/Versions/3.6/bin/python3 -m venv venv
                    . venv/bin/activate
                    python3 -m pip install --ignore-installed -r requirements.txt
                '''

            // To run Maven on a Windows agent, use
            // bat "mvn -Dmaven.test.failure.ignore=true clean package"
         }
      }

      stage('Smoke') {
          steps {
             //Run only smoke test group
               sh '''
                      python3 -m pytest -v -m smoke

                  '''

         }
       }
      stage('Regression') {
           steps {
              //Run only regression group
              sh 'python3 -m pytest -v -m regression'
           }
      }

      }
   }
}