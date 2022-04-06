#!/usr/bin/env python3
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
        input_dir.ls()
        print(key, h_num, h_den)
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
            eff.Draw()
    canvas.SaveAs(f'./output/{plot_name}.png')

def main():
    path = "./DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root"
    root_file = ROOT.TFile(path)
    gem_dir = root_file.Get('DQMData/Run 1/GEM/Run summary')
    eff_dir = gem_dir.Get('Efficiency')

    dir_list = [eff_dir.Get(each) for each in ['type1', 'type2']]

    rl_list = ['M-L2', 'M-L1', 'P-L1', 'P-L2']
    r_list = ['M', 'P']

    draw_eff(dir_list, 'Efficiency/chamber_GE11-{det}', rl_list, 'eff_ch')
    draw_eff(dir_list, 'Efficiency/ieta_GE11-{det}', rl_list, 'eff_ieta')
    draw_eff(dir_list, 'Efficiency/muon_eta_GE11-{det}', r_list, 'eff_eta')
    draw(dir_list, 'Efficiency/muon_eta_GE11-{det}', r_list, 'eta')
    draw(dir_list, 'Efficiency/muon_eta_GE11-{det}_matched', r_list, 'eta_matched')
    draw(dir_list, 'Misc/prop_r_err', ['none'], 'prop_r_err')
    draw(dir_list, 'Misc/prop_phi_err', ['none'], 'prop_phi_err')

if __name__ == '__main__':
    main()
