#https://github.com/Sunnysaloni
#https://t.me/Noob_to_pro_hack
#https://t.me/Sunny_ki_duniya

import sys
import logging
import importlib
from pathlib import Path

def load_plugins(plugin_name):
    path = Path(f"main/plugins/{plugin_name}.py")
    name = f"main.plugins.{plugin_name}"
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules[f"main.plugins.{plugin_name}"] = load
    print(f"main has Imported {plugin_name}")
