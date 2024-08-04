import sys
import subprocess

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
    output, error = process.communicate()
    if process.returncode != 0:
        print(f"Error: {error}")
        sys.exit(1)
    return output

def migrate(message):
    print(f"Running migration with message: {message}")
    migrate_output = run_command(f'docker-compose exec -T flaskapp flask db migrate -m "{message}"')
    print(migrate_output)

    print("Migration successful. Running upgrade...")
    upgrade_output = run_command('docker-compose exec -T flaskapp flask db upgrade')
    print(upgrade_output)

    print("Migration process completed.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Please provide a migration message.")
        print("Usage: python migrate.py \"Your migration message\"")
        sys.exit(1)

    message = sys.argv[1]
    migrate(message)
