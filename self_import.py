import os, sys, subprocess

def ensure_import(module_name, dest_path=None):
    try:
        return __import__(module_name)
    except:
        install_module(["-m", "pip", "install", module_name], dest_path)
        return  __import__(module_name)

def install_dependencies(dep_file, dest_path=None):
    install_module(["-m", "pip", "install", "-r", dep_file], dest_path)

def install_module(command, dest_path=None):
    try:
        subprocess.check_call([sys.executable, "-m", "ensurepip"])
        exe = [sys.executable]
        exe_cmd = exe.extend(command)
        if dest_path:
            subprocess.check_call(exe_cmd.extend(["-t", dest_path]))
            sys.append(dest_path)
            os.environ["PYTHONPATH"] = dest_path + (";" + os.environ["PYTHONPATH"] if "PYTHONPATH" in os.environ else "")
        else:
            subprocess.check_call(exe_cmd)
    except subprocess.CalledProcessError(e):
        print(e.output)
