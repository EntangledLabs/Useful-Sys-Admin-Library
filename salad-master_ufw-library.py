import os, time

def enable(yesno):
  if yesno:
    os.system("ufw enable")
  else:
    os.system("ufw disable")

def convert_allow(allow):
  if allow:
    return "allow"
  else:
    return "deny"

def default(allow, direction):
  os.system("ufw default " + convert_allow(allow) + " " + direction)

def rule(allow, direction, port):
  os.system("ufw " + convert_allow(allow) + " " + direction + " " + port)
