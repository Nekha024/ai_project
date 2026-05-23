# ATS Troubleshooting Guide

# 1. Resume Not Parsing

Cause:
- Unsupported format
- Corrupted PDF

Solution:
- Validate file type
- Retry extraction

---

# 2. Low Skill Detection

Cause:
- Missing synonyms
- Poor formatting

Solution:
- Expand skill dictionary
- Improve preprocessing

---

# 3. Wrong ATS Score

Cause:
- Missing fields
- Incorrect weights

Solution:
- Validate JSON inputs
- Verify weight configuration

---

# 4. Slow Performance

Cause:
- Large resumes
- Heavy NLP models

Solution:
- Enable caching
- Use optimized engine
- Reduce repeated processing

---

# 5. Bias in Results

Cause:
- Sensitive data exposure

Solution:
- Apply fairness engine
- Mask sensitive attributes

---

# 6. Semantic Matching Errors

Cause:
- Weak embeddings
- Incomplete job descriptions

Solution:
- Use better transformer models
- Improve JD quality

---

# 7. Timeout Issues

Cause:
- Large datasets

Solution:
- Use batch processing
- Apply async execution