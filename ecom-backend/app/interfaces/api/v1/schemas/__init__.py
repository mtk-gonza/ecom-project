from .product_schema import ProductResponse, ProductResponseSummary
from .license_schema import LicenseResponse, LicenseResponseSummary
from .category_schema import CategoryResponse, CategoryResponseSummary

# Resuelve las referencias circulares aquí, después de que todo está importado
ProductResponse.model_rebuild()
LicenseResponse.model_rebuild()
CategoryResponse.model_rebuild()