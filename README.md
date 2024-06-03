# Fetch
To run the application in this repository:
* Clone the repo into your workspace.
* Ensure you are in the directory labeled `Fetch` with the file `manage.py`
* Once there, run the following command: `python3 manage.py migrate`
* This will ensure the database is setup accordingly on your device.
* Afterwards, you can run the built in server using the command: `python3 manage.py runserver`
* Then navigate to the url shown in your terminal: `http://localhost:8000`

This should display a button with the name `Click me`. Once you do, it will redirect you to the success page showing you the
data stored in the database.
