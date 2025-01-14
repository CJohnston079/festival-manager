import pytest

from src.calculate_lesson_time import calculate_lesson_time


@pytest.mark.xfail
class TestCalculateLessonTime():
    @pytest.mark.parametrize(
        "entries, allocated_time, expected",
        [(10, 5, 70), (6, 8, 70), (3, 12, 50), (0, 5, 0)],
    )
    def test_calculate_lesson_time(self, entries, allocated_time, expected):
        result = calculate_lesson_time(entries, allocated_time)
        assert result == expected
