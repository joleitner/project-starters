# FastAPI Template with PostgreSQL and SQLModel

> Further information about frameworks and libraries used:
>
> - [FastAPI](https://fastapi.tiangolo.com/) the main framework
> - [SQLModel](https://sqlmodel.tiangolo.com/) for (database) models based on Pydantic and SQLAlchemy
> - [Alembic](https://alembic.sqlalchemy.org/en/latest/tutorial.html) for migration management

Readme in progress..

## Configuration with Pydantic Settings

Every slightly more complex application needs some kind of configuration.
Usually, this is done with environment variables.
To access these environment variables with ease and to have a clearly defined configuration, we can use Pydantic settings.

To add Pydantic settings to the project, we need to add `pydantic-settings` to the [requirements.txt](./app/requirements.txt) file.

```requirements.txt
pydantic-settings
```

In this template, we define the application configuration in a `config.py` file inside the `app/core` folder.

```python
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Application settings
    APP_NAME: str = "FastAPI"

    # Database settings
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str


settings = Settings()
```

We can define our variables and even set default values. The `BaseSettings` class will then automatically read the environment variables and assign them to the corresponding variables.
Trough that we can just import the `settings` object and access the configuration values.

```python
from app.core.config import settings

print(settings.APP_NAME)
```

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

## Testing

For testing we need to add `pytest` and `httpx` to the [requirements.txt](./app/requirements.txt) file.

```requirements.txt
pytest
httpx
```

Afterwards we can create a `tests` folder and create a `conftest.py` file to create our pytest fixtures.
They help us to initialize our test functions with a TestClient and a database session.
More information about fixtures can be found [here](https://docs.pytest.org/en/6.2.x/fixture.html).

```python
from typing import Generator
import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture(scope="module")
def client() -> Generator:

    with TestClient(app) as c:
        yield c
```

Now we can create corresponding test files. As example we can create a `test_main.py` file to test the main route of our application.

```python
from fastapi.testclient import TestClient
from app.core.config import settings


def test_read_main(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": f"Hello World from {settings.APP_NAME}"}
```

As you can see the `client` fixture is used to send a request to the main route and check the response. Pytest will automatically provide the fixtures to the test functions.

To run your tests you can simply type the following command in your terminal.

```bash
pytest
```

## ToDos

- [ ] Finish Readme
- [ ] Add more advanced testing examples
- [ ] add mail support
- [ ] create better user model and add ToDo items as example
