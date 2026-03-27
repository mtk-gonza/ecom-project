app/
│
├── application/
│   └── services/
│       ├── auth_service.py
│       ├── category_service.py
│       ├── image_service.py
│       ├── license_service.py
│       ├── product_service.py
│       ├── role_service.py
│       ├── specification_service.py
│       └── user_service.py
│
├── config/
│   └── settings.py
│
├── domain/
│   ├── entities/
│   │   ├── category.py
│   │   ├── image.py
│   │   ├── license.py
│   │   ├── product.py
│   │   ├── role.py
│   │   ├── specification.py
│   │   └── user.py
│   ├── enums/
│   │   ├── currency.py
│   │   ├── entity_type.py
│   │   ├── image_type.py
│   │   ├── product_status.py
│   │   └── role_type.py
│   ├── ports/
│   │   ├── category_repository.py
│   │   ├── image_repository.py
│   │   ├── license_repository.py
│   │   ├── product_repository.py
│   │   ├── role_repository.py
│   │   ├── specification_repository.py
│   │   └── user_repository.py
│   └── exceptions.py
│
├── infrastructure/
│   ├── db/
│   │   ├── base.py
│   │   ├── session.py
│   │   └── models/
│   │       ├── category_model.py
│   │       ├── image_model.py
│   │       ├── license_model.py
│   │       ├── product_model.py
│   │       ├── role_model.py
│   │       ├── specification_model.py
│   │       ├── user_model.py
│   │       └── user_roles_model.py
│   ├── logging/
│   │   ├── config.py
│   │   └── logger.py
│   ├── mappers/
│   │   ├── base_mapper.py
│   │   ├── category_mapper.py
│   │   ├── image_mapper.py
│   │   ├── license_mapper.py
│   │   ├── product_mapper.py
│   │   ├── role_mapper.py
│   │   ├── specification_mapper.py
│   │   └── user_mapper.py
│   └── repositories/
│       ├── category_repository_impl.py
│       ├── image_repository_impl.py 
│       ├── license_repository_impl.py 
│       ├── product_repository_impl.py 
│       ├── role_repository_impl.py 
│       ├── specification_repository_impl.py 
│       └── user_repository_impl.py
│
├── interfaces/
│   └── api/
│       └── v1/
│           ├── dependencies/
│           │   ├── auth.py
│           │   ├── db.py
│           │   ├── repositories.py
│           │   ├── role.py
│           │   └── services.py
│           ├── routes/
│           │   ├── auth_router.py
│           │   ├── category_router.py
│           │   ├── image_router.py
│           │   ├── license_router.py
│           │   ├── product_router.py
│           │   ├── role_router.py
│           │   ├── specification_router.py
│           │   └── user_router.py
│           ├── schemas/
│           │   ├── auth_schema.py
│           │   ├── base_schema.py
│           │   ├── category_schema.py
│           │   ├── image_schema.py
│           │   ├── license_schema.py
│           │   ├── product_schema.py
│           │   ├── role_schema.py
│           │   ├── specification_schema.py
│           │   └── user_schema.py
│           └── handlers.py
│
├── utils/
│   ├── jwt_handler.py
│   ├── password_utils.py
│   ├── role_handler.py
│   └── slug_handler.py
│
└── main.py