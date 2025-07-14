import os

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


processed_dict = create_dict_from_file('tables_full_pdf_old.txt')

with open('list_full_tables_old.txt', 'w+', encoding='utf-8') as f:
    for tables, description in processed_dict.items():
        f.write(tables + "\n")
