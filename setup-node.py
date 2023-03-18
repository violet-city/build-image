import requests
import platform
import tarfile
import subprocess
import glob
import os

bit, _ = platform.architecture()

urls = {
    '64bit' : 'https://nodejs.org/dist/v18.15.0/node-v18.15.0-linux-arm64.tar.xz'
}


with open('node.tar.xz', 'wb') as file:
    print("downloading node")
    response = requests.get(urls[bit])
    file.write(response.content)

with tarfile.open('node.tar.xz', 'r') as file:
    file.extractall()

os.remove("node.tar.xz")

subprocess.run(["stow", "--target=/usr/local", glob.glob('node*')[0]])