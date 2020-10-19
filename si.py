import sys, subprocess

def ensure_import(module_name)
subprocess.run([sys.executable, "-m", "ensurepip"])
subprocess.run([sys.executable, "-m", "pip", "install", module_name])