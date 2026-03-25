from typing import Type, TypeVar

Domain = TypeVar("Domain")
Model = TypeVar("Model")

class BaseMapper:
    @staticmethod
    def to_domain(model: Model, domain_class: Type[Domain]) -> Domain:
        return domain_class(**{
            column.name: getattr(model, column.name)
            for column in model.__table__.columns
            if hasattr(domain_class, column.name)
        })

    @staticmethod
    def from_domain(domain: Domain, model_class: Type[Model]) -> Model:
        return model_class(**domain.dict())

    @staticmethod
    def update_model_from_domain(model: Model, domain: Domain):
        for key, value in domain.dict(exclude_unset=True).items():
            if hasattr(model, key):
                setattr(model, key, value)