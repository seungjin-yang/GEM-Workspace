#!/usr/bin/env python3.6
from pathlib import Path
import argparse
import htcondor # type: ignore

def main():
    """TODO: Docstring for main.
    :returns: TODO

    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dry-run", action="store_true", default=False, help="dry run")
    args = parser.parse_args()

    executable = Path('./run-step2_RAW2DIGI_L1Reco_RECO_GEMCSCSegment.sh').resolve()

    log_dir = Path('./logs/step2_RAW2DIGI_L1Reco_RECO_GEMCSCSegment/')
    if not log_dir.exists():
        log_dir.mkdir(parents=True)

    job_batch_name = 'GEM__220722_GE21-ME21-Segment-Reco__12_5_0_pre4__reco-with-relval__step2_RAW2DIGI_L1Reco_RECO_GEMCSCSegment'
    transfer_input_files = './step2_RAW2DIGI_L1Reco_RECO_GEMCSCSegment.py'

    dest = '/store/user/seyang/GEM/SW-Dev/220722_GE21-ME21-Segment-Reco/test/CMSSW_12_5_0_pre4/reco-with-relval/step2_RAW2DIGI_L1Reco_RECO_GEMCSCSegment/'
    transfer_output_remaps = f'\"output.root = {dest}/$(stem).root\"'

    submit = {
        "executable": executable,
        'universe': 'vanilla',
        'JobBatchName': job_batch_name,
        'getenv': 'True',
        'request_memory': '3GB',
        'should_transfer_files': 'YES',
        'when_to_transfer_output': 'ON_EXIT',
        'transfer_input_files': transfer_input_files,
        'arguments': '$(input_file)',
        'output': log_dir / 'job_$(stem).out',
        'error': log_dir / 'job_$(stem).err',
        'log': log_dir / 'condor.log',
        'x509userproxy': '$ENV(X509_USER_PROXY)',
        'use_x509userproxy': True,
        'transfer_output_remaps': transfer_output_remaps,
    }
    submit = {key: str(value) for key, value in submit.items()}
    condor = htcondor.Submit(submit)
    schedd = htcondor.Schedd()

    with open('filelist.txt', 'r') as txt_file:
        file_list = txt_file.read().split('\n')
        file_list = filter(lambda each: len(each) > 0, file_list)
    itemdata = [{'input_file': each, 'stem': Path(each).stem} for each in file_list]

    for each in itemdata:
        print(each)

    print(submit)

    if args.dry_run:
        return

    with schedd.transaction() as txn:
        cluster_id = condor.queue_with_itemdata(txn, itemdata=iter(itemdata))
        print(f'{len(itemdata)} jobs submmited with job id {cluster_id.cluster()}')

if __name__ == "__main__":
    main()
