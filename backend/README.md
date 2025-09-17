# Household backend

## Running the backend
- `fastapi dev main.py --reload` [//] run the backend for development (auto-reload)

## Working with migrations
- starts with `alembic init migrations` [//] tool - command - folder

- `alembic revision --autogenerate -m "First revision" --rev-id 0001` [//] makes changes revision
- `alembic upgrade head` [//] run migrations to the highest level
- `alembic upgrade #hash#` [//] run specific migration
- `alembic downgrade #hash#` [//] revert specific migration

❗❗ When new model is created and inherits from BaseModel, DO NOT FORGET to call `attach_updated_at_triggers_to_all_tables()` in alembic migrations (upgrade method). It set update_at trigger. ❗❗

## Pre-commit
- `pre-commit install` [//] install pre-commit hooks

# Auth
generate `SECRET_KEY` for JWT token
```
openssl rand -hex 32
```

# Well-known bugs
- Pydantic alias vs Fastapi open api schema: https://github.com/fastapi/fastapi/issues/1810#issuecomment-895126406
