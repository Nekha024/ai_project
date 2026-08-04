from machine_test.evaluation_logic import calculate_task_score


def test_machine():

    result = calculate_task_score(
        5,
        10,
        1.5,
        "print('Hello World')",
        2
    )

    assert result["task_score"] > 0


if __name__ == "__main__":
    test_machine()
    print("Machine Test Passed")