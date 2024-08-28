pipeline {
  agent {
       label "dots-nexus-sync"
  }
stages {
    stage('SCM') {
      steps {
        checkout scm
      }
    }
    stage('SonarQube Analysis') {
      //def scannerHome = tool 'SonarScanner';
      steps{
        withSonarQubeEnv(installationName: 'sonar-test') {
          sh "${scannerHome}/bin/sonar-scanner"
        }
      }
    }
  }
}
