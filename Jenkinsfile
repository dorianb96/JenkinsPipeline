pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
    }

  }
  stages {
    stage('Build') {
      steps {
        sh '''python -m py_compile /demo/src/data_wrangler.py
python -m py_compile /demo/test/main_tests.py

pip install astroid
pip install isort
pip install pylint
pylint /demo/src/data_wrangler.py -r no
pylint /demo/test/main_tests.py -r no'''
      }
    }
  }
}