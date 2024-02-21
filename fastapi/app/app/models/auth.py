from typing import Union

from sqlmodel import SQLModel


class Token(SQLModel):
    access_token: str
    token_type: str
    
# Contents of JWT token
class TokenPayload(SQLModel):
    sub: Union[str, None] = None

    
    