""" Config """
import os

from pydantic_settings import BaseSettings


class FileSettings(BaseSettings):
    """File Settings"""

    cur_dir: str = os.path.dirname(os.path.abspath(__file__))
    parent_dir: str = os.path.dirname(cur_dir)
    project_dir: str = os.path.dirname(parent_dir)

    log_config_filename: str = f'{cur_dir}/log_conf.yaml'

    if not os.path.exists(f'{project_dir}/logs'):
        os.makedirs(f'{project_dir}/logs')

    log_rotation_filename: str = f'{project_dir}/logs/logs.log'


file_settings = FileSettings()
