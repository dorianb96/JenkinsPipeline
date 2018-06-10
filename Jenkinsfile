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
        python -m py_compile ./test/test_data_wrangler.py
        pylint ./src/data_wrangler.py -r no || exit 0
'''
      }
    }
    stage('Test') {
      steps {
        sh '''
        pytest --pyargs test --junitxml results.xml'''
      }
    }
  }
}