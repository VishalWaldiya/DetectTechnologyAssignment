Hi this is the solution for the backend problem i.e problem number 1 to 8 from the file "Problem Statement- Detect.docx"

#Getting Started
##Installation
1. Install `virtualenv`
2. Make a new virtual enviornment
3. Install necessary packages from requirements.txt
4. Activate Virtual enviornment
5. Delete db.sqlite3 file if you want a fresh start(optional)
6. Migrate Project using
    > `python mange.py makemigrations`
    > `python mange.py migrate`
7. Load Existing Employes Data using 
    > `python manage.py loademployee filename number_of_records`
    
    Example
    > `python manage.py loademployee employees.json 3`

    loademployees is and custom mangement tag defined in the path 
    > `/account/management/commands/loademployee`
8. Similarily Load Background Tasks to check and load data from file
    > `python manage.py loaddata tasks.json`

9. Create a SuperUser of your choice using command
    > `python manage.py createsuperuser`

10. To  Excecute Tests
    > `python -Wa manage.py test`

11. Rest APIs
    > 'GET' Urls

    > To get list of all Employess
    > `/api/employees/`
    > To get Particular Employee Details
    > `/api/employees/<int:pk>`

    > 'POST' Urls

    > To store data into DB
    > `/api/employees/`

    >'PUT' Urls

    > To Update Employee Details
    > `/api/employees/<int:pk>`

    >'DELETE' Urls

    >To Delete Employee Object from DB
    > `/api/employees/<int:pk>`