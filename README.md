## SKELETON TO START PROJECT IN PYTHON

<p align="center">
  <a target="blank"><img src="https://mukulrathi.com/static/9340fcb15b4c44184a11848ce18fb4c8/8326d/docker-flask-postgres.png" width="300" alt="python-flask-postgresql-docker" /></a>
</p>

1. Clone the repository
2. create the virtual environment

* if you are on windows run the following command
  __virtualenv venv__

* if you are on linux run the following command
  __python -m venv name__

3. enter the virtual environment

* if you are on windows run the following command
  __source venv/Scripts/activate__

* if you are on linux run the following command
  __source bin/activate__

4. install the necessary libraries that are in the archive ```requirements.txt```

* __pip install -r requirements.txt__

5. Environment Variables 🚧

copy the variables that are in the ```.env.example``` file and create a file called ```.env``` where you should place these variables and fill them with the corresponding values

4. enter the following commands

* __export FLASK_APP=entrypoint__
* __export FLASK_DEBUG=1__
* __flask run__

5. You can access the api documentation here:

```
http:localhost:5000/apidocs
```

# Stack

* Flask 
* PostgreSql 
* Docker