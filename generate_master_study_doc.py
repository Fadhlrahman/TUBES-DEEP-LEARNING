# -*- coding: utf-8 -*-
"""
Master Study Guide Generator for Indoor Localization System.
Generates 'Panduan_Lengkap_Indoor_Localization.docx' with 9 detailed chapters,
including a dedicated, in-depth breakdown of the 4 Main Processes and their components.
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def create_document():
    doc = docx.Document()
    
    # Page setup - Margins (1 inch = 72 pt = 1440 twips)
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        section.different_first_page_header_footer = True
        
        # Header / Footer
        footer = section.footer
        p_ft = footer.paragraphs[0]
        p_ft.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r_ft = p_ft.add_run("Panduan Lengkap Indoor Localization | Deep Learning Mini Project")
        r_ft.font.name = "Arial"
        r_ft.font.size = Pt(8.5)
        r_ft.font.color.rgb = RGBColor(156, 163, 175)

    def set_cell_background(cell, hex_color):
        tcPr = cell._element.get_or_add_tcPr()
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
        tcPr.append(shd)

    def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
        tcPr = cell._element.get_or_add_tcPr()
        tcMar = OxmlElement('w:tcMar')
        for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
            node = OxmlElement(f'w:{m}')
            node.set(qn('w:w'), str(val))
            node.set(qn('w:type'), 'dxa')
            tcMar.append(node)
        tcPr.append(tcMar)

    def add_callout(title, text, box_type="info"):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False
        tbl.columns[0].width = Inches(6.5)
        
        cell = tbl.cell(0, 0)
        set_cell_margins(cell, top=120, bottom=120, left=180, right=160)
        
        if box_type == "info":
            bg_color = "EFF6FF"
            border_color = "2563EB"
            prefix = "💡 CATATAN PENTING:"
            title_color = RGBColor(37, 99, 235)
        elif box_type == "warning":
            bg_color = "FEF2F2"
            border_color = "DC2626"
            prefix = "⚠️ PERHATIAN / WASPADA:"
            title_color = RGBColor(220, 38, 38)
        elif box_type == "concept":
            bg_color = "F0FDF4"
            border_color = "16A34A"
            prefix = "📌 ANALOGI / INTUISI DASAR:"
            title_color = RGBColor(22, 163, 74)
        else:
            bg_color = "F8FAFC"
            border_color = "64748B"
            prefix = "ℹ️ INFO:"
            title_color = RGBColor(100, 116, 139)
            
        set_cell_background(cell, bg_color)
        
        tcPr = cell._element.get_or_add_tcPr()
        tcBorders = parse_xml(
            f'<w:tcBorders {nsdecls("w")}>'
            f'<w:left w:val="single" w:sz="36" w:space="0" w:color="{border_color}"/>'
            f'<w:top w:val="none"/>'
            f'<w:right w:val="none"/>'
            f'<w:bottom w:val="none"/>'
            f'</w:tcBorders>'
        )
        tcPr.append(tcBorders)
        
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        run_prefix = p.add_run(f"{prefix} {title}\n")
        run_prefix.bold = True
        run_prefix.font.size = Pt(10.5)
        run_prefix.font.name = "Arial"
        run_prefix.font.color.rgb = title_color
        
        run_text = p.add_run(text)
        run_text.font.size = Pt(9.5)
        run_text.font.name = "Arial"
        run_text.font.color.rgb = RGBColor(31, 41, 55)
        
        p_after = doc.add_paragraph()
        p_after.paragraph_format.space_before = Pt(0)
        p_after.paragraph_format.space_after = Pt(4)

    def add_code_block(code_str, caption=None):
        if caption:
            p_cap = doc.add_paragraph()
            p_cap.paragraph_format.space_before = Pt(6)
            p_cap.paragraph_format.space_after = Pt(2)
            r_cap = p_cap.add_run(f"💻 Cuplikan Kode: {caption}")
            r_cap.bold = True
            r_cap.font.size = Pt(9)
            r_cap.font.name = "Arial"
            r_cap.font.color.rgb = RGBColor(75, 85, 99)
            
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False
        tbl.columns[0].width = Inches(6.5)
        
        cell = tbl.cell(0, 0)
        set_cell_background(cell, "F3F4F6")
        set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
        
        tcPr = cell._element.get_or_add_tcPr()
        tcBorders = parse_xml(
            f'<w:tcBorders {nsdecls("w")}>'
            f'<w:left w:val="single" w:sz="18" w:space="0" w:color="9CA3AF"/>'
            f'<w:top w:val="single" w:sz="6" w:space="0" w:color="E5E7EB"/>'
            f'<w:right w:val="single" w:sz="6" w:space="0" w:color="E5E7EB"/>'
            f'<w:bottom w:val="single" w:sz="6" w:space="0" w:color="E5E7EB"/>'
            f'</w:tcBorders>'
        )
        tcPr.append(tcBorders)
        
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.05
        run = p.add_run(code_str.strip())
        run.font.name = "Consolas"
        run.font.size = Pt(8.5)
        run.font.color.rgb = RGBColor(17, 24, 39)
        
        p_after = doc.add_paragraph()
        p_after.paragraph_format.space_before = Pt(0)
        p_after.paragraph_format.space_after = Pt(4)

    def add_figure(img_path, caption, width_inch=5.6):
        if os.path.exists(img_path):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(8)
            p_img.paragraph_format.space_after = Pt(3)
            run_img = p_img.add_run()
            run_img.add_picture(img_path, width=Inches(width_inch))
            
            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_before = Pt(0)
            p_cap.paragraph_format.space_after = Pt(8)
            run_cap = p_cap.add_run(f"Gambar: {caption}")
            run_cap.italic = True
            run_cap.font.size = Pt(9)
            run_cap.font.name = "Arial"
            run_cap.font.color.rgb = RGBColor(75, 85, 99)

    def add_h1(text):
        h = doc.add_heading(level=1)
        h.paragraph_format.space_before = Pt(18)
        h.paragraph_format.space_after = Pt(6)
        h.paragraph_format.keep_with_next = True
        run = h.add_run(text)
        run.font.name = "Arial"
        run.font.size = Pt(15)
        run.bold = True
        run.font.color.rgb = RGBColor(30, 58, 138)
        return h

    def add_h2(text):
        h = doc.add_heading(level=2)
        h.paragraph_format.space_before = Pt(14)
        h.paragraph_format.space_after = Pt(4)
        h.paragraph_format.keep_with_next = True
        run = h.add_run(text)
        run.font.name = "Arial"
        run.font.size = Pt(12)
        run.bold = True
        run.font.color.rgb = RGBColor(37, 99, 235)
        return h

    def add_h3(text):
        h = doc.add_heading(level=3)
        h.paragraph_format.space_before = Pt(10)
        h.paragraph_format.space_after = Pt(2)
        h.paragraph_format.keep_with_next = True
        run = h.add_run(text)
        run.font.name = "Arial"
        run.font.size = Pt(10.5)
        run.bold = True
        run.font.color.rgb = RGBColor(55, 65, 81)
        return h

    def add_p(text, bold_prefix=None):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(5)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_pre = p.add_run(bold_prefix)
            r_pre.bold = True
            r_pre.font.name = "Arial"
            r_pre.font.size = Pt(9.5)
            r_pre.font.color.rgb = RGBColor(31, 41, 55)
        r = p.add_run(text)
        r.font.name = "Arial"
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor(55, 65, 81)
        return p

    def create_table(headers, rows_data, col_widths=None):
        tbl = doc.add_table(rows=len(rows_data) + 1, cols=len(headers))
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False
        
        hdr_cells = tbl.rows[0].cells
        for i, h in enumerate(headers):
            hdr_cells[i].text = h
            set_cell_background(hdr_cells[i], "1E3A8A")
            set_cell_margins(hdr_cells[i], top=90, bottom=90, left=110, right=110)
            p = hdr_cells[i].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in p.runs:
                run.font.bold = True
                run.font.name = "Arial"
                run.font.size = Pt(9)
                run.font.color.rgb = RGBColor(255, 255, 255)
                
        for r_idx, row_vals in enumerate(rows_data):
            row_cells = tbl.rows[r_idx + 1].cells
            bg_col = "F9FAFB" if r_idx % 2 == 1 else "FFFFFF"
            for c_idx, val in enumerate(row_vals):
                row_cells[c_idx].text = str(val)
                set_cell_background(row_cells[c_idx], bg_col)
                set_cell_margins(row_cells[c_idx], top=70, bottom=70, left=110, right=110)
                p = row_cells[c_idx].paragraphs[0]
                for run in p.runs:
                    run.font.name = "Arial"
                    run.font.size = Pt(8.5)
                    run.font.color.rgb = RGBColor(31, 41, 55)
                    
        if col_widths:
            for row in tbl.rows:
                for c_idx, w in enumerate(col_widths):
                    row.cells[c_idx].width = Inches(w)
                    
        p_after = doc.add_paragraph()
        p_after.paragraph_format.space_before = Pt(0)
        p_after.paragraph_format.space_after = Pt(4)

    # -------------------------------------------------------------
    # COVER / HEADER TITLE
    # -------------------------------------------------------------
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(36)
    p_title.paragraph_format.space_after = Pt(8)
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("PANDUAN LENGKAP & DEEP DIVE TEKNIS\nSISTEM INDOOR POSITIONING BERBASIS WI-FI FINGERPRINTING & DEEP LEARNING")
    r_title.bold = True
    r_title.font.name = "Arial"
    r_title.font.size = Pt(20)
    r_title.font.color.rgb = RGBColor(30, 58, 138)
    
    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_before = Pt(0)
    p_sub.paragraph_format.space_after = Pt(24)
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("Buku Panduan Komprehensif: Dari Konsep Awam, Fisika Sinyal Radio, Glosarium Istilah, Alur 4 Proses Metodologi & Komponennya, Cara Analisis Visual Grafik, Bedah Coding Baris-per-Baris, hingga Evaluasi Overfitting vs Covariate Shift")
    r_sub.italic = True
    r_sub.font.name = "Arial"
    r_sub.font.size = Pt(11)
    r_sub.font.color.rgb = RGBColor(75, 85, 99)

    add_callout(
        "Tujuan & Sasaran Dokumen Ini",
        "Dokumen ini disusun khusus bagi siapa saja (termasuk pembaca awam tanpa latar belakang telekomunikasi) yang ingin memahami proyek Indoor Positioning secara mendalam, dari konsep logika paling dasar hingga level teknis implementasi machine learning & deep learning. Setiap tahapan proses, grafik, rumus matematika, dan baris kode dijelaskan secara gamblang dengan analogi nyata.",
        "concept"
    )

    doc.add_page_break()

    # -------------------------------------------------------------
    # BAB 1: PENGANTAR & KONSEP DASAR (DARI SUDUT PANDANG AWAM)
    # -------------------------------------------------------------
    add_h1("BAB 1: PENGANTAR & KONSEP DASAR (DARI SUDUT PANDANG AWAM)")
    
    add_h2("1.1 Masalah Nyata: Mengapa GPS Mati di Dalam Gedung?")
    add_p(
        "Di ruang terbuka (outdoor), smartphone kita dengan sangat mudah menentukan lokasi menggunakan teknologi GPS (Global Positioning System). Satelit GPS yang mengorbit di luar angkasa pada ketinggian ~20.000 km memancarkan gelombang radio frekuensi 1.5 GHz langsung ke permukaan bumi. Smartphone kita menangkap sinyal minimal dari 4 satelit untuk melakukan perhitungan triangulasi (trilaterasi) waktu tempuh sinyal.",
        "Prinsip Kerja GPS Outdoor: "
    )
    add_p(
        "Begitu kita melangkah masuk ke dalam gedung bertingkat, mall, stasiun bawah tanah, atau rumah sakit, sinyal GPS tiba-tiba hilang total atau melenceng ratusan meter. Mengapa hal ini terjadi? Penyebab utamanya adalah:\n"
        "1. Ketiadaan Garis Pandang Langsung (No Line-of-Sight): Dinding beton bertulang (reinforced concrete), atap cor, dan struktur baja bertindak sebagai perisai elektromagnetik (efek Sangkar Faraday / Faraday Cage) yang memblokir atau menyerap gelombang radio satelit yang dayanya sudah sangat lemah saat tiba di bumi.\n"
        "2. Redaman Kaca Modern (Low-E Glass): Kaca gedung bertingkat dilapisi oksida logam tipis penahan panas yang memantulkan gelombang radio satelit.\n"
        "3. Pantulan Jamak (Multipath Fading): Sinyal satelit yang lolos akan memantul bolak-balik di lantai, pilar, dan dinding, sehingga waktu tempuh sinyal kacau balau dan posisi yang dihitung menjadi ngawur puluhan meter.",
        "Mengapa GPS Gagal di Indoor? "
    )

    add_h2("1.2 Solusi Cerdas: Konsep Wi-Fi Fingerprinting (Analogi Sidik Jari)")
    add_p(
        "Karena memasang satelit di dalam gedung adalah hal yang mustahil, para insinyur telekomunikasi memanfaatkan infrastruktur yang SUDAH TERSEDIA di dalam setiap gedung modern: router Wi-Fi atau Wireless Access Point (WAP).",
        "Pemanfaatan Infrastruktur yang Ada: "
    )
    add_callout(
        "Analogi Sidik Jari Manusia vs Sidik Jari Wi-Fi",
        "Setiap manusia memiliki sidik jari unik di ujung jarinya. Meskipun dua orang sama-sama memiliki 10 jari, pola guratan garisnya tidak akan pernah sama.\n\n"
        "Hal serupa terjadi di dalam gedung: Bayangkan ada 100 router Wi-Fi terpasang di langit-langit gedung. Saat Anda berdiri di depan Ruang Kuliah 101, ponsel Anda menerima sinyal dari Router A sebesar -45 dBm (sangat dekat), Router B sebesar -68 dBm, Router C sebesar -80 dBm, dan 97 router lainnya sama sekali tidak terdeteksi. Kombinasi kekuatan sinyal ini adalah 'SIDIK JARI RADIO' unik untuk titik tersebut!\n\n"
        "Jika Anda bergeser 10 meter ke Ruang 102, Router A akan melemah menjadi -60 dBm, sedangkan Router B menguat menjadi -40 dBm. Polanya berubah! Dengan merekam sidik jari radio di seluruh ruangan (fase offline), kita dapat melatih model AI untuk menebak lokasi seseorang hanya dengan membaca kombinasi sinyal Wi-Fi di ponselnya (fase online).",
        "concept"
    )

    add_h2("1.3 Memahami Sinyal Wi-Fi: RSSI dan Satuan dBm")
    add_p(
        "Kekuatan sinyal radio yang diterima oleh antena smartphone diukur dalam satuan RSSI (Received Signal Strength Indication), dengan skala logaritmik bernama dBm (desibel relatif terhadap 1 miliwatt).",
        "Apa itu RSSI? "
    )
    add_p(
        "Banyak orang awam bingung: Mengapa nilai RSSI Wi-Fi selalu bernilai minus (negatif), misalnya -40 dBm, -75 dBm, atau -90 dBm?\n"
        "• Daya 1 miliwatt (1 mW) didefinisikan sebagai 0 dBm.\n"
        "• Gelombang radio menyebar di udara mengikuti hukum kuadrat terbalik (Inverse Square Law), artinya kekuatannya berkurang drastis seiring jarak.\n"
        "• Daya sinyal yang tiba di antena smartphone kita hanyalah sepersejuta (0.000001 mW) hingga sepersemiliar miliwatt! Karena logaritma dari angka di bawah 1 adalah angka minus, maka nilainya menjadi negatif.",
        "Mengapa Angkanya Selalu Negatif? "
    )
    
    headers_rssi = ["Rentang Nilai RSSI", "Kualitas Sinyal", "Arti Fisik di Lapangan"]
    rows_rssi = [
        ["-30 dBm s.d. -45 dBm", "Sangat Kuat (Luar Biasa)", "Ponsel berada persis di bawah router Wi-Fi (jarak 1-3 meter)."],
        ["-50 dBm s.d. -65 dBm", "Kuat & Stabil", "Jarak normal di dalam satu ruangan yang sama."],
        ["-70 dBm s.d. -79 dBm", "Sedang / Mulai Lemah", "Sinyal mulai terhalang 1-2 dinding bata atau berada di koridor."],
        ["-80 dBm s.d. -89 dBm", "Sangat Lemah", "Batas minimal koneksi stabil, rentan putus, terhalang lantai beton."],
        ["-90 dBm s.d. -104 dBm", "Ambang Batas Derau (Noise)", "Sinyal hampir lenyap, nyaris tidak bisa didekode oleh antena."],
        ["-105 dBm / Tidak Terdeteksi", "Nol / Tiada Sinyal", "Router berada terlalu jauh atau di gedung lain (di luar jangkauan)."]
    ]
    create_table(headers_rssi, rows_rssi, [2.0, 1.8, 2.7])

    add_h2("1.4 Glosarium Lengkap Istilah Kunci (Kamus Istilah untuk Pemula)")
    add_p(
        "Tabel berikut merangkum seluruh istilah teknis yang digunakan di dalam proyek ini beserta padanan artinya dalam bahasa sehari-hari:",
        "Daftar Istilah: "
    )
    
    headers_glo = ["Istilah Teknis", "Definisi Sederhana", "Perannya dalam Proyek Ini"]
    rows_glo = [
        ["WAP (Wireless Access Point)", "Perangkat pemancar Wi-Fi / router di gedung.", "Menjadi fitur input utama model AI (WAP001 - WAP520)."],
        ["BSSID / MAC Address", "Nomor identitas unik dari setiap antena router.", "Pembeda antara router satu dengan router lainnya."],
        ["UTM Coordinate", "Sistem koordinat peta dalam satuan meter (bukan derajat GPS).", "Target regresi kita (Longitude & Latitude dalam meter riil)."],
        ["Multi-Output Regression", "Model AI yang memprediksi 2 angka kontinu sekaligus.", "Memprediksi sumbu X (Longitude) dan sumbu Y (Latitude) serentak."],
        ["Classification", "Tugas AI untuk menebak kategori/grup diskrit.", "Menebak Gedung (0, 1, 2) dan Lantai (0, 1, 2, 3, 4)."],
        ["Min-Max Normalization", "Mengubah rentang angka sembarang menjadi 0 sampai 1.", "Menghindari ledakan gradien matematis pada neural network."],
        ["VarianceThreshold", "Metode pembuangan fitur yang nilainya konstan di semua baris.", "Menghapus WAP mati yang tidak pernah terdeteksi sama sekali."],
        ["Cross-Validation (CV)", "Teknik membagi data jadi k bagian untuk menguji kestabilan.", "Memastikan model tidak hanya beruntung pada satu potongan data."],
        ["Epoch", "Satu putaran penuh model membaca seluruh data latih.", "Menentukan seberapa lama neural network berlatih (misal 50 epoch)."],
        ["Batch Size", "Jumlah sampel data yang diproses sebelum bobot AI diperbarui.", "Ukuran kelompok data latih sekali jalan (misal 64 baris)."],
        ["Dropout", "Teknik mematikan neuron acak selama proses latihan.", "Obat pencegah overfitting agar neural network tidak menghafal."],
        ["Early Stopping", "Mekanisme penghentian otomatis latihan jika model mulai mandek.", "Menghemat waktu komputasi dan mencegah model memorisasi noise."],
        ["Loss Function (MSE)", "Fungsi pengukur seberapa besar kesalahan tebakan model.", "Menghitung rata-rata kuadrat selisih antara tebakan vs asli."],
        ["Euclidean Distance", "Jarak garis lurus antara dua titik pada bidang datar ($d = \\sqrt{\\Delta x^2 + \\Delta y^2}$).", "Metrik evaluasi utama dalam meter (Positioning Error)."],
        ["Domain Shift / Covariate Shift", "Perubahan karakteristik data antara saat latihan dan pengujian nyata.", "Penyebab galat naik di data validasi karena beda smartphone/waktu."]
    ]
    create_table(headers_glo, rows_glo, [1.8, 2.3, 2.4])

    doc.add_page_break()

    # -------------------------------------------------------------
    # BAB 2: METODOLOGI & ALUR PENGERJAAN 4 PROSES UTAMA (BEDAH PER KOMPONEN)
    # -------------------------------------------------------------
    add_h1("BAB 2: METODOLOGI & ALUR PENGERJAAN 4 PROSES UTAMA (BEDAH PER KOMPONEN)")
    add_p(
        "Seluruh alur pengerjaan pada proyek ini terstruktur secara rapi menjadi 4 PROSES UTAMA yang saling berkesinambungan. Setiap proses memiliki tujuan, tantangan, dan komponen teknis spesifik yang dieksekusi secara ketat guna menjamin kualitas model dan mencegah kebocoran data (data leakage).",
        "Ikhtisar Alur Kerja: "
    )
    
    headers_proses_summary = ["Proses Utama", "Fokus Utama", "Metode & Algoritma", "Luaran / Output Kunci"]
    rows_proses_summary = [
        ["PROSES 1: EDA & Data Preprocessing", "Pembersihan sinyal, rekayasa nilai sentinel, scaling, seleksi fitur, & splitting.", "Imputation -105 dBm, Min-Max Scaling, VarianceThreshold, Stratified Split.", "Dataset bersih siap latih (Train/Test 80:20 & 70:30) tanpa data leakage."],
        ["PROSES 2: Clustering (Unsupervised)", "Eksplorasi struktur intrinsik sinyal tanpa label spasial.", "K-Means (k=3), DBSCAN, PCA 2D Dimensionality Reduction.", "Pembuktian bahwa sinyal Wi-Fi secara alami membentuk klaster gedung."],
        ["PROSES 3: Supervised Machine Learning", "Pemodelan prediktif klasik untuk klasifikasi dan regresi koordinat.", "Random Forest, k-NN, SVR, Gradient Boosting, 5-Fold Stratified CV.", "Akurasi Gedung (99.8%), Lantai (99.6%), baseline regresi, Feature Importance."],
        ["PROSES 4: Deep Learning (ANN/MLP) & Evaluasi", "Arsitektur jaringan saraf tiruan mendalam & validasi lapangan menyeluruh.", "Multi-Layer Perceptron (Dense-Dropout-ReLU-Linear), Adam, Early Stopping.", "Koordinat 2D (Galat 4.15 m internal), kurva loss konvergen, uji validasi eksternal."]
    ]
    create_table(headers_proses_summary, rows_proses_summary, [1.8, 1.8, 1.6, 1.3])

    # ----------------- PROSES 1 -----------------
    add_h2("2.1 PROSES 1: Exploratory Data Analysis (EDA) & Data Preprocessing")
    add_p(
        "Tujuan: Memahami karakteristik statistik data, mentransformasikan sinyal mentah ke bentuk representasi fisik yang benar, membersihkan fitur mubazir, dan membagi dataset secara adil tanpa kebocoran data.",
        "Sasaran Proses: "
    )
    
    add_h3("Komponen 1.1: Pemeriksaan Struktur Data & Tipe Fitur")
    add_p(
        "Melakukan audit terhadap 19.937 baris dan 529 kolom. Mengidentifikasi bahwa 520 kolom pertama (WAP001–WAP520) adalah fitur numerik kontinu RSSI yang tidak memerlukan One-Hot Encoding teks, sedangkan kolom target terdiri dari target kategorik (BUILDINGID, FLOOR) dan target numerik kontinu (LONGITUDE, LATITUDE).",
        "Aktivitas: "
    )

    add_h3("Komponen 1.2: Penanganan Nilai Sentinel (+100 dBm ke -105 dBm)")
    add_p(
        "Nilai bawaan +100 (router tidak terdeteksi) diganti dengan -105 dBm. Secara fisis, -105 dBm adalah batas ambang bawah kebisingan termal (noise floor) antena smartphone komersial. Mengubahnya ke -105 dBm memosisikan sinyal yang tidak ada sebagai sinyal terlemah, bukan terkuat.",
        "Aktivitas: "
    )

    add_h3("Komponen 1.3: Normalisasi Fitur (Feature Scaling [0, 1])")
    add_p(
        "Menerapkan Min-Max Scaling dengan rumus x_norm = (x - (-105)) / (-30 - (-105)). Hasilnya, sinyal tidak terdeteksi bernilai 0.0 murni dan sinyal terkuat bernilai 1.0. Penyekalaan ini dilakukan dengan prinsip anti-leakage: parameter fitting hanya dipelajari dari data training.",
        "Aktivitas: "
    )

    add_h3("Komponen 1.4: Seleksi Fitur (VarianceThreshold Filtering)")
    add_p(
        "Menghitung variansi dari seluruh 520 WAP pada data latih. WAP yang memiliki variansi 0.0 (artinya bernilai konstan -105 dBm di seluruh rekaman) dieliminasi dari matriks input. Komponen ini sukses memangkas puluhan WAP mati yang tidak membawa informasi diskriminasi spasial.",
        "Aktivitas: "
    )

    add_h3("Komponen 1.5: Pembagian Data (Data Splitting 80:20 & 70:30)")
    add_p(
        "Membagi data trainingData.csv menjadi dua skenario eksperimen: (1) Skenario 80:20 untuk evaluasi utama, dan (2) Skenario 70:30 untuk menguji stabilitas model saat volume data latih dikurangi. Untuk target klasifikasi, pembagian menggunakan Stratified Split guna menjamin proporsi setiap gedung dan lantai tetap seimbang.",
        "Aktivitas: "
    )

    # ----------------- PROSES 2 -----------------
    add_h2("2.2 PROSES 2: Clustering (Unsupervised Learning)")
    add_p(
        "Tujuan: Menyelidiki apakah data sinyal Wi-Fi mentah memiliki struktur geometri alami yang mampu membedakan gedung dan zona ruangan secara mandiri tanpa membutuhkan label supervisi manusia.",
        "Sasaran Proses: "
    )

    add_h3("Komponen 2.1: Reduksi Dimensi Fitur untuk Visualisasi (PCA)")
    add_p(
        "Menerapkan Principal Component Analysis (PCA) untuk mereduksi 400+ dimensi sinyal WAP aktif menjadi 2 komponen utama (PC1 dan PC2). Komponen ini memungkinkan visualisasi sebaran energi radio pada bidang kartesius 2D.",
        "Aktivitas: "
    )

    add_h3("Komponen 2.2: Klasterisasi K-Means Berbasis Jarak Euclidean")
    add_p(
        "Menjalankan algoritma K-Means dengan k=3 (sesuai jumlah gedung kampus). Algoritma secara iteratif memperbarui posisi centroid hingga konvergen. Hasilnya, 3 klaster unsupervised terbentuk dengan sangat tegas dan hampir 100% kongruen dengan batas 3 gedung fisik.",
        "Aktivitas: "
    )

    add_h3("Komponen 2.3: Klasterisasi Berbasis Densitas (DBSCAN)")
    add_p(
        "Menguji pengelompokan berbasis kepadatan menggunakan DBSCAN. Komponen ini berhasil mendeteksi area titik-titik koridor padat serta mengisolasi titik-titik anomali/derau sinyal di luar klaster utama.",
        "Aktivitas: "
    )

    add_h3("Komponen 2.4: Validasi Metrik Klaster (Silhouette & Centroid Analysis)")
    add_p(
        "Mengevaluasi separabilitas klaster menggunakan Silhouette Score dan mengekstraksi koordinat pusat massa (centroid) untuk membuktikan kestabilan klasterisasi spasial.",
        "Aktivitas: "
    )

    # ----------------- PROSES 3 -----------------
    add_h2("2.3 PROSES 3: Model Machine Learning Supervised")
    add_p(
        "Tujuan: Membangun model prediktif terawasi (supervised) untuk menyelesaikan dua tugas utama: klasifikasi ruang diskrit (Gedung & Lantai) dan regresi koordinat ruang kontinu (Longitude & Latitude).",
        "Sasaran Proses: "
    )

    add_h3("Komponen 3.1: Desain Pipeline Bebas Kebocoran Data (Pipeline Architecture)")
    add_p(
        "Membungkus seluruh tahapan preprocessing dan estimator ke dalam sklearn.pipeline.Pipeline. Ini menjamin bahwa dalam setiap iterasi cross-validation, scaler dan selector hanya di-fit pada fold pelatihan dan diterapkan pada fold validasi.",
        "Aktivitas: "
    )

    add_h3("Komponen 3.2: Klasifikasi Hierarkis (Building & Floor Classification)")
    add_p(
        "Melatih dan membandingkan beberapa algoritma: Random Forest Classifier, k-Nearest Neighbors (k-NN), Decision Tree, dan SVM. Menggunakan protokol 5-Fold Stratified Cross-Validation dengan metrik Accuracy dan Macro F1-score. Random Forest tampil sebagai model terbaik dengan akurasi gedung 99.8% dan lantai 99.6%.",
        "Aktivitas: "
    )

    add_h3("Komponen 3.3: Regresi Koordinat 2D (Longitude & Latitude Regression)")
    add_p(
        "Mengembangkan model regresi untuk memprediksi koordinat meter riil menggunakan k-NN Regressor, Random Forest Regressor, Gradient Boosting, dan Support Vector Regressor (SVR). Evaluasi dilakukan menggunakan metrik Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), dan koefisien determinasi (R² score).",
        "Aktivitas: "
    )

    add_h3("Komponen 3.4: Ekstraksi Kepentingan Fitur (Feature Importance Analysis)")
    add_p(
        "Mengekstraksi nilai Gini Importance dari ensemble Random Forest. Mengidentifikasi 15 WAP teratas (seperti WAP248, WAP500, dll.) yang memiliki kontribusi terbesar terhadap penurunan ketidakmurnian pohon keputusan saat menentukan lokasi.",
        "Aktivitas: "
    )

    # ----------------- PROSES 4 -----------------
    add_h2("2.4 PROSES 4: Multilayer Perceptron (MLP / ANN) & Evaluasi Akhir")
    add_p(
        "Tujuan: Merancang arsitektur Deep Learning jaringan saraf tiruan untuk regresi koordinat simultan serta melakukan evaluasi komprehensif pada data uji internal dan data validasi independen lapangan.",
        "Sasaran Proses: "
    )

    add_h3("Komponen 4.1: Desain Arsitektur Deep Learning Piramida Terbalik")
    add_p(
        "Membangun Multi-Layer Perceptron (MLP) dengan susunan 3 hidden layer: Dense 256 -> Dense 128 -> Dense 64 dengan aktivasi non-linear ReLU, dan lapisan output Dense 2 dengan aktivasi Linear untuk memprediksi Longitude dan Latitude secara serentak.",
        "Aktivitas: "
    )

    add_h3("Komponen 4.2: Mekanisme Regularisasi & Optimasi Pelatihan")
    add_p(
        "Menerapkan Dropout (rate 0.2) di setiap antar-layer, optimizer Adam dengan loss Mean Squared Error (MSE), normalisasi target StandardScaler, serta EarlyStopping callback (patience=10, restore_best_weights=True) guna memutus pelatihan otomatis saat validasi loss mulai plateau.",
        "Aktivitas: "
    )

    add_h3("Komponen 4.3: Evaluasi Data Uji Internal (Internal Test Set 80:20 & 70:30)")
    add_p(
        "Menghitung metrik Galat Posisi 2D Euclidean dalam satuan METER fisik. Menghasilkan rata-rata galat 4.15 meter (median 2.13 meter) pada split 80:20, serta 4.30 meter pada split 70:30. Menghasilkan visualisasi kurva loss, scatter prediksi vs aktual, dan residual plot.",
        "Aktivitas: "
    )

    add_h3("Komponen 4.4: Uji Validasi Lapangan pada Dataset Independen (External Validation)")
    add_p(
        "Menguji model terpilih langsung pada berkas validationData.csv (1.111 sampel baru) tanpa melakukan fitting ulang. Mengukur ketahanan model di dunia nyata dan menganalisis secara ilmiah penyebab kenaikan galat posisi melalui teori Covariate Shift / Domain Shift pada sinyal radio.",
        "Aktivitas: "
    )

    doc.add_page_break()

    # -------------------------------------------------------------
    # BAB 3: BEDAH DATASET & TAHAPAN PREPROCESSING TEKNIS
    # -------------------------------------------------------------
    add_h1("BAB 3: BEDAH DATASET & TAHAPAN PREPROCESSING TEKNIS")
    
    add_h2("3.1 Struktur Dataset Resmi UJIIndoorLoc")
    add_p(
        "Dataset yang digunakan adalah UJIIndoorLoc, standar baku dunia (benchmark) untuk penelitian indoor localization yang dikumpulkan oleh peneliti di Universitas Jaume I, Spanyol. Dataset ini terdiri dari dua berkas terpisah:\n"
        "• trainingData.csv: Berisi 19.937 sampel rekaman sinyal yang diambil oleh para peneliti dan relawan.\n"
        "• validationData.csv: Berisi 1.111 sampel independen yang diambil pada periode waktu berbeda dengan pengguna dan smartphone berbeda untuk menguji ketangguhan sistem di dunia nyata.",
        "Komposisi Berkas: "
    )
    add_p(
        "Setiap baris data mewakili 1 kali pemindaian Wi-Fi pada 1 titik koordinat tertentu, yang terdiri dari 529 kolom:\n"
        "1. Kolom 1 s.d. 520 (WAP001 - WAP520): Nilai RSSI yang ditangkap dari 520 router Wi-Fi yang ada di kampus.\n"
        "2. Kolom 521 & 522 (LONGITUDE, LATITUDE): Posisi koordinat presisi dalam sistem koordinat UTM (Universal Transverse Mercator) dengan satuan METER.\n"
        "3. Kolom 523 (FLOOR): Nomor lantai tempat pemindaian dilakukan (nilai integer 0 s.d. 4).\n"
        "4. Kolom 524 (BUILDINGID): Nomor identitas gedung (0: Gedung TI, 1: Gedung Sains, 2: Gedung Teknik).\n"
        "5. Kolom 525 - 529: Metadata pelengkap (SPACEID, RELATIVEPOSITION, USERID, PHONEID, TIMESTAMP).",
        "Rincian 529 Kolom: "
    )

    add_h2("3.2 Anomali Nilai `+100` dan Bahaya Matematisnya")
    add_p(
        "Di dalam file CSV mentah UJIIndoorLoc, pembuat dataset menggunakan angka +100 untuk menandai kondisi 'Router Wi-Fi tersebut tidak terdeteksi oleh smartphone'.",
        "Mengapa Ada Nilai +100? "
    )
    add_callout(
        "Mengapa Nilai +100 Sangat Fatal Jika Langsung Diumpan ke Model AI?",
        "Ingat konsep fisika RSSI:\n"
        "-30 dBm = Sinyal SANGAT KUAT (sangat dekat).\n"
        "-90 dBm = Sinyal SANGAT LEMAH (sangat jauh).\n\n"
        "Jika kita membiarkan nilai +100 tetap ada, algoritma matematika seperti Linear Regression, k-NN, atau Neural Network akan menganggap angka +100 adalah sinyal yang SEJUTA KALI LEBIH KUAT daripada -30 dBm! Model AI akan menyimpulkan bahwa WAP yang sebenarnya MATI/TIDAK TERDETEKSI justru berada persis menempel di kening pengguna! Ini akan menghancurkan akurasi model secara total.",
        "warning"
    )

    add_h2("3.3 Solusi Teknis: Penggantian ke -105 dBm dan Normalisasi Min-Max")
    add_p(
        "Untuk memperbaiki anomali ini, kita melakukan tahapan preprocessing dua langkah yang sangat elegan:\n"
        "1. Langkah 1: Mengganti semua nilai +100 menjadi -105 dBm. Mengapa angka -105? Karena batas derau terendah antena ponsel adalah sekitar -104 dBm. Memberi nilai -105 dBm secara fisik merepresentasikan 'sinyal berada di bawah ambang batas deteksi antena' (silent/no signal).\n"
        "2. Langkah 2: Melakukan Normalisasi Skala Min-Max ke Rentang [0, 1]. Rentang sinyal asli [-105 dBm s.d. -30 dBm] dipetakan ke [0.0 s.d. 1.0].",
        "Prosedur Perbaikan: "
    )
    add_p(
        "Rumus matematika transformasi sinyal yang kita gunakan adalah:\n\n"
        "x_norm = (x - (-105)) / (-30 - (-105)) = (x + 105) / 75\n\n"
        "• Jika WAP tidak terdeteksi (x = -105 dBm) -> x_norm = (-105 + 105) / 75 = 0.0 (Nol murni).\n"
        "• Jika WAP sangat kuat (x = -30 dBm) -> x_norm = (-30 + 105) / 75 = 75 / 75 = 1.0 (Maksimal).\n"
        "Dengan cara ini, nilai 0 secara intuitif berarti 'tidak ada sinyal', dan angka mendekati 1 berarti 'sinyal sangat kuat'. Neural Network sangat menyukai angka dalam rentang [0, 1] karena komputasi gradien matriks bobotnya menjadi sangat stabil dan cepat konvergen.",
        "Rumus Transformasi: "
    )

    add_h2("3.4 Seleksi Fitur dengan VarianceThreshold (Membuang WAP Mati)")
    add_p(
        "Dari 520 WAP yang tercatat di dataset, apakah semuanya berguna? Ternyata tidak!\n"
        "Saat kita mengecek variansi nilai dari 520 WAP tersebut, terdapat puluhan WAP yang nilainya konstan 0.0 (alias -105 dBm) di SELURUH 19.937 baris data latih. Artinya, WAP tersebut mungkin router cadangan yang mati, WAP yang sudah dicabut, atau hanya ada di gedung lain yang tidak pernah terdeteksi sama sekali selama pengambilan data latih.",
        "Masalah WAP Mati: "
    )
    add_p(
        "Fitur yang variansinya nol tidak memiliki daya pembeda sama sekali (Zero Information Gain). Oleh karena itu, kita menjalankan modul VarianceThreshold(threshold=0.0) dari scikit-learn. Modul ini secara otomatis mengeliminasi WAP yang mati tersebut, menyisakan hanya WAP yang benar-benar aktif. Hasilnya:\n"
        "• Mengurangi beban komputasi memori RAM dan GPU secara drastis.\n"
        "• Mencegah model menghafal bobot sia-sia (mengurangi risiko overfitting).",
        "Tindakan Pembersihan: "
    )

    doc.add_page_break()

    # -------------------------------------------------------------
    # BAB 4: PANDUAN LITERASI VISUAL: CARA MEMBACA & MENGANALISIS GRAFIK
    # -------------------------------------------------------------
    add_h1("BAB 4: PANDUAN LITERASI VISUAL (CARA MEMBACA & MENGANALISIS SETIAP GRAFIK)")
    add_p(
        "Bab ini adalah intisari bagi pembaca awam untuk memahami makna mendalam di balik grafik-grafik visual yang dihasilkan oleh proyek ini. Jangan hanya melihat grafik sebagai gambar warna-warni, tetapi pahami cerita ilmiah di baliknya!",
        "Pengantar Visual: "
    )

    # Grafik 1
    add_h2("4.1 Grafik 1: Peta Sebaran Spasial Pengguna (Indoor Localization Map)")
    add_figure("assets/indoor_localization_map.png", "Peta Sebaran Pengguna Berdasarkan Koordinat UTM Asli (Gedung 0, 1, dan 2)", 5.2)
    add_p(
        "• Sumbu X (Mendatar): Menunjukkan koordinat Longitude UTM dalam satuan METER (berkisar antara -7690 m hingga -7300 m).\n"
        "• Sumbu Y (Tegak): Menunjukkan koordinat Latitude UTM dalam satuan METER (berkisar antara 4.86475 × 10⁶ m hingga 4.86505 × 10⁶ m).\n"
        "• Warna Titik: Menunjukkan identitas gedung tempat titik direkam (Warna Merah = Gedung 0, Hijau = Gedung 1, Biru = Gedung 2).",
        "Cara Membaca Elemen Grafik: "
    )
    add_p(
        "1. Tiga Gugusan Terpisah: Terlihat sangat jelas ada 3 blok area besar yang terpisah secara fisik. Ini adalah 3 gedung utama di kampus Universitas Jaume I.\n"
        "2. Gedung Berorientasi Miring: Mengapa gugusan titik tidak membentuk kotak horizontal tegak lurus melainkan agak menyerong miring? Karena bangunan gedung di dunia nyata memang dibangun mengikuti kontur jalan kampus yang memiliki sudut kemiringan (rotasi azimuth) tertentu terhadap arah utara bumi.\n"
        "3. Kepadatan Titik: Titik-titik berbaris rapat mengikuti jalur koridor, selasar, dan pintu-pintu ruangan tempat para pengambil data berjalan merekam sinyal Wi-Fi.",
        "Analisis Mendalam & Kesimpulan: "
    )

    # Grafik 2
    add_h2("4.2 Grafik 2: Reduksi Dimensi PCA & Klaster K-Means")
    add_figure("assets/clustering_pca2d.png", "Visualisasi Klaster K-Means (K=3) pada Bidang 2D Hasil Reduksi Dimensi PCA", 5.2)
    add_p(
        "• Kita memiliki lebih dari 400 WAP aktif (artinya data kita memiliki 400 dimensi lebih). Manusia tidak bisa membayangkan grafik 400 dimensi!\n"
        "• Algoritma PCA (Principal Component Analysis) digunakan untuk memadatkan 400 dimensi sinyal Wi-Fi tersebut menjadi hanya 2 dimensi utama (PC1 dan PC2) yang merangkum sebagian besar variansi energi sinyal.\n"
        "• Sumbu X (PC1) & Sumbu Y (PC2): Kombinasi linear matematis dari kekuatan sinyal WAP.\n"
        "• Tanda Bintang Merah Besar (★): Pusat massa (centroid) dari masing-masing klaster yang ditemukan oleh algoritma unsupervised K-Means.",
        "Cara Membaca Elemen Grafik: "
    )
    add_p(
        "1. K-Means Bekerja Tanpa Mengetahui Label Gedung: Algoritma K-Means dijalankan murni secara unsupervised (tanpa diberitahu koordinat maupun nomor gedung).\n"
        "2. Klaster Alami Terbentuk Sempurna: Ajaibnya, titik-titik data otomatis memisahkan diri menjadi 3 klaster besar yang sangat rapi! Bentuk pemisahan ini hampir 100% cocok dengan pemisahan gedung fisik.\n"
        "3. Makna Fisika Telekomunikasi: Ini membuktikan secara empiris bahwa sidik jari sinyal Wi-Fi memang memiliki daya diskriminasi spasial alami yang luar biasa kuat. Router di Gedung 0 hampir tidak pernah terdengar di Gedung 2, sehingga jarak matematikanya sangat jauh.",
        "Analisis Mendalam & Kesimpulan: "
    )

    # Grafik 3
    add_h2("4.3 Grafik 3: Confusion Matrix (Klasifikasi Gedung & Lantai)")
    add_figure("assets/confusion_matrix.png", "Confusion Matrix untuk Klasifikasi Gedung (Kiri) dan Klasifikasi Lantai (Kanan)", 5.6)
    add_p(
        "• Sumbu Y (Baris Tegak): Label Sebenarnya (True Class) di dunia nyata.\n"
        "• Sumbu X (Kolom Mendatar): Label Hasil Prediksi (Predicted Class) oleh model Random Forest.\n"
        "• Garis Diagonal Utama (Kiri Atas ke Kanan Bawah): Kotak-kotak tempat prediksi model BENAR 100% (True Positive).\n"
        "• Kotak di Luar Diagonal Utama: Kotak tempat model MELAKUKAN KESALAHAN (Error / Miss-classification). Semakin gelap/pekat warna birunya, semakin banyak jumlah sampel di kotak tersebut.",
        "Cara Membaca Elemen Grafik: "
    )
    add_p(
        "1. Klasifikasi Gedung (Panel Kiri): Nilai di luar diagonal utama hampir NOL BESAR. Akurasi tebakan gedung mencapai 99.8%! Hanya ada 2-3 sampel yang salah tebak. Ini berarti model hampir tidak pernah tersesat salah gedung.\n"
        "2. Klasifikasi Lantai (Panel Kanan): Diagonal utama sangat terang dan tebal (akurasi ~99.6%). Namun jika Anda perhatikan dengan teliti di luar diagonal, terdapat sedikit kesalahan tebak: misalnya Lantai 2 diprediksi sebagai Lantai 1 atau Lantai 3.\n"
        "3. Mengapa Tebakan Lantai Bisa Salah 'Off-by-One'? Dalam fisika radio, gelombang elektromagnetik Wi-Fi merambat ke segala arah secara sferis (3 dimensi). Sinyal router yang menempel di langit-langit Lantai 1 dapat menembus cor-coran lantai beton tipis dan terdeteksi di Lantai 2 dengan kekuatan sinyal yang hampir setara. Inilah yang terkadang mengecoh model dalam membedakan lantai yang bertetangga persis di atas/bawahnya.",
        "Analisis Mendalam & Kesimpulan: "
    )

    # Grafik 4
    add_h2("4.4 Grafik 4: Residual Plot & Scatter Prediksi vs Aktual")
    add_figure("assets/regression_residuals.png", "Evaluasi Model Regresi Koordinat: Garis Prediksi vs Aktual (Kiri) dan Sebaran Residual (Kanan)", 5.6)
    add_p(
        "• Panel Kiri (Garis Prediksi vs Aktual): Sumbu X adalah koordinat asli (meter), dan Sumbu Y adalah koordinat prediksi (meter). Garis merah putus-putus adalah garis kesempurnaan (y = x).\n"
        "• Panel Kanan (Residual Plot): Sumbu X adalah nilai prediksi koordinat, dan Sumbu Y adalah Residual / Galat (Nilai Asli dikurangi Nilai Prediksi, dalam satuan meter). Garis horizontal merah adalah garis galat nol.",
        "Cara Membaca Elemen Grafik: "
    )
    add_p(
        "1. Titik Menempel Sangat Ketat pada Garis Diagonal: Pada panel kiri, ribuan titik data membentuk garis lurus sempurna menempel pada garis diagonal merah. Ini bukti visual mengapa skor R² bernilai di atas 0.99 (korelasi hampir sempurna).\n"
        "2. Sebaran Residual Simetris (Homoscedasticity): Pada panel kanan, sebaran titik-titik galat terpusat padat di sekitar angka 0 meter dan tersebar merata secara acak antara rentang -10 m hingga +10 m. Tidak terlihat adanya pola melengkung atau pola corong melebar (heteroskedasticity). Ini membuktikan bahwa model regresi kita tidak memiliki bias sistematis dan galatnya bersifat acak alami.",
        "Analisis Mendalam & Kesimpulan: "
    )

    # Grafik 5
    add_h2("4.5 Grafik 5: Kurva Pelatihan Deep Learning (Loss Curve)")
    add_figure("assets/mlp_loss_curve.png", "Kurva Pelatihan Multi-Layer Perceptron (Train Loss vs Validation Loss)", 5.0)
    add_p(
        "• Sumbu X (Mendatar): Jumlah putaran latihan (Epoch) dari epoch 1 hingga epoch 50.\n"
        "• Sumbu Y (Tegak): Nilai Mean Squared Error (Loss), yang menunjukkan seberapa besar kesalahan tebakan model.\n"
        "• Garis Biru: Train Loss (kesalahan model pada data yang dipakai latihan).\n"
        "• Garis Oranye: Validation Loss (kesalahan model pada data validasi yang tidak dipakai latihan).",
        "Cara Membaca Elemen Grafik: "
    )
    add_p(
        "1. Penurunan Drastis di Awal (Epoch 1 s.d. 10): Kedua kurva meluncur turun secara tajam. Ini fase di mana neural network dengan sangat cepat menangkap pola geometris dasar sinyal Wi-Fi.\n"
        "2. Kurva Melandai Bersama (Plateau di Epoch 30 s.d. 50): Garis oranye (validasi) terus menempel ketat tepat di samping garis biru (latih) dan keduanya mendatar stabil.\n"
        "3. Tanda Mutlak Model BUKAN Overfitting: Jika model mengalami overfitting, garis biru akan terus turun mendekati nol, sedangkan garis oranye akan BERBALIK NAIK TAJAM ke atas (membentuk pola mulut buaya / divergensi). Karena garis oranye kita tetap rendah dan stabil mendatar, ini adalah bukti empiris tak terbantahkan bahwa Deep Learning kita berstatus GOOD FIT!",
        "Analisis Mendalam & Kesimpulan: "
    )

    # Grafik 6
    add_h2("4.6 Grafik 6: Feature Importance (WAP Paling Berpengaruh)")
    add_figure("assets/feature_importance.png", "15 Router Wi-Fi (WAP) yang Paling Berpengaruh dalam Penentuan Posisi", 5.2)
    add_p(
        "• Sumbu X (Mendatar): Skor Kepentingan Fitur (Feature Importance / Gini Importance) yang dihitung dari algoritma Random Forest.\n"
        "• Sumbu Y (Tegak): Nama-nama Access Point (WAP).\n"
        "• Panjang Batang: Semakin panjang batangnya ke kanan, semakin krusial peran WAP tersebut sebagai penentu lokasi pengguna.",
        "Cara Membaca Elemen Grafik: "
    )
    add_p(
        "1. Segelintir WAP Memegang Peran Kunci: Dari 400+ WAP yang ada, terdapat sekitar 15-20 WAP (seperti WAP248, WAP500, WAP011, dll.) yang memiliki batang sangat panjang dibanding ratusan WAP lainnya yang batangnya nyaris nol.\n"
        "2. Mengapa WAP Tertentu Sangat Penting? Router-router ini umumnya terpasang di lokasi-lokasi strategis: di tengah-tengah persimpangan koridor utama, di aula sentral, atau di batas antar gedung. Ketika sinyal dari WAP ini tertangkap kuat, model AI langsung bisa dengan sangat yakin memastikan koordinat zona pengguna.",
        "Analisis Mendalam & Kesimpulan: "
    )

    doc.add_page_break()

    # -------------------------------------------------------------
    # BAB 5: RUMUS MATEMATIKA, METRIK, & CARA PERHITUNGAN MANUAL
    # -------------------------------------------------------------
    add_h1("BAB 5: RUMUS MATEMATIKA, METRIK, & CARA PERHITUNGAN MANUAL")
    add_p(
        "Bagi orang awam, rumus matematika seringkali terlihat menakutkan. Di bab ini, kita akan membedah setiap rumus menjadi langkah-langkah aritmatika sederhana yang bahkan bisa dihitung menggunakan kalkulator smartphone biasa!",
        "Pengantar Matematika: "
    )

    add_h2("5.1 Rumus Galat Posisi 2D Euclidean (Positioning Error)")
    add_p(
        "Ini adalah metrik evaluasi paling penting di seluruh proyek ini. Kita tidak bisa hanya mengukur 'akurasi 90%' pada koordinat, karena koordinat adalah posisi di bumi. Pengguna ingin tahu: 'Jika aplikasi menebak posisi saya, berapa meter melesetnya dari posisi asli saya?'",
        "Mengapa Butuh Jarak Euclidean? "
    )
    add_p(
        "Rumus jarak garis lurus 2D (berdasarkan teorema Pythagoras kuno):\n\n"
        "Positioning Error_i = √[ (x̂_i - x_i)² + (ŷ_i - y_i)² ]\n\n"
        "Keterangan Simbol:\n"
        "• x̂_i = Nilai Longitude hasil tebakan model AI (meter).\n"
        "• x_i = Nilai Longitude aktual / posisi GPS asli pengguna (meter).\n"
        "• ŷ_i = Nilai Latitude hasil tebakan model AI (meter).\n"
        "• y_i = Nilai Latitude aktual / posisi GPS asli pengguna (meter).\n"
        "• Positioning Error_i = Seberapa jauh tebakan model meleset dalam satuan METER.",
        "Rumus Matematika: "
    )

    add_h2("5.2 Simulasi Perhitungan Manual Langkah Demi Langkah (Contoh Nyata 1 Sampel)")
    add_callout(
        "Mari Menghitung Manual Seperti Mesin Menghitung!",
        "Misalkan seorang mahasiswa berdiri di lantai 1 Gedung Teknik:\n"
        "• Posisi Asli Mahasiswa (Aktual):\n"
        "  Longitude (x) = -7500.00 meter\n"
        "  Latitude (y)  = 4864800.00 meter\n\n"
        "• Hasil Prediksi Model Deep Learning Kita:\n"
        "  Longitude (x̂) = -7502.40 meter\n"
        "  Latitude (ŷ)  = 4864803.20 meter\n\n"
        "LANGKAH PERHITUNGAN:\n"
        "1. Hitung selisih sumbu X (Δx):\n"
        "   Δx = x̂ - x = -7502.40 - (-7500.00) = -2.40 meter (meleset 2.4 m ke barat)\n"
        "2. Hitung selisih sumbu Y (Δy):\n"
        "   Δy = ŷ - y = 4864803.20 - 4864800.00 = +3.20 meter (meleset 3.2 m ke utara)\n"
        "3. Kuadratkan masing-masing selisih:\n"
        "   (Δx)² = (-2.40)² = 5.76\n"
        "   (Δy)² = (3.20)²  = 10.24\n"
        "4. Jumlahkan kedua kuadrat:\n"
        "   Jumlah = 5.76 + 10.24 = 16.00\n"
        "5. Tarik akar kuadrat:\n"
        "   Positioning Error = √16.00 = 4.00 meter!\n\n"
        "Kesimpulan Sederhana: Model AI meleset sejauh tepat 4.00 meter dari posisi kaki mahasiswa tersebut berdiri di dunia nyata.",
        "concept"
    )

    add_h2("5.3 Mean Positioning Error (MPE) vs Median Positioning Error")
    add_p(
        "Jika kita memiliki 3.988 sampel data uji, kita menghitung Positioning Error untuk setiap sampel, lalu merangkumnya:\n"
        "1. Mean Positioning Error (MPE): Rata-rata dari seluruh galat:\n"
        "   MPE = (1 / N) * ∑ [ Positioning Error_i ]\n"
        "   Pada proyek kita, nilai MPE data uji internal adalah 4.15 meter.\n"
        "2. Median Positioning Error: Nilai tengah dari galat setelah diurutkan dari terkecil ke terbesar:\n"
        "   Pada proyek kita, nilai Median Galat adalah 2.13 meter!\n\n"
        "Mengapa Nilai Median Jauh Lebih Kecil (2.13 m vs 4.15 m)?\n"
        "Dalam statistik telekomunikasi, nilai rata-rata (mean) sangat mudah ditarik ke atas oleh segelintir data outlier ekstrem (misalnya ada 5 ponsel yang mengalami error sensor sehingga meleset 50 meter). Nilai median membuktikan bahwa untuk 50% pengguna di lapangan, tebakan model AI meleset HANYA SEJAUH 2 METER (setara 2 langkah kaki manusia)! Ini adalah akurasi yang luar biasa presisi untuk sistem berbasis Wi-Fi komersial.",
        "Analisis Statistik: "
    )

    add_h2("5.4 Mean Absolute Error (MAE) & Skor R²")
    add_p(
        "• MAE Longitude (2.84 meter): Rata-rata kesalahan tebakan pada sumbu mendatar (timur-barat).\n"
        "• MAE Latitude (2.36 meter): Rata-rata kesalahan tebakan pada sumbu tegak (utara-selatan).\n"
        "• R² Score (0.999): Koefisien determinasi. Angka 1.0 berarti prediksi sempurna tanpa cacat. Skor 0.999 menunjukkan bahwa model menangkap 99.9% pola sebaran koordinat gedung secara absolut.",
        "Metrik Per Sumbu: "
    )

    doc.add_page_break()

    # -------------------------------------------------------------
    # BAB 6: ARSITEKTUR MODEL & METODOLOGI PEMBELAJARAN
    # -------------------------------------------------------------
    add_h1("BAB 6: ARSITEKTUR MODEL & METODOLOGI PEMBELAJARAN")
    
    add_h2("6.1 Strategi Dua Tahap (Hierarchical Pipeline)")
    add_p(
        "Alih-alih memaksa satu model AI menebak segala hal sekaligus, sistem navigasi modern menggunakan pendekatan hierarkis dua tahap:\n"
        "• Tahap 1 (Ruang Diskrit / Klasifikasi): Menentukan Gedung (Building 0, 1, 2) dan Lantai (Floor 0 s.d. 4). Karena gedung dan lantai adalah kategori diskrit (tidak ada lantai 2.7 atau gedung 1.5), kita menggunakan model Klasifikasi.\n"
        "• Tahap 2 (Ruang Kontinu / Regresi Koordinat 2D): Menentukan posisi presisi (Longitude & Latitude dalam meter). Karena posisi pengguna adalah angka riil pecahan, kita menggunakan model Regresi.",
        "Arsitektur Sistem: "
    )

    add_h2("6.2 Mengapa Random Forest Sangat Perkasa di Data Sinyal Wi-Fi?")
    add_p(
        "Untuk klasifikasi Gedung dan Lantai, model Random Forest Classifier menghasilkan akurasi mencengangkan ($99.8\\%$ Gedung, $99.6\\%$ Lantai). Mengapa model pohon keputusan (tree-based) sangat unggul?\n"
        "1. Robust terhadap Sinyal Nol (Sparse Data): Sebagian besar nilai WAP adalah 0.0 (tidak terdeteksi). Pohon keputusan bekerja dengan aturan 'If WAP_X > 0.4 then...'. Jika WAP tidak ada, pohon dengan cepat memotong cabang pencarian tanpa terganggu nilai nol.\n"
        "2. Menangani Hubungan Non-Linear & Discontinuous Step: Batas antar lantai beton adalah batas tegas (step function), bukan kurva melengkung halus. Pohon keputusan sangat ahli memisahkan ruang fitur kotak-kotak diskrit seperti ini.\n"
        "3. Ensemble Voting (100 Pohon): Random Forest menggabungkan suara dari 100 pohon keputusan acak. Kesalahan satu pohon akan dikoreksi oleh mayoritas pohon lainnya.",
        "Alasan Ilmiah Keunggulan Random Forest: "
    )

    add_h2("6.3 Bedah Anatomi Multi-Layer Perceptron (MLP Deep Learning)")
    add_p(
        "Untuk memprediksi koordinat Longitude dan Latitude secara simultan, kita membangun jaringan saraf tiruan Multi-Layer Perceptron (MLP) berbasis Keras / TensorFlow.",
        "Arsitektur Neural Network: "
    )
    
    headers_mlp = ["Lapisan (Layer)", "Tipe Layer", "Jumlah Neuron", "Fungsi Aktivasi", "Fungsi & Peran Teknis"]
    rows_mlp = [
        ["Input Layer", "Input", "465 Fitur", "None", "Menerima vektor sinyal Wi-Fi ternormalisasi [0, 1]."],
        ["Hidden Layer 1", "Dense (Linear)", "256 Neuron", "ReLU", "Mengekstraksi representasi fitur global sinyal antar gedung."],
        ["Regularization 1", "Dropout", "Rate = 0.2", "None", "Mematikan 20% neuron secara acak untuk mencegah hafalan."],
        ["Hidden Layer 2", "Dense (Linear)", "128 Neuron", "ReLU", "Memetakan pola sinyal ke zona koridor lokal."],
        ["Regularization 2", "Dropout", "Rate = 0.2", "None", "Mencegah ko-adaptasi bobot antar neuron."],
        ["Hidden Layer 3", "Dense (Linear)", "64 Neuron", "ReLU", "Menghaluskan proyeksi koordinat spasial."],
        ["Output Layer", "Dense (Linear)", "2 Neuron", "Linear", "Menghasilkan 2 angka kontinu: [Longitude, Latitude]."]
    ]
    create_table(headers_mlp, rows_mlp, [1.3, 1.2, 1.1, 1.0, 1.9])

    add_callout(
        "Mengapa Layer Output Menggunakan Aktivasi Linear (Bukan Sigmoid atau Softmax)?",
        "Pertanyaan ini sering ditanyakan penguji!\n"
        "• Fungsi Sigmoid hanya menghasilkan angka antara 0.0 sampai 1.0 (cocok untuk probabilitas biner).\n"
        "• Fungsi Softmax menghasilkan distribusi probabilitas kelas yang jumlah totalnya 1.0 (cocok untuk klasifikasi).\n"
        "• Namun target regresi kita adalah koordinat UTM yang nilainya ribuan meter (misal Longitude = -7500.23 m, Latitude = 4864821.50 m). Oleh karena itu, kita WAJIB menggunakan aktivasi LINEAR (f(x) = x) agar neuron bebas memprediksi angka kontinu skala besar tanpa dibatasi oleh fungsi penjepit.",
        "info"
    )

    add_h2("6.4 Analisis Efisiensi Waktu & Jumlah Parameter")
    add_p(
        "• Total Parameter Terlatih (Trainable Parameters): Sekitar 180.000 bobot dan bias matematis.\n"
        "• Waktu Pelatihan: Hanya memerlukan waktu ~25 s.d. 35 detik pada komputer modern dengan GPU/CPU standar berkat optimasi vektorisasi Adam optimizer.\n"
        "• Waktu Inferensi (Kecepatan Tebak): Kurang dari 1 milidetik per sampel! Ini berarti sistem dapat dijalankan secara real-time pada aplikasi smartphone tanpa membuat ponsel panas atau lag.",
        "Metrik Efisiensi Komputasi: "
    )

    doc.add_page_break()

    # -------------------------------------------------------------
    # BAB 7: BEDAH KODINGAN SECARA TEKNIS (LINE-BY-LINE WALKTHROUGH)
    # -------------------------------------------------------------
    add_h1("BAB 7: BEDAH KODINGAN SECARA TEKNIS (LINE-BY-LINE WALKTHROUGH)")
    add_p(
        "Di bab ini, kita akan membedah potongan kode Python paling krusial yang ada di file `telco.ipynb`. Anda akan memahami fungsi dari setiap baris kode layaknya seorang programmer profesional.",
        "Pengantar Kode: "
    )

    add_h2("7.1 Kode Transformasi Sinyal & Normalisasi")
    code_prep = (
        "# 1. Ganti nilai +100 (tidak ada sinyal) menjadi -105 dBm (noise floor)\n"
        "raw_rssi = df[wap_columns].values\n"
        "raw_rssi[raw_rssi == 100] = -105.0\n\n"
        "# 2. Normalisasi Min-Max ke rentang [0.0, 1.0]\n"
        "# -105 dBm menjadi 0.0 (tiada sinyal), -30 dBm menjadi 1.0 (sinyal maksimal)\n"
        "X_norm = (raw_rssi - (-105.0)) / (-30.0 - (-105.0))\n"
        "X_norm = np.clip(X_norm, 0.0, 1.0)\n\n"
        "# 3. Eliminasi WAP yang mati total (variansi nol)\n"
        "selector = VarianceThreshold(threshold=0.0)\n"
        "X_clean = selector.fit_transform(X_norm)"
    )
    add_code_block(code_prep, "Preprocessing Sinyal Wi-Fi (Cell 35 - 45)")
    add_p(
        "Penjelasan Baris per Baris:\n"
        "• `raw_rssi[raw_rssi == 100] = -105.0`: Menggunakan masking boolean numpy. Semua elemen matriks yang bernilai 100 langsung diubah menjadi -105.0 dalam hitungan milidetik.\n"
        "• `X_norm = (raw_rssi - (-105.0)) / (-30.0 - (-105.0))`: Menerapkan rumus Min-Max Scaling.\n"
        "• `np.clip(X_norm, 0.0, 1.0)`: Memastikan secara absolut bahwa jika ada sinyal ekstrim yang lebih kuat dari -30 dBm (misal -25 dBm), nilainya dikunci di 1.0 (mencegah overflow).\n"
        "• `VarianceThreshold(threshold=0.0)`: Memindai kolom WAP; jika variansi suatu kolom = 0 (semua baris nilainya seragam), kolom tersebut langsung dibuang.",
        "Analisis Kode: "
    )

    add_h2("7.2 Kode Pembangunan Model Deep Learning (Keras Sequential)")
    code_keras = (
        "from tensorflow.keras.models import Sequential\n"
        "from tensorflow.keras.layers import Dense, Dropout\n"
        "from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint\n\n"
        "# Membangun arsitektur Multi-Layer Perceptron (MLP)\n"
        "model = Sequential([\n"
        "    Dense(256, activation='relu', input_shape=(X_train.shape[1],)),\n"
        "    Dropout(0.2),\n"
        "    Dense(128, activation='relu'),\n"
        "    Dropout(0.2),\n"
        "    Dense(64, activation='relu'),\n"
        "    Dense(2, activation='linear')  # Output 2 angka: Longitude & Latitude\n"
        "])\n\n"
        "# Kompilasi model dengan optimizer Adam dan loss MSE\n"
        "model.compile(optimizer='adam', loss='mse', metrics=['mae'])\n\n"
        "# Callback untuk mencegah overfitting\n"
        "callbacks = [\n"
        "    EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)\n"
        "]\n\n"
        "# Pelatihan model\n"
        "history = model.fit(X_train, y_train, validation_split=0.2, \n"
        "                    epochs=50, batch_size=64, callbacks=callbacks)"
    )
    add_code_block(code_keras, "Pembangunan & Pelatihan Neural Network (Cell 165 - 175)")
    add_p(
        "Penjelasan Baris per Baris:\n"
        "• `Dense(256, activation='relu')`: Membuat lapisan saraf buatan dengan 256 neuron yang dihubungkan penuh (*fully-connected*). Fungsi aktivasi ReLU mengabaikan nilai negatif dan meloloskan nilai positif, memungkinkan jaringan mempelajari batas non-linear.\n"
        "• `Dropout(0.2)`: Selama setiap batch latihan, 20% neuron dimatikan secara acak. Ini memaksa neuron lain untuk belajar secara mandiri dan tidak malas bergantung pada satu neuron dominan.\n"
        "• `optimizer='adam'`: Adaptive Moment Estimation, algoritma pembaruan bobot berbasis turunan kalkulus yang otomatis menyesuaikan learning rate secara dinamis.\n"
        "• `EarlyStopping(patience=10)`: Pengawas pintar. Jika loss validasi tidak mengalami penurunan selama 10 epoch berturut-turut, proses latihan langsung dihentikan dan bobot terbaik yang pernah dicapai akan dikembalikan (`restore_best_weights=True`).",
        "Analisis Kode: "
    )

    add_h2("7.3 Kode Komputasi Galat Posisi 2D Euclidean")
    code_error = (
        "# Prediksi koordinat pada data uji\n"
        "y_pred = model.predict(X_test)\n\n"
        "# Hitung galat Euclidean 2D dalam satuan meter\n"
        "delta_lon = y_pred[:, 0] - y_test[:, 0]\n"
        "delta_lat = y_pred[:, 1] - y_test[:, 1]\n"
        "errors_2d = np.sqrt(delta_lon**2 + delta_lat**2)\n\n"
        "# Ringkasan statistik galat\n"
        "mean_error = np.mean(errors_2d)\n"
        "median_error = np.median(errors_2d)\n"
        "print(f'Mean Positioning Error   : {mean_error:.2f} meter')\n"
        "print(f'Median Positioning Error : {median_error:.2f} meter')"
    )
    add_code_block(code_error, "Perhitungan Galat Posisi 2D dalam Meter (Cell 129 & 211)")
    add_p(
        "Penjelasan Baris per Baris:\n"
        "• `y_pred[:, 0]` adalah kolom Longitude hasil prediksi, dan `y_test[:, 0]` adalah Longitude aktual.\n"
        "• `delta_lon**2 + delta_lat**2`: Melakukan kuadrat selisih secara serentak untuk seluruh 3.988 baris data menggunakan vektorisasi numpy berkecepatan tinggi C.\n"
        "• `np.sqrt(...)`: Menarik akar kuadrat sehingga satuan hasil akhirnya kembali menjadi METER fisik.",
        "Analisis Kode: "
    )

    doc.add_page_break()

    # -------------------------------------------------------------
    # BAB 8: ANALISIS EVALUASI: OVERFITTING, UNDERFITTING, & COVARIATE SHIFT
    # -------------------------------------------------------------
    add_h1("BAB 8: ANALISIS EVALUASI: OVERFITTING, UNDERFITTING, & COVARIATE SHIFT")
    
    add_h2("8.1 Cara Membedakan Tiga Kondisi Utama Model AI")
    add_p(
        "Banyak orang salah kaprah saat mengevaluasi model AI. Tabel berikut memberikan panduan sederhana untuk membedakan ketiganya:",
        "Panduan Konsep: "
    )
    
    headers_fit = ["Kondisi Model", "Ciri pada Data Latih (Train)", "Ciri pada Data Uji (Test)", "Analogi Kehidupan Sehari-hari"]
    rows_fit = [
        ["Underfitting", "Jelek (Error besar)", "Jelek (Error besar)", "Siswa malas yang tidak pernah belajar; saat ujian soal apapun nilainya tetap buruk."],
        ["Overfitting", "Sangat Sempurna (Error ~0)", "Anjlok Hancur (Error raksasa)", "Siswa yang menghafal kunci jawaban persis titik komanya; saat ganti soal baru langsung panik dan gagal."],
        ["Good Fit (Optimal)", "Bagus & Rendah", "Bagus & Rendah (Seimbang)", "Siswa yang memahami konsep logika dasar; mampu menyelesaikan soal latihan maupun soal ujian baru dengan tenang."]
    ]
    create_table(headers_fit, rows_fit, [1.5, 1.8, 1.8, 1.9])

    add_h2("8.2 Mengapa Proyek Ini Dipastikan TIDAK Underfitting?")
    add_p(
        "Model kita menghasilkan R² score di atas 0.99, akurasi klasifikasi gedung 99.8%, dan galat rata-rata hanya 4.15 meter pada data uji. Jika model mengalami underfitting, galatnya akan berada di atas 50-100 meter dan akurasi tebakan gedungnya akan acak seperti melempar dadu (33%). Maka, dugaan underfitting sepenuhnya gugur.",
        "Bukti Empiris: "
    )

    add_h2("8.3 Mengapa Evaluasi Internal Berstatus Good Fit?")
    add_p(
        "Pada pengujian internal data latih vs data uji (baik rasio 80:20 maupun 70:30):\n"
        "1. Konsistensi Galat: Galat pada split 80:20 adalah 4.15 meter, dan pada split 70:30 adalah 4.30 meter (hanya selisih tipis 15 cm!). Ini membuktikan model tidak rapuh saat porsi data latih dikurangi.\n"
        "2. Kurva Loss Konvergen Seimbang: Nilai train loss dan val loss pada kurva MLP turun beriringan tanpa ada divergensi.\n"
        "3. K-Fold Cross-Validation: Nilai standar deviasi cross-validation sangat kecil (< 0.01), membuktikan model memiliki stabilitas yang merata di semua lipatan data.",
        "Bukti Empiris: "
    )

    add_h2("8.4 Mengapa Galat Naik di Data Validasi Eksternal (4.15 m -> 13.39 m)? (Bukan Overfitting, Tapi Covariate Shift!)")
    add_p(
        "Ketika diuji dengan file data independen resmi (validationData.csv), galat naik menjadi 13.39 meter (Random Forest) dan 18.75 meter (MLP). Apakah ini berarti model kita overfitting?",
        "Fenomena Lapangan: "
    )
    add_callout(
        "Penjelasan Ilmiah: Ini Adalah Covariate Shift / Domain Shift!",
        "Jawabannya adalah: BUKAN OVERFITTING MURNI, melainkan COVARIATE SHIFT (pergeseran distribusi data masukan) yang merupakan fenomena alami tak terhindarkan dalam sistem telekomunikasi nirkabel.\n\n"
        "Mengapa demikian?\n"
        "1. Heterogenitas Antena Smartphone (Hardware Drift):\n"
        "   Data latih (trainingData.csv) diambil menggunakan ponsel merk tertentu (misalnya Samsung Galaxy S3). Data validasi (validationData.csv) diambil menggunakan ponsel yang sama sekali berbeda (misalnya smartphone HTC atau Sony). Setiap produsen menggunakan chip Wi-Fi, gain antena, dan algoritma filtering firmware yang berbeda. Sebuah router yang terbaca -60 dBm di Samsung bisa terbaca -72 dBm di HTC di titik koordinat yang persis sama!\n\n"
        "2. Redaman Tubuh Manusia (Human Body Shadowing):\n"
        "   Frekuensi Wi-Fi 2.4 GHz memiliki panjang gelombang ~12 cm, yang sangat mudah diserap oleh molekul air. Tubuh manusia terdiri dari ~70% air! Jika pengguna memegang ponsel di depan dada menghadap utara, tubuhnya memblokir sinyal dari router yang ada di belakangnya sebesar 3 s.d. 6 dBm. Di data validasi, orang yang memegang ponsel berbeda tinggi badan, posisi genggaman, dan arah hadapnya.\n\n"
        "3. Fluktuasi Waktu & Lingkungan (Temporal Variations):\n"
        "   Data validasi diambil beberapa minggu/bulan kemudian. Posisi pintu yang tadinya terbuka menjadi tertutup, susunan meja lemari bergeser, dan kelembaban udara berubah, mempengaruhi pantulan gelombang radio (multipath fading).\n\n"
        "Kesimpulan: Model AI kita tidak bodoh ataupun overfit. Buktinya, model TETAP 100% TEPAT MENEBAK GEDUNG pada data validasi eksternal tersebut! Yang terjadi hanyalah pergeseran skala kekuatan sinyal (domain shift).",
        "concept"
    )

    add_h2("8.5 Solusi & Mitigasi di Masa Depan (Untuk Nilai Tambah)")
    add_p(
        "Jika Anda ingin meningkatkan akurasi pada perangkat yang berbeda di masa depan, solusi yang disarankan secara akademis adalah:\n"
        "1. Differential RSSI: Menggunakan selisih kekuatan sinyal antar pasangan WAP (RSSI_WAP1 - RSSI_WAP2) alih-alih nilai absolut. Karena perbedaan gain antena smartphone akan saling menghilangkan saat dikurangkan!\n"
        "2. Data Augmentation: Menambahkan derau acak Gaussian (Gaussian noise ±3 dBm) pada data sinyal Wi-Fi saat melatih neural network agar model kebal terhadap fluktuasi sinyal.\n"
        "3. Transfer Learning / Kalibrasi Cepat: Melakukan fine-tuning model hanya dengan mengambil 10 sampel sinyal cepat pada smartphone baru.",
        "Rekomendasi Riset Lanjutan: "
    )

    doc.add_page_break()

    # -------------------------------------------------------------
    # BAB 9: PANDUAN MENGHADAPI SIDANG / TANYA JAWAB DOSEN (TOP 10 FAQ)
    # -------------------------------------------------------------
    add_h1("BAB 9: PANDUAN MENGHADAPI SIDANG & TANYA JAWAB DOSEN (TOP 10 FAQ)")
    add_p(
        "Bab ini berisi daftar 10 pertanyaan kritis yang paling sering ditanyakan oleh dosen penguji atau audiens teknis, beserta strategi jawaban ilmiah paling cerdas dan berbasis data:",
        "Simulasi Sidang: "
    )

    faqs = [
        ("1. Mengapa memilih studi kasus Indoor Positioning dibanding prediksi telekomunikasi lainnya?",
         "Karena indoor positioning adalah salah satu tantangan terbesar di era modern (smart campus, navigasi rumah sakit, IoT industri, robotika otonom) di mana GPS terbukti lumpuh total. Pemanfaatan sinyal Wi-Fi eksisting adalah solusi zero-hardware cost yang sangat aplikatif dan menantang secara pemodelan spasial."),
         
        ("2. Kenapa nilai +100 pada dataset harus diubah ke -105 dBm dan bukan 0?",
         "Jika diubah menjadi 0, dalam skala dBm angka 0 justru berarti daya 1 miliwatt (sinyal yang luar biasa kuat). Mengubahnya ke -105 dBm adalah representasi fisik yang benar karena mencerminkan batas derau terbawah (noise floor) di mana antena tidak dapat mendeteksi sinyal router tersebut."),
         
        ("3. Mengapa untuk tebakan gedung & lantai Anda memakai Klasifikasi, bukan Regresi?",
         "Gedung dan lantai adalah entitas fisik diskrit dengan batas yang tegas (categorical boundaries). Tidak ada orang yang berdiri di 'Lantai 2.45' atau 'Gedung 0.8'. Menggunakan klasifikasi memungkinkan kita menggunakan metrik akurasi kelas dan fungsi loss cross-entropy yang memang didesain untuk probabilitas diskrit."),
         
        ("4. Mengapa Random Forest mengungguli model lain pada klasifikasi lantai?",
         "Karena Random Forest adalah ensemble tree yang tidak mengasumsikan distribusi linear. Sinyal Wi-Fi terhalang lantai beton mengalami pelemahan mendadak (discontinuous drop) yang sangat cocok dimodelkan oleh split orthogonal pohon keputusan."),
         
        ("5. Apa alasan arsitektur MLP Anda memiliki 3 hidden layer (256-128-64)?",
         "Arsitektur ini menerapkan prinsip piramida terbalik (funnel architecture). Lapisan pertama (256) menangkap kombinasi global dari ratusan router, lapisan kedua (128) menyaring pola area lokal gedung, dan lapisan ketiga (64) memproyeksikan fitur ke koordinat spasial halus sebelum diterjemahkan oleh 2 neuron output."),
         
        ("6. Mengapa pada layer output MLP menggunakan aktivasi linear?",
         "Karena target regresi kita adalah koordinat UTM yang bernilai ribuan meter (misal -7500 m dan 4.864.800 m). Aktivasi non-linear seperti Sigmoid atau Tanh akan membatasi rentang output antara 0 s.d. 1 atau -1 s.d. 1, yang akan merusak prediksi koordinat meter riil."),
         
        ("7. Apa fungsi Dropout dan Early Stopping dalam model Anda?",
         "Keduanya adalah senjata utama regularisasi. Dropout (0.2) mematikan 20% neuron secara acak untuk mencegah penghafalan data (co-adaptation). Early Stopping menghentikan proses iterasi secara otomatis begitu loss validasi berhenti membaik selama 10 epoch, mencegah overfitting."),
         
        ("8. Mengapa Anda menggunakan metrik Mean Positioning Error 2D (Euclidean) dan bukan MSE saja?",
         "MSE mengukur rata-rata kuadrat error secara terpisah per sumbu, yang sulit diimajinasikan secara intuitif. Galat Euclidean 2D menghitung jarak garis lurus langsung di atas tanah dalam satuan METER fisik, yang secara langsung menjawab pertanyaan praktis: 'Berapa meter sistem ini meleset di dunia nyata?'"),
         
        ("9. Apakah model Anda mengalami overfitting?",
         "Tidak. Pada pengujian internal, performa data latih dan data uji sangat seimbang (galat 4.15 m pada split 80:20 vs 4.30 m pada split 70:30) dan kurva loss validasi melandai stabil tanpa divergensi. Kenaikan galat pada dataset validasi independen UJIIndoorLoc disebabkan oleh fenomena Covariate Shift (perbedaan perangkat smartphone penerima dan variasi temporal), bukan karena model overfit."),
         
        ("10. Jika sistem ini diimplementasikan di gedung baru, apa yang harus dilakukan?",
         "Kita hanya perlu melakukan 'Site Survey' singkat (fase offline) dengan berjalan merekam sinyal Wi-Fi di titik-titik koridor gedung baru tersebut, menyimpan fingerprint-nya, lalu melatih model AI menggunakan pipeline kode yang sudah kita bangun ini. Sistem siap digunakan secara real-time.")
    ]

    for q, a in faqs:
        add_callout(q, a, "info")

    doc.add_page_break()

    # -------------------------------------------------------------
    # PENUTUP & KESIMPULAN AKHIR
    # -------------------------------------------------------------
    add_h1("KESIMPULAN AKHIR")
    add_p(
        "Proyek Mini Project Deep Learning 'Indoor Positioning System' ini telah membuktikan secara komprehensif bahwa:\n"
        "1. Pendekatan Hierarkis (Klasifikasi Random Forest + Regresi MLP Deep Learning) adalah kombinasi arsitektur terbaik yang sangat tangguh untuk memecahkan masalah navigasi dalam ruangan.\n"
        "2. Pipeline Preprocessing yang higienis (penanganan nilai +100 ke -105 dBm, normalisasi Min-Max, dan seleksi VarianceThreshold) adalah kunci utama keberhasilan model meraih akurasi gedung 99.8% dan rata-rata galat posisi 4.15 meter.\n"
        "3. Evaluasi menyeluruh membuktikan model memiliki generalisasi yang sangat stabil (Good Fit), dan tantangan penurunan akurasi pada data eksternal berhasil dijelaskan secara saintifik melalui konsep Covariate Shift pada fisika gelombang radio.",
        "Rangkuman Eksekutif: "
    )
    
    add_callout(
        "Dokumentasi Selesai Disusun",
        "Gunakan dokumen ini sebagai panduan belajar mandiri, bahan penyusunan laporan akhir, serta bekal persiapan presentasi dan ujian sidang mini project Anda. Selamat belajar dan sukses selalu!",
        "concept"
    )

    output_filename = "Panduan_Lengkap_Indoor_Localization.docx"
    try:
        doc.save(output_filename)
        print(f"Document successfully created and saved as: {output_filename}")
    except PermissionError:
        output_filename = "Panduan_Lengkap_Indoor_Localization_v2.docx"
        doc.save(output_filename)
        print(f"Original file was open in Word, saved successfully as: {output_filename}")

if __name__ == "__main__":
    create_document()
