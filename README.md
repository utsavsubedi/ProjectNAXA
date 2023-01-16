# ProjectNAXA


# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/utsavsubedi/ProjectNAXA.git
    $ cd projectNAXA
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements.txt

Then move into project directory

    $ cd project
    
Then simply apply the migrations:

    $ python manage.py migrate
    
 Crete superuser for accessing database through django admin:
 
    $ python manage.py createsuperuser
 
 Then enter username, email and password.

You can now run the development server:

    $ python manage.py runserver

For testing, a postman collection if attached according to the specified task.

- Open Postman and click the "Import" button in the top left corner of the application.

- Select "Import From File"

- Then navigate to the ProjectNAXA folder and select it. 

- Postman will then display a preview of the collection and its requests. Review the collection and requests to ensure they are correct.

- Click the "Import" button to complete the process.
