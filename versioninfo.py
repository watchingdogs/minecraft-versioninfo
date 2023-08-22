import os
import nbtlib
from operator import itemgetter
import argparse


# Filter list for files inside dimension subfolders
serverFolders = ('world_nether', 'world_the_end', 'DIM1', 'DIM-1')
serverFiles = ['server.properties', 'server-icon.png', 'ops.json', 'eula.txt']


def checkServer(root):
    parent = os.path.join(root, os.pardir)
    dirlist = os.listdir(parent)
    if any(item in serverFiles for item in dirlist):
        return os.path.abspath(parent)


def getVersion(path):
    file = nbtlib.load(path)
    # Try to load data version number, only works with worlds created in and after 15w32a, "the fourth snapshot released for Java Edition 1.9".
    # For more info on data version, seek https://minecraft.fandom.com/wiki/Data_version
    try:
        verid = file['']['Data']['Version']['Id']
    except KeyError:
        return -1, "???"
    return verid, file['']['Data']['Version']['Name']


def search(dir_path):
    # Check if the input directory is valid or not.
    assert os.path.isdir(dir_path), "Given directory is invalid"

    # Declearing default lists.
    worlds, servers, versioninfo = [], [], {}
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file == "level.dat":
                path = f'{root}/{str(file)}'
                # Filtering out different dimensions on servers and MCEdit folders.
                if root.endswith(serverFolders) or ".UNDO##" in root:
                    continue
                # Checking if the directory contains files indicating a server.
                server = checkServer(root)
                if server != None:
                    if server not in servers: servers.append(server)

                # Getting and converting data version to human readable version number.
                verid, vername = getVersion(path)
                versioninfo[verid] = vername
                worlds.append([verid, os.path.abspath(os.path.join(path, os.pardir))])

    # Sorting world list by increasing data version number.
    sw = sorted(worlds, key=itemgetter(0))
    worlds = []
    for w in sw: worlds.append([versioninfo[w[0]], w[1]])
    return worlds, servers

def main():
    # Setting up arguments if executing in terminal.
    par = argparse.ArgumentParser()
    par.add_argument('-p', '--path', help="Path to the root folder to be scanned.", type=str, required=True)
    arg = par.parse_args()
    worlds, servers = search(arg.path)

    # Printing results.
    if worlds != []:
        print("\nWORLDS")
        for i in worlds: print(f"{i[0]:<8}  {i[1]}")
    if servers != []:
        print("\nSERVERS")
        for i in servers: print(f"Found server at {i}")


if __name__ == "__main__":
    main()
