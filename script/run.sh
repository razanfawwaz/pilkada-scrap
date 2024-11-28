#!/bin/bash

echo "Starting data scraping process..."

# Run pkwkp scraper
echo "Scraping PKWKP data..."
python3 scrap-pkwkp.py

# Run pkwkp district scraper
echo "Scraping PKWKP district data..."
python3 scrap-pkwkp-district.py

# Run pkwkk scraper
echo "Scraping PKWKK data..."
python3 scrap-pkwkk.py

# Run pkwkk district scraper
echo "Scraping PKWKK district data..."
python3 scrap-pkwkk-district.py

# Run compiler
echo "Compiling data..."
python3 compiler.py

echo "All scraping tasks completed!"
