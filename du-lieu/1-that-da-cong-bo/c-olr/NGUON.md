# Nguồn gốc bộ dữ liệu C-OLR

- **Kho:** https://github.com/arashrockey/C-OLR – "Constrained Ordinal Logistic Regression for Atmospheric Corrosivity Classification"
- **Phiên bản đã tải:** commit `107ffa4` (10/2026)
- **Giấy phép:** MIT (xem `LICENSE.txt`). Dữ liệu của bên thứ ba vẫn chịu các điều kiện của nhà cung cấp gốc.
- **Phân loại:** 🟢 xanh – dữ liệu đã công bố.

## Nguồn gốc số liệu (theo sheet `Read me` và cột `Ref.`)

| Nhóm | Số quan sát | Công bố gốc |
|---|---|---|
| ISOCORRAG | 190 | Chico B., de la Fuente D., Díaz I., Simancas J., Morcillo M. (2017). Annual atmospheric corrosion of carbon steel worldwide. An integration of ISOCORRAG, ICP/UNECE and MICAT databases. *Materials* 10(6):601. https://doi.org/10.3390/ma10060601 |
| MICAT | 130 | Pintos S., Queipo N.V., de Rincón O.T., Rincón A., Morcillo M. (2000). Artificial neural network modeling of atmospheric corrosion in the MICAT project. *Corrosion Science* 42:35–52. https://doi.org/10.1016/S0010-938X(99)00054-2 |
| Việt Nam ("Lien et al.") | 12 | Nhiều khả năng: Le Thi Hong Lien, Pham Thy San, Hoang Lam Hong (2007). Results of studying atmospheric corrosion in Vietnam 1995–2005. *Sci. Technol. Adv. Mater.* 8(7–8):552–558 – **cần đối chiếu bảng số liệu gốc** |
| Nga ("mikhailov et al.") | 18 | **Chưa xác định chắc chắn** – có thể thuộc chương trình thử nghiệm Viễn Đông (nhóm Mikhailovsky, Panchenko…) |
| Tây Ban Nha, Canary, Colombia | 37 | de la Fuente et al.; Morales et al.; Castaño et al.; Santa et al. (theo cột `Ref.`) |

## Biến số

| Cột | Ý nghĩa | Đơn vị |
|---|---|---|
| Source, Site, Ref. | Nhóm nguồn, tên trạm, công bố gốc | – |
| Atmosphere | Loại khí quyển (1–4) | – |
| Temperature | Nhiệt độ trung bình năm | °C |
| TOW | Thời gian ẩm ướt | giờ/năm |
| Cl, SO2 | Tốc độ lắng đọng clorua, SO₂ | mg/m²/ngày |
| WL | Tốc độ ăn mòn năm đầu | **µm/năm** (nguồn ghi nhầm g/m²) |
| CAT | Cấp ăn mòn ISO 9223 | C2–C5 (2 trạm ghi sai: Barcelona, El Hierro) |
