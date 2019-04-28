#!/usr/bin/env python3

import sys

windows_path = sys.argv[1]
unix_path = windows_path.replace(r"C:", r"/mnt/c").replace("\\", "/")

print(unix_path)
