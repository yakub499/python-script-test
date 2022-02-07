pipeline{
  agent { label 'master' }
  
  stages{
    stage("Build"){
      steps{
        script{
         def db_name= "mydb"
        }
        sh "python python_script_test3/first.py"
      }    
    }
  }
}
