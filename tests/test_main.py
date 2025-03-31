import pytest
from unittest.mock import patch
from algorithmstolivebypaulalexander.main  import main

def test_main():
    with patch('builtins.input', return_value='0'):
        assert main() == 1


