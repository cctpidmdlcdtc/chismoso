# Install

```shell
python3 -m venv venv
source venv/bin/activate
pip install pip --upgrade
pip install -r requirements.txt
```

## API

La API no necesita estar arrancada para que la web funcione:

```shell
hug -f api.py
```

La primera vez que ejecutamos la aplicación, podemos inicializar la bbdd con datos de prueba:

```shell
curl -svk http://localhost:8000/initial_load
```

## Flask

Arrancar la aplicación web:

```shell
python app.py
```


