#!/usr/bin/python3
#Fabric script that generates a .tgz archive from the contents of the web_static

import os
import time
from datetime import datetime
from fabric.operations import local

def do_pack():
    """ Generates the .tgz archive """

    datenow = datetime.now()
    full_date = datenow.strftime("%Y%m%d%H%M%S")

    try:
        if not os.path.isdir("versions"):
            local("mkdir versions")
        local_command = local("tar -cvzf versions/web_static_{}.tgz web_static".format(full_date))
        return local_command
    except Exception:
        return None
