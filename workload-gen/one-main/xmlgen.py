import sys
import xml.etree.ElementTree as ET
import os

class bcolors:
    YELLOW = '\033[1;33m'
    END = '\033[0m'

# Define the static output directory one level above the current working directory
output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "all-xml"))

def update_worker_count(xml_file, new_worker_count):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    main_workstage = root.find(".//workstage[@name='main']")
    main_work = main_workstage.find("./work")
    main_work.set('workers', str(new_worker_count))

    modified_xml_file = xml_file.replace('.xml', f'-w{new_worker_count}.xml')
    modified_xml_path = os.path.join(output_dir, modified_xml_file)
    
    tree.write(modified_xml_path, encoding='utf-8', xml_declaration='<?xml version="1.0" encoding="utf-8"?>')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py [input.xml] [max_worker_count]")
        sys.exit(1)

    xml_file_name = sys.argv[1]
    max_worker_count = int(sys.argv[2])

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    worker_counts = [2**i for i in range(int(max_worker_count.bit_length()))]

    for count in worker_counts:
        update_worker_count(xml_file_name, count)
        print(f"Modified XML for {bcolors.YELLOW}{count}{bcolors.END} workers saved in {output_dir}.")

    print("All modifications complete.")
