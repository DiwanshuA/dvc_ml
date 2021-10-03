import os 
from src.utils.all_utils import read_yaml, create_directory, save_local_df
#from src.all_utils import read_yaml
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split

def splitandsave(config_path, params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    #remote_data_path = config["data_source"]
    #df = pd.read_csv(remote_data_path, sep=";")

    #save dataset in the local directory
    #create path to directory: artifacts/raw_local_dir/data.
    artifacts_dir = config["artifacts"]["artifacts_dir"]
    raw_local_dir = config["artifacts"]["raw_local_dir"]
    raw_local_file = config["artifacts"]["raw_local_file"]

    raw_local_dir_path = os.path.join(artifacts_dir, raw_local_dir)
    raw_local_file_path = os.path.join(raw_local_dir_path,raw_local_file)

    df = pd.read_csv(raw_local_file_path)

    split_ratio = params["base"]["test_size"]
    random_state = params["base"]["random_state"]

    train, test = train_test_split(df, test_size=split_ratio, random_state=random_state)

    split_datadir = config["artifacts"]["split_data_dir"]
    
    create_directory([os.path.join(artifacts_dir, split_datadir)])

    train_filename = config["artifacts"]["train"]
    test_filename = config["artifacts"]["test"]

    train_datapath = os.path.join(artifacts_dir, split_datadir, train_filename)
    test_datapath = os.path.join(artifacts_dir, split_datadir, test_filename)

    for data, datapath in (train, train_datapath), (test, test_datapath):
        save_local_df(data, datapath)


if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")

    parsed_args = args.parse_args()

    splitandsave(config_path=parsed_args.config, params_path=parsed_args.params)