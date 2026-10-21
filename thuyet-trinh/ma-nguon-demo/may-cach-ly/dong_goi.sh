#!/usr/bin/env bash
# Đóng gói công cụ để chép sang máy KHÔNG Internet (chạy trên máy CÓ Internet, không chứa dữ liệu mật).
# Dùng:  ./dong_goi.sh            → goi-may-cach-ly/ (mã + cấu hình + kiểm tra + hướng dẫn)
#        ./dong_goi.sh --thu-vien → thêm bộ cài numpy, matplotlib cho Windows 64-bit, Python 3.12 (tệp .whl)
set -euo pipefail
cd "$(dirname "$0")"
PY=${PYTHON:-python3}
GOI=goi-may-cach-ly
$PY kiem_tra_an_toan.py                       # dừng ngay nếu mã có kết nối mạng / lệnh hệ thống
rm -rf "$GOI"; mkdir -p "$GOI"
cp cong_cu_lo_trinh.py cau_hinh_mac_dinh.json kiem_tra_an_toan.py README.md "$GOI"/
printf 'numpy\nmatplotlib\n' > "$GOI"/requirements.txt
cat > "$GOI"/chay.bat <<'BAT'
@echo off
REM Chạy trên máy không Internet (Windows). Sửa đường dẫn dữ liệu thật cho phù hợp.
python kiem_tra_an_toan.py --doi-chieu . || (echo Ma bi thay doi - DUNG LAI & pause & exit /b 1)
python cong_cu_lo_trinh.py --du-lieu du_lieu\luoi.csv --nhiem-vu du_lieu\nhiem_vu.json --ra ket_qua
pause
BAT
if [[ "${1:-}" == "--thu-vien" ]]; then
  $PY -m pip download numpy matplotlib -d "$GOI"/thu-vien --only-binary=:all: \
      --platform win_amd64 --python-version 3.12
  cp "$GOI"/thu-vien/*.whl "$GOI"/
  rm -rf "$GOI"/thu-vien
fi
$PY kiem_tra_an_toan.py "$GOI"                # lập MANIFEST.sha256 cho cả gói
echo "Xong: $GOI/ – chép sang máy không Internet theo quy định chuyển dữ liệu của đơn vị."
