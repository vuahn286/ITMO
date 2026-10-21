# Thí nghiệm: phân tích khám phá dữ liệu CÓ dùng Skill

- **Skill:** `exploratory-data-analysis` v1.4 – K-Dense Scientific Agent Skills
  (https://github.com/K-Dense-AI/claude-scientific-skills, commit 593377b, giấy phép MIT).
  Trích dẫn: Kassis T., Agarwal V., He Y., Patel D., Brueckner A.M. (2026). *Scientific Agent Skills:
  A Library of Procedural Knowledge for Research Agents.* arXiv:2609.00065.
- **Dữ liệu:** `../du_lieu_hop_nhat.csv` (387 số đo, đổi tên thành `an_mon_387.csv` trong thư mục chạy riêng).
- **Môi trường:** Python 3.13, chỉ thư viện chuẩn; chạy cục bộ, không kết nối mạng.

## Lệnh đã chạy (trong thư mục `skills/exploratory-data-analysis` của kho K-Dense)

```bash
python3 scripts/capability_manifest.py inspect an_mon_387.csv --root <thư-mục-dữ-liệu> --output manifest.json
python3 scripts/missingness_leakage_audit.py an_mon_387.csv --root <thư-mục-dữ-liệu> \
    --group-column quoc_gia --entity-column tram --split-column tap --reveal-identifiers --output leak.json
python3 scripts/distribution_sensitivity.py an_mon_387.csv --root <thư-mục-dữ-liệu> \
    --column r_corr_um_nam --reveal-identifiers --output dist.json
python3 scripts/tabular_profile.py an_mon_387.csv --root <thư-mục-dữ-liệu> --reveal-identifiers --output profile.json
```

## Kết quả chính

| Kiểm tra | Kết quả | So với phân tích ban đầu (không dùng Skill) |
|---|---|---|
| Độ lệch phân bố r_corr | 4,66 (thô) → −0,02 (sau log1p) | Ban đầu dùng thang log theo kinh nghiệm, không nêu căn cứ |
| Ngoại lệ (ngưỡng IQR) | 31/387 ngoài ngưỡng; TB 37,7 → 29,2 µm/năm nếu bỏ; trung vị 28,1 | Ban đầu không báo cáo độ nhạy ngoại lệ |
| Rò rỉ giữa tập huấn luyện – kiểm định | Không có trạm, nhóm hay dòng trùng giữa hai tập | Ban đầu không kiểm tra |
| Dữ liệu thiếu | 0 ô trống ở mọi cột, mọi nhóm, mọi tập | Ban đầu kiểm tra tổng số ô trống |

Skill không tự xóa, tự điền hay tự biến đổi dữ liệu; chỉ báo cáo để nhà khoa học quyết định.

**Giới hạn của phép so sánh:** "không dùng Skill" là phân tích ban đầu của chính bộ mã nghiên cứu (`ma-nguon/01–03`),
không phải một lần chạy AI độc lập. Để trình diễn, nên chạy lại trực tiếp trên Claude: một lần không tải Skill,
một lần tải Skill (tệp ZIP), cùng câu lệnh và cùng dữ liệu.
