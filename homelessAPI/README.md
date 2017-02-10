##Instructions to install API and run it locally
In order to follow these instructions you need to have access to the AWS DB information for our team, and have Python 3, Pip, and Virtualenv installed. If you need this information send a message to @zakkent on the Homelessness team's slack channel. 

### 1. Clone this repo 
### 2. Make a virtual environment 
Run these commands in the outer most level of the repo
- Setup virtual env: 
  - ```virtualenv -p /usr/local/bin/python3 venv3``` 
  Or change the path to location of your Python 3 
- Activate virtual env: 
  - ```source venv3/bin/activate``` 
  
### 3. Install depencencies with pip
- Install depedencies from requirements.txt: 
  - pip install -r requirements.txt
  
### 4. Create a project_config.py file 
- In order for the API to be able to access the AWS DB you need to make a local project_config.py file in the homelessAPI/ directory. It should be in the same directory as the settings.py file. In this file create an object that has the connection information to our AWS DB and the Django Secret Key. See example below: 
```Python
AWS = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'DB name here',
        'HOST': 'DB IP address here',
        'USER': 'DB user here',
        'PASSWORD': 'DB password here' 
      }

DJANGO_SECRET = 'secret key here'
        
```
### 5. Start server
- In directory with manage.py run this command: 
  - ```python manage.py runserver```
  - see working root endpoint at: [http://localhost:8000/homeless/](http://localhost:8000/example/)
