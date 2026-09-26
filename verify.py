import getpass
import hashlib
import os
import sys
from datetime import datetime


try:
    import pytest
    pytest_version = pytest.__version__
except ImportError:
    pytest_version = None

username = getpass.getuser()
timestamp = datetime.now().isoformat(timespec="seconds")

conda_env = os.environ.get("CONDA_DEFAULT_ENV", "<not set>")
python_executable = sys.executable
python_version = f"{sys.version_info.major}.{sys.version_info.minor}"

checks = {"Environment name": conda_env == "pyintro",
          "Python version": python_version == "3.12",
          "pytest installed": pytest_version is not None}

token = hashlib.sha256(
    f"{username}|{timestamp}|{python_executable}".encode()).hexdigest()[:8]

print("=== PYINTRO ENVIRONMENT CHECK ===")
print()
print(f"Timestamp: {timestamp}")
print(f"Username: {username}")
print(f"Verification code: {token}")
print()
print(f"Environment : {conda_env}")
print(f"Python : {python_version}")
print(f"Executable : {python_executable}")
print(f"pytest : {pytest_version}")
print()

for name, passed in checks.items():
    print(f"{'✓' if passed else '✗'} {name}")

print()

