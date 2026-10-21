"""
Kiểm tra an toàn mã TRƯỚC KHI chép vào máy không Internet.

1. Quét mọi tệp .py trong thư mục: báo nếu có thư viện mạng, lệnh gọi hệ thống, địa chỉ web.
2. Lập danh sách mã băm SHA-256 (MANIFEST.sha256) – trên máy không Internet tính lại để chắc mã không bị sửa
   trên đường chuyển.

Chạy:  python kiem_tra_an_toan.py [thư_mục]     (mặc định: thư mục chứa tệp này)
Kiểm lại trên máy đích:  python kiem_tra_an_toan.py --doi-chieu [thư_mục]
"""
import hashlib
import re
import sys
from pathlib import Path

CAM = {
    r"^\s*(import|from)\s+(socket|urllib|http|requests|httpx|aiohttp|ftplib|smtplib|telnetlib|paramiko|websocket)":
        "thư viện kết nối mạng",
    r"^\s*(import|from)\s+(subprocess|ctypes)": "gọi chương trình / thư viện hệ thống",
    r"os\.system|os\.popen|eval\(|exec\(|__import__": "thực thi lệnh động",
    r"https?://|ftp://": "địa chỉ web",
}


def quet(thu_muc):
    loi = []
    for tep in sorted(thu_muc.glob("*.py")):
        if tep.name == Path(__file__).name:
            continue
        for so, dong in enumerate(tep.read_text(encoding="utf-8").splitlines(), 1):
            for mau, mo_ta in CAM.items():
                if re.search(mau, dong):
                    loi.append(f"{tep.name}:{so}: {mo_ta} → {dong.strip()}")
    return loi


def bam(thu_muc):
    return {t.name: hashlib.sha256(t.read_bytes()).hexdigest()
            for t in sorted(thu_muc.iterdir()) if t.is_file() and t.suffix in {".py", ".json", ".txt", ".md", ".whl", ".bat"}
            and t.name != "MANIFEST.sha256"}


def main():
    doi_chieu = "--doi-chieu" in sys.argv
    con_lai = [a for a in sys.argv[1:] if a != "--doi-chieu"]
    thu_muc = Path(con_lai[0]) if con_lai else Path(__file__).resolve().parent
    manifest = thu_muc / "MANIFEST.sha256"
    if doi_chieu:
        cu = dict(reversed(l.split("  ", 1)) for l in manifest.read_text(encoding="utf-8").splitlines() if l)
        moi = bam(thu_muc)
        sai = [t for t in cu if moi.get(t) != cu[t]]
        print("KHỚP – mã nguyên vẹn." if not sai else f"KHÔNG KHỚP: {sai}")
        sys.exit(1 if sai else 0)
    loi = quet(thu_muc)
    if loi:
        print("PHÁT HIỆN MÃ KHÔNG ĐƯỢC PHÉP – không chép sang máy không Internet:")
        print("\n".join("  " + l for l in loi))
        sys.exit(1)
    manifest.write_text("".join(f"{h}  {t}\n" for t, h in bam(thu_muc).items()), encoding="utf-8")
    print(f"Không phát hiện kết nối mạng hay lệnh hệ thống. Đã ghi {manifest.name}.")


if __name__ == "__main__":
    main()
