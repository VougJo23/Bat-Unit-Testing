# Bat-Unit-Testing
Tests a provided Python module (bat_functions.py) using pytest

## Methodology

### Exercise 1:
1. Basic testing for calculate_bat_power
- Generates random levels (0-100).  
- Validates power output is divisible by 42.
2. Test signal_strength using pytest's parametrization
- Verifies strength matches expected values.

### Exercise 2: Test get_bat_vehicle with fixtures
- Used @pytest.fixture to provide reusable test data
- Injected into test_get_bat_vehicle for clean, isolated test runs.
- Ensures invalid vehicles raise `ValueError`.

### Exercise 3: Test get_bat_vehicle using mocking
- Mocks API call to skip delays.  
- Used pytest-mock to patch time.sleep and mock fetch_joker_info to get custom result. 

### Exercise 4: Create github workflow for CI
 