# AI Data Model – Recruitment System

## 1. Candidate Profile
Represents structured resume data.

Fields:
- name
- email
- skills
- experience_years
- education
- certifications

---

## 2. Job Profile
Represents job requirements.

Fields:
- job_title
- required_skills
- preferred_skills
- experience_required
- education_required

---

## 3. Matching Logic

The system compares:

### Skills Matching
- Intersection of candidate and required skills

### Experience Matching
- Candidate years vs required years

### Final Score
Final Score = (Skill Weight) + (Experience Weight)

---

## 4. Output
The system generates:
- Candidate score
- Matching percentage