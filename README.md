# auth0-device-authorization-example

## How to run

### Create a virtualenv
```
mkvirtualenv auth0-device-authorization --python=$(which python3)
```

### Install requirements
```
pip install -r requirements.txt
```

### Copy `.env.dist` to `.env` and change it's content
```
cp .env.dist .env
```

```
python generate_access_token.py
```
