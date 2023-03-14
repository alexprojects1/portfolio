pipeline {
  parameters{
      string(name:'parameter1',  defaultValue:''  ?: '')
      string(name:'parameter2',  defaultValue:''  ?: 'test')
      string(name:'parameter3',  defaultValue:''  ?: '')
  }
  agent any 
  stages {
        stage('Build') { 
            steps {
                sh 'echo ${parameter1}'
            }
        }
        stage('Test') { 
            steps {
                sh 'echo ${parameter2}' 
            }
        }
        stage('Deploy') { 
            steps {
                sh 'echo ${parameter3}'
            }
        }
    }
}