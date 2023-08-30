import xml.etree.ElementTree as ET

class bcolors:
    YELLOW = '\033[1;33m'
    END = '\033[0m'

def update_worker_count(xml_file, new_worker_count):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    main_workstage = root.find(".//workstage[@name='main']")
    main_work = main_workstage.find("./work")
    main_work.set('workers', str(new_worker_count))

    modified_xml_file = xml_file.replace('.xml', f'-w{new_worker_count}.xml')
    tree.write(modified_xml_file, encoding='utf-8', xml_declaration='<?xml version="1.0" encoding="utf-8"?>')

if __name__ == "__main__":
    xml_file_name = input("Enter the XML file name: ")
    max_worker_count = int(input("Enter the maximum number of workers: "))

    worker_counts = [2**i for i in range(int(max_worker_count.bit_length()))]

    for count in worker_counts:
        update_worker_count(xml_file_name, count)
        print(f"Modified XML for {bcolors.YELLOW}{count}{bcolors.END} workers saved.")

    #print("All modifications complete.")
