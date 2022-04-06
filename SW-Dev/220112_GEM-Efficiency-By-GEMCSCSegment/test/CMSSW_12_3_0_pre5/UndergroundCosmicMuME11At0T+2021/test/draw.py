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
    eff = ROOT.TEfficiency(h_num, h_den)
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

def draw_eff(trk_dir, sta_dir, glb_dir):
    canvas = ROOT.TCanvas(f"c-{uuid.uuid4()}", "", 1600, 1000)
    canvas.Divide(3, 2)

###############################################################################
    top_key = 'Efficiency/chamber_GE11-P-L1'

    trk_pad = canvas.cd(1)
    trk_eff = make_eff(trk_dir, top_key)
    trk_eff.Draw()
    add_line(trk_pad, trk_eff)

    sta_pad = canvas.cd(2)
    sta_eff = make_eff(sta_dir, top_key)
    sta_eff.Draw()
    add_line(sta_pad, sta_eff)

    glb_pad = canvas.cd(3)
    glb_eff = make_eff(glb_dir, top_key)
    glb_eff.Draw()
    add_line(glb_pad, glb_eff)

###############################################################################
    bottom_key = 'Efficiency/muon_eta_GE11-P'

    trk_pad = canvas.cd(4)
    trk_eff = make_eff(trk_dir, bottom_key)
    trk_eff.Draw()
    add_line(trk_pad, trk_eff)

    sta_pad = canvas.cd(5)
    sta_eff = make_eff(sta_dir, bottom_key)
    sta_eff.Draw()
    add_line(sta_pad, sta_eff)

    glb_pad = canvas.cd(6)
    glb_eff = make_eff(glb_dir, bottom_key)
    glb_eff.Draw()
    add_line(glb_pad, glb_eff)

###############################################################################
    canvas.SaveAs('./output/eff.png')

def draw_debug(trk_dir, sta_dir, glb_dir):
    canvas = ROOT.TCanvas(f"c-{uuid.uuid4()}", "", 1600, 1500)
    canvas.Divide(3, 3)

###############################################################################
    trk_pad = canvas.cd(1)
    trk_eff = make_eff(trk_dir, 'Misc/prop_err_r_GE11-P')
    trk_eff.Draw()
    add_line(trk_pad, trk_eff)

    sta_pad = canvas.cd(2)
    sta_eff = make_eff(sta_dir, 'Misc/prop_err_r_GE11-P')
    sta_eff.Draw()
    add_line(sta_pad, sta_eff)

    glb_pad = canvas.cd(3)
    glb_eff = make_eff(glb_dir, 'Misc/prop_err_r_GE11-P')
    glb_eff.Draw()
    add_line(glb_pad, glb_eff)

###############################################################################
    trk_pad = canvas.cd(4)
    trk_eff = make_eff(trk_dir, 'Misc/prop_err_phi_GE11-P')
    trk_eff.Draw()
    add_line(trk_pad, trk_eff)

    sta_pad = canvas.cd(5)
    sta_eff = make_eff(sta_dir, 'Misc/prop_err_phi_GE11-P')
    sta_eff.Draw()
    add_line(sta_pad, sta_eff)

    glb_pad = canvas.cd(6)
    glb_eff = make_eff(glb_dir, 'Misc/prop_err_phi_GE11-P')
    glb_eff.Draw()
    add_line(glb_pad, glb_eff)

###############################################################################
    trk_pad = canvas.cd(7)
    trk_eff = make_eff(trk_dir, 'Misc/start_det_GE11-P')
    trk_eff.Draw()
    add_line(trk_pad, trk_eff)

    sta_pad = canvas.cd(8)
    sta_eff = make_eff(sta_dir, 'Misc/start_det_GE11-P')
    sta_eff.Draw()
    add_line(sta_pad, sta_eff)

    glb_pad = canvas.cd(9)
    glb_eff = make_eff(glb_dir, 'Misc/start_det_GE11-P')
    glb_eff.Draw()
    add_line(glb_pad, glb_eff)

###############################################################################
    canvas.SaveAs('./output/debug.png')

def main():
    path = "DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root"
    root_file = ROOT.TFile(path)
    gem_dir = root_file.Get('DQMData/Run 1/GEM/Run summary')
    eff_dir = gem_dir.Get('Efficiency')
    gemcsc_dir = eff_dir.Get('GEMCSCSegment')
    glb_dir = eff_dir.Get('GLBMuon')
    sta_dir = eff_dir.Get('STAMuon')
    trk_dir = eff_dir.Get('TRKMuon')

    draw_eff(trk_dir, sta_dir, glb_dir)
    draw_debug(trk_dir, sta_dir, glb_dir)

if __name__ == '__main__':
    main()
