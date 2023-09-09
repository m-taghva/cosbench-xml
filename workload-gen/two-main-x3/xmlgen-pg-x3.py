import xml.etree.ElementTree as ET
import copy
import os
import sys

class bcolors:
    YELLOW = '\033[1;33m'
    END = '\033[0m'

def update_worker_counts(xml_file, max_workers_main1):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    original_file_name = os.path.splitext(os.path.basename(xml_file))[0]

    workers_main1 = 1
    while workers_main1 <= max_workers_main1:
        workers_main2 = workers_main1 * 3
        new_root = copy.deepcopy(root)

        for work in new_root.findall(".//work[@name='main1']"):
            work.set('workers', str(workers_main1))

        for work in new_root.findall(".//work[@name='main2']"):
            work.set('workers', str(workers_main2))

        updated_file_name = f"{original_file_name}-p{workers_main1}-g{workers_main2}.xml"
        updated_file_path = os.path.join(os.path.dirname(xml_file), updated_file_name)

        tree_copy = ET.ElementTree(new_root)
        tree_copy.write(updated_file_path)

        print(f"XML configuration updated for main1={bcolors.YELLOW}{workers_main1}{bcolors.END} and main2={bcolors.YELLOW}{workers_main2}{bcolors.END} workers and saved to {updated_file_name}.")

        workers_main1 *= 2

    print("All configurations have been generated.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py [xml_file] [max_workers_main1]")
        sys.exit(1)

    xml_file_name = sys.argv[1]
    max_workers_main1 = int(sys.argv[2])

    update_worker_counts(xml_file_name, max_workers_main1)
