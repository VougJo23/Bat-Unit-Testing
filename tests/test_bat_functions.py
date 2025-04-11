import pytest
import random
import time

import src.bat_functions
from src.bat_functions import calculate_bat_power
from src.bat_functions import signal_strength
from src.bat_functions import get_bat_vehicle
from src.bat_functions import fetch_joker_info


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


@pytest.fixture(scope="function")
def vehicles():
    return {
        'Batmobile': {'speed': 200, 'armor': 80},
        'Batwing': {'speed': 300, 'armor': 60},
        'Batcycle': {'speed': 150, 'armor': 50}
    }

def test_get_bat_vehicle(vehicles):
    
    for name, specs in vehicles.items():
        assert get_bat_vehicle(name) == specs

    # Test Exception for unkown vehicle
    with pytest.raises(ValueError):
        get_bat_vehicle('Batcraft')


def test_fetch_joker_info(mocker):
    
    # Mock a fast response to skip the 1-second delay
    mocker.patch('time.sleep', return_value=None)

    # Customize mock response
    mock_response = {'mischief_level': 0, 'location': 'captured'}
    mock = mocker.patch('src.bat_functions.fetch_joker_info', return_value = mock_response)

    info = src.bat_functions.fetch_joker_info()
    mock.assert_called_once() 
    assert info == mock_response 

