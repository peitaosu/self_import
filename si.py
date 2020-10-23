import sys, subprocess

def ensure_import(module_name)
    try:
        __import__(module_name)
    except:
        subprocess.run([sys.executable, "-m", "ensurepip"])
        subprocess.run([sys.executable, "-m", "pip", "install", module_name])
        __import__(module_name)

def update_path(path = None):
    sys.path.append([sys.executable, "Lib", "site-packages"])
    if path:
        sys.path.append(path)