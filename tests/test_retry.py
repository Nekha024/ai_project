def test_retry():
    from api.error_handling import retry_request

    result = retry_request(lambda: 1)

    assert result == 1