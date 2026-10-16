import json, csv
from typing import List, Dict, Any


class Students:
    """Pemrosesan data mahasiswa menggunakan filter() + lambda."""

    def __init__(self, file_path: str, passing_score: float = 70.0) -> None:
        self.file_path: str = file_path
        self.passing_score: float = passing_score
        self.raw_data: List[Dict[str, Any]] = []
        self.processed_data: List[Dict[str, Any]] = []

    def load_data(self) -> None:
        """Membaca file JSON dari disk."""
        with open(self.file_path, mode='r', encoding='utf-8') as file:
            payload: Dict[str, Any] = json.load(file)
            raw_students = payload.get('students')
            self.raw_data = raw_students if isinstance(raw_students, list) else []

    def process_data(self) -> List[Dict[str, Any]]:
        """Filter mahasiswa aktif dengan nilai lulus memakai filter + lambda."""
        # Tahap 1: filter dengan lambda (aktif DAN skor >= batas lulus)
        passed = filter(
            lambda s: s.get('is_active') is True and float(s.get('score', 0.0)) >= self.passing_score,
            self.raw_data,
        )

        # Tahap 2: rapikan hasil filter (scholarship null -> TANPA BEASISWA)
        self.processed_data = [
            {
                'student_id': s.get('student_id'),
                'name': s.get('name'),
                'score': float(s.get('score', 0.0)),
                'scholarship_code': s.get('scholarship_code') or 'TANPA BEASISWA',
            }
            for s in passed
        ]
        return self.processed_data

    def export_to_csv(self, output_path: str) -> None:
        """Menyimpan hasil ekstraksi ke file CSV."""
        if not self.processed_data:
            print("[WARNING] Data kosong, file tidak dibuat.")
            return

        headers: List[str] = list(self.processed_data[0].keys())
        with open(output_path, mode='w', encoding='utf-8', newline='') as file:
            writer: csv.DictWriter = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(self.processed_data)

        print(f"[SUCCESS] Data berhasil disimpan di: {output_path}")
