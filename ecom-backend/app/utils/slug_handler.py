import re
import unicodedata

def generate_slug(text: str) -> str:
    """Convierte un texto a slug URL-friendly."""
    # Normalizar caracteres (quitar acentos)
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')
    # Minúsculas
    text = text.lower()
    # Reemplazar espacios y caracteres especiales por guiones
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    # Quitar guiones al inicio/final
    return text.strip('-')