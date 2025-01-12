import pytest

from src.add_entrants_to_lesson import add_entrants_to_lesson


class TestAddEntrantsToLesson:
    @pytest.fixture
    def test_data(self):
        test_lesson_data = [
            {
                "Number": "001",
                "Name": "PIANO BEGINNERS",
                "Description": "Own choice.",
                "Max Duration": "3",
            },
            {
                "Number": "002",
                "Name": "PIANO INTERMEDIATE",
                "Description": "Own choice.",
                "Max Duration": "4",
            },
            {
                "Number": "003",
                "Name": "PIANO ADVANCED",
                "Description": "Own choice.",
                "Max Duration": "5",
            }
        ]
        test_entrant_data = [
            {"Class Number": "001"},
            {"Class Number": "001"},
            {"Class Number": "001"},
            {"Class Number": "001"},
            {"Class Number": "002"},
            {"Class Number": "002"},
            {"Class Number": "002"},
            {"Class Number": "003"}
        ]

        return test_lesson_data, test_entrant_data

    def test_add_entrants_to_lesson(self, test_data, mocker):
        lessons_data, entrants_data = test_data

        mocker.patch(
            "src.add_entrants_to_lesson.read_csv",
            side_effect=lambda file_path: (
                lessons_data if "lesson" in file_path else entrants_data
            )
        )
        expected = [
            {
                "Number": "001",
                "Name": "PIANO BEGINNERS",
                "Max Duration": "3",
                "Number of entries": 4
            },
            {
                "Number": "002",
                "Name": "PIANO INTERMEDIATE",
                "Max Duration": "4",
                "Number of entries": 3
            },
            {
                "Number": "003",
                "Name": "PIANO ADVANCED",
                "Max Duration": "5",
                "Number of entries": 1
            }
        ]
        result = add_entrants_to_lesson("lessons.csv", "entrants.csv")

        assert result == expected
