from my_package.services.hello_world_service import HelloWorldService

def test_hello_world_service_initialization() -> None:
    """Test that HelloWorldService can be initialized."""
    service = HelloWorldService()
    assert service is not None

def test_say_hello_returns_correct_message() -> None:
    """Test that say_hello returns the expected message."""
    service = HelloWorldService()
    expected_message = "Hello, World!"
    actual_message = service.say_hello()
    assert actual_message == expected_message
