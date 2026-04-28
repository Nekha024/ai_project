# Storage Design

## Folder Structure

data/
│
├── resumes/
│   ├── raw/
│   ├── cleaned/
│
├── jobs/
│   ├── raw_jd/
│   ├── parsed_jds.json
│
├── scores/
│   ├── ats_scores.json
│
├── interviews/
│   ├── interview_results.json
│
├── final/
│   ├── selected_candidates.json


## Description

- Raw resumes → uploaded files
- Cleaned resumes → parsed text
- Jobs → structured job data
- Scores → ATS matching scores
- Interviews → interview outputs
- Final → selected candidates