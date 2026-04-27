"""
===============================================================
  Job Description Parsing System
===============================================================
  Reads all .txt files from data/JD/
  Outputs structured JSON to data/final_jobs.json

  Usage:
    python jd_parser.py                        # reads from data/JD/
    python jd_parser.py --folder path/to/JDs   # custom folder
    python jd_parser.py --output out.json      # custom output file
===============================================================
"""

import re
import sys
import json
import os
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional


# ══════════════════════════════════════════════════════════════
#  SKILL SYNONYM / NORMALIZATION DICTIONARY
#  Maps raw text variants → canonical skill name
# ══════════════════════════════════════════════════════════════
SKILL_SYNONYMS: Dict[str, str] = {
    # Programming languages
    "python":                     "Python",
    "python3":                    "Python",
    "sql":                        "SQL",
    "mysql":                      "SQL/MySQL",
    "postgresql":                 "SQL/PostgreSQL",
    "java":                       "Java",
    "javascript":                 "JavaScript",
    "js":                         "JavaScript",
    "c++":                        "C++",
    "c#":                         "C#",
    "matlab":                     "MATLAB",
    # Big Data
    "hadoop":                     "Hadoop",
    "spark":                      "Apache Spark",
    "apache spark":               "Apache Spark",
    "kafka":                      "Apache Kafka",
    "hive":                       "Apache Hive",
    "hdfs":                       "HDFS",
    # Cloud
    "aws":                        "AWS",
    "amazon web services":        "AWS",
    "azure":                      "Microsoft Azure",
    "microsoft azure":            "Microsoft Azure",
    "gcp":                        "Google Cloud Platform",
    "google cloud":               "Google Cloud Platform",
    # IoT / Embedded
    "iot":                        "IoT",
    "iot data processing":        "IoT Data Processing",
    "mqtt":                       "MQTT Protocol",
    "plc":                        "PLC Programming",
    "dcs":                        "DCS Systems",
    "scada":                      "SCADA",
    # Automotive
    "can":                        "CAN Bus",
    "lin":                        "LIN Protocol",
    "can/lin":                    "CAN/LIN Protocols",
    "obd":                        "OBD Diagnostics",
    "ecu":                        "ECU Development",
    "iso 26262":                  "ISO 26262 (Functional Safety)",
    # Instrumentation
    "pid":                        "PID Control",
    "pid control":                "PID Control",
    "pid tuning":                 "PID Tuning",
    "calibration":                "Calibration Techniques",
    "isa":                        "ISA Standards",
    # ML / AI
    "machine learning":           "Machine Learning",
    "ml":                         "Machine Learning",
    "deep learning":              "Deep Learning",
    "dl":                         "Deep Learning",
    "nlp":                        "Natural Language Processing",
    "computer vision":            "Computer Vision",
    "tensorflow":                 "TensorFlow",
    "pytorch":                    "PyTorch",
    "scikit-learn":               "Scikit-Learn",
    # Tools
    "git":                        "Git",
    "github":                     "GitHub",
    "docker":                     "Docker",
    "kubernetes":                 "Kubernetes",
    "jenkins":                    "Jenkins",
    "power bi":                   "Power BI",
    "tableau":                    "Tableau",
    "autocad":                    "AutoCAD",
    "revit":                      "Revit",
    "etap":                       "ETAP",
    "pscad":                      "PSCAD",
    "pss/e":                      "PSS/E",
    # Embedded
    "embedded c/c++":             "Embedded C/C++",
    "embedded c":                 "Embedded C",
    "rtos":                       "RTOS",
    "uart":                       "UART Protocol",
    "spi":                        "SPI Protocol",
    "i2c":                        "I2C Protocol",
    "arm":                        "ARM Architecture",
    "avr":                        "AVR Microcontroller",
    "pic":                        "PIC Microcontroller",
    # VLSI / FPGA
    "vlsi":                       "VLSI Design",
    "fpga":                       "FPGA",
    "verilog":                    "Verilog",
    "vhdl":                       "VHDL",
    # EV / Energy
    "matlab/simulink":            "MATLAB/Simulink",
    "simulink":                   "Simulink",
    "hvac":                       "HVAC Systems",
    "bms":                        "BMS",
    "solar":                      "Solar Energy",
    "wind":                       "Wind Energy",
    "power systems":              "Power Systems",
    "relay":                      "Relay Protection",
    "control systems":            "Control Systems",
    "networking":                 "Networking",
    # Telecom
    "rf":                         "RF Engineering",
}

