pipeline {
  agent {
       label "dots-nexus-sync"
  }
stages {
    stage('SCM') {
      checkout scm
    }
    stage('SonarQube Analysis') {
      def scannerHome = tool 'SonarScanner';
      withSonarQubeEnv() {
        sh "${scannerHome}/bin/sonar-scanner"
      }
    }
  }
}
