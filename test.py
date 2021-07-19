import yaml
import logging


def config_file(file):
    with open(file,'r') as myfile:
        try:
            return yaml.safe_load(myfile)
        except yaml.YAMLError as exc:
            logging.error(exc)
            
            
def col_validation(df,table_config):
    
    config_cols = list(map(lambda x: x.lower(),table_config['columns']))
    config_cols.sort()
    df.columns = list(map(lambda x: x.lower(),list(df.columns)))    
    if len(df.columns)== len(config_cols) and list(config_cols).sort() == list(df.columns).sort():
        print('Column name and column length validation passed')
        return 1
    else:
        print('Column name and column length validation failed')
        mismatched_columns_file = list(set(df.columns).difference(config_cols))
        print("Following columns are not in the YAML file",mismatched_columns_file)
        missing_YAML_file = list(set(config_cols).difference(df.columns))
        print("Following YAML columns are not in the file uploaded",missing_YAML_file)
        logging.info(f'df.columns: {df.columns}')
        logging.info(f'config_cols: {config_cols}')
        return 0
