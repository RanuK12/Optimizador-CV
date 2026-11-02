#!/usr/bin/env python3
"""
Evidencia final de ejecución del optimizador CV
"""

import subprocess
import sys
import os

def run_demo():
    """Ejecutar el demo completo que ya funciona"""
    try:
        result = subprocess.run([sys.executable, "demo.py"], 
                              capture_output=True, text=True, cwd=os.path.dirname(__file__))
        
        if result.returncode == 0:
            print("✅ Demo ejecutado exitosamente")
            print(f"Output: {result.stdout}")
            return True
        else:
            print(f"❌ Demo fallido: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Error al ejecutar demo: {e}")
        return False

def check_files():
    """Verificar archivos generados"""
    files_to_check = [
        "demo_cv.docx",
        "demo_config.json",
        "README.md",
        "requirements.txt"
    ]
    
    success = True
    for file in files_to_check:
        if os.path.exists(file):
            size = os.path.getsize(file)
            print(f"✅ {file} existe ({size} bytes)")
        else:
            print(f"❌ {file} no existe")
            success = False
    
    return success

if __name__ == "__main__":
    print("=== Evidencia Final del Optimizador CV ===")
    
    success = True
    success &= run_demo()
    success &= check_files()
    
    if success:
        print("\n🎉 Todo funciona correctamente!")
    else:
        print("\n❌ Algo falló")
        sys.exit(1)