import pathlib
import json
import os


def main():
    data_path = pathlib.Path("data")
    json_files = list(data_path.rglob("*.json"))


    def read_json(file: str) -> dict:
        # Open json file for reading
        try:
            with open(file, "r") as f:
                data = json.loads(f.read())
        except:
            raise Exception(f"Reading [{file}] file encountered an error.")
        
        return data
    

    def flatten_json(data: dict) -> dict:
        # Define dictionary for flattening json data
        flatten_data = dict()

        # Iterate through dictionary
        for key, value in data.items():
            # Check out if value is not dictionary
            if not isinstance(value, dict):
                flatten_data[key] = value
            # Else generate key from key & subkey
            else:
                for k, v in value.items():
                    flatten_data[key + "_" + k] = v

        return flatten_data
    

    def write_csv(file: str, data: dict) -> bool:
        file_name, file_extension = os.path.splitext(file)
        csv_file_name = f"{file_name}.csv"

        # Define csv columns in a list
        csv_columns = data.keys()
        # Generate the first row of csv
        csv_data = ",".join(csv_columns) + "\n"
        print(csv_data)
 

        csv_rows = list()
        for col in csv_columns:
            csv_rows.append(str(data[col]))
        
        csv_data += ",".join(csv_rows) + "\n"       

        try:
            with open(csv_file_name, "w+") as f:
                f.write(csv_data)
        except:
            raise Exception(f"Saving data to [{csv_file_name}] encountered an error.")
        
        print(csv_data)


    #
    for file in json_files:
        json_data = read_json(file=file)
        flatten_json_file = flatten_json(data=json_data)
        write_csv(file=file, data=flatten_json_file)
        print(f"File = [{file}]")
  


if __name__ == "__main__":
    main()
