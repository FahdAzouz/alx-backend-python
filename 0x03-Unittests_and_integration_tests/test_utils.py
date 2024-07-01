#!/usr/bin/env python3
'''Unit test module 0'''

from unittest import TestCase
import pytest
from parametrized import parametrized
access_nested_map = __import__("utils").access_nested_map
from typing import Dict, Tuple, Union

class TestAccessNestedMap(TestCase):
    '''Test function accessNestedMap'''
    
    @parametrized.expand([
        ({"a", 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a",), 2),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
            ) -> None:
        """Tests `access_nested_map`'s output."""
        self.assertEqual(access_nested_map(nested_map, path), expected)
