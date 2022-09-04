from src.syncronizer import Replica
from src.cli_parser import cli

if __name__ == "__main__":
    args = cli()
    r = Replica(args[0], args[1], args[2])
    r.sync()