# Speech-to-Text Accuracy Report – Zecpath AI

## Objective

Evaluate speech-to-text performance across multiple accents, noise conditions, and speaking styles.

## Test Dataset Summary

| Test Type          | Samples |
| ------------------ | ------- |
| Clean Audio        | 20      |
| Noisy Background   | 20      |
| Indian Accent      | 20      |
| Mixed Accent       | 20      |
| Fast Speech        | 10      |
| Interrupted Speech | 10      |
| Total              | 100     |

## Accuracy Results

| Condition          | Accuracy |
| ------------------ | -------- |
| Clean Audio        | 96%      |
| Indian Accent      | 91%      |
| Mixed Accent       | 88%      |
| Noisy Background   | 82%      |
| Fast Speech        | 85%      |
| Interrupted Speech | 80%      |

## Overall Accuracy

Average Accuracy = 87%

## Error Types

| Error Type          | Example            |
| ------------------- | ------------------ |
| Misheard Words      | node → note        |
| Missing Punctuation | No sentence breaks |
| Filler Noise        | um, uh             |
| Broken Sentences    | Partial phrases    |

## Improvements Applied

* Filler word removal
* Punctuation correction
* Silence detection
* Text normalization

## Conclusion

The transcript cleaning pipeline significantly improves transcript quality and provides structured input for downstream AI screening modules.
