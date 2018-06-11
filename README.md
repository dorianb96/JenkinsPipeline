## CI/CD of a Python application using Jenkins and Docker

### How it works?

**Problem**   

We have a github repository with our application. We would like to automate the build, testing and deployment process. 

**Solution**   
 
We will use Jenkins 2.x to solve this problem.    
With the addition of _"Pipeline as Code"_ we can simple define our CI/CD in a Jenkins file.   
The repository for our application will thus contain a **Jenkinsfile** which defines the CI/CD pipeline with code.   
Thus when using Jenkins for CI/CD of our application, we can just point Jenkins to our Jenkinsfile in our repository without having to do any manual configuration and it will build the whole pipeline.

We will use docker as an agent to run our tests.   
Specifically Jenkins will use the image created by our Dockerfile to create a docker container each time the pipeline is triggered. 

In the docker file we define the docker image of the container we will use to run our application.   
First off, we use the base python image. We then copy the files from our application into the container.   
The requirements.txt file is used to install all the dependencies from the application.   
Lastly, we install additional testing libraries. 


### Steps in the application
##### 1. Run Jenkins on your machine

I ran Jenkins in a docker container whose data was persisted on my machine: 

>
docker run \  
--rm \  
-u root \  
-p 8080:8080 \  
-v jenkins-data:/var/jenkins_home \  
-v /var/run/docker.sock:/var/run/docker.sock \  
-v "$HOME":/home \  
--name jenkins-tutorials \  
jenkinsci/blueocean  


##### 2. Login into Jenkins.   
If logging into for the first time, make sure to install all suggested pipelines. Also create an administrator account.

##### 3. Define the new pipeline

I prefer the Blue Ocean interface for this. 
Make a new pipeline from your github repository and tell Jenkins to use the Jenkinsfile for this. 	

##### 4. Ready to use
You can now use Jenkins to do the whole CI/CD pipeline.   
You can also add additional features to the pipeline either by changing the code of Jenkinsfile
or working with the Blue Ocean UI.    


## TO-DO 
- expand the application    
- add integration/performance tests          
- add code coverage test to Jenkins UI reports      
- add pylint test reports to Jenkins UI reports     
- add conditionals of pylint/code coverage to the build   
- add deployment stage       


