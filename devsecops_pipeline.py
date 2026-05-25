import subprocess
import sys

def run_command(command):
    result = subprocess.run(
        command,
        shell=True,
        text=True,
        capture_output=True
    )

    if result.returncode != 0:
        print(f"FAILED: {command}")
        print(result.stdout)
        print(result.stderr)
        sys.exit(result.returncode)

    print(result.stdout)

def main():
    print("Running Bandit...")
    run_command("bandit -r .")

    print("Running pip-audit...")
    run_command("pip-audit")

    print("Running Ruff...")
    run_command("ruff check .")

    print("DevSecOps pipeline completed successfully!")

if __name__ == "__main__":
    main()
    