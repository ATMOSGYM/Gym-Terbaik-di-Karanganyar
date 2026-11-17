# ATMOS GYM Karanganyar — Website

Website profil & promosi **ATMOS GYM Karanganyar**: satu halaman statis (HTML + CSS + JS murni), tanpa framework dan tanpa build step. Cukup upload, langsung jalan.

> **Gym Terbaik di Karanganyar** · Member **Rp100.000/bulan** · Non member **Rp10.000/visit** · Buka **06.00–22.00** setiap hari
> Tegalgede/Tegalwinangun, barat Pasar Tegalgede, Kabupaten Karanganyar, Jawa Tengah — Plus Code **9XVC+QJ2**
> WhatsApp **0857 2796 6040** · TikTok **ATMOS GYM KARANGANYAR**

---

## 1. Isi repository

```
.
├── index.html            # seluruh website (HTML + CSS + JS inline)
├── assets/               # foto & ikon
│   ├── real1.jpg         # FOTO ASLI dari Google Maps — area alat (multi-gym merah)
│   ├── real2.jpg         # FOTO ASLI dari Google Maps — alat kardio
│   ├── real3.jpg         # FOTO ASLI dari Google Maps — cable & dumbbell
│   ├── hero-gym.jpg      # foto hero (pria latihan, lighting emas)
│   ├── strip-gym.jpg     # foto strip info
│   ├── banner.jpg        # banner promo resmi (dipakai di galeri)
│   ├── sign.jpg          # foto papan nama ATMOS GYM
│   ├── p1..p11.jpg       # foto profil 10 ulasan testimoni
│   ├── favicon-64.png
│   └── apple-touch-icon.png
├── brand/                # aset logo
│   ├── logo-atmosgym.svg        # logo utama (vektor, tajam di segala ukuran)
│   ├── logo-atmosgym-1024.png   # PNG transparan
│   ├── logo-mark.svg            # ikon shield + dumbbell + monogram AG
│   └── logo-mark-512.png
├── tools/                # opsional: skrip pembuat logo
│   ├── build_logo.py
│   └── Anton-Regular.ttf
├── .nojekyll             # wajib untuk GitHub Pages (agar folder assets terbaca)
├── .gitignore
└── README.md
```

## 2. Cara upload ke GitHub

### A. Lewat web GitHub (paling mudah, tanpa Git)
1. Buka <https://github.com/new> → isi **Repository name** (mis. `atmos-gym`) → **Public** → **Create repository**.
2. Klik **uploading an existing file**.
3. Ekstrak dulu file ZIP ini di komputer, lalu **drag semua isi folder** (bukan file ZIP-nya) ke area upload — pastikan `index.html` ada di root, dan folder `assets/`, `brand/`, `tools/` ikut ter-upload.
4. Isi pesan commit → **Commit changes**.

### B. Lewat Git (command line)
```bash
# ekstrak zip, lalu masuk ke foldernya
cd atmosgym-website
git init
git branch -M main
git add .
git commit -m "Website ATMOS GYM Karanganyar"
git remote add origin https://github.com/USERNAME/atmos-gym.git
git push -u origin main
```

## 3. Publikasikan gratis dengan GitHub Pages
1. Buka repo → **Settings** → **Pages**.
2. **Source**: `Deploy from a branch` → **Branch**: `main` → folder **/ (root)** → **Save**.
3. Tunggu ±1 menit, situs live di:
   `https://USERNAME.github.io/atmos-gym/`

> File `.nojekyll` **jangan dihapus** — itu mencegah Jekyll mengabaikan folder yang namanya diawali garis bawah dan mempercepat build.

### Alternatif hosting lain
- **Netlify / Vercel / Cloudflare Pages**: drag & drop folder ini, langsung online.
- **Hosting cPanel**: upload isi folder ke `public_html`.

---

## 4. Bagian-bagian halaman

| Bagian | Keterangan |
|---|---|
| Header | Logo, menu, ikon sosial, tombol **Daftar · Datang Hari Ini** (langsung ke WhatsApp) |
| Hero | Foto full-screen, headline, CTA WhatsApp + tombol lihat banner promo |
| Strip info | Alamat, harga member/non member, jam buka |
| 3 Fitur | Latihan beban, pendampingan trainer, program profesional |
| Paket & Harga | Non member Rp10K · Member Rp100K (paling hemat) · Pemula + **kalkulator** member vs harian |
| Fasilitas & Galeri | Banner promo + 3 foto asli Maps + foto trainer + papan nama (klik untuk perbesar) |
| Jam Buka | Status **buka/tutup otomatis** dihitung dari jam WIB |
| Testimoni | Rating **5,0 ★★★★★ ATMOS GYM** + slider berjalan 10 ulasan (geser/hover untuk berhenti) |
| Peta | Sketsa peta lokasi + tombol **Muat Peta Interaktif** (Google Maps embed) |
| FAQ | Accordion |
| Foto asli | Strip **“Suasana Asli ATMOS GYM”** (5 foto) + tombol *Lihat semua foto di Google Maps* |
| CTA + Marquee | Banner "Ayo… Segera Daftar!" + tulisan berjalan "Gym Terbaik di Karanganyar" |
| Footer | Navigasi, kontak, jam buka |

## 5. Nomor WhatsApp & pesan otomatis

Nomor: **0857 2796 6040** → format internasional `6285727966040`.

