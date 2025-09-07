from setuptools import setup
import os

# Compile the suid binary
os.system("gcc ./privesc.c -o ./privesc")
# Set permissions
os.system("chmod 4755 ./privesc")

setup(
    name='pwn',
    version='0.1',
    py_modules=['dummy_module'],
)

