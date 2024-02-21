# FastAPI Template with SQLModel

> Further information about frameworks and libraries used:
>
> - [FastAPI](https://fastapi.tiangolo.com/)
> - [SQLModel](https://sqlmodel.tiangolo.com/)

Readme in progress...

## Use of Pydantic Settings

Pydantic settings are used for setting up the application configuration.
`pydantic-settings` needs to get installed therefore it is added to the [requirements.txt](./app/requirements.txt) file.

The config settings are defined in the `app/config.py` file.
With the help of Pydantic settings we can define a clearly-defined, type-hintend application configuration.

> A detailed documentation can be found [here](https://docs.pydantic.dev/dev/concepts/pydantic_settings/).

## DB Connection

To connect to PostgreSQL add `psycopg2-binary` to the [requirements.txt](./app/requirements.txt) file.

### Alembic for migrations

Add `alembic` to the [requirements.txt](./app/requirements.txt) file.

in case of own setup

```bash
alembic init migrations
```

Add an `sqlmodel` import to the [script.py.mako](./app/migrations/script.py.mako) file in the migrations folder.

```python
from alembic import op
import sqlalchemy as sa
import sqlmodel
```

configurating SQLModel metadata object in `migrations/env.py`

```python
from app.models import SQLModel

target_metadata = SQLModel.metadata
```

configure `sqlalchemy.url` in `migrations/env.py` from environment variable

```python
config = context.config

def get_url() -> str:
    from app.config import settings

    return str(settings.POSTGRES_URI)

config.set_main_option("sqlalchemy.url", get_url())
```

### Create a migration

```bash
alembic revision --autogenerate -m "init"
```

### Update the database

```bash
alembic upgrade head
```

## Security / Authentication

Install `passlib[bcrypt]` for password hashing.

password hashing..

## Authentication with JWT

We need to add `python-multipart` and `python-jose[cryptography]` to the [requirements.txt](./app/requirements.txt) file. `python-multipart` is necessary for OAuth2 to use form data and `python-jose` is necessary for JWT token creation and validation.

Create own secret key for JWT token and add it to the `.env` file.

```bash
openssl rand -hex 32
```
