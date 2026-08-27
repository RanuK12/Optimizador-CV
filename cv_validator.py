"""Validator for CV configuration files."""

import re
import json
from typing import Dict, Any, List
from typing_extensions import TypedDict

# Define required fields structure
RequiredFields = TypedDict('RequiredFields', {
    'personal': List[str],
    'experience': List[str],
    'education': List[str]
})

# Define required fields
REQUIRED_FIELDS: RequiredFields = {
    'personal': ['name', 'title', 'email', 'phone'],
    'experience': ['company', 'title', 'dates'],
    'education': ['degree', 'institution', 'dates']
}

# Define optional fields
OPTIONAL_FIELDS = {
    'personal': ['linkedin', 'github', 'summary'],
    'experience': ['description'],
    'education': []
}

# Valid email regex pattern
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Valid date patterns
DATE_PATTERNS = [
    r'^\d{4} - \d{4}$',  # YYYY - YYYY
    r'^\d{4} - Presente$',  # YYYY - Presente
    r'^\d{4} - actualidad$',  # YYYY - actualidad
    r'^\d{4} - now$',  # YYYY - now
    r'^\d{4} - Present$',  # YYYY - Present
]


class CVValidationError(Exception):
    """Exception raised when CV configuration validation fails."""
    pass


class CVValidator:
    """Validator for CV configuration files."""
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate email format."""
        return re.match(EMAIL_REGEX, email) is not None
    
    @staticmethod
    def validate_date(date: str) -> bool:
        """Validate date format."""
        for pattern in DATE_PATTERNS:
            if re.match(pattern, date):
                return True
        return False
    
    @staticmethod
    def validate_required_fields(config: Dict[str, Any], section: str, required: List[str]) -> None:
        """Validate that all required fields exist in a section."""
        if section == 'personal':
            # Personal fields are at the top level of config
            for field in required:
                if field not in config:
                    raise CVValidationError(f"Missing required field '{field}'")
        else:
            # Other sections are nested
            section_data = config.get(section, {})
            for field in required:
                if field not in section_data:
                    raise CVValidationError(f"Missing required field '{field}' in {section} section")
    
    @staticmethod
    def validate_unknown_fields(config: Dict[str, Any], section: str, valid_fields: List[str]) -> None:
        """Validate that there are no unknown fields in a section."""
        section_data = config.get(section, {})
        for field in section_data:
            if field not in valid_fields:
                raise CVValidationError(f"Unknown field '{field}' found in {section} section")
    
    @staticmethod
    def validate_experience(experience: List[Dict[str, Any]]) -> None:
        """Validate experience section."""
        if not isinstance(experience, list):
            raise CVValidationError("Experience must be a list")
        
        for i, exp in enumerate(experience):
            if not isinstance(exp, dict):
                raise CVValidationError(f"Experience item {i} must be a dictionary")
            
            # Check required fields
            CVValidator.validate_required_fields(
                {'experience': exp}, 
                'experience', 
                REQUIRED_FIELDS['experience']
            )
            
            # Check date format
            if not CVValidator.validate_date(exp['dates']):
                raise CVValidationError(f"Invalid date format in experience item {i}: {exp['dates']}")
    
    @staticmethod
    def validate_education(education: List[Dict[str, Any]]) -> None:
        """Validate education section."""
        if not isinstance(education, list):
            raise CVValidationError("Education must be a list")
        
        for i, edu in enumerate(education):
            if not isinstance(edu, dict):
                raise CVValidationError(f"Education item {i} must be a dictionary")
            
            # Check required fields
            CVValidator.validate_required_fields(
                {'education': edu}, 
                'education', 
                REQUIRED_FIELDS['education']
            )
            
            # Check date format
            if not CVValidator.validate_date(edu['dates']):
                raise CVValidationError(f"Invalid date format in education item {i}: {edu['dates']}")
    
    @staticmethod
    def validate_skills(skills: List[str]) -> None:
        """Validate skills section."""
        if not isinstance(skills, list):
            raise CVValidationError("Skills must be a list")
        
        for skill in skills:
            if not isinstance(skill, str):
                raise CVValidationError("All skills must be strings")
            if not skill.strip():
                raise CVValidationError("Empty skill found")
    
    @staticmethod
    def validate(config: Dict[str, Any]) -> bool:
        """
        Validate CV configuration.
        
        Args:
            config: Dictionary with configuration data
            
        Returns:
            True if configuration is valid
            
        Raises:
            CVValidationError: If validation fails with specific error message
        """
        # Check personal information
        CVValidator.validate_required_fields(config, 'personal', REQUIRED_FIELDS['personal'])
        
        # Validate email
        if not CVValidator.validate_email(config['email']):
            raise CVValidationError(f"Invalid email format: {config['email']}")
        
        # Check unknown fields in personal section
        all_personal_fields = REQUIRED_FIELDS['personal'] + OPTIONAL_FIELDS['personal']
        CVValidator.validate_unknown_fields(config, 'personal', all_personal_fields)
        
        # Validate experience if present
        if 'experience' in config:
            CVValidator.validate_experience(config['experience'])
        
        # Validate education if present
        if 'education' in config:
            CVValidator.validate_education(config['education'])
        
        # Validate skills if present
        if 'skills' in config:
            CVValidator.validate_skills(config['skills'])
        
        # Validate summary if present
        if 'summary' in config:
            if not isinstance(config['summary'], str):
                raise CVValidationError("Summary must be a string")
        
        return True


def validate_config_file(config_path: str) -> bool:
    """
    Validate a CV configuration file.
    
    Args:
        config_path: Path to the configuration file
        
    Returns:
        True if configuration is valid
        
    Raises:
        FileNotFoundError: If the configuration file doesn't exist
        CVValidationError: If validation fails
        json.JSONDecodeError: If JSON parsing fails
    """
    if not config_path.endswith(('.json', '.yaml', '.yml')):
        raise CVValidationError("Configuration file must be .json, .yaml or .yml")
    
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            if config_path.endswith('.json'):
                config = json.load(f)
            else:
                # For YAML files, we need PyYAML but we'll handle it separately
                # For now, just check if it's a dict
                import yaml
                config = yaml.safe_load(f)
        
        return CVValidator.validate(config)
    
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON format: {e}", e.doc, e.pos)
    except Exception as e:
        raise CVValidationError(f"Error loading configuration: {str(e)}")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Validate CV configuration file")
    parser.add_argument("config", help="Path to configuration file")
    args = parser.parse_args()
    
    try:
        if validate_config_file(args.config):
            print(f"✅ Configuration file {args.config} is valid")
    except Exception as e:
        print(f"❌ Validation failed: {str(e)}")
        exit(1)