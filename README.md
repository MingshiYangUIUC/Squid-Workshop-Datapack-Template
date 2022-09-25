# Squid-Workshop-Datapack-Template
Generate a template data pack directory based on [our convention](https://github.com/Squid-Workshop/Minecraft-Datapacks-Project/blob/master/CONTRIBUTING.md).

## Usage
- Open a local terminal and activate your python environment.
- Execute the script with arguments.

        python main.py -args

- Get help by running

        python main.py -h

### Required Arguments
- Minecraft version set by -v or --version, in x.xx.x format. A version must support datapack.

        python main.py -v 1.19.2

### Optioanl Arguments
- Output directory (often the /datapacks folder) set by `-o \<path\>` or `--outputdir \<path\>`. Only support absolute path.

- Name of the datapack set by -n \<name\> or --pname \<name\>. This will be the name showing after the command /datapack list.

- Core name set by -f \<name\>. This will be the name of your core function folders.

- Datapack description set by -d \<your-description\>. This will appear as description in the pack.mcmeta file.

- Whether to create empty load function, tick function, and load/unload messages, set by -l, -t, and -m with boolean arguments.
