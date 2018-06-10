pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
    }

  }
  stages {
    stage('Build') {
      steps {
        sh '''python -m py_compile ./demo/src/data_wrangler.py
        python -m py_compile ./demo/test/main_tests.py

pylint ./demo/src/data_wrangler.py -r no || exit 0
'''
      }
    }
    stage('Test') {
      steps {
        sh '''
py.test --junitxml results.xml ./demo/test/main_tests.py'''
      }
    }
  }
}