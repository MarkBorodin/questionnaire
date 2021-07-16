# INSTALL APP

## Setup

### Run this in docker

clone repository:
```
git clone https://github.com/MarkBorodin/questionnaire.git
```

move to folder "questionnaire":
```
cd questionnaire
```

run:
```
docker-compose up --build
```

migrate:
```
docker-compose exec backend python manage.py migrate
```

create super user:
```
docker-compose exec backend python manage.py createsuperuser
```
(after executing this command:
create and enter a username;
enter your email address;
create and enter a password;
enter the password again;)

collect static:
```
docker-compose exec backend python manage.py collectstatic
```

follow the link:
```
http://localhost/admin/
```
(or another host that will host the application)

### Finish


### Run this without docker

clone repository:
```
git clone https://github.com/MarkBorodin/questionnaire.git
```
move to folder "questionnaire":
```
cd questionnaire
```

in ".env" file set: RUN_IN_DOCKER=False

to install the required libraries, run on command line:
```
pip install -r requirements.txt
```

run redis:
```
redis-server
```

(in another terminal) run celery:
```
celery -A app worker -l info
```

(in another terminal) migrate:
``` 
python manage.py migrate
```

create super user:
```
python manage.py createsuperuser
```

(after executing this command:
create and enter a username;
enter your email address;
create and enter a password;
enter the password again;)

to start the server - run:
```
python manage.py runserver
```

follow the link:
```
http://127.0.0.1:8000/admin
```
(or another host that will host the application)


### Finish
