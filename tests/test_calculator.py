import pytest
import sys
from calculator import evaluate, main

def test_evaluate_simple_addition():
    assert evaluate("2 + 3") == 5

def test_evaluate_with_parentheses():
    assert evaluate("(10 - 2) / 4 * 2") == 4.0

def test_evaluate_division_float():
    assert evaluate("1 / 2") == 0.5

def test_evaluate_zero_division():
    with pytest.raises(ZeroDivisionError):
        evaluate("1 / 0")

def test_evaluate_invalid_expression():
    with pytest.raises(NameError):
        evaluate("2 + unknown")

def test_main_success(monkeypatch, capsys):
    monkeypatch.setattr(sys, 'argv', ['calculator.py', '2 + 3 * 4'])
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "14"
    assert captured.err == ""