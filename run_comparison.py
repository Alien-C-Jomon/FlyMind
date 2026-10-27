import sys, os, pathlib
sys.path.append('repo')
from model import run_exp
from model import default_params as params
import utils as utl
from brian2 import Hz, second
pathlib.Path('./results/flymind_comparison').mkdir(parents=True, exist_ok=True)
config = {'path_res': './results/flymind_comparison', 'path_comp': './repo/2023_03_23_completeness_630_final.csv', 'path_con': './repo/2023_03_23_connectivity_630_final.parquet', 'n_proc': -1}
neu_sugar = [720575940624963786, 720575940630233916, 720575940637568838, 720575940638202345, 720575940617000768, 720575940630797113]
print('Starting FlyMind Sugar Simulation Test...')
params['t_run'] = 0.5 * second
params['n_run'] = 2
run_exp(exp_name='sugar_test', neu_exc=neu_sugar, params=params, **config)
print('Sugar simulation completed successfully and saved!')