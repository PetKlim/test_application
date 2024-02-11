## Install Test Task on the local environment


1.  ### Clone project from git repository

```shell
 git clone https://github.com/PetKlim/test_application.git
```

2.  ### Run docker-compose

Go to develop directory ``/develop`` and run docker-compose

```shell
docker-compose up --build
```

3. ### Application and Swagger address
``127.0.0.1:8000`` - Application address.

``http://127.0.0.1:8000/api/schema/swagger-ui`` - Application's documentation.

4. ### Tests
In order to run the tests you need to go to the app container shell:

```shell
docker exec -it bank_app bash
```
Then execute command ``pytest -vv --ff`` or just press button up on keyboard 
(command was already saved in bash history).
