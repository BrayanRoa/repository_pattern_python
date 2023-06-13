from dependency_injector import containers, providers
from app.unit_of_work.imp.unit_of_work import UnitOfWork


class Container(containers.DeclarativeContainer):
    unitow = providers.Singleton(UnitOfWork)


container = Container()
unitow_imp = container.unitow()
