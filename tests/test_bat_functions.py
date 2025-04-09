import pytest
import random
from src.bat_functions import calculate_bat_power
from src.bat_functions import signal_strength

def test_calculate_bat_power():
    
    for _ in range(10):
        level = random.randint(0, 100)
        bat_power = calculate_bat_power(level)
        assert  bat_power % 42 == 0
    
@pytest.mark.parametrize("distance, expected", 
                         [(0, 100), (5, 50), (10, 0), (12, 0)])

def test_signal_strength(distance, expected):
    
    strength = signal_strength(distance)
    assert strength == expected
