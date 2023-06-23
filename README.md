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

1) python3 -m venv venv
2) source venv/bin/activate

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
