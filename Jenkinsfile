pipeline {
   agent any

   stages {
      stage('Build') {


         steps {
            // Get some code from a GitHub repository
            git branch:'jenkins_integration', url:'https://github.com/vitaliisotnichenko/python_automation'

            // Install libraries
            sh '''
                    /Library/Frameworks/Python.framework/Versions/3.7/bin/python3 -m venv venv
                    . venv/bin/activate
                    python3 -m pip install --ignore-installed -r requirements.txt
               '''
                }
           }

      stage('Smoke') {
          steps {
             //Run only smoke test group

                sh '''
                    /Library/Frameworks/Python.framework/Versions/3.7/bin/python3 -m venv venv
                    . venv/bin/activate
                    python3 -m pytest -m smoke -v
                   '''
                }

             }
      stage('Regression') {
           steps {
              //Run only regression group
                sh '''
                    /Library/Frameworks/Python.framework/Versions/3.7/bin/python3 -m venv venv
                    . venv/bin/activate
                    python3 -m pytest -m regression -v
                    '''

                 }
            }

        }

      post {
                always {
                    allure([
                        includeProperties: false,
                        jdk: '',
                        properties: [],
                        reportBuildPolicy: 'ALWAYS',
                        results: [[path: '/Users/vitaliisotnichenko/.jenkins/workspace/Jira_automation_tests/allure-report']]
                    ])
                    }
            }

  }

