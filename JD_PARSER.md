# Job Description Parsing System

## Overview
This module converts raw job description text files into structured JSON format.

## Input
- Multiple `.txt` job description files in `data/JD/`

## Output
- `parsed_jds.json` containing structured job data

## Extracted Fields
- Job Title
- Required Skills
- Experience Required
- Education

## Approach
- Used keyword-based skill extraction
- Used regex for experience extraction
- Cleaned job titles by removing numbering

## Limitations
- Skill extraction depends on keyword matching
- May not detect all variations of skills

## Future Improvements
- Use NLP models for better accuracy
- Improve skill synonym detection