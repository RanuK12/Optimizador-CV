#!/usr/bin/env python3
"""
Evidencia de ejecución del código para el optimizador CV
"""

import sys
import os

# Agregar el directorio actual al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test de importación de módulos"""
    try:
        from build_cv import main
        from cv_validator import validate_config_file, CVValidationError
        from config_loader import load_config
        print("✅ Todos los imports exitosos")
        return True
    except Exception as e:
        print(f"❌ Error en imports: {e}")
        return False

def test_cv_generation():
    """Test de generación de CV"""
    try:
        # Cargar configuración de ejemplo
        from config_loader import load_config
        config = load_config("demo_config.json")
        print("✅ Configuración cargada exitosamente")
        
        # Validar configuración
        from cv_validator import validate_config_file
        if validate_config_file("demo_config.json"):
            print("✅ Configuración validada exitosamente")
        else:
            print("❌ Validación fallida")
            return False
        
        # Generar CV usando el script directamente
        import subprocess
        result = subprocess.run([sys.executable, "build_cv.py", "demo_config.json", "--output-pdf"], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ CV generado exitosamente")
            return True
        else:
            print(f"❌ Error en generación: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Error en generación: {e}")
        return False

def test_yaml_support():
    """Test de soporte YAML"""
    try:
        from config_loader import load_config
        config = load_config("example_config.yaml")
        print("✅ Configuración YAML cargada exitosamente")
        return True
    except Exception as e:
        print(f"❌ Error con YAML: {e}")
        return False

if __name__ == "__main__":
    print("=== Evidencia de Ejecución del Código ===")
    
    success = True
    success &= test_imports()
    success &= test_yaml_support()
    success &= test_cv_generation()
    
    if success:
        print("\n🎉 Todos los tests pasaron!")
    else:
        print("\n❌ Algunos tests fallaron")
        sys.exit(1)