#!/usr/bin/env python3

import subprocess
import sys
import os

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(current_dir, 'backend', 'loan-service')
    build_script_path = os.path.join(build_dir, 'build_package.py')
    
    if not os.path.exists(build_script_path):
        print(f"Error: The build script does not exist at {build_script_path}")
        sys.exit(1)
    
    try:
        os.chdir(build_dir)
        print(f"Changed working directory to: {build_dir}")
        
        result = subprocess.run([sys.executable, 'build_package.py'], check=True, capture_output=True, text=True)
        
        print("Build script output:")
        print(result.stdout)
        
        if result.stderr:
            print("Build script errors:")
            print(result.stderr)
        
        print("Build script completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: The build script failed with exit code {e.returncode}")
        print("Error output:")
        print(e.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
