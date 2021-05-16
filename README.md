# CreditApprovalTechTestBackEnd

### Deployment

_Download or clone all the repository and then with console run the next commands:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata client_data.json
python manage.py loaddata personal_credit_data.json
python manage.py runserver
```
and automatically will run the backend service

### Pre-requirements 📋

_Python3
_Port localhost:8000 open
