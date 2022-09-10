## How to run server

Install the requirements:
```
pip install -r requirements.txt
```

Downloade, install and run MongoDB following the instructions in https://www.mongodb.com/docs/manual/installation/.

Run the server:

```
python3 run.py
```

Send request to the server

```
curl --location --request POST 'http://127.0.0.1:9292/v1/users/createUser' \
--header 'Authorization: Bearer B1n0FlddHVnfBLeAkC' \
--form 'username="john"' \
--form 'password="doe"' \
--form 'age="25"'
```