# ══════════════════════════════════════════════════════════════
#  ROLE VARIATION NORMALIZATION
# ══════════════════════════════════════════════════════════════
ROLE_SYNONYMS: Dict[str, str] = {
    "data engineer":                          "Data Engineer",
    "data engineer (smart grids)":            "Data Engineer (Smart Grids)",
    "automotive electrical engineer":         "Automotive Electrical Engineer",
    "instrumentation & control engineer":     "Instrumentation & Control Engineer",
    "instrumentation and control engineer":   "Instrumentation & Control Engineer",
    "software engineer":                      "Software Engineer",
    "software developer":                     "Software Developer",
    "data scientist":                         "Data Scientist",
    "ml engineer":                            "Machine Learning Engineer",
    "machine learning engineer":              "Machine Learning Engineer",
    "devops engineer":                        "DevOps Engineer",
    "backend engineer":                       "Backend Engineer",
    "frontend engineer":                      "Frontend Engineer",
    "full stack engineer":                    "Full Stack Engineer",
    "full-stack engineer":                    "Full Stack Engineer",
    "electrical engineer":                    "Electrical Engineer",
    "embedded systems engineer":              "Embedded Systems Engineer",
    "control systems engineer":               "Control Systems Engineer",
    "ev design engineer":                     "EV Design Engineer",
    "network planning engineer":              "Network Planning Engineer",
    "scada engineer":                         "SCADA / Automation Engineer",
    "plc engineer":                           "PLC / Automation Engineer",
    "solar pv design engineer":               "Solar PV Design Engineer",
    "wind energy engineer":                   "Wind Energy Engineer",
    "rf engineer":                            "RF Engineer",
    "power systems engineer":                 "Power Systems Engineer",
    "vlsi design engineer":                   "VLSI Design Engineer",
    "instrumentation engineer":               "Instrumentation Engineer",
}

# ══════════════════════════════════════════════════════════════
#  EXPERIENCE PATTERNS
# ══════════════════════════════════════════════════════════════
EXPERIENCE_PATTERNS = [
    re.compile(r'\b(\d+)\+?\s*years?\b', re.IGNORECASE),
    re.compile(r'\bentry[\s-]?level\b', re.IGNORECASE),
    re.compile(r'\bjunior\b', re.IGNORECASE),
    re.compile(r'\bmid[\s-]?level\b', re.IGNORECASE),
    re.compile(r'\bsenior\b', re.IGNORECASE),
    re.compile(r'\bfresher\b', re.IGNORECASE),
    re.compile(r'\bexperience\s+(of|in|with)?\s*\d+', re.IGNORECASE),
]

# ══════════════════════════════════════════════════════════════
#  EDUCATION KEYWORDS
# ══════════════════════════════════════════════════════════════
EDUCATION_KEYWORDS = [
    r"b\.?e\.?", r"b\.?tech\.?", r"m\.?tech\.?", r"m\.?e\.?",
    r"b\.?sc\.?", r"m\.?sc\.?", r"b\.?s\.?", r"m\.?s\.?",
    r"ph\.?d\.?", r"mba", r"bachelor", r"master",
    r"degree", r"diploma", r"certification", r"graduate",
]
EDUCATION_RE = re.compile(
    r'(' + '|'.join(EDUCATION_KEYWORDS) + r')',
    re.IGNORECASE
)


# ══════════════════════════════════════════════════════════════
#  DATA MODEL
# ══════════════════════════════════════════════════════════════

@dataclass
class JobRequirement:
    """Structured AI-readable job requirement object."""
    role_name: str = ""
    summary: str = ""
    required_skills: List[str] = field(default_factory=list)
    # normalized_skills: List[str] = field(default_factory=list)
    education: List[str] = field(default_factory=list)
    experience: List[str] = field(default_factory=list)
    # raw_qualifications: List[str] = field(default_factory=list)

    def is_valid(self) -> bool:
        return bool(self.role_name)

    def to_dict(self) -> dict:
        d = asdict(self)
        # d.pop("raw_qualifications", None)
        return d


# ══════════════════════════════════════════════════════════════
#  TEXT HELPERS
# ══════════════════════════════════════════════════════════════

def normalize_text(text: str) -> str:
    """Clean raw text: strip markdown links, HTML tags, normalize whitespace."""
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'[ \t]+', ' ', text)
    text = text.replace('\u2013', '-').replace('\u2014', '-')
    return text.strip()


