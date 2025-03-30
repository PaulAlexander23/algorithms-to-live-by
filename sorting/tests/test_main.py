import pytest
from unittest.mock import patch

from sorting.main import main

def test_main_sorting_does_not_fail_for_valid_inputs():
    for n_items in [0, 1, 10]:
        with patch('builtins.input', side_effect=['1', n_items, '1']):
            assert main() == 0

def test_main_searching_does_not_fail_for_valid_inputs():
    for n_items in [0, 1, 10]:
        with patch('builtins.input', side_effect=['2', n_items, '1', '1']):
            assert main() == 0

