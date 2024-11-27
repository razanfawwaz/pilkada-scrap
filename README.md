# Scraping Data Pilkada 2024

## How to Use
1. Make sure you have the `province.json` file in the `script` directory
2. Run the script by using `python <script-name>.py`

## Data Collected
- [x] Province
- [x] District
- [x] PKWKP (Gubernur)
- [x] PKWKK (Bupati/Walikota)

## Folder Data Structure
- `pkwkp`
  - `kode_provinsi`
    - `kode_provinsi.json`
    - `kode_provinsi_kotakab.json`

- `pkwkk`
  - `0.json` (rekap keseluruhan provinsi)
  - `kode_provinsi`
    - `kode_provinsi.json`
    - `kode_provinsi_kotakab.json`

- `district`
  - `kode_provinsi`
    - `kode_provinsi.json`

