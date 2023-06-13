from app.db import db
from ..user_repository import IUserRepository
from ...entity.user_entity import UserEntity
from ....repository.imp.repository import Repository


class UserRepositoryImp(IUserRepository, Repository):
    def __init__(self):
        self.session = db.session
        self.model_cls = UserEntity
        self.model_cls.start_mapper()

    def view_users(self, page, per_page):
        return self.list(self, page, per_page)