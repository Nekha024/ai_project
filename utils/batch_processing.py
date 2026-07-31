"""
Batch Processing Utility
"""


def batch_process(data, function):

    results = []

    for item in data:
        results.append(
            function(item)
        )

    return results