from runners.runner_transaction import run_transaction_loop
from runners.runner_server import run_server
from runners.runner_student import run_student

def main() -> None:
    print("==========================================")
    print(" EXECUTION PIPELINE - OOP DATA PROCESSOR ")
    print("==========================================\n")

    # Menjalankan masing-masing runner
    run_transaction_loop()
    run_server()
    run_student()

    print("==========================================")
    print(" SELURUH PROSES ETL & EKSPOR CSV SELESAI  ")
    print("==========================================")

if __name__ == "__main__":
    main()
