from api.error_handling import retry_request


def test_retry_failure():
    def failing_function():
        raise Exception("Something went wrong")

    result = retry_request(failing_function, retries=3)

    assert result == {"error": "Max retries exceeded"}