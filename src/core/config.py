""" Config """
import os


def _mk_log_dir(folder: str) -> None:
    if not os.path.exists(folder):
        os.makedirs(folder)


cur_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(cur_dir)
log_filename = f'{cur_dir}/log_conf.yaml'
_mk_log_dir(f'{parent_dir}/logs')
_mk_log_dir(f'{os.path.dirname(parent_dir)}/tests/logs')
