from src.core.db import Database
from src.utils.config import get_config
from src.utils.args import parse_arguments

def main():
    config = get_config()['database']
    db = Database(config['host'],config['database'],config['user'],config['password'])

if __name__ == "__main__":
    parse_arguments()
    main()
