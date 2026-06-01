from pathlib import Path

import polars as pl
import logging


def read_dataset(path: str) -> pl.DataFrame:
    """
    Read a dataset from file into a Polars DataFrame.

    Supports: .csv, .tsv, .xlsx, .xls, .json, .jsonl, .parquet, .pq

    Args:
        path: Path to the dataset file.

    Returns:
        Polars DataFrame containing the dataset.

    Raises:
        ValueError: If the file type is not supported.
    """
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"The file '{path}' does not exist.")
    
    if file_path.stat().st_size == 0:
        logging.info(f"The file '{path}' is empty. Returning an empty DataFrame.")
        return pl.DataFrame()

    suffix = file_path.suffix.lower()

    try:
        if suffix == ".csv":
            return pl.read_csv(file_path)

        if suffix == ".tsv":
            return pl.read_csv(file_path, separator="\t")

        if suffix in [".xlsx", ".xls"]:
            return pl.read_excel(file_path)

        if suffix == ".json":
            return pl.read_json(file_path)

        if suffix == ".jsonl":
            return pl.read_ndjson(file_path)

        if suffix in [".parquet", ".pq"]:
            return pl.read_parquet(file_path)

    except Exception as e:
        logging.warning(f"Could not read file '{path}': {e}. Returning empty DataFrame.")
        return pl.DataFrame()

    raise ValueError(
        f"Unsupported file type: {suffix}. "
        "Supported types: ['.csv', '.tsv', '.json', '.jsonl', '.parquet', '.xls', '.xlsx']"
    )