def clean_bullet(line: str) -> str:
    """Strip bullet/list markers from a line."""
    line = re.sub(r'^[\s]*[•\-\*\u2022\u25cf\u2023◦○]\s*', '', line)
    line = re.sub(r'^[\s]*\d+[\.\)]\s*', '', line)
    return line.strip()


def normalize_skill(raw: str) -> str:
    """Map a raw skill string to its canonical form."""
    key = raw.strip().lower()
    if key in SKILL_SYNONYMS:
        return SKILL_SYNONYMS[key]
    for syn_key, canonical in SKILL_SYNONYMS.items():
        if len(syn_key) <= 2:
            continue  # skip ambiguous single/double char keys
        if syn_key in key:
            return canonical
    return raw.strip().title()


def normalize_role(raw: str) -> str:
    """Map a raw role title to its canonical form."""
    key = raw.strip().lower()
    if key in ROLE_SYNONYMS:
        return ROLE_SYNONYMS[key]
    for role_key, canonical in ROLE_SYNONYMS.items():
        if role_key in key:
            return canonical
    return raw.strip().title()


# ══════════════════════════════════════════════════════════════
#  SECTION DETECTOR
# ══════════════════════════════════════════════════════════════

SECTION_HEADERS = {
    "job summary":              "summary",
    "summary":                  "summary",
    "overview":                 "summary",
    "role overview":            "summary",
    "key responsibilities":     "responsibilities",
    "responsibilities":         "responsibilities",
    "duties":                   "responsibilities",
    "job responsibilities":     "responsibilities",
    "required skills":          "skills",
    "skills":                   "skills",
    "skills required":          "skills",
    "technical skills":         "skills",
    "qualifications":           "qualifications",
    "qualification":            "qualifications",
    "education":                "qualifications",
    "requirements":             "qualifications",
    "eligibility":              "qualifications",
}

def detect_section(line: str) -> Optional[str]:
    stripped = line.strip().rstrip(':').lower()
    if stripped in SECTION_HEADERS:
        return SECTION_HEADERS[stripped]
    return None


# ══════════════════════════════════════════════════════════════
#  TITLE LINE DETECTION
#  Used when a single .txt file contains multiple job blocks
# ══════════════════════════════════════════════════════════════

def is_title_line(line: str) -> bool:
    line = line.strip()
    if not line or line[0] in ('•', '-', '*', '◦', '○'):
        return False
    if detect_section(line):
        return False
    if len(line) < 4 or len(line) > 100:
        return False
    if re.match(r'^\d+[\.\)]\s*\S', line):
        return True
    if not line[0].isupper():
        return False
    job_suffixes = (
        'engineer', 'developer', 'analyst', 'manager', 'architect',
        'scientist', 'designer', 'lead', 'specialist', 'consultant',
        'administrator', 'officer', 'director', 'technician', 'operator'
    )
    lower = line.lower()
    if any(lower.rstrip(')').endswith(s) for s in job_suffixes):
        return True
    return False


def split_into_job_blocks(text: str) -> List[str]:
    """Split text that may contain multiple job descriptions."""
    lines = text.splitlines()
    blocks: List[str] = []
    current: List[str] = []

    for line in lines:
        if is_title_line(line) and current:
            block = '\n'.join(current)
            if len(block.strip()) > 80:
                blocks.append(block)
            current = [line]
        else:
            current.append(line)

    if current:
        block = '\n'.join(current)
        if len(block.strip()) > 80:
            blocks.append(block)

    return blocks


# ══════════════════════════════════════════════════════════════
#  SINGLE JOB BLOCK PARSER
# ══════════════════════════════════════════════════════════════

