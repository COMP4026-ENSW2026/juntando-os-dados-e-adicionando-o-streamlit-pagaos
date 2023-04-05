import json
import os

def mount_json(filename, json_list):
    if os.path.isfile(filename):
        with open(filename, "r+") as f:
            existing_data = json.load(f)
            existing_data.extend(json_list)
            f.seek(0)
            json.dump(existing_data, f, indent=4, ensure_ascii=False)
            f.truncate()
    else:
        with open(filename, "w") as f:
            json.dump(json_list, f, indent=4, ensure_ascii=False)

        with open(filename, "a") as f:
            f.write("\n")
