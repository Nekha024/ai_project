from observability.logging import calculate_metrics, check_alerts


def test_metrics():
    metrics = calculate_metrics(
        9,
        10,
        [1.0, 1.2, 0.8]
    )

    assert metrics["success_rate"] == 0.9
    assert metrics["avg_latency"] == 1.0


def test_high_latency_alert():
    metrics = {
        "success_rate": 0.95,
        "avg_latency": 3.0
    }

    alerts = check_alerts(metrics)

    assert "High latency detected" in alerts


def test_low_success_alert():
    metrics = {
        "success_rate": 0.80,
        "avg_latency": 1.0
    }

    alerts = check_alerts(metrics)

    assert "Low success rate" in alerts