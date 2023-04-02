# Reminders!

## How to run locally

Go inside todo and run pip install -r requirements.txt

Change the Databases-section in the settings.py according to your mysql/mariadb setup.

Run python manage.py makemigrations && python manage.py migrate \
Run python manage.py runserver



## Members

Michael Mueller (st122797) \
Sricharan Yedu Thirnathi (st122037) \
Panuvit Chantara (st121410) \
Sai Preetham Kamishetty (st122038) \

## Contributions

![Contributions](https://user-images.githubusercontent.com/97950172/163948774-4c3ac69d-1fc1-4bc1-add9-a69c5366c306.png)


## Containerization

The current repo contains a monolithic version of the application that can be installed and run locally. For our attempts to dockerize and deploy it with two separated services for the authentication and the reminders, check out the following repos:
1. https://github.com/panuvitchantara/reminder.git
2. https://github.com/panuvitchantara/reminder_microservice
3. http://sad1-a.cs.ait.ac.th:8000/

