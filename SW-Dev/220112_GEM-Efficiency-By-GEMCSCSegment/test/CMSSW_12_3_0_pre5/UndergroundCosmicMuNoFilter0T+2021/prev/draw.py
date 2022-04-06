#!/usr/bin/env python3
import argparse
import ROOT
from ROOT import gPad, gStyle, gROOT
import uuid
gROOT.SetBatch()
gStyle.SetOptStat(0)

MEM = []

def make_eff(input_dir, key):
    h_den = input_dir.Get(key)
    h_num = input_dir.Get(key + '_matched')
    try:
        eff = ROOT.TEfficiency(h_num, h_den)
    except Exception as exception:
        print(key, h_num, h_den)
        print(key in [each.GetName() for each in input_dir.GetListOfKeys()])
        input_dir.ls()
        raise exception
    global MEM
    MEM += [eff]
    return eff

def add_line(pad, eff):
    pad.Draw()
    x_axis = eff.GetPaintedGraph().GetXaxis()
    nbinx = x_axis.GetNbins()
    x_min = x_axis.GetBinLowEdge(1)
    x_max = x_axis.GetBinUpEdge(nbinx) + x_axis.GetBinWidth(nbinx)
    line = ROOT.TLine(0, 0.95, x_max, 0.95)
    line.SetLineColor(ROOT.kGreen)
    line.SetLineStyle(ROOT.kDashed)
    line.SetLineWidth(2)
    line.Draw('SAME')

    global MEM
    MEM += [line]

def draw_eff(dir_list, key_template, det_list, plot_name):
    canvas = ROOT.TCanvas(f"c-{uuid.uuid4()}", "", 500 * len(det_list), 500 * len(dir_list))
    canvas.Divide(len(det_list), len(dir_list))

    ###############################################################################
    for dir_idx, directory in enumerate(dir_list):
        for idx, det in enumerate(det_list, 1 + dir_idx * len(det_list)):
            key = key_template.format(det=det)
            pad = canvas.cd(idx)
            eff = make_eff(directory, key)
            eff.Draw()
            add_line(pad, eff)

    canvas.SaveAs(f'./output/{plot_name}.png')

def draw(dir_list, key_template, det_list, plot_name):
    canvas = ROOT.TCanvas(f"c-{uuid.uuid4()}", "", 500 * len(det_list), 500 * len(dir_list))
    canvas.Divide(len(det_list), len(dir_list))

    ###############################################################################
    for dir_idx, directory in enumerate(dir_list):
        for idx, det in enumerate(det_list, 1 + dir_idx * len(det_list)):
            key = key_template.format(det=det)
            pad = canvas.cd(idx)
            eff = directory.Get(key)
            eff.Draw('HIST E1')
    canvas.SaveAs(f'./output/{plot_name}.png')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, default="./DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root")
    args = parser.parse_args()
    root_file = ROOT.TFile(args.path)
    gem_dir = root_file.Get('DQMData/Run 1/GEM/Run summary')
    eff_dir = gem_dir.Get('Efficiency')

    dir_list = [eff_dir.Get(each) for each in ['type1', 'type2']]

    rl_list = ['GE-11_L2', 'GE-11_L1', 'GE+11_L1', 'GE+11_L2']
    r_list = ['GE-11', 'GE+11']

    draw_eff(dir_list, 'Efficiency/chamber_{det}', rl_list, 'ch')
    draw_eff(dir_list, 'Efficiency/ieta_{det}', rl_list, 'ieta')
    draw_eff(dir_list, 'Efficiency/muon_eta_{det}', r_list, 'eta')

    draw(dir_list, 'Efficiency/muon_pt_{det}', r_list, 'pt')
    draw(dir_list, 'Efficiency/muon_eta_{det}', r_list, 'eta')
    draw(dir_list, 'Efficiency/muon_eta_{det}_matched', r_list, 'eta_matched')

    draw(dir_list, 'Misc/prop_r_err', ['dummy'], 'prop_r_err')
    draw(dir_list, 'Misc/prop_phi_err', ['dummy'], 'prop_phi_err')


if __name__ == '__main__':
    main()
