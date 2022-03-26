#== objects.py ==#

from collections import namedtuple
from datetime import datetime

import aiohttp

from . import http

__all__ = (
        'User',
        )

class APIOBJECT():
    __slots__ = (
        'response',
    )

    def __init__(self, response: dict, session: aiohttp.ClientSession) -> None:
        self.response = response
        self.state = session


    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}>'

class _BaseUser(APIOBJECT):
    __slots__ = (
        'reponse',
        'name',
        'id',
        )
    def __init__(self, response: dict, session: aiohttp.ClientSession) -> None:
        super().__init__(response, session=session)
        self.login = response.get('login')
        self.id = response.get('id')

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}; id = {self.id}, login = {self.login}>'

class User(_BaseUser): 
    __slots__ = (
        'login',
        'id',
        'avatar_url',
        'html_url',
        'public_repos',
        'public_gists',
        'followers',
        'following'
        'created_at',
        )
    def __init__(self, response: dict, session: aiohttp.ClientSession) -> None:
        super().__init__(response, session)
        ...





    