"""Configuration loader for CV generator."""

import json
import os
import sys
from typing import Dict, Any


def load_config(config_path: str = "cv_config.json") -> Dict[str, Any]:
    """
    Load CV configuration from a JSON file.
    
    Args:
        config_path: Path to the JSON configuration file
        
    Returns:
        Dictionary containing CV configuration data
        
    Raises:
        FileNotFoundError: If the config file doesn't exist
        json.JSONDecodeError: If the config file contains invalid JSON
        ValueError: If required fields are missing
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON in configuration file: {e}", e.doc, e.pos)
    
    # Validate required fields
    required_fields = ['name', 'title', 'email', 'phone']
    missing_fields = [field for field in required_fields if field not in config]
    
    if missing_fields:
        raise ValueError(f"Missing required fields in configuration: {', '.join(missing_fields)}")
    
    return config


def validate_config(config: Dict[str, Any]) -> None:
    """
    Soft validation: warns about missing optional sections but doesn't fail.
    
    Args:
        config: Configuration dictionary to validate
    """
    optional_sections = {
        'summary': 'professional summary',
        'experience': 'work experience',
        'education': 'education history',
        'skills': 'skills list',
        'languages': 'languages',
        'certifications': 'certifications',
        'projects': 'projects',
    }
    
    for section, label in optional_sections.items():
        if section not in config:
            print(f"Note: '{section}' section ({label}) not found in config.", file=sys.stderr)