import subprocess
import sys

def run_script(script_path, xml_path, a_number):
    try:
        subprocess.check_call(["python3", script_path, xml_path, str(a_number)])
        print(f"Script {script_path} executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python new_script.py <script1_path> <xml1_path> <script2_path> <xml2_path> ... <a_number>")
        sys.exit(1)

    script_paths = sys.argv[1:-1]
    a_number = int(sys.argv[-1])

    if len(script_paths) % 2 != 0:
        print("Error: You must provide an even number of arguments for script and XML pairs.")
        sys.exit(1)

    for i in range(0, len(script_paths), 2):
        script_path = script_paths[i]
        xml_path = script_paths[i + 1]
        run_script(script_path, xml_path, a_number)
