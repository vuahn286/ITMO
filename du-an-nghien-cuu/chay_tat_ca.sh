#!/usr/bin/env bash
# Chạy lại toàn bộ chuỗi phân tích của dự án: hợp nhất – kiểm tra → mô hình → hiệu chỉnh vùng → mô hình 3D.
# Dùng:  ./chay_tat_ca.sh   (Windows: Git Bash hoặc WSL, hoặc gọi lần lượt 4 lệnh python bên dưới)
set -euo pipefail
cd "$(dirname "$0")/04-ma-nguon"
PY=${PYTHON:-python3}
echo "== 1. Hợp nhất và kiểm tra chất lượng dữ liệu (03-du-lieu → 03-du-lieu/2-da-xu-ly)"
$PY 01_hop_nhat_kiem_tra.py | tail -n 10
echo "== 2. Mô hình và kiểm định độc lập (→ 05-ket-qua/bang, hinh, mo-hinh)"
$PY 02_mo_hinh.py > /dev/null
echo "== 3. Hiệu chỉnh vùng – kiểm định bỏ-một-trạm"
$PY 03_hieu_chinh_dia_phuong.py
echo "== 4. Mô hình 3D (→ 05-ket-qua/mo-hinh-3d)"
$PY 04_mo_hinh_3d.py > /dev/null
echo "== Xong."
