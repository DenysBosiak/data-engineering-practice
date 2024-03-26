import pathlib
import json


def main():
    data_path = pathlib.Path("data")
    json_files = list(data_path.rglob("*.json"))


    def read_json(file: str) -> dict:
        try:
            with open(file, "r") as f:
                data = json.loads(f.read())
        except:
            raise Exception(f"Reading [{file}] file encountered an error.")
        
        return data
    

    def normalize_json(data: dict) -> dict:
        normalize_data = dict()

        for key, value in data.items():
            if not isinstance(value, dict):
                normalize_data[key] = value
            else:
                for k, v in value.items():
                    normalize_data[key + "_" + k] = v

        return normalize_data


    for file in json_files:
        json_data = read_json(file=file)
        normalize_json_file = normalize_json(data=json_data)
        print(f"File = [{file}]")
        print(json_data)
        print(normalize_json_file)
        print('')




if __name__ == "__main__":
    main()
