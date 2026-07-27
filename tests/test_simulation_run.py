from tests.hr_simulation import (
    run_simulation
)

from tests.simulation_analysis import (

    calculate_accuracy,

    average_scores,

    candidate_distribution

)


results = run_simulation()

print("=" * 60)

print("HR INTERVIEW AI SIMULATION")

print("=" * 60)

print()

for item in results[:10]:

    print(item)

print()

print("=" * 60)

print(

    "Candidate Distribution"

)

print(

    candidate_distribution(results)

)

print()

print(

    "Average Scores"

)

print(

    average_scores(results)

)

print()

print(

    "Decision Match Accuracy:",

    calculate_accuracy(results),

    "%"

)

print()

print("=" * 60)