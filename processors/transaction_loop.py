import json, csv 
from typing import List, Dict, Any, Optional 

class Transactions: 
    """Pemrosesan transaksi e-commerce menggunakan pendekatan Standard For Loop."""

    def __init__(self, file_path: str, tax_rate: float = 0.11) -> None:
        self.file_path: str = file_path
        self.tax_rate: float = tax_rate
        self.raw_data: List[Dict[str, Any]] = []
        self.processed_data: List[Dict[str, Any]] = []

    def load_data(self) -> None:
        """Membaca file JSON dari disk."""
        with open(self.file_path, mode='r', encoding='utf-8') as file:
            payload: Dict[str, Any] = json.load(file)
            raw_trs = payload.get('transactions')
            self.raw_data = raw_trs if isinstance(raw_trs, list) else []

    def process_data(self) -> List[Dict[str, Any]]: 
        """Memproses data transaksi dengan perhitungan pajak."""
        self.processed_data = [] 
        for item in self.raw_data:
            if item.get('status') == 'SUCCESS':
                voucher: Optional[str] = item.get('voucher')
                voucher_status: str = voucher if voucher is not None else 'TANPA VOUCHER'
                
                amount: float = float(item.get('amount', 0.0))
                total: float = round(amount + (amount * self.tax_rate), 2)
                
                cleaned_item: Dict[str, Any] = {
                    'trx_id': item.get('trx_id'), 
                    'amount': amount, 
                    'voucher_code': voucher_status,
                    'total_payment': total
                }
                self.processed_data.append(cleaned_item)
                
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