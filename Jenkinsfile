pipeline {
  agent {
       label "dots-nexus-sync"
  }
  environment {
     scannerHome = tool 'SonarScanner'
  }
stages {
    stage('SCM') {
      steps {
        checkout scm
      }
    }
    stage('SonarQube Analysis') {
      steps{
        withSonarQubeEnv(installationName: 'sonar-test') {
          sh "${scannerHome}/bin/sonar-scanner"
        }
      }
    }
  }
}
