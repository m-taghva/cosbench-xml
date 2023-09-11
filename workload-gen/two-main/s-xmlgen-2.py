import sys
import xml.etree.ElementTree as ET
import os

class bcolors:
    YELLOW = '\033[1;33m'
    END = '\033[0m'

# Define the output directory as an absolute path
output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),"..", "all-xml"))

def generate_xml(xml_file, max_worker_count):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    main_workstage = root.find(".//workstage[@name='main']")
    main1_session = main_workstage.find("./work[@name='main1']")
    main2_session = main_workstage.find("./work[@name='main2']")

    worker_count = 2
    while worker_count <= max_worker_count - 1:
        main1_session.set("workers", str(worker_count))
        main2_session.set("workers", str(worker_count))

        modified_xml_file = os.path.basename(xml_file).replace('.xml', f'-{worker_count}-{worker_count}.xml')
        modified_xml_path = os.path.join(output_dir, modified_xml_file)
        
        tree.write(modified_xml_path, encoding='utf-8', xml_declaration='<?xml version="1.0" encoding="UTF-8" ?>')

        worker_count *= 2

    main1_session.set("workers", str(max_worker_count - 1))
    main2_session.set("workers", str(max_worker_count - 1))

    modified_xml_file = os.path.basename(xml_file).replace('.xml', f'-{max_worker_count - 1}-{max_worker_count - 1}.xml')
    modified_xml_path = os.path.join(output_dir, modified_xml_file)

    tree.write(modified_xml_path, encoding='utf-8', xml_declaration='<?xml version="1.0" encoding="UTF-8" ?>')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py [input.xml] [max_worker_count]")
        sys.exit(1)

    xml_file_path = os.path.abspath(sys.argv[1])
    max_worker_count = int(sys.argv[2])

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    generate_xml(xml_file_path, max_worker_count)
    #print(f"{bcolors.YELLOW}Modified XML files generated{bcolors.END}")
