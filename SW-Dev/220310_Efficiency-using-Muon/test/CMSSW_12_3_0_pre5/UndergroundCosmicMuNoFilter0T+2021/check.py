#!/usr/bin/env python3
import argparse
from pathlib import Path
import tqdm
import ROOT

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_dir', type=Path)
    parser.add_argument('-o', '--output-dir', type=Path, default='./logs/')
    parser.add_argument('--check-events', action='store_true')
    args = parser.parse_args()

    file_list = list(args.data_dir.glob('*.root'))
    pbar = tqdm.tqdm(file_list)

    total = len(file_list)
    wrong_list = []
    for checked, path in enumerate(pbar, 1):
        try:
            root_file = ROOT.TFile(str(path))
            checked_events = False
            for key in root_file.GetListOfKeys():
                name = key.GetName()
                root_file.Get(name)
                if name == 'Events':
                    checked_events = True
            if (not checked_events) and args.check_events:
                root_file.Get('Events')
        except Exception as error:
            print(error)
            wrong_list.append(str(path))

        wrong = len(wrong_list)
        frac_wrong = 100 * wrong / checked
        pbar.set_description(f'wrong / checked = {wrong} / {checked} ({frac_wrong:.2f} %)')

    output_path = args.output_dir / f'wrong-{args.data_dir.name}.txt'
    with open(output_path, 'w') as txt_file:
        text = '\n'.join(wrong_list)
        txt_file.write(text)

if __name__ == '__main__':
    main()
