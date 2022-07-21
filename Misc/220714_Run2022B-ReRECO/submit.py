import sys
import os
import importlib.util
import json
import subprocess
from pathlib import Path
import argparse

PROJECT_DIR = Path(__file__).parent
CONFIG_DIR = PROJECT_DIR / 'data' / 'reco_config'
assert CONFIG_DIR.exists(), CONFIG_DIR

CRAB_CONFIG_FILE = PROJECT_DIR / 'crabConfig.py'
assert CRAB_CONFIG_FILE.exists(), CRAB_CONFIG_FILE


def download_config(run):
    url = f'https://cmsweb.cern.ch/t0wmadatasvc/prod/reco_config?run={run}'
    output_file = str(CONFIG_DIR / f'run-{run}.json')

    print(f'downloading reco_config for {run=} from {url=} ...')

    args =  [
        'wget',
        '--no-check-certificate',
        url,
        '-O',
        output_file,
    ]

    subprocess.run(args)
    return output_file


def read_json(path):
    with open(path, 'r') as json_file:
        data = json.load(json_file)
    return data


def check_dataset(run,
                  primary_dataset,
                  checklist):
    config_path = CONFIG_DIR / f'run-{run}.json'
    if not os.path.exists(config_path):
        download_config(run)

    config = read_json(config_path)
    config = config['result']

    has_dataset = False
    for each in config:
        if each['primary_dataset'] == primary_dataset:
            assert each['run'] == run
            assert each['cmssw'] == checklist['cmssw']
            assert each['scenario'] == checklist['scenario']
            assert each['global_tag'] == checklist['global_tag']
            has_dataset = True
            break
    if not has_dataset:
        print(f'{run=}: {primary_dataset} not found')
    return has_dataset


def check_global_tag(request):
    pset_name = Path(request['pset_name'])
    assert pset_name.exists(), pset_name.resolve()
    module_name = pset_name.stem
    spec = importlib.util.spec_from_file_location(module_name, pset_name)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    assert module.process.GlobalTag.globaltag.value() == request['global_tag']


def submit(request_path, dry_run=False):
    request = read_json(request_path)
    assert os.getenv('CMSSW_VERSION') == request['cmssw'], os.getenv('CMSSW_VERSION')
    check_global_tag(request)
    pset_name = request['pset_name']

    for input_dataset in request['dataset']:
        print('#' * 120)
        _, primary_dataset, processed_dataset, data_tier = input_dataset.split('/')

        run_list = [run for run in request['run'] if check_dataset(run=run, primary_dataset=primary_dataset, checklist=request)]
        if len(run_list) < 1:
            print(f'{input_dataset}: run not found')
            continue
        run_range = ','.join(map(str, run_list))

        output_dataset_tag = f'GEM-reRECO-GEM-only__{processed_dataset}__{data_tier}'
        request_name = output_dataset_tag

        args = (
            'crab', 'submit',
            '--config', str(CRAB_CONFIG_FILE),
            'General.workArea=./crabWorkArea/',
            f'General.requestName={request_name}',
            f'JobType.psetName={pset_name}',
            f'Data.runRange={run_range}',
            f'Data.inputDataset={input_dataset}',
            f'Data.outputDatasetTag={output_dataset_tag}',
        )

        print(' '.join(args))
        if dry_run:
            continue

        subprocess.run(args)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--request-path", type=str, required=True, help="a json file")
    parser.add_argument("-d", "--dry-run", action="store_true", default=False, help="dry run")
    args = parser.parse_args()

    submit(args.request_path, args.dry_run)


if __name__ == '__main__':
    main()
