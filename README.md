## Getting Started

These instructions will get you a copy of the app up and running on your local machine for development and testing purposes.

### Prerequisites

Things you need to install the software and how to install them
- Ensure you have `Python 3` installed on your local machine
- Ensure you have `MongoDB` installed as well
- Virtualenv: A virtual environment wrapper is needed to install all the dependencies required for the project to run
Install virtualenv on your local machine like so

  ```
  pip3 install virtualenv
  ```

### Installing

This is a step by step series of examples to get the project up and running on your local machine

First thing is to enter the working directory like so

```
cd smart-steel-task
```

Secondly create a new `virtualenv` wrapper with the following command

```
virtualenv -p Python3 venv
```
After creating a virtual environment wrapper, the next step is to activate the wrapper so we can install our dependencies


```
source venv/bin/activate
```

Next step is to install all our dependencies from the `requirements.txt` file like so

```
pip install -r requirements.txt
```

After installing the dependencies, we need to export some environment variables in the command line. We need to export our flask app and flask debug settings.

```
export FLASK_DEBUG=1
```
Next stage is exporting our PythonPath so which will enables access files in different modules. First we need is to get our current working path like so

```
pwd  ## /home/path-to-project
```
After retrieving the path, we need to export it like so

```
export PYTHONPATH=/home/path-to-project
```

The next stage is to create a `.env` file in the root directory of the project  where we will some key environment variables such as our  `MongoDB` database Url. A `.env-sample` file has been created for this purpose.

## Running both applications
We have currently have two applications, the first is located in the `/server/` directory and it contains our simple `Flask` server for serving the temperature logs from the database. 
The second is located in `/upload/` directory and it transfers the logs from the `task_data.csv` file into our `MongoDB` database.

The following steps are needed to successfully run the application

Firstly we need to ensure we have `MongoDB` installed and running on our local machine. We can start up our `MongoDB` server like so

```
mongod
```

Next we need to upload the `CSV` data into our `MongoDB` database. We can do so with this command

```
python upload/upload_task_data.py
```
At the execution of this command, a `stdout` should be printed which shows that the `CSV` data was tranferred successfully

The final stage is running our web application. The command below is used to start the web server

```
python server/app.py
```
Once the server starts, you can navigate to the browser and access the temperature logs through the following url `http://127.0.0.1:5000/logs`


## Justification
- For this project, I decided to utilize the `Flask` web framework which is a simple minimalistic for getting our simple web server up and running. 
- We needed a datastore where the data can be transferred easily without the constraints of relationships and traditional rows and columns. A document DB came to be right approach for this project.
- In larger applications that deals with extracting large amounts of data from CSV files, `Pandas` might be the most suitable choice of library. Since this was a small application I decided to leverage on python's inbuilt CSV library for the converting the CSV data into a `dictionary`.

- Finally We needed two seperate applications that weren't dependent on each other. 
  - The first application handled the transferring of data from the CSV file to our `MongoDB` datastore.
  - The second was a simple `flask` server that served the results from the datastore. 

By default, `Flask` ships with `Jinja2` which is a templating engine and it was utilized for displaying the data from the database in the a simple `html` table.

## Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The web framework used
* [PyMongo](https://api.mongodb.com/python/current/index.html/) - A Python engine for communicating with our `MongoDB` database
* [Jinj2](https://jinja.palletsprojects.com/en/2.11.x/) - Templating engine for serving our logs in `html` format
* [MongoDB](https://docs.mongodb.com/manual/introduction/) - The NOSQL database used for this project



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