def parse_job_block(block: str) -> Optional[JobRequirement]:
    lines = [normalize_text(l) for l in block.splitlines()]
    lines = [l for l in lines if l]

    if not lines:
        return None

    job = JobRequirement()

    # First non-empty line is the role title
    first_line = lines[0].strip()
    title_match = re.match(r'^\d+[\.\)]\s*(.+)', first_line)
    job.role_name = title_match.group(1).strip() if title_match else first_line

    current_section = None
    summary_lines: List[str] = []
    skill_lines: List[str] = []
    qual_lines: List[str] = []

    i = 1
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        sec = detect_section(stripped)
        if sec:
            current_section = sec
            i += 1
            continue

        if not stripped:
            i += 1
            continue

        content = clean_bullet(stripped)
        if not content:
            i += 1
            continue

        if current_section == "summary":
            summary_lines.append(content)
        elif current_section == "skills":
            skill_lines.append(content)
        elif current_section == "qualifications":
            qual_lines.append(content)
        elif current_section is None:
            # Pre-section text treated as part of summary
            summary_lines.append(content)

        i += 1

    job.summary = ' '.join(summary_lines).strip()
    # Skills: split comma/semicolon-separated lists within each bullet
    raw_skills = []
    for sk_line in skill_lines:
        parts = [p.strip() for p in re.split(r'[,;]', sk_line) if p.strip()]
        raw_skills.extend(parts)
    job.required_skills = raw_skills
    # job.normalized_skills = [normalize_skill(s) for s in raw_skills]

    # Qualifications: classify into education vs experience
    for q in qual_lines:
        # job.raw_qualifications.append(q)
        if EDUCATION_RE.search(q):
            job.education.append(q)
        elif any(p.search(q) for p in EXPERIENCE_PATTERNS):
            job.experience.append(q)
        else:
            lower_q = q.lower()
            if any(kw in lower_q for kw in ['year', 'experience', 'fresher', 'senior', 'junior']):
                job.experience.append(q)
            else:
                job.education.append(q)

    return job if job.is_valid() else None


# ══════════════════════════════════════════════════════════════
#  FOLDER PROCESSOR
# ══════════════════════════════════════════════════════════════

def process_jd_folder(folder_path: str) -> List[JobRequirement]:
    """
    Read every .txt file in folder_path.
    Each file may contain one or multiple job descriptions.
    """
    if not os.path.isdir(folder_path):
        print(f"[ERROR] Folder not found: {folder_path}")
        sys.exit(1)

    all_jobs: List[JobRequirement] = []
    txt_files = sorted([f for f in os.listdir(folder_path) if f.endswith(".txt")])

    if not txt_files:
        print(f"[!] No .txt files found in: {folder_path}")
        sys.exit(0)

    print(f"[•] Found {len(txt_files)} .txt file(s) in '{folder_path}'")

    for filename in txt_files:
        filepath = os.path.join(folder_path, filename)
        try:
            with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
                raw_text = f.read()
        except Exception as e:
            print(f"  [WARN] Could not read {filename}: {e}")
            continue

        # A single file might have one or multiple job descriptions
        blocks = split_into_job_blocks(raw_text)

        if not blocks:
            print(f"  [SKIP] {filename} — no parseable content found")
            continue

        file_jobs = []
        for block in blocks:
            job = parse_job_block(block)
            if job:
                file_jobs.append(job)

        print(f"  [✔] {filename} → {len(file_jobs)} job(s) parsed")
        all_jobs.extend(file_jobs)

    return all_jobs


# ══════════════════════════════════════════════════════════════
#  JSON EXPORT
# ══════════════════════════════════════════════════════════════

def export_json(jobs: List[JobRequirement], filepath: str) -> None:
    os.makedirs(os.path.dirname(filepath) if os.path.dirname(filepath) else '.', exist_ok=True)
    data = [job.to_dict() for job in jobs]
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"\n[✔] JSON exported → {filepath}")
    print(f"[✔] Total job descriptions saved: {len(jobs)}")


# ══════════════════════════════════════════════════════════════
#  ENTRY POINT
# ══════════════════════════════════════════════════════════════

def main():
    args = sys.argv[1:]

    folder_path = "data/JD"
    output_file = "data/final_jobs.json"

    # --folder override
    if "--folder" in args:
        idx = args.index("--folder")
        try:
            folder_path = args[idx + 1]
            args = [a for i, a in enumerate(args) if i not in (idx, idx + 1)]
        except IndexError:
            print("[ERROR] --folder requires a path argument")
            sys.exit(1)

    # --output override
    if "--output" in args:
        idx = args.index("--output")
        try:
            output_file = args[idx + 1]
            args = [a for i, a in enumerate(args) if i not in (idx, idx + 1)]
        except IndexError:
            print("[ERROR] --output requires a file path argument")
            sys.exit(1)

    print(f"\n{'='*60}")
    print(f"  Job Description Parsing System")
    print(f"{'='*60}")
    print(f"  Folder : {folder_path}")
    print(f"  Output : {output_file}")
    print(f"{'='*60}\n")

    jobs = process_jd_folder(folder_path)

    if not jobs:
        print("[!] No valid job descriptions found.")
        sys.exit(0)

    export_json(jobs, output_file)


if __name__ == "__main__":
    main()