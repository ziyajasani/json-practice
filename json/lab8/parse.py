import json

with open('somefile.json', 'r') as file:
    data = json.load(file)

with open('chacon.csv', 'w') as csv_file:
    for item in data[:5]:
        name = item.get('name', '')
        html_url = item.get('html_url', '')
        updated_at = item.get('updated_at', '')
        visibility = item.get('visibility', '')
        line = f"{name},{html_url},{updated_at},{visibility}\n"
        csv_file.write(line)

print("The first 5 entries have been written to chacon.csv")

