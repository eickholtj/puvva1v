Clone the repo.  In the root directory of the repo, run 'vagrant up' and then 'vagrant ssh'.  Once in the VM, reposition yourself into the /opt/ebook directory and run 'mvn package' and then 'java -jar target/*.jar'.  The application should then be available on the host machine at 127.0.0.1:8080.  

Alternatively, you can clone the repository to your local system.  In Eclipse, import a Maven Project (File > Import > Maven > Existing Maven Project) and browse and select the cloned repo.  You may need to set the group id and Artifact name.  Note that you may have issues with the jdk.tools dependency.  See Stack Overflow question 11118070 for more details.

To run and/or package, on the package name, right click and run as '5 Maven build...' then set the target to 'compile package'.  You may have to select the src/main/java folder and "use as src folder".
