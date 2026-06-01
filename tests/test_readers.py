import pytest
import tempfile
import polars as pl
from pathlib import Path

from aniwa.io.readers import read_dataset


def test_read_csv(tmp_path):
    file_path = tmp_path / "customers.csv"
    file_path.write_text("id,name\n1,Ama\n2,Kofi\n", encoding="utf-8")

    df = read_dataset(str(file_path))

    assert df.shape == (2, 2)
    assert df.columns == ["id", "name"]


def test_read_json(tmp_path):
    file_path = tmp_path / "customers.json"
    file_path.write_text(
        '[{"id": 1, "name": "Ama"}, {"id": 2, "name": "Kofi"}]',
        encoding="utf-8",
    )

    df = read_dataset(str(file_path))

    assert df.shape == (2, 2)
    assert df.columns == ["id", "name"]


def test_read_parquet(tmp_path):
    file_path = tmp_path / "customers.parquet"

    original_df = pl.DataFrame(
        {
            "id": [1, 2],
            "name": ["Ama", "Kofi"],
        }
    )
    original_df.write_parquet(file_path)

    df = read_dataset(str(file_path))

    assert df.shape == (2, 2)
    assert df.columns == ["id", "name"]


def test_read_excel(tmp_path):
    file_path = tmp_path / "customers.xlsx"

    original_df = pl.DataFrame(
        {
            "id": [1, 2],
            "name": ["Ama", "Kofi"],
        }
    )
    original_df.write_excel(file_path)

    df = read_dataset(str(file_path))

    assert df.shape == (2, 2)
    assert df.columns == ["id", "name"]


def test_read_xls_dispatches_to_excel_reader(tmp_path, monkeypatch):
    file_path = tmp_path / "customers.xls"
    file_path.write_text("fake excel content", encoding="utf-8")

    called = {"value": False}

    def fake_read_excel(path):
        called["value"] = True
        return pl.DataFrame({"id": [1], "name": ["Ama"]})

    monkeypatch.setattr(pl, "read_excel", fake_read_excel)

    df = read_dataset(str(file_path))

    assert called["value"] is True
    assert df.shape == (1, 2)
    assert df.columns == ["id", "name"]


def test_unsupported_file_type(tmp_path):
    file_path = tmp_path / "customers.txt"
    file_path.write_text("id,name\n1,Ama\n", encoding="utf-8")

    try:
        read_dataset(str(file_path))
    except ValueError as exc:
        assert "Unsupported file type" in str(exc)
    else:
        raise AssertionError("Expected ValueError for unsupported file type")

def test_read_tsv(tmp_path):
    file_path = tmp_path / "customers.tsv"
    file_path.write_text(
        "id\tname\tcountry\n1\tAma\tGhana\n2\tKofi\tGhana\n",
        encoding="utf-8",
    )

    df = read_dataset(str(file_path))

    assert df.shape == (2, 3)
    assert df.columns == ["id", "name", "country"]

def test_read_jsonl(tmp_path):
    file_path = tmp_path / "events.jsonl"
    file_path.write_text(
        '{"id": 1, "event": "signup", "country": "Ghana"}\n'
        '{"id": 2, "event": "purchase", "country": "Nigeria"}\n',
        encoding="utf-8",
    )

    df = read_dataset(str(file_path))

    assert df.shape == (2, 3)
    assert df.columns == ["id", "event", "country"]

def test_empty_csv_file():
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        # Option 1: Completely empty file
        # f.write("")  # File is already empty
        
        # Option 2: Headers only, no data (uncomment if you prefer)
        # f.write("column1,column2,column3\n")
        f.close()
        
        temp_path = Path(f.name)
        
        try:
            # Try to read the empty file
            df = read_dataset(str(temp_path))
            
            # Assertions - verify it doesn't crash
            assert df is not None
            assert isinstance(df, pl.DataFrame)
            # Empty file should have 0 rows
            assert df.height == 0
            
        finally:
            # Clean up - delete the temporary file
            temp_path.unlink()

def test_empty_csv_file_with_headers():   
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        f.write("name,age,email\n")  # Headers only, no data
        f.close()
        
        temp_path = Path(f.name)
        
        try:
            df = read_dataset(str(temp_path))
            
            assert df is not None
            assert isinstance(df, pl.DataFrame)
            # Should have 0 rows but columns defined
            assert df.height == 0
            assert df.width == 3  # Three columns from headers
            
        finally:
            temp_path.unlink()

def test_completely_empty_file():
    """Test completely empty file (0 bytes)."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        # Write nothing - file is empty
        pass
        # ... rest of test

def test_file_with_only_newlines():
    """Test file containing only newlines."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        f.write("\n\n\n")
        # ... rest of test

@pytest.mark.parametrize("content", [
    "",           # Empty file
    "\n",         # Just newline
    "a,b,c\n",    # Headers only
    "a,b,c\n\n\n", # Headers with empty lines
])
def test_empty_csv_variations(content):
    """Test various empty CSV scenarios."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        f.write(content)
        # ... rest of test