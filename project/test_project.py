from project import get_user_location, validate_location, suggest_places

def test_get_user_location_valid_input():
    # Mocked input values
    mock_values = ["Valid Location", "y"]

    # Mocking input
    get_input = lambda prompt: mock_values.pop(0)
    result = get_user_location(get_input)

    expected_output = {
        "city": "Dihlabeng",  
        "state": "",  
        "country": "ZA",  
        "zipcode": "9702",  
        "latitude": -28.21791,  
        "longitude": 28.31756,  
    }

    print("Actual Result:", result)
    print("Expected Output:", expected_output)
    assert result == expected_output

# Run the test
test_get_user_location_valid_input()