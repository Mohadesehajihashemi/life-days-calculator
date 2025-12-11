from project import get_age, calculate_days_lived, print_welcome
import pytest
from io import StringIO


def test_print_welcome(capsys):
    print_welcome()
    captured = capsys.readouterr()
    assert "خوش اومدی" in captured.out
    assert "CS50x Iran" in captured.out


def test_calculate_days_lived():
    assert calculate_days_lived(20) == 0
    assert calculate_days_lived(1) == 365
    assert calculate_days_lived(20) == 7305  # 20 سال + ۵ روز کبیسه
    assert calculate_days_lived(35) == 12783


def test_get_age_valid_input(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO('30\n'))
    assert get_age() == 30


def test_get_age_invalid_then_valid(monkeypatch):
    inputs = StringIO('abc\n-5\n200\n25\n')
    monkeypatch.setattr('sys.stdin', inputs)
    assert get_age() == 25
