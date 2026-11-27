"""Tests para el validador de configuración del CV (cv_validator.py)."""

import os
import sys
import json
import tempfile

import pytest
import yaml

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cv_validator import validate_config, validate_config_file, validate_config_or_raise, CVValidationError


VALID_CONFIG = {
    "name": "Emilio Ranucoli",
    "title": "Machine Learning Engineer",
    "email": "emilio@example.com",
    "phone": "+54 9 11 5555 5555",
    "linkedin": "https://linkedin.com/in/emilioranucoli",
    "github": "https://github.com/RanuK12",
    "summary": "ML engineer with 10+ years experience.",
    "experience": [
        {
            "company": "Acme",
            "title": "ML Engineer",
            "dates": "2020-2024",
            "description": "Built ML systems.",
        }
    ],
    "education": [
        {
            "degree": "MSc",
            "institution": "MIT",
            "dates": "2018-2020",
        }
    ],
    "skills": ["Python", "PyTorch", "AWS"],
}


def test_valid_config_has_no_errors():
    assert validate_config(VALID_CONFIG) == []


def test_missing_required_fields():
    config = {"title": "ML Engineer"}
    errors = validate_config(config)
    assert len(errors) > 0
    assert any("Missing required field 'name'" in e for e in errors)
    assert any("Missing required field 'email'" in e for e in errors)


def test_empty_required_fields():
    config = {
        "name": "   ",
        "title": "",
        "email": "",
        "phone": "",
    }
    errors = validate_config(config)
    assert len(errors) > 0
    assert any("must be a non-empty string" in e for e in errors)


def test_invalid_email():
    config = dict(VALID_CONFIG, email="not-an-email")
    errors = validate_config(config)
    assert any("must be a valid email address" in e for e in errors)


def test_linkedin_must_be_url_or_null():
    config = dict(VALID_CONFIG, linkedin="linkedin.com/in/emilio")
    errors = validate_config(config)
    assert any("must be a valid URL or null" in e for e in errors)


def test_github_must_be_url_or_null():
    config = dict(VALID_CONFIG, github=None)
    assert validate_config(config) == []


def test_summary_none_is_valid():
    config = dict(VALID_CONFIG, summary=None)
    assert validate_config(config) == []


def test_summary_must_be_string_or_null():
    config = dict(VALID_CONFIG, summary=123)
    errors = validate_config(config)
    assert any("must be a string or null" in e for e in errors)


def test_experience_must_be_list_of_objects():
    config = dict(VALID_CONFIG, experience="not-a-list")
    errors = validate_config(config)
    assert any("must be a list" in e for e in errors)


def test_experience_item_missing_required_field():
    config = dict(VALID_CONFIG, experience=[{"company": "Acme"}])
    errors = validate_config(config)
    assert any("Experience item 0 missing required field 'title'" in e for e in errors)


def test_education_must_be_list_of_objects():
    config = dict(VALID_CONFIG, education="not-a-list")
    errors = validate_config(config)
    assert any("must be a list" in e for e in errors)


def test_education_item_missing_required_field():
    config = dict(VALID_CONFIG, education=[{"degree": "MSc"}])
    errors = validate_config(config)
    assert any("Education item 0 missing required field 'institution'" in e for e in errors)


def test_skills_must_be_list_of_strings():
    config = dict(VALID_CONFIG, skills="Python")
    errors = validate_config(config)
    assert any("must be a list" in e for e in errors)


def test_validate_config_or_raise_raises():
    with pytest.raises(CVValidationError):
        validate_config_or_raise({"name": "x"})


def test_validate_config_file_json_valid(tmp_path):
    path = tmp_path / "config.json"
    path.write_text(json.dumps(VALID_CONFIG), encoding="utf-8")
    assert validate_config_file(str(path)) is True


def test_validate_config_file_json_invalid(tmp_path):
    path = tmp_path / "config.json"
    path.write_text(json.dumps({"name": "x"}), encoding="utf-8")
    assert validate_config_file(str(path)) is False


def test_validate_config_file_yaml_valid(tmp_path):
    path = tmp_path / "config.yaml"
    path.write_text(yaml.safe_dump(VALID_CONFIG), encoding="utf-8")
    assert validate_config_file(str(path)) is True


def test_validate_config_file_not_found():
    assert validate_config_file("/tmp/definitely_not_a_file_xyz.json") is False


def test_validate_config_file_unsupported_format(tmp_path):
    path = tmp_path / "config.txt"
    path.write_text("hello", encoding="utf-8")
    assert validate_config_file(str(path)) is False


def test_validate_config_file_empty(tmp_path):
    path = tmp_path / "config.yaml"
    path.write_text("", encoding="utf-8")
    assert validate_config_file(str(path)) is False
