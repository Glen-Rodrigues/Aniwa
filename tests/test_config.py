"""Tests for configuration loading and flattening."""

import pytest
import tempfile
from pathlib import Path

from aniwa.config_loader import (
    load_config,
    get_flattened_config,
    SUPPORTED_CONFIG_EXTENSIONS,
)


def test_load_config_missing_file():
    """Test loading a non-existent config file raises error."""
    with pytest.raises(ValueError, match="Configuration file not found"):
        load_config("non_existent_file.yaml")


def test_load_config_unsupported_extension():
    """Test loading config with unsupported extension raises error."""
    with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as f:
        f.write(b"mode: deep")
        f.close()
        
        try:
            with pytest.raises(ValueError, match="Unsupported configuration file type"):
                load_config(f.name)
        finally:
            Path(f.name).unlink()


def test_load_config_empty_yaml(tmp_path):
    """Test loading empty YAML file returns empty dict."""
    config_file = tmp_path / "aniwa.yaml"
    config_file.write_text("", encoding="utf-8")
    
    result = load_config(str(config_file))
    assert result == {}


def test_load_config_valid_yaml(tmp_path):
    """Test loading valid YAML config file."""
    config_file = tmp_path / "aniwa.yaml"
    config_file.write_text(
        """
mode: deep
report:
  format: html
  template: enterprise
sections:
  include:
    - summary
    - schema
    - quality
verbosity: verbose
""",
        encoding="utf-8",
    )
    
    result = load_config(str(config_file))
    assert result["mode"] == "deep"
    assert result["report"]["format"] == "html"
    assert result["report"]["template"] == "enterprise"
    assert result["sections"]["include"] == ["summary", "schema", "quality"]
    assert result["verbosity"] == "verbose"


def test_load_config_invalid_yaml(tmp_path):
    """Test loading invalid YAML raises error."""
    config_file = tmp_path / "aniwa.yaml"
    config_file.write_text("mode: [deep", encoding="utf-8")
    
    with pytest.raises(ValueError, match="Error parsing config file"):
        load_config(str(config_file))


def test_load_config_valid_json(tmp_path):
    """Test loading valid JSON config file."""
    config_file = tmp_path / "aniwa.json"
    config_file.write_text(
        """
{
    "mode": "fast",
    "report": {
        "format": "json"
    },
    "verbosity": "quiet"
}
""",
        encoding="utf-8",
    )
    
    result = load_config(str(config_file))
    assert result["mode"] == "fast"
    assert result["report"]["format"] == "json"
    assert result["verbosity"] == "quiet"


def test_load_config_invalid_json(tmp_path):
    """Test loading invalid JSON raises error."""
    config_file = tmp_path / "aniwa.json"
    config_file.write_text('{"mode": "deep"', encoding="utf-8")
    
    with pytest.raises(ValueError, match="Error parsing config file"):
        load_config(str(config_file))


def test_load_config_valid_toml(tmp_path):
    """Test loading valid TOML config file."""
    config_file = tmp_path / "aniwa.toml"
    config_file.write_text(
        """
mode = "deep"

[report]
format = "html"
template = "dark"

[sections]
include = ["summary", "schema"]

verbosity = "debug"
""",
        encoding="utf-8",
    )
    
    result = load_config(str(config_file))
    assert result["mode"] == "deep"
    assert result["report"]["format"] == "html"
    assert result["report"]["template"] == "dark"
    assert result["sections"]["include"] == ["summary", "schema"]
    assert result["verbosity"] == "debug"


def test_get_flattened_config_missing_file():
    """Test missing config file returns empty dict."""
    result = get_flattened_config("non_existent_file.yaml")
    assert result == {}


def test_get_flattened_config_empty_yaml(tmp_path):
    """Test empty YAML config returns empty dict."""
    config_file = tmp_path / "aniwa.yaml"
    config_file.write_text("", encoding="utf-8")
    
    result = get_flattened_config(str(config_file))
    assert result == {}


def test_get_flattened_config_with_mode(tmp_path):
    """Test flattening config with mode."""
    config_file = tmp_path / "aniwa.yaml"
    config_file.write_text("mode: fast", encoding="utf-8")
    
    result = get_flattened_config(str(config_file))
    assert result["mode"] == "fast"


def test_get_flattened_config_invalid_mode(tmp_path):
    """Test invalid mode raises error."""
    config_file = tmp_path / "aniwa.yaml"
    config_file.write_text("mode: invalid", encoding="utf-8")
    
    with pytest.raises(ValueError, match="Invalid mode in config"):
        get_flattened_config(str(config_file))


