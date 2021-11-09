#! /usr/bin/env python3

import pexpect
from config import inv


"""
Pexpect spawns child processes, controls them with parent process,
and responds to expected patterns in output. Similar to TCL
(Tool Command Language) Expect module.

Example from "Mastering Python Networking" by Eric Chou
"""

dev = inv.get("iosv-1")

# Connect to network device
child = pexpect.spawn(f"telnet {dev.get('host')}")

# Logging into the device
child.expect("Username")
child.sendline(dev.get("user"))
child.expect("Password")
child.sendline(dev.get("pass"))

# Expecting prompt
child.expect("iosv-1#")

# Run show version
child.expect("show version")

# View show version output
child.before

# Close the connection
child.sendline("exit")

# NOTE: Regex with Pexpect is not greedy, so it will match little as possible

# SSH Example
child = pexpect.pxssh.pxssh()
child.login("172.16.1.20", "cisco", "cisco", auto_prompt_reset=False)
# Returns True

# Run show version
child.sendline("show version")
child.expect("iosv-1#")

# View output
child.before

# Logout
child.logout()
