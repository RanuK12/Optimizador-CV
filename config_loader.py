"""Configuration loader for CV generator."""

import json
import os
from typing import Dict, Any, Optional

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
    Validate the configuration data structure.
    
    Args:
        config: Configuration dictionary to validate
        
    Raises:
        ValueError: If configuration structure is invalid
    """
    # Check if all main sections exist
    required_sections = ['experience', 'education', 'skills', 'languages']
    missing_sections = [section for section in required_sections if section not in config]
    
    if missing_sections:
        raise ValueError(f"Missing required sections in configuration: {', '.join(missing_sections)}")
    
    # Validate experience section
    if not isinstance(config['experience'], list):
        raise ValueError("'experience' must be a list")
    
    for exp in config['experience']:
        if not all(key in exp for key in ['role', 'company', 'location']):
            raise ValueError("Each experience entry must have 'role', 'company', and 'location'")
    
    # Validate education section
    if not isinstance(config['education'], list):
        raise ValueError("'education' must be a list")
    
    for edu in config['education']:
        if not all(key in edu for key in ['degree', 'institution']):
            raise ValueError("Each education entry must have 'degree' and 'institution'")
    
    # Validate skills section
    if 'skills' not in config:
        raise ValueError("'skills' section is required")
    
    # Validate languages section
    if not isinstance(config['languages'], list):
        raise ValueError("'languages' must be a list")
    
    for lang in config['languages']:
        if not all(key in lang for key in ['language', 'proficiency']):
            raise ValueError("Each language entry must have 'language' and 'proficiency'")