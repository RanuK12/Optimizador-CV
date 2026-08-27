#!/usr/bin/env python3
"""
Demo script showing how to use the CV generator with validation.
This script demonstrates:
1. How to create a valid CV configuration
2. How to validate a configuration file
3. How to generate a CV from a validated configuration
"""

import os
import sys
import json
import argparse
from pathlib import Path

# Add current directory to path to import modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from build_cv import main as build_cv_main
from cv_validator import validate_config_file, CVValidationError

def create_demo_config(output_path: str):
    """Create a demo configuration file."""
    demo_config = {
        "name": "Jane Smith",
        "title": "Senior Data Scientist",
        "email": "jane.smith@example.com",
        "phone": "+1 (555) 987-6543",
        "linkedin": "https://linkedin.com/in/janesmith",
        "github": "https://github.com/janesmith",
        "summary": "Data scientist with 6+ years of experience in machine learning, statistical analysis, and data visualization. Expert in translating complex data insights into actionable business strategies.",
        "experience": [
            {
                "company": "Analytics Corp",
                "title": "Senior Data Scientist",
                "dates": "2018 - Present",
                "description": "Developed predictive models increasing customer retention by 25%. Led team of 3 data scientists. Implemented A/B testing framework resulting in 15% improvement in conversion rates."
            },
            {
                "company": "Data Solutions Ltd.",
                "title": "Data Scientist",
                "dates": "2016 - 2018",
                "description": "Built recommendation systems for e-commerce platform. Created data pipelines processing 10M+ records daily. Collaborated with engineering team to deploy models to production."
            }
        ],
        "education": [
            {
                "degree": "Master of Science in Data Science",
                "institution": "University of Data Science",
                "dates": "2014 - 2016"
            },
            {
                "degree": "Bachelor of Science in Statistics",
                "institution": "State University",
                "dates": "2010 - 2014"
            }
        ],
        "skills": [
            "Python",
            "R",
            "SQL",
            "Machine Learning",
            "Statistical Analysis",
            "Data Visualization",
            "TensorFlow",
            "PyTorch",
            "Spark",
            "AWS"
        ]
    }
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(demo_config, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Created demo configuration file: {output_path}")
    return demo_config

def test_validation(config_path: str):
    """Test configuration validation."""
    print(f"\n🔍 Testing validation for: {config_path}")
    
    try:
        is_valid = validate_config_file(config_path)
        print(f"✅ Configuration is valid: {is_valid}")
        return True
    except CVValidationError as e:
        print(f"❌ Validation failed: {str(e)}")
        return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def test_cv_generation(config_path: str):
    """Test CV generation."""
    print(f"\n📄 Testing CV generation for: {config_path}")
    
    # Mock command line arguments
    sys.argv = ['build_cv.py', config_path, '--output', 'demo_cv']
    
    try:
        build_cv_main()
        print("✅ CV generation completed successfully")
        return True
    except Exception as e:
        print(f"❌ CV generation failed: {str(e)}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Demo script for CV generator with validation")
    parser.add_argument("--create-demo", action="store_true", help="Create demo configuration file")
    parser.add_argument("--validate", action="store_true", help="Validate configuration file")
    parser.add_argument("--generate", action="store_true", help="Generate CV from configuration")
    parser.add_argument("--config", default="demo_config.json", help="Configuration file to use")
    
    args = parser.parse_args()
    
    # Create demo config if requested
    if args.create_demo:
        create_demo_config(args.config)
    
    # Validate config if requested
    if args.validate:
        test_validation(args.config)
    
    # Generate CV if requested
    if args.generate:
        test_cv_generation(args.config)
    
    # Run all steps if no specific action requested
    if not any([args.create_demo, args.validate, args.generate]):
        print("Running full demo process...")
        
        # Step 1: Create demo config
        create_demo_config(args.config)
        
        # Step 2: Validate config
        if test_validation(args.config):
            # Step 3: Generate CV
            test_cv_generation(args.config)
        else:
            print("❌ Demo aborted due to validation failure")

if __name__ == "__main__":
    main()