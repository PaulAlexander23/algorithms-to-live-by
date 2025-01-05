import pytest
from unittest.mock import patch

from sorting.main import main

def test_main_no_input():
    with patch('builtins.input', side_effect=['0','1']):
        assert main() == 0

def test_main_1():
    with patch('builtins.input', side_effect=['1','1']):
        assert main() == 0

def test_main_10():
    with patch('builtins.input', side_effect=['10','1']):
        assert main() == 0
