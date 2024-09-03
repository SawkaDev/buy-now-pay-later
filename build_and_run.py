import os
import subprocess
import platform

def run_shell_command(command, cwd=None):
    """Run a shell command in a specified directory."""
    try:
        if platform.system() == "Windows":
            result = subprocess.run(command, shell=True, check=True, cwd=cwd)
        else:
            result = subprocess.run(command, shell=True, check=True, cwd=cwd)
        return result.returncode
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing: {command}")
        print(e)
        return e.returncode

def main():
    # Store the original directory
    original_dir = os.getcwd()

    services = [
        os.path.join("backend", "merchant-integration-service"),
        os.path.join("backend", "credit-service"),
        os.path.join("backend", "loan-service")
    ]

    # Build packages for each service
    for service in services:
        if platform.system() == "Windows":
            # TODO: update to .bat files?
            run_shell_command("build_package.sh", cwd=service)
        else:
            run_shell_command("./build_package.sh", cwd=service)
        os.chdir(original_dir)

    # Run docker compose
    # run_shell_command("docker compose up --build", cwd=original_dir)

if __name__ == "__main__":
    main()
