# Installation

## Environment variables:
```export APP_SETTINGS="config.DevelopmentConfig"```

```export DATABASE_URL="postgresql://user:password@server/database"```

## Delivering changes to database:
```python manage.py db init```

```python manage.py db migrate```

```python manage.py db upgrade```

## Run app:
```python app.py```
