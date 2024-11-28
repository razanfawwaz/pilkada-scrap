import json
import os

def compile_province_data():
    # Initialize the structure similar to 0.json
    compiled_data = {
        "mode": "hhcw",
        "tungsura": {
            "chart": {
                "progres": {
                    "total": 0,
                    "persen": 0,
                    "progres": 0
                }
            },
            "table": {}
        },
        "psu": "Reguler",
        "progres": {
            "total": 0,
            "progres": 0
        },
        "ts": "2024-11-28 10:45:04"  # Added timestamp
    }

    # Get all province folders in pkwkp directory
    pkwkp_dir = "../pkwkp"
    province_folders = [f for f in os.listdir(pkwkp_dir) if os.path.isdir(os.path.join(pkwkp_dir, f))]

    total_all = 0
    progres_all = 0

    # Process each province
    for province in province_folders:
        if province == "0":  # Skip the summary file
            continue
            
        province_file = os.path.join(pkwkp_dir, province, f"{province}.json")
        
        try:
            with open(province_file, 'r', encoding='utf-8') as f:
                province_data = json.load(f)
                
            # Add province data to compiled structure
            compiled_data["tungsura"]["table"][province] = {
                "psu": "Reguler"
            }
            
            # Copy data from tungsura chart
            if "tungsura" in province_data and "chart" in province_data["tungsura"]:
                chart_data = province_data["tungsura"]["chart"]
                for key, value in chart_data.items():
                    if key.startswith("1000"):
                        compiled_data["tungsura"]["table"][province][key] = value
            
            # Copy progress data
            if "progres" in province_data:
                # Handle nested progres data structure
                if isinstance(province_data["progres"], dict):
                    compiled_data["tungsura"]["table"][province]["progres"] = {
                        "total": province_data["progres"].get("total", 0),
                        "persen": province_data["progres"].get("persen", 0),
                        "progres": province_data["progres"].get("progres", 0)
                    }
                    total_all += province_data["progres"].get("total", 0)
                    progres_all += province_data["progres"].get("progres", 0)
                
            compiled_data["tungsura"]["table"][province]["status_progress"] = True

        except Exception as e:
            print(f"Error processing province {province}: {e}")
            continue

    # Update total progress
    compiled_data["tungsura"]["chart"]["progres"]["total"] = total_all
    compiled_data["tungsura"]["chart"]["progres"]["progres"] = progres_all
    if total_all > 0:
        compiled_data["tungsura"]["chart"]["progres"]["persen"] = round((progres_all / total_all) * 100, 2)
    
    compiled_data["progres"]["total"] = total_all
    compiled_data["progres"]["progres"] = progres_all

    # sort table by key
    compiled_data["tungsura"]["table"] = dict(sorted(compiled_data["tungsura"]["table"].items()))

    # Save compiled data
    output_file = os.path.join(pkwkp_dir, "0.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(compiled_data, f, ensure_ascii=False, indent=4)
        
    print(f"Compiled data saved to {output_file}")

if __name__ == "__main__":
    compile_province_data()
