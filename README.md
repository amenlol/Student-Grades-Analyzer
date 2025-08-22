## Student Grades Analyzer

A minimal, reproducible project that analyzes a small dataset of student marks using Pandas and visualizes results with Matplotlib.

### Overview
- **Objective**: Load a CSV of student marks, compute per‑student averages, identify the top student, and generate plots.
- **Technologies**: Python, Pandas, Matplotlib.

### Dataset
The dataset is provided in `students.csv` with the following columns: `Name`, `Math`, `Science`, `English`.

```
Name,Math,Science,English
abel,85,90,78
abebe,92,88,95
hana,76,85,80
naol,89,76,90
kena,95,92,88
```

### Features
- Loads and validates the dataset from CSV.
- Computes an `Average` score per student across Math, Science, and English.
- Reports the top‑performing student.
- Produces three plots saved to the `plots/` directory:
  - `average_marks.png`: Bar chart of average marks per student.
  - `marks_by_subject.png`: Line chart of marks by subject for each student.
  - `marks_distribution.png`: Histogram of all marks across subjects.

### Requirements
- Python 3.10+
- See `requirements.txt` for Python dependencies.

### Installation
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Usage
```bash
python student_grades_analyzer.py
```
The script prints a preview of the data, the full table with the computed `Average`, and the top student. Figures are saved in the `plots/` directory.

### Project Structure
```
.
├── README.md
├── requirements.txt
├── student_grades_analyzer.py
├── students.csv
└── plots/
```

### Reproducibility Notes
- The script uses a non‑interactive Matplotlib backend to save figures, which is suitable for servers and CI environments.
- If you modify column names or add subjects, update the required columns in `student_grades_analyzer.py` accordingly.

### License
This project is provided as‑is for educational purposes. Consider adding a license before public distribution.

### Author
Maintained by `amenlol` on GitHub: [github.com/amenlol](https://github.com/amenlol)
# Student-Grades-Analyzer
# Student-Grades-Analyzer
# Student-Grades-Analyzer
