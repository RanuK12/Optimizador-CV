#!/usr/bin/env python3
"""
Validador de configuración para el optimizador de CV.
Valida que el archivo de configuración JSON/YAML tenga la estructura correcta
para generar un CV válido.
"""

import json
import sys
import os
from typing import Dict, Any, List

def validate_config(config: Dict[str, Any]) -> List[str]:
    """
    Valida la configuración del CV y retorna una lista de errores.
    Si la lista está vacía, la configuración es válida.
    """
    errors = []
    
    # Campos obligatorios en el nivel raíz
    required_fields = ['name', 'title', 'email', 'phone']
    for field in required_fields:
        if field not in config:
            errors.append(f"Missing required field '{field}'")
        elif not isinstance(config[field], str) or not config[field].strip():
            errors.append(f"Field '{field}' must be a non-empty string")
    
    # Validar email (básico)
    if 'email' in config and isinstance(config['email'], str):
        if '@' not in config['email'] or '.' not in config['email'].split('@')[-1]:
            errors.append("Field 'email' must be a valid email address")
    
    # Validar campos opcionales
    if 'linkedin' in config and config['linkedin'] is not None:
        if not isinstance(config['linkedin'], str) or not config['linkedin'].startswith('http'):
            errors.append("Field 'linkedin' must be a valid URL or null")
    
    if 'github' in config and config['github'] is not None:
        if not isinstance(config['github'], str) or not config['github'].startswith('http'):
            errors.append("Field 'github' must be a valid URL or null")
    
    if 'summary' in config and config['summary'] is not None:
        if not isinstance(config['summary'], str):
            errors.append("Field 'summary' must be a string or null")
    
    # Validar experiencia
    if 'experience' in config:
        if not isinstance(config['experience'], list):
            errors.append("Field 'experience' must be a list")
        else:
            for i, exp in enumerate(config['experience']):
                if not isinstance(exp, dict):
                    errors.append(f"Experience item {i} must be an object")
                else:
                    # Campos requeridos en experiencia
                    exp_required = ['company', 'title', 'dates', 'description']
                    for field in exp_required:
                        if field not in exp:
                            errors.append(f"Experience item {i} missing required field '{field}'")
                        elif not isinstance(exp[field], str) or not exp[field].strip():
                            errors.append(f"Experience item {i} field '{field}' must be a non-empty string")
    
    # Validar educación
    if 'education' in config:
        if not isinstance(config['education'], list):
            errors.append("Field 'education' must be a list")
        else:
            for i, edu in enumerate(config['education']):
                if not isinstance(edu, dict):
                    errors.append(f"Education item {i} must be an object")
                else:
                    # Campos requeridos en educación
                    edu_required = ['degree', 'institution', 'dates']
                    for field in edu_required:
                        if field not in edu:
                            errors.append(f"Education item {i} missing required field '{field}'")
                        elif not isinstance(edu[field], str) or not edu[field].strip():
                            errors.append(f"Education item {i} field '{field}' must be a non-empty string")
    
    # Validar habilidades
    if 'skills' in config:
        if not isinstance(config['skills'], list):
            errors.append("Field 'skills' must be a list")
        else:
            for i, skill in enumerate(config['skills']):
                if not isinstance(skill, str) or not skill.strip():
                    errors.append(f"Skills item {i} must be a non-empty string")
    
    return errors

def validate_config_file(filepath: str) -> bool:
    """
    Valida un archivo de configuración JSON o YAML.
    Retorna True si es válido, False en caso contrario.
    """
    if not os.path.exists(filepath):
        print(f"❌ Configuration file not found: {filepath}")
        return False
    
    try:
        if filepath.endswith('.json'):
            with open(filepath, 'r', encoding='utf-8') as f:
                config = json.load(f)
        elif filepath.endswith(('.yaml', '.yml')):
            import yaml
            with open(filepath, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
        else:
            print(f"❌ Unsupported file format: {filepath}")
            print("   Supported formats: .json, .yaml, .yml")
            return False
        
        if config is None:
            print(f"❌ Configuration file is empty: {filepath}")
            return False
            
        errors = validate_config(config)
        
        if errors:
            print(f"❌ Configuration validation failed:")
            for error in errors:
                print(f"   • {error}")
            return False
        
        return True
        
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON in {filepath}: {e}")
        return False
    except Exception as e:
        print(f"❌ Error reading {filepath}: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cv_validator.py <config_file.json|yaml>")
        sys.exit(1)
    
    config_file = sys.argv[1]
    if validate_config_file(config_file):
        print(f"✅ Configuration file '{config_file}' is valid")
        sys.exit(0)
    else:
        sys.exit(1)