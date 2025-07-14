import os
import sys

def create_dict_from_file(file_path: str) -> dict:
    result_dict = {}
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return result_dict
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line_number, line in enumerate(f, 1):
                clean_line = line.strip()
                if not clean_line or clean_line.startswith('#'):
                    continue
                parts = clean_line.split(' ', 1)
                if len(parts) == 2:
                    key = parts[0]
                    value = parts[1]
                    result_dict[key] = value
                else:
                    print(f"Warning: Line {line_number} in file '{file_path}' was ignored (unexpected format).")
    except Exception as e:
        print(f"An error occurred while processing file '{file_path}': {e}")
    return result_dict

def generate_sql_scripts(source_folder: str, output_folder: str = 'SQL'):
    if not os.path.isdir(source_folder):
        print(f"Error: Source directory '{source_folder}' not found.")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Directory '{output_folder}' created.")

    for filename in os.listdir(source_folder):
        if filename.endswith(".txt"):
            table_name = os.path.splitext(filename)[0]
            full_txt_path = os.path.join(source_folder, filename)
            
            processed_dict = create_dict_from_file(full_txt_path)

            if not processed_dict:
                print(f"Warning: No data read from '{filename}', SQL file will not be generated.")
                continue

            sql_filename = table_name + '.sql'
            full_sql_path = os.path.join(output_folder, sql_filename)
            
            columns = list(processed_dict.keys())
            select_clause = ",\n    ".join(columns)
            
            sql_content = f"select\n    {select_clause}\nfrom\n    {table_name};\n"

            with open(full_sql_path, 'w', encoding='utf-8') as f:
                f.write(sql_content)
            
            print(f"Success: File '{full_sql_path}' was generated.")

if __name__ == "__main__":
    target_folder = '../tables_structures'

    if len(sys.argv) > 1:
        target_folder = sys.argv[1]
        
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    generate_sql_scripts(target_folder)