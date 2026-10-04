import yaml
import json
import os

def load_data(path: str) -> dict:
    """Carga datos desde un archivo YAML o JSON.
    
    Args:
        path (str): Ruta al archivo de entrada.
        
    Returns:
        dict: Datos cargados desde el archivo.
        
    Raises:
        ValueError: Si el archivo no es YAML ni JSON.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"El archivo {path} no existe.")
        
    if path.endswith(('.yaml', '.yml')):
        with open(path, 'r') as file:
            data = yaml.safe_load(file)
    elif path.endswith('.json'):
        with open(path, 'r') as file:
            data = json.load(file)
    else:
        raise ValueError(f"Formato no soportado: {path}. Solo se permiten YAML o JSON.")
        
    if data is None:
        raise ValueError(f"El archivo {path} está vacío.")
        
    return data