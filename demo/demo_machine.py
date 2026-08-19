from machine_test.sample_input import sample_data
from machine_test.scoring_pipeline import machine_test_pipeline

result = machine_test_pipeline(sample_data)

print(result)