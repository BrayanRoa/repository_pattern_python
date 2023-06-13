from app.unit_of_work.IUnit_of_work import IUnitOfWork
from app.user.repository.imp.user_repository_imp import UserRepositoryImp

class UnitOfWork(IUnitOfWork):
    def __init__(self):
        self.user = UserRepositoryImp()
