"""Configuration loader for CV generator with JSON and YAML support."""

import json
import os
import re
import sys
from typing import Dict, Any
import yaml

def load_config(config_path: str) -> Dict[str, Any]:
    """
    Load configuration from JSON or YAML file.
    
    Args:
        config_path: Path to the configuration file
        
    Returns:
        Dictionary with configuration data
        
    Raises:
        FileNotFoundError: If the configuration file doesn't exist
        ValueError: If the file format is not supported
        json.JSONDecodeError: If JSON parsing fails
        yaml.YAMLError: If YAML parsing fails
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    
    file_ext = os.path.splitext(config_path)[1].lower()
    
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            if file_ext == '.json':
                config = json.load(f)
            elif file_ext in ['.yaml', '.yml']:
                config = yaml.safe_load(f)
            else:
                raise ValueError(f"Unsupported file format: {file_ext}. Use .json, .yaml or .yml")
        
        # Validate required fields
        required_fields = ['name', 'title', 'email', 'phone']
        for field in required_fields:
            if field not in config:
                raise ValueError(f"Missing required field: {field}")
        
        # Sanitize AI-related terms
        if 'summary' in config:
            config['summary'] = re.sub(r'\bAl\b', 'AI', config['summary'], flags=re.IGNORECASE)
        if 'experience' in config:
            for exp in config['experience']:
                if 'description' in exp:
                    exp['description'] = re.sub(r'\bAl\b', 'AI', exp['description'], flags=re.IGNORECASE)
        
        return config
    
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON format: {e}", e.doc, e.pos)
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Invalid YAML format: {e}")