import csv
import os
import sys
import requests
from bs4 import BeautifulSoup

def main():
    if len(sys.argv) != 6:
        print("Usage: python geturl.py INPUT URL COL HTML OUTPUT")
        return

    input_file = sys.argv[1]
    base_url = sys.argv[2]
    column_name = sys.argv[3]
    html_folder = sys.argv[4]
    output_file = sys.argv[5]

    if not os.path.exists(html_folder):
        os.makedirs(html_folder)

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
                    response = requests.get(url_prefix, allow_redirects=True)
                    response.raise_for_status()

                    # Get the final URL after redirection, if any
                    final_url = response.url
                    url_prefix = final_url

                    soup = BeautifulSoup(response.text, 'html.parser')
                    title = soup.title.string if soup.title else 'N/A'
                    description = ''
                    meta_tags = soup.find_all('meta')

                    for meta in meta_tags:
                        if meta.get('name') == 'description':
                            description = meta.get('content', '')
                            break

                    meta_data = {meta.get('name', ''): meta.get('content', '') for meta in meta_tags if 'name' in meta.attrs}

                    # Write the HTML content to a file in the specified folder
                    html_file_path = os.path.join(html_folder, f"{prefix}.html")
                    with open(html_file_path, 'w', encoding='utf-8') as html_file:
                        html_file.write(response.text)

                    results.append({
                        'URL': url_prefix,
                        'NAME': title,
                        'DESCRIPTION': description,
                        'META': meta_data
                    })

                except requests.RequestException as e:
                    print(f"Error fetching URL: {url_prefix}, Error: {e}")
                    continue

            with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
                fieldnames = ['URL', 'NAME', 'DESCRIPTION', 'META']
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)

                writer.writeheader()
                for result in results:
                    # To ensure the 'META' field is written as a string, not a dictionary
                    result['META'] = str(result['META'])
                    writer.writerow(result)

            print(f"Data has been written to {output_file}")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found")
        return

if __name__ == "__main__":
    main()