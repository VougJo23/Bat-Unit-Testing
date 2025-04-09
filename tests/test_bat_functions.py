import pytest
import random
from src.bat_functions import calculate_bat_power

def test_calculate_bat_power():
    
    for _ in range(10):
        level = random.randint(0, 100)
        bat_power = calculate_bat_power(level)
        assert  bat_power % 42 == 0
    
