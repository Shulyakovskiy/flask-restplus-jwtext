#### FLASK RESTFUL API BOILER-PLATE WITH JWT
[![Python 3](https://pyup.io/repos/github/Shulyakovskiy/flask-restplus-template/python-3-shield.svg)](https://pyup.io/repos/github/Shulyakovskiy/flask-restplus-template/)
[![Updates](https://pyup.io/repos/github/Shulyakovskiy/flask-restplus-template/shield.svg)](https://pyup.io/repos/github/Shulyakovskiy/flask-restplus-template/)

### Terminal commands
    gunicorn --config ./app/conf/gunicorn_config.py server:api
    python manager.py run
    ------------------------
    Initial installation: make install

    To run test: make tests

    To run application: make run

    To run all commands at once : make all


### Viewing the app ###

    Open the following url on your browser to view swagger documentation
    http://127.0.0.1:5000/


### Using Postman ####

    Authorization header is in the following format:

    Key: Authorization
    Value: "token_generated_during_login"

    For testing authorization, url for getting all user requires an admin token while url for getting a single
    user by public_id requires just a regular authentication.

### Full description and guide ###
https://medium.freecodecamp.org/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563


### Contributing
If you want to contribute to this flask restplus boilerplate, clone the repository and just start making pull requests.

```
https://github.com/Shulyakovskiy/flask-restplus-jwtext.git
```
