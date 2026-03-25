app/
│
├── application/
│   ├── schemas/
│   │   └── product_schema.py
│   └── services/
│       └── product_service.py
│
├── config/
│   └── settings.py
│
├── domain/
│   ├── entities/
│   │   └── product.py
│   └── ports/
│       └── product_repository.py
│
├── infrastructure/
│   ├── db/
│   │   ├── base.py
│   │   ├── session.py
│   │   └── models/
│   │       └── product_model.py
│   │
│   └── repositories/
│       └── product_repository_impl.py
│
├── interfaces/
│   └── api/
│       └── v1/
│           └── product_routes.py
│
└── main.py