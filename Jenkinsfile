pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
    }

  }
  stages {
    stage('Build') {
      steps {
        sh '''python -m py_compile ./src/data_wrangler.py
        python -m py_compile ./test/main_tests.py

pylint ./src/data_wrangler.py -r no || exit 0
'''
      }
    }
    stage('Test') {
      steps {
        sh '''
py.test --junitxml results.xml ./test/main_tests.py'''
      }
    }
  }
}