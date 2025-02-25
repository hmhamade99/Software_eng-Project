import pandas as pd
from .base_loader import DataLoader


class CSVLoader(DataLoader):
    def load_data(self, file_path: str) -> pd.DataFrame:
        """Load data from a CSV file.

        Args:
            file_path (str): The path to the CSV file.

        Returns:
            pd.DataFrame: The loaded data as a DataFrame.
        """
        return pd.read_csv(file_path)
