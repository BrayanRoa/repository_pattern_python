from app.repository.abstract_repository import AbstractRepository
from app.db import db
from datetime import datetime


class Repository(AbstractRepository):
    def __init__(self, model_cls) -> None:
        self.session = db.Model
        self.model_cls = model_cls

    def add(self, model):
        try:
            setattr(model, "created_at", datetime.now())
            setattr(model, "updated_at", datetime.now())
            self.session.add(model)
            self.session.commit()
            return model
        except Exception as e:
            print(e.args)
            return model

    def list(self, page, per_page):
        data_model = self.session.query(self.model_cls).paginate(
            page=page, per_page=per_page
        )
        meta = {
            "page": data_model.page,
            "pages": data_model.pages,
            "total_count": data_model.total,
            "prev_page": data_model.prev_num,
            "next_page": data_model.next_num,
            "has_next": data_model.has_next,
            "has_prev": data_model.has_prev,
        }
        return data_model.items, meta

    def get(self, id_):
        print(id_)
