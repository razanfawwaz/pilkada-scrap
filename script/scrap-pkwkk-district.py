import requests
import json
import os
from tqdm import tqdm

def fetch_and_save_district_data(selected_province, selected_district):
    url = f"https://sirekappilkada-obj-data.kpu.go.id/pilkada/hhcw/pkwkk/{selected_province}/{selected_district}.json"
    
    # Create directory structure
    os.makedirs(f'pkwkk/{selected_province}', exist_ok=True)
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # Save to JSON file
        output_path = f"pkwkk/{selected_province}/{selected_district}.json"
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
        return data
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for province {selected_province}, district {selected_district}: {e}")
        return None

def get_districts_for_province(selected_province):
    try:
        # Read district data from the corresponding province file
        district_file = f"district/{selected_province}/{selected_province}.json"
        with open(district_file, 'r', encoding='utf-8') as f:
            districts = json.load(f)
        return districts
    except FileNotFoundError:
        print(f"No district file found for province {selected_province}")
        return []

def main():
    # Read province codes from province.json
    with open('province.json', 'r', encoding='utf-8') as f:
        provinces = json.load(f)
    
    # Create progress bar for provinces
    province_pbar = tqdm(provinces, desc="Processing provinces")
    
    # Loop through each province
    for province in province_pbar:
        selected_province = province['kode']
        province_pbar.set_description(f"Processing province {selected_province}")
        
        # Get districts for this province
        districts = get_districts_for_province(selected_province)
        
        # Create progress bar for districts within this province
        district_pbar = tqdm(districts, desc=f"Districts in {selected_province}", leave=False)
        
        # Process each district
        for district in district_pbar:
            selected_district = district['kode']
            district_pbar.set_description(f"Processing district {selected_district}")
            
            result = fetch_and_save_district_data(selected_province, selected_district)
            if result is None:
                continue

if __name__ == "__main__":
    main()

