import xml.etree.ElementTree as ET
import copy
import os

class bcolors:
    YELLOW = '\033[1;33m'
    END = '\033[0m'

# Get user input for the XML file path
xml_file_path = input("Enter the path to the XML configuration file: ")

# Parse the XML configuration file
try:
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
except FileNotFoundError:
    print("File not found. Please provide a valid XML file path.")
    exit(1)
except ET.ParseError:
    print("Invalid XML file. Please provide a valid XML file.")
    exit(1)

# Get user input for the maximum number of workers for both "main1" and "main2"
try:
    max_workers = int(input("Enter the maximum number of workers for both main1 and main2: "))
    if max_workers < 1:
        print("Maximum number of workers must be at least 1.")
        exit(1)
except ValueError:
    print("Invalid input. Please enter a valid number for the maximum workers.")
    exit(1)

# Extract the original XML file name (without extension)
original_file_name = os.path.splitext(os.path.basename(xml_file_path))[0]

# Initialize the worker count for "main1" and "main2" to 1
workers_main1 = 1
workers_main2 = 1

# Create a set to store unique worker count combinations
unique_combinations = set()

# Create XML files with "main1" having a static 1 and "main2" in a range, counting in double (Type 1)
while workers_main2 <= max_workers:
    # Create a deep copy of the root element for each iteration
    new_root = copy.deepcopy(root)
    
    # Find and update the number of workers in main1 (static 1)
    for work in new_root.findall(".//work[@name='main1']"):
        work.set('workers', '1')
    
    # Find and update the number of workers in main2 (range, counting in double)
    for work in new_root.findall(".//work[@name='main2']"):
        work.set('workers', str(workers_main2))
    
    # Generate a new XML file name based on the specified format
    updated_file_name = f"{original_file_name}-type1-p1-g{workers_main2}.xml"
    
    # Check if the combination has already been processed
    combination = (1, workers_main2)
    if combination not in unique_combinations:
        unique_combinations.add(combination)
        
        updated_file_path = os.path.join(os.path.dirname(xml_file_path), updated_file_name)
        
        # Save the updated XML to a new file
        tree_copy = ET.ElementTree(new_root)
        tree_copy.write(updated_file_path)
        
        print(f"Type 1: XML configuration updated for main1={bcolors.YELLOW}1{bcolors.END} and main2={bcolors.YELLOW}{workers_main2}{bcolors.END} workers and saved to {bcolors.YELLOW}{updated_file_name}{bcolors.END}")
    
    # Double the worker count for "main2" for the next iteration
    workers_main2 *= 2

# Reset worker counts
workers_main1 = 1
workers_main2 = 1

# Create XML files with "main2" having a static 1 and "main1" in a range, counting in double (Type 2)
while workers_main1 <= max_workers:
    # Create a deep copy of the root element for each iteration
    new_root = copy.deepcopy(root)
    
    # Find and update the number of workers in main2 (static 1)
    for work in new_root.findall(".//work[@name='main2']"):
        work.set('workers', '1')
    
    # Find and update the number of workers in main1 (range, counting in double)
    for work in new_root.findall(".//work[@name='main1']"):
        work.set('workers', str(workers_main1))
    
    # Generate a new XML file name based on the specified format
    updated_file_name = f"{original_file_name}-type2-p{workers_main1}-g1.xml"
    
    # Check if the combination has already been processed
    combination = (workers_main1, 1)
    if combination not in unique_combinations:
        unique_combinations.add(combination)
        
        updated_file_path = os.path.join(os.path.dirname(xml_file_path), updated_file_name)
        
        # Save the updated XML to a new file
        tree_copy = ET.ElementTree(new_root)
        tree_copy.write(updated_file_path)
        
        print(f"Type 2: XML configuration updated for main1={bcolors.YELLOW}{workers_main1}{bcolors.END} and main2={bcolors.YELLOW}1{bcolors.END} workers and saved to {bcolors.YELLOW}{updated_file_name}{bcolors.END}")
    
    # Double the worker count for "main1" for the next iteration
    workers_main1 *= 2

# Reset worker counts
workers_main1 = 1
workers_main2 = 1

# Create XML files with "main1" having the maximum number and "main2" in a range, counting in double (Type 3)
while workers_main2 <= max_workers:
    # Create a deep copy of the root element for each iteration
    new_root = copy.deepcopy(root)
    
    # Find and update the number of workers in main1 (maximum)
    for work in new_root.findall(".//work[@name='main1']"):
        work.set('workers', str(max_workers))
    
    # Find and update the number of workers in main2 (range, counting in double)
    for work in new_root.findall(".//work[@name='main2']"):
        work.set('workers', str(workers_main2))
    
    # Generate a new XML file name based on the specified format
    updated_file_name = f"{original_file_name}-type3-p{max_workers}-g{workers_main2}.xml"
    
    # Check if the combination has already been processed
    combination = (max_workers, workers_main2)
    if combination not in unique_combinations:
        unique_combinations.add(combination)
        
        updated_file_path = os.path.join(os.path.dirname(xml_file_path), updated_file_name)
        
        # Save the updated XML to a new file
        tree_copy = ET.ElementTree(new_root)
        tree_copy.write(updated_file_path)
        
        print(f"Type 3: XML configuration updated for main1={bcolors.YELLOW}{max_workers}{bcolors.END} and main2={bcolors.YELLOW}{workers_main2}{bcolors.END} workers and saved to {bcolors.YELLOW}{updated_file_name}{bcolors.END}")
    
    # Double the worker count for "main2" for the next iteration
    workers_main2 *= 2

# Reset worker counts
workers_main1 = 1
workers_main2 = 1

# Create XML files with "main2" having the maximum number and "main1" in a range, counting in double (Type 4)
while workers_main1 <= max_workers:
    # Create a deep copy of the root element for each iteration
    new_root = copy.deepcopy(root)
    
    # Find and update the number of workers in main2 (maximum)
    for work in new_root.findall(".//work[@name='main2']"):
        work.set('workers', str(max_workers))
    
    # Find and update the number of workers in main1 (range, counting in double)
    for work in new_root.findall(".//work[@name='main1']"):
        work.set('workers', str(workers_main1))
    
    # Generate a new XML file name based on the specified format
    updated_file_name = f"{original_file_name}-type4-p{workers_main1}-g{max_workers}.xml"
    
    # Check if the combination has already been processed
    combination = (workers_main1, max_workers)
    if combination not in unique_combinations:
        unique_combinations.add(combination)
        
        updated_file_path = os.path.join(os.path.dirname(xml_file_path), updated_file_name)
        
        # Save the updated XML to a new file
        tree_copy = ET.ElementTree(new_root)
        tree_copy.write(updated_file_path)
        
        print(f"Type 4: XML configuration updated for main1={bcolors.YELLOW}{workers_main1}{bcolors.END} and main2={bcolors.YELLOW}{max_workers}{bcolors.END} workers and saved to {bcolors.YELLOW}{updated_file_name}{bcolors.END}")
    
    # Double the worker count for "main1" for the next iteration
    workers_main1 *= 2

print("All configurations have been generated.")
