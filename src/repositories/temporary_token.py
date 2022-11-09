from repositories import BaseRepo
from models import TemporaryToken
from schemas import TemporaryTokenIn, TemporaryTokenUpdate


temporary_token_repo = BaseRepo[TemporaryToken, TemporaryTokenIn, TemporaryTokenUpdate](TemporaryToken)
