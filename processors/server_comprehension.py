import json, csv
from typing import List, Dict, Any


class ServerLogs:
    """Pemrosesan log server menggunakan pendekatan List Comprehension."""

    def __init__(self, file_path: str, slow_threshold_ms: int = 1000) -> None:
        self.file_path: str = file_path
        self.slow_threshold_ms: int = slow_threshold_ms
        self.raw_data: List[Dict[str, Any]] = []
        self.processed_data: List[Dict[str, Any]] = []

    def load_data(self) -> None:
        """Membaca file JSON dari disk."""
        with open(self.file_path, mode='r', encoding='utf-8') as file:
            payload: Dict[str, Any] = json.load(file)
            raw_logs = payload.get('logs')
            self.raw_data = raw_logs if isinstance(raw_logs, list) else []

    def process_data(self) -> List[Dict[str, Any]]:
        """Mengambil log level ERROR lalu menandai tingkat keparahan (List Comprehension)."""
        self.processed_data = [
            {
                'log_id': item.get('log_id'),
                'level': item.get('level'),
                'response_ms': item.get('response_ms', 0),
                # user_id null -> ANONYMOUS
                'user_id': item.get('user_id') if item.get('user_id') is not None else 'ANONYMOUS',
                'severity': 'CRITICAL' if item.get('response_ms', 0) >= self.slow_threshold_ms else 'WARNING',
            }
            for item in self.raw_data
            if item.get('level') == 'ERROR'
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
