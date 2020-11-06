import sys, subprocess

def ensure_import(module_name, dest_path=None):
    try:
        return __import__(module_name)
    except:
        subprocess.check_call([sys.executable, "-m", "ensurepip"])
        if dest_path:
            subprocess.check_call([sys.executable, "-m", "pip", "install", module_name, "-t", dest_path])
            sys.append(dest_path)
        else:
            subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
        return  __import__(module_name)

def install_dependencies(dep_file, dest_path=None):
    subprocess.check_call([sys.executable, "-m", "ensurepip"])
    if dest_path:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", dep_file, "-t", dest_path])
        sys.append(dest_path)
    else:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", dep_file])
