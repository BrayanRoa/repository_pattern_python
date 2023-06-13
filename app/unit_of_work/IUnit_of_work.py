from ..user.repository.user_repository import IUserRepository


class IUnitOfWork():
    user = IUserRepository
