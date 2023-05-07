# Using the infos in config.ini, starts the EC2 instance

from toolbox.aws import start_instance_from_config
import argparse

def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", type=str)
    args = parser.parse_args()
    return args
    
start_instance_from_config('config.ini', name=get_args().name)
