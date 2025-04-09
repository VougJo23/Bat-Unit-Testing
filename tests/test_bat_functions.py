import pytest
import random
from src.bat_functions import calculate_bat_power
from src.bat_functions import signal_strength
from src.bat_functions import get_bat_vehicle

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



@pytest.fixture
def vehicles():
    return {
        'Batmobile': {'speed': 200, 'armor': 80},
        'Batwing': {'speed': 300, 'armor': 60},
        'Batcycle': {'speed': 150, 'armor': 50}
    }

def test_get_bat_vehicle(vehicles):
    
    for name, specs in vehicles.items():
        assert get_bat_vehicle(name) == specs
       
    with pytest.raises(ValueError) as vehicle_not_found:
        get_bat_vehicle('Batcraft')

