# CurrenciesConverter

Prerequisites

    Python 3.x installed on your computer
    pip package manager installed on your computer

Installation

    Clone the repository from GitHub using the following command:

git clone https://github.com/qbnil/CurrenciesConverter.git

Navigate to the project directory:

cd your-project-name

Create a virtual environment and activate it:

python3 -m venv venv
source venv/bin/activate

Install the required packages from the requirements.txt file:

pip install -r requirements.txt

Set up the necessary environment variables. This may include setting up a .env file containing your API keys or database credentials. Make sure not to commit this file to version control.

Run the database migrations:

    python manage.py migrate

Running the Application:

    Start the development server by running the following command:

    python manage.py runserver

    Open your browser and navigate to http://localhost:8000/. You should see the default home page of your Django application.

And that's it! These instructions will help users set up and run your Django project on their local machine. Remember to provide any additional instructions specific to your project, such as how to create a superuser account or how to deploy the project to a production server.
