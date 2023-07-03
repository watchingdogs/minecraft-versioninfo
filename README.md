# Introduction
This tool tells you where your Minecraft worlds are located on your disk and and in which version were they last opened in. This can be useful if you have 120+ random worlds accumulated over the years, as I have.
I hope this tool will save you from opening worlds in the wrong versions and thus preventing world corruption.

# How it works
The code searches for `level.dat` files and tries to get the [data version](https://minecraft.fandom.com/wiki/Data_version) from them. This system was only implemented after 13w41a, "the tenth snapshot for Java Edition **1.7.2**", hence **worlds last opened before that version are not identified**.

**The code does not work for Bedrock Edition worlds**. They will, however, show up on the world list.

# How to use
Make sure Python 3 is installed. The code uses [nbtlib](https://github.com/vberlier/nbtlib), run the following command to install it.
```bash
$ pip install "nbtlib==1.12.1"
```

Example usage:

```bash
$ python3 versioninfo.py -p C:\Users\John

WORLDS
1.16.5    C:\Users\John\AppData\Roaming\.minecraft\saves\survival
1.16.5    C:\Users\John\Documents\MultiMC\instances\1.16.5\saves\jungle
1.18.1    C:\Users\John\AppData\Roaming\.minecraft\saves\amplified
1.18.1    C:\Users\John\AppData\Roaming\.minecraft\saves\New World
1.19      C:\Users\John\AppData\Roaming\.minecraft\saves\New World (1)

SERVERS
Found server at C:\Users\John\Documents\moddedserver
```

# Implementation
If you wish to use the code in your project, you can get a list of the worlds and the servers using the method below.
```python
import versioninfo

worlds, servers = versioninfo.search("C:\Users\John")
print(f"{worlds[0]} \n {servers[0]}")
```
```python
['1.16.5', 'C:\Users\John\AppData\Roaming\.minecraft\saves\survival'] 
C:\Users\John\Documents\moddedserver
```
