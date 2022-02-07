pipeline{
  agent { label 'master' }
  
  stages{
    stage("Build"){
      steps{
        script{
         def db_name= "mydb"
        }
        sh "python first.py"
      }    
    }
  }
}
