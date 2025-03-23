from my_package.services.hello_world_service import HelloWorldService

def main() -> None:
    """Main entry point of the application."""
    # Create an instance of HelloWorldService
    service = HelloWorldService()
    
    # Call the say_hello method and store the result
    message = service.say_hello()

    # Print the result
    print(message)

if __name__ == "__main__":
    main()