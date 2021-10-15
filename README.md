# akvelon_python_internship_3_ainur_nazirov

# TASK # 1

Used: Python, Django, SQLite, Swagger.

To run the program, do:
1. In the terminal go to the project directory
2. Run the commands:
python -m venv venv
venv \ Scripts \ activate
pip install django
pip install djangorestframework
pip install -U drf_yasg
pip install django-filter
python manage.py migrate
python manage.py runserver

Next, you need to add data to the database using POST requests on the pages http://127.0.0.1:8000/users/ and http://127.0.0.1:8000/transactions/.
To make it faster, examples are in the examples.json.

API Documentation: http://127.0.0.1:8000/

/ transactions /
Available: GET, POST
List of all transactions. There is filtering and sorting by the user_id, amount and date fields, as well as searching by the amount and date fields.
Examples of GET requests: http://127.0.0.1:8000/transactions/?date=2021-05-25&ordering=amount - transactions made on May 25, 2021, sorted in ascending order of the transaction amount.
http://127.0.0.1:8000/transactions/?search=2960 - transactions containing the substring '2960'.

/ transactions / {id} /
Available: GET, PUT, PATCH, DELETE
Transaction available by id.
Example GET request: http://127.0.0.1:8000/transactions/1/ - transactions with id equal to 1.

/ transactionsbydate / {id} /
Available: GET
Sum of user's transactions, grouped by date.
An example of a GET request: http://127.0.0.1:8000/transactionsbydate/1/ - the sums of transactions of the user with id equal to 1, grouped by date.

/ transactionsbytype / {type} /
Available: GET
List of all transactions, filtered by type. type takes the values ​​income and outcome, otherwise it lists all the user's transactions.
Example GET request: http://127.0.0.1:8000/transactionsbytype/income/ - list of all income.

transactionsbytype / {type} / {id}
Available: GET
List of user transactions, available by type and user_id. type takes the values ​​income and outcome, otherwise it lists all transactions.
An example of a GET request: http://127.0.0.1:8000/transactionsbytype/income/1/ - a list of all incomes for a user with id equal to 1.

/ users /
Available: GET, POST
List of all users. There is filtering, searching and sorting by fields first_name, last_name and email.
Examples of GET requests: http://127.0.0.1:8000/users/?last_name=Ivanov&ordering=email - users with the last name Ivanov, sorted alphabetically by email.
http://127.0.0.1:8000/transactions/?search=Ivan - users with the 'Ivan' substring.

/ users / {id} /
Available: GET, PUT, PATCH, DELETE
User accessible by id.
Example GET request: http://127.0.0.1:8000/users/1/ - users with id equal to 1.


# TASK # 2

The implemented function is in the utils.py file.
