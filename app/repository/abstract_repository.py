import abc

class AbstractRepository(abc.ABC):
    
    @abc.abstractmethod
    def add(self):
        raise NotImplementedError
    
    @abc.abstractmethod
    def list(self, references, page, per_page):
        raise NotImplementedError
    
    @abc.abstractmethod
    def get(self, page, per_page):
        raise NotImplementedError