import csv

csv_file_path = r'C:\Users\achaud12\Downloads\ACE_TEXT_RULE_BODY_pt_2024_04_15_07_18.csv'

with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        pri_key = row['pri_key']
        text_rule_body = row['text_rule_body']
        new_line_count = text_rule_body.count('\n')
        print(f"pri_key: {pri_key}, New line count: {new_line_count}")

    print("hello")
    print(2+3)