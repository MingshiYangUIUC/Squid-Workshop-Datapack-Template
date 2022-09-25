# Squid-Workshop-Datapack-Template
Generate a template datapack directory based on [our Contributing Convention](https://github.com/Squid-Workshop/Minecraft-Datapacks-Project/blob/master/CONTRIBUTING.md).

Feel free to modify the script for your own needs, but please credit us.

## Usage
- Open a local terminal and activate your python environment.
- Execute the script with arguments.

        python main.py -args

- Get help by running

        python main.py -h

### Required Arguments
- Minecraft version set by `-v <version>` or `--version <version>`, formatted as `x.xx.x`. A valid version must support datapack.

        python main.py -v 1.19.2

### Optional Arguments
- Output directory (often the /datapacks folder) set by `-o <path>` or `--outputdir <path>`. Only support absolute path.

- Name of the datapack set by `-n <pack-name>` or `--packname <pack-name>`. This will be the name showing after the command /datapack list.

- Core name set by `-c <core-name>` or `--corename <core-name>`. This will be the name of your core function folders.

- Datapack description set by `-d <your-description>` or `--description <your-description>`. This will appear as description in the pack.mcmeta file.

- Options to create empty load function, tick function, and default load/unload messages, set by `-l` or `--loadfunc`, `-t` or `--tickfunc`, and `-m` or `--loadmsg` with boolean arguments.
