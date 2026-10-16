from pathlib import Path
from processors.transaction_loop import Transactions

DATA_DIR = Path(__file__).resolve().parent.parent / 'data'


def run_transaction_loop() -> None:
    print("=== [STUDI KASUS 1: TRANSACTION (STANDARD LOOP)] ===")
    # Inisiasi Object
    trs: Transactions = Transactions(file_path=str(DATA_DIR / 'transactions.json'), tax_rate=0.11)

    trs.load_data()
    trs.process_data()
    trs.export_to_csv(output_path=str(DATA_DIR / 'success_transactions_clean.csv'))
    print()
