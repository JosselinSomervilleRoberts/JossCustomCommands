# Using the infos in config.ini, stops the EC2 instance

from toolbox.aws import stop_instance_from_config
import argparse

def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", type=str)
    args = parser.parse_args()
    return args
    
stop_instance_from_config('config.ini', name=get_args().name)
