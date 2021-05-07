There are few steps to run this script:
  1. Create a new directory on your computer and clone the repo into it.
  
    $ cd ~/<some_dir>
    $ git clone https://github.com/Qaminono/Yahoo_Finance/new/main/Skraper
   
  2. Then install the software packages specified by Pipenv and start a new shell.
  
    $ pipenv install
    $ pipenv shell
  
  3. Then run the 'main.py' script.
    
    $ python main.py
  
  The script will run in automatic mode. It will go through all the companies that are defined in the "companies" variable, find the data on the site, download it, and post it to the Rest service. If the company is not found, the following message will be displayed: 'No matches for "<company-name>" were found.
