from pathlib import Path
from processors.student_lambda import Students

DATA_DIR = Path(__file__).resolve().parent.parent / 'data'


def run_student() -> None:
    print("=== [STUDI KASUS 3: STUDENT (FILTER + LAMBDA)] ===")
    students: Students = Students(file_path=str(DATA_DIR / 'student_grades.json'), passing_score=70.0)

    students.load_data()
    students.process_data()
    students.export_to_csv(output_path=str(DATA_DIR / 'passed_students_clean.csv'))
    print()
