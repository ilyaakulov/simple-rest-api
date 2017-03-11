# Installation

## Environment variables:
```export APP_SETTINGS="config.DevelopmentConfig"```

```export DATABASE_URL="postgresql://user:password@server/database"```

```export SECRET_KEY="YOUR_SECRET_KEY"```

## Delivering changes to database:
```python manage.py db init```

```python manage.py db migrate```

```python manage.py db upgrade```

## Run app:
```python app.py```
