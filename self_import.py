import sys, subprocess

def ensure_import(module_name):
    try:
        return __import__(module_name)
    except:
        subprocess.check_call([sys.executable, "-m", "ensurepip"])
        subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
        return  __import__(module_name)

def update_lib_path(path = None):
    sys.path.append([sys.executable, "Lib", "site-packages"])
    if path:
        sys.path.append(path)

def install_dependencies(dep_file):
    subprocess.check_call([sys.executable, "-m", "ensurepip"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", dep_file])
