pipeline{
  agent { label 'master' }
  
  stages{
    stage("Build"){
      steps{
        script{
         def db_name= "mydb"
        }
        sh "export DB_NAME = ${db_name}"
        sh "python first.py"
      }    
    }
  }
}
