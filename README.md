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
```
docker-compose exec backend python manage.py migrate
```
```
docker-compose exec backend python manage.py createsuperuser
```
(after executing this command:
create and enter a username;
enter your email address;
create and enter a password;
enter the password again;)
```
docker-compose exec backend python manage.py collectstatic
```

follow the link:
```
http://localhost/admin/
```
(or another host that will host the application)

### Finish