def test_get_flattened_config_with_report(tmp_path):
    """Test flattening config with report section."""
    config_file = tmp_path / "aniwa.yaml"
    config_file.write_text(
        """
report:
  format: html
  template: clean
  output: custom.html
  output_dir: ./reports
""",
        encoding="utf-8",
    )
    
    result = get_flattened_config(str(config_file))
    assert result["report"] == "html"
    assert result["template"] == "clean"
    assert result["output"] == "custom.html"
    assert result["output_dir"] == "./reports"


def test_get_flattened_config_report_not_dict(tmp_path):
    """Test report section not being a dict raises error."""
    config_file = tmp_path / "aniwa.yaml"
    config_file.write_text("report: string", encoding="utf-8")
    
    with pytest.raises(ValueError, match="'report' must be an object"):
        get_flattened_config(str(config_file))


def test_get_flattened_config_with_sections_include(tmp_path):
    """Test flattening config with sections include."""
    config_file = tmp_path / "aniwa.yaml"
    config_file.write_text(
        """
sections:
  include:
    - summary
    - schema
    - quality
""",
        encoding="utf-8",
    )
    
    result = get_flattened_config(str(config_file))
    assert result["include"] == "summary,schema,quality"


def test_get_flattened_config_with_sections_exclude(tmp_path):
    """Test flattening config with sections exclude."""
    config_file = tmp_path / "aniwa.yaml"
    config_file.write_text(
        """
sections:
  exclude:
    - statistics
    - charts
""",
        encoding="utf-8",
    )
    
    result = get_flattened_config(str(config_file))
    assert result["exclude"] == "statistics,charts"


def test_get_flattened_config_sections_both_include_exclude(tmp_path):
    """Test using both include and exclude in sections raises error."""
    config_file = tmp_path / "aniwa.yaml"
    config_file.write_text(
        """
sections:
  include:
    - summary
  exclude:
    - statistics
""",
        encoding="utf-8",
    )
    
    with pytest.raises(ValueError, match="use either sections.include or sections.exclude"):
        get_flattened_config(str(config_file))


def test_get_flattened_config_sections_not_dict(tmp_path):
    """Test sections not being a dict raises error."""
    config_file = tmp_path / "aniwa.yaml"
    config_file.write_text("sections: list", encoding="utf-8")
    
    with pytest.raises(ValueError, match="'sections' must be an object"):
        get_flattened_config(str(config_file))


def test_get_flattened_config_sections_include_not_list(tmp_path):
    """Test sections.include not being a list raises error."""
    config_file = tmp_path / "aniwa.yaml"
    config_file.write_text("sections:\n  include: string", encoding="utf-8")
    
    with pytest.raises(ValueError, match="sections.include must be a list"):
        get_flattened_config(str(config_file))


def test_get_flattened_config_sections_exclude_not_list(tmp_path):
    """Test sections.exclude not being a list raises error."""
    config_file = tmp_path / "aniwa.yaml"
    config_file.write_text("sections:\n  exclude: string", encoding="utf-8")
    
    with pytest.raises(ValueError, match="sections.exclude must be a list"):
        get_flattened_config(str(config_file))


def test_get_flattened_config_with_verbosity(tmp_path):
    """Test flattening config with verbosity."""
    config_file = tmp_path / "aniwa.yaml"
    config_file.write_text("verbosity: debug", encoding="utf-8")
    
    result = get_flattened_config(str(config_file))
    assert result["verbosity"] == "debug"


def test_get_flattened_config_complete(tmp_path):
    """Test flattening a complete config file."""
    config_file = tmp_path / "aniwa.yaml"
    config_file.write_text(
        """
mode: deep
report:
  format: html
  template: enterprise
  output_dir: ./reports
sections:
  include:
    - summary
    - schema
    - quality
    - statistics
    - insights
verbosity: verbose
""",
        encoding="utf-8",
    )
    
    result = get_flattened_config(str(config_file))
    assert result["mode"] == "deep"
    assert result["report"] == "html"
    assert result["template"] == "enterprise"
    assert result["output_dir"] == "./reports"
    assert result["include"] == "summary,schema,quality,statistics,insights"
    assert result["verbosity"] == "verbose"


def test_supported_extensions():
    """Test that supported extensions are correctly defined."""
    expected_extensions = {".yaml", ".yml", ".toml", ".json"}
    assert SUPPORTED_CONFIG_EXTENSIONS == expected_extensions