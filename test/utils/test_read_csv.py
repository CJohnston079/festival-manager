import csv
import os
import pytest

from src.utils.read_csv import read_csv


@pytest.mark.xfail
class TestReadCSV:
    @pytest.fixture
    def temp_csv_file(self):
        file_name = "test.csv"
        test_data = [
            {"name": "Janet", "section": "Dance"},
            {"name": "Saam", "section": "Pianoforte"},
            {"name": "Nihira", "section": "Speech & Drama"},
        ]
        with open(file_name, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "section"])
            writer.writeheader()
            writer.writerows(test_data)

        yield file_name, test_data

        if os.path.exists(file_name):
            os.remove(file_name)
    
    def test_returns_list_of_dicts(self, temp_csv_file):
        file_name, expected_data = temp_csv_file
        result = read_csv(file_name)
        assert isinstance(result, list), (
            f"expected a list, received {type(result).__name__}"
        )
        assert all(isinstance(item, dict) for item in result), (
            f"one or more list item is not a dictionary: {result}"
        )

    def test_returns_expected_data(self, temp_csv_file):
        file_name, expected_data = temp_csv_file
        result = read_csv(file_name)
        assert result == expected_data
