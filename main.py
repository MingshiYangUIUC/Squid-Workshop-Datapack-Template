"""
Created by YMS2001, format designed by Squid Workshop
"""

# imports
from json import load
import sys, getopt
import os
import shutil


def versionparser(v):
    """Read version of x.xx.x format and return pack format as well as integer version number"""

    code = None
    # get integer version number
    v = v.split(".")
    if len(v) == 2:
        v.append("0")
    if len(v[-1]) > 1:
        print("Version Not Supported")
    v = int("".join(v)[:4])

    # assign pack format
    if v < 1130:
        print("Version Not Supported")
    elif v <= 1144:
        code = 4
    elif v <= 1161:
        code = 5
    elif v <= 1165:
        code = 6
    elif v <= 1171:
        code = 7
    elif v <= 1181:
        code = 8
    elif v == 1182:
        code = 9
    elif v <= 1199:
        code = 10
    else:
        print("Version Not Supported")
    return v, code


if __name__ == "__main__":
    """Main Execution"""

    # get directory
    wd0 = os.path.dirname(__file__)

    # get arguments
    opts, args = getopt.getopt(
        sys.argv[1:],
        "v:n:d:l:t:m:o:f:u:hI",
        [
            "version=",
            "pname=",
            "pdescription=",
            "loadfunc=",
            "tickfunc=",
            "loadmsg=",
            "outputdir=",
            "funcname=",
            "unloadfunc=",
            "help=$OPTARG",
        ],
    )

    # initialize default parameters
    pack_version = None
    pack_name = "myTemplate"
    func_name = "mypack"
    pack_descrip = "Squid Workshop Generated Template"
    pack_outdir = None
    load_function = True
    load_message = True
    unload_function = True
    tick_function = True
    creator_help = False

    for pair in opts:
        if pair[0] == "-v" or pair[0] == "--version":
            pack_version = pair[1]
            pack_n, pack_format = versionparser(pack_version)
        elif pair[0] == "-n" or pair[0] == "--pname":
            pack_name = pair[1]
        elif pair[0] == "-d" or pair[0] == "--pdescription":
            pack_descrip = pair[1]
        elif pair[0] == "-o" or pair[0] == "--outputdir":
            pack_outdir = pair[1]
        elif pair[0] == "-f" or pair[0] == "--funcname":
            func_name = pair[1]
        elif pair[0] == "-l" or pair[0] == "--loadfunc":
            load_function = bool(pair[1])
        elif pair[0] == "-m" or pair[0] == "--loadmsg":
            load_message = bool(pair[1])
        elif pair[0] == "-t" or pair[0] == "--tickfunc":
            tick_function = bool(pair[1])
        elif pair[0] == "-u" or pair[0] == "--unloadfunc":
            unload_function = bool(pair[1])
        elif pair[0] == "-h" or pair[0] == "--help":
            if not bool(pair[1]):
                creator_help = True
        else:
            print("Invalid Arguments!!!")
            sys.exit(1)

    if not creator_help and (
        pack_version == None or pack_format == None or func_name == None
    ):
        print("Missing Critical information!!!")
        print(f'For help:\n    python {os.path.join(wd0,"creator.py")} -h')
        sys.exit(1)

    if creator_help:
        print(
            "User help:\n",
            "    Help: -h\n",
            "    Set game version: -v 1.19.2\n",
            "    Set pack folder name: -n myTemplate\n",
            "    Set function header name: -f mypack\n",
            '    Set custom pack description: -d "my description"\n',
            "    Set another output dir: -o absolute/path/to/output\n",
            "    Load function: -l boolean\n",
            "    Default load message: -m boolean\n",
            "    Tick function: -t boolean\n",
            "    Unload function: -u boolean",
        )
        sys.exit(0)

    if pack_outdir:
        wd0 = pack_outdir

    # create main directory
    wd1 = os.path.join(wd0, pack_name + "-" + pack_version)

    if os.path.isdir(wd1):
        shutil.rmtree(wd1)
    os.mkdir(wd1)
    os.mkdir(os.path.join(wd1, "data"))

    print("Output to:", wd1)

    # create pack.mcmeta
    meta = open(os.path.join(wd1, "pack.mcmeta"), "w")
    meta.write(
        "{\n"
        + '    "pack": {\n'
        + f'        "pack_format": {pack_format},\n'
        + f'        "description": "{pack_descrip}"\n'
        + "    }\n"
        + "}\n"
    )
    meta.close()

    # create main directory
    wd_main = os.path.join(wd1, "data", func_name, "functions", "classes", "main")
    os.makedirs(wd_main)

    # create load and tick directory
    wd_load = os.path.join(wd1, "data", "minecraft", "tags", "functions")
    os.makedirs(wd_load)

    # create load functions
    if load_function:
        lf = open(os.path.join(wd_load, "load.json"), "w")
        lf.write(
            "{\n"
            + '"values": [\n'
            + f'    "{func_name}:classes/main/load"\n'
            + "    ]\n"
            + "}\n"
        )
        lf.close()

        mainload = open(os.path.join(wd_main, "load.mcfunction"), "w")
        if load_message:
            mainload.write(
                "# Default Load Message:\n"
                + f'tellraw @a {{"text":"Datapack {pack_name} is loaded."}}'
            )
        mainload.close()

    # create tick functions
    if tick_function:
        tf = open(os.path.join(wd_load, "tick.json"), "w")
        tf.write(
            "{\n"
            + '"values": [\n'
            + f'    "{func_name}:classes/main/tick"\n'
            + "    ]\n"
            + "}\n"
        )
        tf.close()

        maintick = open(os.path.join(wd_main, "tick.mcfunction"), "w")
        maintick.close()

    # create app directory
    wd_app = os.path.join(wd1, "data", "app", "functions")
    os.makedirs(wd_app)
    os.makedirs(os.path.join(wd_app, "get", func_name))
    os.makedirs(os.path.join(wd_app, "settings", func_name))
    os.makedirs(os.path.join(wd_app, "help", func_name))

    # create unload function
    if unload_function:
        mainclean = open(os.path.join(wd_main, "clean.mcfunction"), "w")
        mainclean.close()

        os.makedirs(os.path.join(wd_app, "unload"))
        uf = open(os.path.join(wd_app, "unload", func_name + ".mcfunction"), "w")
        if load_message:
            uf.write(
                "# Default Unload Message:\n"
                + f'tellraw @a {{"text":"Datapack {pack_name} is unloaded."}}\n'
            )
        uf.write(
            f"function {func_name}:classes/main/clean\n"
            + f'datapack disable "file/{pack_name}-{pack_version}"\n'
        )
        uf.close()

    print("Execution Complete.")
