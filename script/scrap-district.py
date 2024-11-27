import requests
import json
import os

def fetch_and_save_province_data(selected_province):
    url = f"https://sirekappilkada-obj-data.kpu.go.id/wilayah/pilkada/pkwkp/{selected_province}.json"
    
    # Create directory for the selected province if it doesn't exist
    os.makedirs(f'district/{selected_province}', exist_ok=True)
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # Save to JSON file
        output_path = f"district/{selected_province}/{selected_province}.json"
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
        print(f"Data saved to {output_path}")
        return data
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def main():
    # Read province codes from province.json
    with open('province.json', 'r', encoding='utf-8') as f:
        provinces = json.load(f)
    
    # Loop through each province and fetch data
    for province in provinces:
        selected_province = province['kode']
        print(f"Fetching data for province code: {selected_province}")
        result = fetch_and_save_province_data(selected_province)
        if result is None:
            print(f"Skipping province {selected_province}")
            continue

if __name__ == "__main__":
    main()

