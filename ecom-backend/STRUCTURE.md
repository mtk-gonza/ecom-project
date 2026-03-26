app/
│
├── application/
│   ├── dtos/
│   │   └── product_dto.py
│   ├── services/
│   │   └── product_service.py
│   ├── use_cases
│   │   └── product/
│   └── exceptions.py
│
│
├── config/
│   └── settings.py
│
├── domain/
│   ├── entities/
│   │   └── product.py
│   ├── enums/
│   └── ports/
│       └── product_repository.py
│
├── infrastructure/
│   ├── db/
│   │   ├── base.py
│   │   ├── session.py
│   │   └── models/
│   │       └── product_model.py
│   ├── logging/
│   ├── mappers/
│   └── repositories/
│       └── product_repository_impl.py
│
├── interfaces/
│   └── api/
│       └── v1/
│           ├── dependencies/
│           ├── routes/
│           ├── schemas/
│           └── handlers.py
│
├── utils/
│
└── main.py