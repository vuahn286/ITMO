#!/usr/bin/env bash
# Chạy lại toàn bộ: sinh dữ liệu demo → phân tích demo → nghiên cứu dữ liệu thật → mô hình 3D.
# Dùng:  ./chay_tat_ca.sh        (trên Windows: chạy trong Git Bash hoặc WSL, hoặc gọi từng lệnh python bên dưới)
set -euo pipefail
cd "$(dirname "$0")"
PY=${PYTHON:-python3}

echo "== 1. Dữ liệu giả lập (tình huống xuyên suốt)"
$PY ma-nguon/demo-gia-lap/sinh_du_lieu_gia_lap.py
$PY ma-nguon/demo-gia-lap/phan_tich_an_mon.py > /dev/null
$PY ma-nguon/demo-gia-lap/ve_gantt.py > /dev/null

echo "== 2. Bộ dữ liệu thật nhiều nguồn (demo Slide 8)"
$PY ma-nguon/demo-nhieu-nguon/tao_bo_du_lieu.py > /dev/null

echo "== 3. Nghiên cứu ăn mòn với dữ liệu thật (387 số đo + du-lieu/4-bo-sung/)"
$PY ma-nguon/nghien-cuu-an-mon/01_hop_nhat_kiem_tra.py | tail -n 12
$PY ma-nguon/nghien-cuu-an-mon/02_mo_hinh.py > /dev/null
$PY ma-nguon/nghien-cuu-an-mon/03_hieu_chinh_dia_phuong.py
$PY ma-nguon/nghien-cuu-an-mon/04_mo_hinh_3d.py > /dev/null

echo "== Xong. Kết quả: ket-qua/demo-gia-lap/ và ket-qua/nghien-cuu-an-mon/"
