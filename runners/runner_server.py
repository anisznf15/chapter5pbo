from pathlib import Path
from processors.server_comprehension import ServerLogs

DATA_DIR = Path(__file__).resolve().parent.parent / 'data'


def run_server() -> None:
    print("=== [STUDI KASUS 2: SERVER LOGS (LIST COMPREHENSION)] ===")
    logs: ServerLogs = ServerLogs(file_path=str(DATA_DIR / 'server_logs.json'), slow_threshold_ms=1000)

    logs.load_data()
    logs.process_data()
    logs.export_to_csv(output_path=str(DATA_DIR / 'error_logs_clean.csv'))
    print()
