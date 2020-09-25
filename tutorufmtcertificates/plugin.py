from glob import glob
import os

from .__about__ import __version__

HERE = os.path.abspath(os.path.dirname(__file__))

templates = os.path.join(HERE, "templates")

config = {
    "add": {
        "UFMT_CERTIFICATES_MYSQL_USERNAME": "ufmtcertificates",
        "UFMT_CERTIFICATES_MYSQL_PASSWORD":"ufmtcertificatesonline2020"
    }
}

hooks = {
    "init": ["ufmtcertificates"]
}
patches={
   
}

def patches():
    all_patches = {
        
    }
    for path in glob(os.path.join(HERE, "patches", "*")):
        with open(path) as patch_file:
            name = os.path.basename(path)
            content = patch_file.read()
            all_patches[name] = content
    return all_patches

def load_all(root):
    """
    Return:
        current (dict): params currently saved in config.yml
        defaults (dict): default values of params which might be missing from the
        current config
    """
    defaults = load_defaults()
    current = load_current(root, defaults)
    return current, defaults

