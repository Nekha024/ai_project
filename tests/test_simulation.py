from tests.hr_simulation import run_simulation


def test_simulation():

    results = run_simulation()

    assert len(results) == 40