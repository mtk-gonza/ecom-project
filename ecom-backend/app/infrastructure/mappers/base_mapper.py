from typing import Type, TypeVar, Union

Domain = TypeVar("Domain")
Model = TypeVar("Model")

class BaseMapper:
    # ✅ Soporta strings o clases: {'products': ProductMapper} o {'products': 'ProductMapper'}
    RELATION_MAPPERS: dict[str, Union[type, str]] = {}
    
    @classmethod
    def to_domain(cls, model: Model, domain_class: Type[Domain]) -> Domain:
        data = {}
        
        for field in domain_class.__annotations__.keys():
            if not hasattr(model, field):
                continue
                
            value = getattr(model, field)
            
            if value is None:
                data[field] = None
                continue
            
            # ✅ Verificar si el campo tiene un mapper registrado
            if field in cls.RELATION_MAPPERS:
                mapper_ref = cls.RELATION_MAPPERS[field]
                
                # ✅ Resolver string a clase si es necesario
                if isinstance(mapper_ref, str):
                    mapper_class = cls._resolve_mapper(mapper_ref)
                else:
                    mapper_class = mapper_ref
                
                # ✅ Mapear lista o objeto único
                if isinstance(value, list):
                    data[field] = [mapper_class.to_domain(item) for item in value]
                else:
                    data[field] = mapper_class.to_domain(value)
            else:
                # ✅ Campo escalar normal
                data[field] = value
        
        return domain_class(**data)
    
    @classmethod
    def _resolve_mapper(cls, mapper_name: str) -> type:
        """
        Resuelve un string como 'ProductMapper' a la clase real.
        Usa importación dinámica para evitar círculos.
        """
        # Mapeo de nombres a rutas de módulo (configurar según tu proyecto)
        mapper_registry = {
            'ProductMapper': ('app.infrastructure.mappers.product_mapper', 'ProductMapper'),
            'LicenseMapper': ('app.infrastructure.mappers.license_mapper', 'LicenseMapper'),
            'CategoryMapper': ('app.infrastructure.mappers.category_mapper', 'CategoryMapper'),
            'ImageMapper': ('app.infrastructure.mappers.image_mapper', 'ImageMapper'),
            'SpecificationMapper': ('app.infrastructure.mappers.specification_mapper', 'SpecificationMapper'),
        }
        
        if mapper_name not in mapper_registry:
            raise ValueError(f"Mapper '{mapper_name}' no registrado en _resolve_mapper")
        
        module_path, class_name = mapper_registry[mapper_name]
        module = __import__(module_path, fromlist=[class_name])
        return getattr(module, class_name)

    @staticmethod
    def from_domain(domain: Domain, model_class: Type[Model]) -> Model:
        return model_class(**domain.dict())

    @staticmethod
    def update_model_from_domain(model: Model, domain: Domain):
        for key, value in domain.dict(exclude_unset=True).items():
            if hasattr(model, key):
                setattr(model, key, value)