import csv
from urllib.parse import unquote

def find_sku_in_file_names(manual_list, sku_list, output_file):
    # Get file names from the manual list
    with open(manual_list, 'r') as manual_file:
        manual_reader = csv.reader(manual_file)
        manual_header = next(manual_reader)
        manual_text_column_index = manual_header.index('File Names')
        file_names = [row[manual_text_column_index] for row in manual_reader]

    # Get SKUs from the SKU list
    with open(sku_list, 'r', encoding='utf-8') as sku_file:
        sku_reader = csv.reader(sku_file)
        sku_list = [row[0] for row in sku_reader]

    # Find and write matches to the output CSV file
    with open(output_file, 'a', newline='', encoding='utf-8') as csv_output_file:
        csv_writer = csv.writer(csv_output_file)

        # Write header to the output CSV file
        csv_writer.writerow(['SKU', '<p>&nbsp;</p><h3>Descarca de aici <strong>documentatia necesara:</strong></h3><p>&nbsp;</p>'])

        for sku in sku_list:
            matching_file_names = [file_name for file_name in file_names if sku in file_name]
            if matching_file_names:
                # Create HTML content for column B
                html_content = '<p>&nbsp;</p><h3>Descarca de aici <strong>documentatia necesara:</strong></h3><p>&nbsp;</p>' + '<p>'.join([
                    f'<a href="{file_name}">{unquote(file_name.split("/")[-1].split(".pdf")[0])}</a>'
                    for file_name in matching_file_names
                ]) + '</p>'
                print(html_content)
                csv_writer.writerow([sku, html_content])

# Example usage
manual_list_path = 'file_names.csv'
sku_list_path = 'book.csv'
output_csv_path = 'output.csv'

find_sku_in_file_names(manual_list_path, sku_list_path, output_csv_path)
