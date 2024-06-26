import re


def extract_schema_name_from_dtd(dtd_file_path):
    with open(dtd_file_path, 'r') as dtd_file:
        dtd_content = dtd_file.read()

        # Use regular expression to find the schema name
        match = re.search(r'<\!ELEMENT\s+\w+\s+\((\w+)\s+', dtd_content)

        if match:
            schema_name = match.group(1)
            return schema_name
        else:
            return None


# Example usage
dtd_file_path = 'C:\\Users\\achaud12\\Downloads\\go.dtd'
schema_name = extract_schema_name_from_dtd(dtd_file_path)

if schema_name:
    print(f"Schema Name: {schema_name}")
else:
    print("Schema name not found.")