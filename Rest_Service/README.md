There are few steps to run this service in Docker container:
  1. Create a new directory on your mashine and clone the repo into it.
  
    cd ~/some_dir
    git clone https://github.com/Qaminono/Yahoo_Finance/tree/main/Rest_Service
 
  2. Now start the Docker container using the up command, adding the -d flag so it runs in detached mode, and the --build flag to build our initial image. If we did not add this flag, we'd need to open a separate command line tab to execute commands.
  
    docker-compose up -d --build
    
  3. We should migrate our database at this point on Docker.
  
    docker-compose exec web python manage.py migrate
  
  4. Done. Now go to http://127.0.0.1:8000.
