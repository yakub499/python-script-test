pipeline{
  agent { label 'master' }
  
  stages{
    stage("Build"){
      steps{
        db_name= "mydb"
        sh "python-script-test/test.py"
      }    
    }
  }
}
