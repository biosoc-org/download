
import csv
import sys
import requests
from bs4 import BeautifulSoup

def main():
    if len(sys.argv) != 4:
        print("Usage: python geturl.py INPUT URL COL")
        return

    input_file = sys.argv[1]
    base_url = sys.argv[2]
    column_name = sys.argv[3]

    try:
        with open(input_file, mode='r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            if column_name not in reader.fieldnames:
                print(f"Error: Column '{column_name}' not found in the CSV file.")
                return

            results = []
            for row in reader:
                prefix = row[column_name]
                url_prefix = f"{base_url}{prefix}"

                try:
                    response = requests.get(url_prefix)
                    response.raise_for_status()

                    soup = BeautifulSoup(response.text, 'html.parser')
                    title = soup.title.string if soup.title else 'N/A'
                    description = ''
                    meta_tags = soup.find_all('meta')

                    for meta in meta_tags:
                        if meta.get('name') == 'description':
                            description = meta.get('content', '')
                            break

                    meta_data = {meta.get('name', ''): meta.get('content', '') for meta in meta_tags if 'name' in meta.attrs}

                    results.append({
                        'URL': url_prefix,
                        'NAME': title,
                        'DESCRIPTION': description,
                        'META': meta_data
                    })

                except requests.RequestException as e:
                    print(f"Error fetching URL: {url_prefix}, Error: {e}")
                    continue

            output_file = 'output.csv'
            with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
                fieldnames = ['URL', 'NAME', 'DESCRIPTION', 'META']
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)

                writer.writeheader()
                for result in results:
                    writer.writerow(result)

            print(f"Data has been written to {output_file}")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found")
        return

if __name__ == "__main__":
    main()