Semua tombol WhatsApp sudah memakai link `https://wa.me/6285727966040?text=...` **yang tertanam langsung di HTML** (tidak bergantung JavaScript), dengan pesan yang berbeda per tombol — semuanya bernuansa "datang hari ini". Tombol besar di bagian bawah halaman menampilkan **nomor 0857 2796 6040 langsung di tombolnya** agar pengunjung bisa membaca/menyalin nomor tanpa harus membuka WhatsApp:

| Tombol | Pesan |
|---|---|
| Daftar · Datang Hari Ini (header) | daftar member Rp100.000/bulan + datang hari ini |
| Daftar Member — Datang Hari Ini (hero) | daftar member hari ini |
| Datang Hari Ini (non member) | latihan harian Rp10.000 hari ini |
| Konsultasi Pemula | pemula, datang hari ini minta didampingi trainer |
| Daftar via WhatsApp (banner CTA) | daftar member hari ini |
| Floating button & footer | datang & latihan hari ini |
| Minta Patokan WA (peta) | datang hari ini + minta patokan 9XVC+QJ2 |

### Cara mengganti nomor
Cari dan ganti **`6285727966040`** di `index.html` (ada di blok `<script>` variabel `PHONE_INTL` dan pada `href` tombol). Jangan lupa ubah juga teks `0857 2796 6040` yang tampil di halaman.

### Tautan foto Google Maps
Tombol **“Lihat semua foto di Google Maps”** mengarah ke:
```
https://www.google.com/maps/search/?api=1&query=ATMOS%20GYM%20KARANGANYAR%2C%20Tegalwinangun%2C%20Tegalgede%2C%20Karanganyar
```
Link ini bisa diganti dengan **URL listing Google Maps resmi** milik ATMOS GYM (buka listing di Maps → Bagikan → Salin link, biasanya berbentuk `https://maps.app.goo.gl/xxxx` atau `https://www.google.com/maps/place/...`). Setelah punya link resmi, ganti pada 2 tempat di `index.html`: atribut `href` tombol `id="galMap2"` (seksi Foto Asli) dan `id="galMap"` (catatan galeri). Link resmi lebih presisi karena langsung membuka profil + tab Foto bisnis Anda.

### Cara mengganti tautan TikTok
Saat ini tombol TikTok mengarah ke **pencarian** "ATMOS GYM KARANGANYAR". Bila sudah punya akun, ganti `TIKTOK_URL` di `<script>` menjadi mis. `https://www.tiktok.com/@atmosgym.karanganyar`.

## 6. Informasi yang perlu diperbarui (opsional)

| Data | Lokasi di `index.html` |
|---|---|
| Harga member / non member | teks kartu paket + `PRICE_MEMBER` / `PRICE_VISIT` di `<script>` |
| Jam buka | `OPEN_H = 6`, `CLOSE_H = 22` di `<script>` + teks di bagian Jam Buka |
| Plus Code / alamat | teks alamat, `src` iframe Google Maps, `MAP_URL` |
| Ulasan testimoni | blok `<article class="review">` |
| Foto member | ganti file `assets/p1..p11.jpg` (rasio 1:1) |

## 7. Catatan tentang foto

### Foto asli dari Google Maps
`assets/real1.jpg`, `real2.jpg`, `real3.jpg` diambil dari **foto publik ATMOS GYM KARANGANYAR di Google Maps** (screenshot foto profil Maps), lalu dipotong dan dipertajam. Foto Google Maps adalah milik pengunggahnya; karena itu:

- Website mencantumkan kredit **“Foto asli · Google Maps”** pada setiap foto.
- Tombol **“Lihat semua foto di Google Maps”** mengarah ke listing ATMOS GYM agar pengunjung melihat foto terbaru langsung dari sumbernya.
- Kalau nanti Anda punya **file foto aslinya** (dari HP/kamera), tinggal ganti `real1.jpg`, `real2.jpg`, `real3.jpg` dengan nama file yang sama — tidak perlu mengubah HTML. Kualitas akan jauh lebih tajam daripada hasil potong screenshot.
- Foto **“Trainer mendampingi”** (`g5.jpg`) adalah **ilustrasi** (ruangan & alat asli, dua orang ditambahkan), jadi jangan diklaim sebagai foto dokumentasi.

Cara menambah foto baru ke galeri: simpan file di `assets/`, duplikasi satu blok `<figure data-src="assets/…">` di bagian `#gallery`, lalu ganti path-nya.

## 8. Catatan lain tentang foto

- **Foto hero, interior, dan foto profil ulasan dibuat khusus** (AI) agar senada dengan tema. Ganti dengan foto asli ATMOS GYM agar lebih otentik — rasio hero 3:2, foto ulasan 1:1.
- Foto asli dari Anda yang sudah dipakai: **banner promo** (`assets/banner.jpg`) dan **papan nama** (`assets/sign.jpg`).
- Ulasan pada bagian testimoni adalah **contoh tulisan**. Sebaiknya ganti dengan ulasan asli pengunjung (dengan izin mereka). Untuk versi resmi, jangan memakai foto orang lain dari internet tanpa izin.

## 9. Ringkasan teknis
- HTML5 + CSS3 + JavaScript vanilla, **tanpa dependensi** dan tanpa CDN (aman untuk preview offline).
- Responsif diuji pada lebar 320px – 1920px.
- Mendukung `prefers-reduced-motion` (animasi berhenti otomatis bagi yang memintanya).
- Aksesibilitas: gambar punya `alt`, tombol punya `aria-label`, galeri bisa dibuka dengan keyboard (Enter/Space).

---

© ATMOS GYM Karanganyar. Raih hidup lebih sehat dan lebih kuat. 💪
