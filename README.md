# CurrenciesConverter

Prerequisites (Требования)

    Python 3.x installed on your computer
    pip package manager installed on your computer

Installation (Установка)

    Clone the repository from GitHub using the following command:

git clone https://github.com/qbnil/CurrenciesConverter.git

Navigate to the project directory: (Переместитесь в главную директорию проекта)

cd CurrenciesConverter

Create a virtual environment and activate it: (Разверните виртуальное окружение)

Install virtualenv package using pip: pip install virtualenv

Create a new virtual environment by running the command:

    For Windows: virtualenv env
    For Linux/Mac OS: python -m venv env (Here "env" is the name of the virtual environment you want to create. You can choose any name you like.)

Activate the virtual environment by running the command:

    For Windows: .\env\Scripts\activate
    For Linux/Mac OS: source env/bin/activate



Install the required packages from the requirements.txt file: (Установите зависимости из файла - requirements.txt)

pip install -r requirements.txt

Set up the necessary environment variables. This may include setting up a .env file containing your API keys or database credentials. Make sure not to commit this file to version control. (не обязательно)

Run the database migrations:

    python manage.py migrate

Running the Application:

    Start the development server by running the following command:

    python manage.py runserver

    Open your browser and navigate to http://localhost:8000/. You should see the default home page of your Django application.

And that's it. (if you want to work with the database, you need to creat the superuser using the following command:
python manage.py createsuperuser)
