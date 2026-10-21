#!/usr/bin/env bash
# Sinh lại dữ liệu và kết quả mẫu cho các demo trong bài thuyết trình.
set -euo pipefail
cd "$(dirname "$0")"
PY=${PYTHON:-python3}
$PY ma-nguon-demo/gia-lap/sinh_du_lieu_gia_lap.py
$PY ma-nguon-demo/gia-lap/phan_tich_an_mon.py > /dev/null
$PY ma-nguon-demo/gia-lap/ve_gantt.py > /dev/null
$PY ma-nguon-demo/nhieu-nguon/tao_bo_du_lieu.py > /dev/null
echo "Xong: du-lieu-demo/, ket-qua-demo/"
