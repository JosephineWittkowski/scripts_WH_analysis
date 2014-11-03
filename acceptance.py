#!/usr/bin/env python
import ROOT
import sys
from ROOT import TLatex
#import numpy as np
#import matplotlib.pyplot as plt
#from matplotlib import rc
#from pylab import *

# activate latex text rendering
#rc('text', usetex=True)
#import "RooStats/NumberCountingUtils.h"

from gridCoord import getGridCoordinates, reqidByMc1Mn1

ROOT.gROOT.ProcessLine("gROOT->SetBatch()")

names_of_TruthSignal_files = [
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177501_n0150_Truth_BJetDR04_02_06_14.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177502_n0150_Truth_BJetDR04_02_06_14.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177503_n0150_Truth_BJetDR04_02_06_14.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177504_n0150_Truth_BJetDR04_02_06_14.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177505_n0150_Truth_BJetDR04_02_06_14.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177506_n0150_Truth_BJetDR04_02_06_14.root", 
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177507_n0150_Truth_BJetDR04_02_06_14.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177508_n0150_Truth_BJetDR04_02_06_14.root", 
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177509_n0150_Truth_BJetDR04_02_06_14.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177510_n0150_Truth_BJetDR04_02_06_14.root", 
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177511_n0150_Truth_BJetDR04_02_06_14.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177512_n0150_Truth_BJetDR04_02_06_14.root", 
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177513_n0150_Truth_BJetDR04_02_06_14.root", 
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177514_n0150_Truth_BJetDR04_02_06_14.root", 
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177515_n0150_Truth_BJetDR04_02_06_14.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177516_n0150_Truth_BJetDR04_02_06_14.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177517_n0150_Truth_BJetDR04_02_06_14.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177518_n0150_Truth_BJetDR04_02_06_14.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177519_n0150_Truth_BJetDR04_02_06_14.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177520_n0150_Truth_BJetDR04_02_06_14.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177521_n0150_Truth_BJetDR04_02_06_14.root", 
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177522_n0150_Truth_BJetDR04_02_06_14.root", 
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177523_n0150_Truth_BJetDR04_02_06_14.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177524_n0150_Truth_BJetDR04_02_06_14.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177525_n0150_Truth_BJetDR04_02_06_14.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177526_n0150_Truth_BJetDR04_02_06_14.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177527_n0150_Truth_BJetDR04_02_06_14.root"
		       ]
		       
names_of_RecoSignal_files = [
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177501_n0150_02_06_14.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177502_n0150_02_06_14.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177503_n0150_02_06_14.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177504_n0150_02_06_14.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177505_n0150_02_06_14.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177506_n0150_02_06_14.root", 
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177507_n0150_02_06_14.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177508_n0150_02_06_14.root", 
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177509_n0150_02_06_14.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177510_n0150_02_06_14.root", 
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177511_n0150_02_06_14.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177512_n0150_02_06_14.root", 
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177513_n0150_02_06_14.root", 
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177514_n0150_02_06_14.root", 
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177515_n0150_02_06_14.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177516_n0150_02_06_14.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177517_n0150_02_06_14.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177518_n0150_02_06_14.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177519_n0150_02_06_14.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177520_n0150_02_06_14.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177521_n0150_02_06_14.root", 
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177522_n0150_02_06_14.root", 
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177523_n0150_02_06_14.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177524_n0150_02_06_14.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177525_n0150_02_06_14.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177526_n0150_02_06_14.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16_n0150/histos_ZN_177527_n0150_02_06_14.root"
		       ]		       
		       
		       
rootfiles_TruthSignal = []
for f in names_of_TruthSignal_files:
  rootfiles_TruthSignal.append(ROOT.TFile(f))
  
rootfiles_RecoSignal = []
for f in names_of_RecoSignal_files:
  rootfiles_RecoSignal.append(ROOT.TFile(f))  
  
mcid_of_grid_point = [177501, 177502, 177503, 177504, 177505, 177506, 177507, 177508, 177509, 177510, 177511, 177512, 177513, 177514, 177515, 177516, 177517, 177518, 177519, 177520, 177521, 177522, 177523, 177524, 177525, 177526, 177527]
histonames_list = ["cutflow_EE_ALL", "cutflow_MM_ALL", "cutflow_EM_ALL"]  






graphProduced = ROOT.TGraph2D()
graphXsec = ROOT.TGraph2D()
graphXsec_x_BR = ROOT.TGraph2D()
text_produced = []
text_xsec = []
text_xsec_x_BR = []
txt_array_produced = []
txt_array_xsec = []
txt_array_xsec_x_BR = []
    
BR = 0.30636 #SUSYTools/trunk/data/mc12_8TeV/Herwigpp_UEEE3_CTEQ6L1_simplifiedModel_wA.tx
#loop over 1 jet bin, 2,3 jet bin:
for i_j in range(0, 2):
  #loop over histonames:
  for i_h, histoname in enumerate(histonames_list):
    N_points=0
    i_Acc = 0
    i_Eff = 0
    i_Acc_x_Eff = 0
    i_produced = 0
    i_xsec = 0
    i_xsec_x_BR = 0
    #define array with entry for every grid point:  
    A_N = [0., 0., 0., 0. ,0. ,0. ,0. ,0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]
    E_N = [0., 0., 0., 0. ,0. ,0. ,0. ,0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]
    A_x_E_N = [0., 0., 0., 0. ,0. ,0. ,0. ,0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]
    N = [0., 0., 0., 0. ,0. ,0. ,0. ,0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]
    txt_array_Acc = []
    txt_array_Eff = []
    txt_array_Acc_x_Eff = []

    text_Acc = []
    text_Eff = []
    text_Acc_x_Eff = []

    graphAcc = ROOT.TGraph2D()
    graphEff = ROOT.TGraph2D()
    graphAcc_x_Eff = ROOT.TGraph2D()


    #loop over grid points:
    for i_r, TruthSigFile in enumerate(rootfiles_TruthSignal):
	
      ybin = 0
      if "EE" in histoname:
	if i_j == 0:
	  ybin = 34
	  title = "SR 1j EE"
	if i_j == 1:
	  ybin = 42
	  title = "SR 2,3j EE"
      if "MM" in histoname:
	if i_j == 0:
	  ybin = 32
	  title = "SR 1j MM"
	if i_j == 1:
	  ybin = 41
	  title = "SR 2,3j MM"
      if "EM" in histoname:
	if i_j == 0:
	  ybin = 32
	  title = "SR 1j EM"
	if i_j == 1:
	  ybin = 42	  
	  title = "SR 2,3j EM"
      SR_yieldTruth = TruthSigFile.Get(histoname).Integral(ybin, ybin)
      sample_yieldTruth = TruthSigFile.Get(histoname).Integral(1, 1)
      SR_yieldReco = rootfiles_RecoSignal[i_r].Get(histoname).Integral(ybin, ybin)
      if N_points == 0:
	print N_points, "sample_yieldTruth ", sample_yieldTruth, "SR_yieldTruth= ", SR_yieldTruth
	print "SR_yieldReco= ", SR_yieldReco
      acceptance = SR_yieldTruth / sample_yieldTruth
      if SR_yieldTruth>0:
	efficiency = SR_yieldReco / SR_yieldTruth      
      else:
	efficiency = 0
	print "SR_yieldTruth= ", SR_yieldTruth
      acceptance_x_efficiency = SR_yieldReco / sample_yieldTruth

      #calc acceptance for all grid points [r]:
      A_N[i_r] = 100*acceptance
      
      #calc Efficiency for all grid points [r]:
      E_N[i_r] = 100*efficiency
      
      A_x_E_N[i_r] = 100 * acceptance * efficiency

      #get grid coordinates for this grid point:
      xcoord, ycoord, xsec = getGridCoordinates(mcid_of_grid_point[i_r])
      if N_points == 0:
	print "acceptance ", acceptance, "efficiency", efficiency, "acceptance * efficiency", acceptance * efficiency
	#print "A_N[i_r] ", A_N[i_r], "E_N[i_r]", E_N[i_r], "A_N[i_r] * E_N[i_r]", A_N[i_r] * E_N[i_r]
      graphAcc.SetPoint(N_points, xcoord, ycoord, A_N[i_r])
      graphEff.SetPoint(N_points, xcoord, ycoord, E_N[i_r])
      graphAcc_x_Eff.SetPoint(N_points, xcoord, ycoord, A_x_E_N[i_r])
      if i_j == 0 and "cutflow_EE_ALL" in histoname:
	graphProduced.SetPoint(N_points, xcoord, ycoord, sample_yieldTruth/1000)
	graphXsec.SetPoint(N_points, xcoord, ycoord, xsec)
	graphXsec_x_BR.SetPoint(N_points, xcoord, ycoord, xsec*BR)
	
      #if N_points == 0:
	#print "str(round(A_N[i_r],2))", str(round(A_N[i_r],2))
	#print "str(round(E_N[i_r],2))", str(round(E_N[i_r],2))
	#print "str(round(A_E_N[i_r],2))", str(round(A_x_E_N[i_r],2))
      txt_array_Acc.append(str(round(A_N[i_r],2)))
      txt_array_Eff.append(str(round(E_N[i_r],2)))
      txt_array_Acc_x_Eff.append(str(round(A_x_E_N[i_r],4)))
      if i_j == 0 and "cutflow_EE" in histoname:
	txt_array_produced.append(str((int(sample_yieldTruth+1)/1000)))
	txt_array_xsec.append(str(round(xsec, 2)))
	txt_array_xsec_x_BR.append(str(round(xsec * BR, 2)))
	
      N_points += 1
	
      #end loop over grid points
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    if i_j == 0:
      njets_name = "1jet"
    else:
      njets_name = "2OR3jets"
    #make TCanvas, draw TGraph2D:  
    canvasAcc = ROOT.TCanvas("Acc_"+ histoname + njets_name,"Acc_"+ histoname + njets_name, 600, 600)
    
    ROOT.gStyle.SetPalette(1); 
    graphAcc.SetTitle("Acceptance [%]   ")
    graphAcc.GetYaxis().SetTitle("#tilde{#chi}_{1}^{0}")
    graphAcc.GetXaxis().SetTitle("#tilde{#chi}_{1}^{#pm}/#tilde{#chi}_{2}^{0}")  
    
    graphAcc.Draw("COLZ")

    canvasAcc.SetRightMargin(0.15)
    
    #write text for each grid point:
    for r in range(0, len(rootfiles_TruthSignal)):
      if r == 0:
	print "txt_array_Acc[", i_Acc, "]", txt_array_Acc[i_Acc]
      xcoord, ycoord, xsec = getGridCoordinates(mcid_of_grid_point[r])
      text_Acc.append(ROOT.TText(xcoord, ycoord, txt_array_Acc[i_Acc]))
      text_Acc[i_Acc].SetTextSize(0.03);
      text_Acc[i_Acc].Draw("same")
      i_Acc += 1
      #end loop over grid points
      
    graphAcc.GetYaxis().SetTitle("#tilde{#chi}_{1}^{0}")
    graphAcc.GetXaxis().SetTitle("#tilde{#chi}_{1}^{#pm}/#tilde{#chi}_{2}^{0}")  
    graphAcc.GetXaxis().SetTitleOffset(1.2);
    graphAcc.GetYaxis().SetTitleOffset(1.3);
    graphAcc.GetXaxis().SetLimits(125, 350)
    graphAcc.GetYaxis().SetLimits(0, 90)
    l = ROOT.TLatex()
    l.SetTextAlign(22); 
    l.SetTextSize(0.04); 
    l.SetNDC();
    l.SetTextFont(72);
    l.DrawLatex(0.26, 0.85, "ATLAS #bf{#it{Internal}}")
    l.DrawLatex(0.7, 0.85, "#it{#scale[0.6]{#int} L dt = 20.3 fb^{-1}}")
    l.DrawLatex(0.7, 0.75, "#it{#sqrt{s} = 8 TeV}")
    
    
    #txt_atlas_label = ROOT.TText(140., 65., "#bf{ATLAS} Internal")
    #txt_atlas_label.SetTextSize(0.03);
    #txt_atlas_label.Draw("same")
    canvasAcc.Update()
    graphAcc.SetName("acceptance_" + histoname + "_" + njets_name)
    outputfile = ROOT.TFile("/data/etp3/jwittkow/figures_acc/acceptance_efficiency.root", "update")
    graphAcc.Write()
    outputfile.Close()   
    canvasAcc.SaveAs("/data/etp3/jwittkow/figures_acc/acceptance_" + histoname + "_" + njets_name + "_29_10_14.eps")    
    #canvasAcc.SaveAs("/data/etp3/jwittkow/figures_acc/acceptance_" + histoname + "_" + njets_name + "_29_10_14.root")    
    graphAcc.GetYaxis().SetTitle("#tilde{#chi}_{1}^{0}")
    graphAcc.GetXaxis().SetTitle("#tilde{#chi}_{1}^{#pm}/#tilde{#chi}_{2}^{0}")  
    graphAcc.GetXaxis().SetTitleOffset(1.2);
    graphAcc.GetYaxis().SetTitleOffset(1.3);
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #make TCanvas, draw TGraph2D:  
    canvasEff = ROOT.TCanvas("Eff_"+ histoname + njets_name,"Eff_"+ histoname + njets_name, 600, 600)
    
    ROOT.gStyle.SetPalette(1); 
    graphEff.SetTitle("Efficiency [%]   ")
    graphEff.GetYaxis().SetTitle("#tilde{#chi}_{1}^{0}")
    graphEff.GetXaxis().SetTitle("#tilde{#chi}_{1}^{#pm}/#tilde{#chi}_{2}^{0}")  
    graphEff.Draw("COLZ")

    canvasEff.SetRightMargin(0.15)
    graphEff.GetYaxis().SetTitleOffset(1.2);
    
    #write text for each grid point:
    for r in range(0, len(rootfiles_TruthSignal)):
      if r == 0:
	print "txt_array_Eff[", i_Eff, "]", txt_array_Eff[i_Eff]
      xcoord, ycoord, xsec = getGridCoordinates(mcid_of_grid_point[r])
      text_Eff.append(ROOT.TText(xcoord, ycoord, txt_array_Eff[i_Eff]))
      text_Eff[i_Eff].SetTextSize(0.03);
      text_Eff[i_Eff].Draw("same")
      i_Eff += 1
      #end loop over grid points
      
    graphEff.GetYaxis().SetTitle("#tilde{#chi}_{1}^{0}")
    graphEff.GetXaxis().SetTitle("#tilde{#chi}_{1}^{#pm}/#tilde{#chi}_{2}^{0}")  
    graphEff.GetXaxis().SetTitleOffset(1.2);
    graphEff.GetYaxis().SetTitleOffset(1.3);
    graphEff.GetXaxis().SetLimits(125, 350)
    graphEff.GetYaxis().SetLimits(0, 90)
    l.DrawLatex(0.26, 0.85, "ATLAS #bf{#it{Internal}}")
    l.DrawLatex(0.7, 0.85, "#it{#scale[0.6]{#int} L dt = 20.3 fb^{-1}}")
    l.DrawLatex(0.7, 0.75, "#it{#sqrt{s} = 8 TeV}")
    canvasEff.Update()
    graphEff.SetName("efficiency_" + histoname + "_" + njets_name)
    outputfile = ROOT.TFile("/data/etp3/jwittkow/figures_acc/acceptance_efficiency.root", "update")
    graphEff.Write()
    outputfile.Close()   
    canvasEff.SaveAs("/data/etp3/jwittkow/figures_acc/efficiency_" + histoname + "_" + njets_name + "_29_10_14.eps")    
    #canvasEff.SaveAs("/data/etp3/jwittkow/figures_acc/efficiency_" + histoname + "_" + njets_name + "_29_10_14.root")    
    graphEff.GetYaxis().SetTitle("#tilde{#chi}_{1}^{0}")
    graphEff.GetXaxis().SetTitle("#tilde{#chi}_{1}^{#pm}/#tilde{#chi}_{2}^{0}")
    graphEff.GetXaxis().SetTitleOffset(1.2);
    graphEff.GetYaxis().SetTitleOffset(1.3);
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #make TCanvas, draw TGraph2D:  
    canvasAcc_x_Eff = ROOT.TCanvas("Acc_x_Eff_"+ histoname + njets_name,"Acc_x_Eff_"+ histoname + njets_name, 600, 600)
    
    ROOT.gStyle.SetPalette(1); 
    graphAcc_x_Eff.SetTitle("Acceptance #times Efficiency [%]   ")
    graphAcc_x_Eff.GetYaxis().SetTitle("#tilde{#chi}_{1}^{0}")
    graphAcc_x_Eff.GetXaxis().SetTitle("#tilde{#chi}_{1}^{#pm}/#tilde{#chi}_{2}^{0}")  
    graphAcc_x_Eff.Draw("COLZ")

    canvasAcc_x_Eff.SetRightMargin(0.15)
    graphAcc_x_Eff.GetYaxis().SetTitleOffset(1.2);
    
    #write text for each grid point:
    for r in range(0, len(rootfiles_TruthSignal)):
      if r == 0:
	print "txt_array_Acc_x_Eff[", i_Acc_x_Eff, "]", txt_array_Acc_x_Eff[i_Acc_x_Eff]
      xcoord, ycoord, xsec = getGridCoordinates(mcid_of_grid_point[r])
      text_Acc_x_Eff.append(ROOT.TText(xcoord, ycoord, txt_array_Acc_x_Eff[i_Acc_x_Eff]))
      text_Acc_x_Eff[i_Acc_x_Eff].SetTextSize(0.03);
      text_Acc_x_Eff[i_Acc_x_Eff].Draw("same")
      i_Acc_x_Eff += 1
      #end loop over grid points
      
    graphAcc_x_Eff.GetYaxis().SetTitle("#tilde{#chi}_{1}^{0}")
    graphAcc_x_Eff.GetXaxis().SetTitle("#tilde{#chi}_{1}^{#pm}/#tilde{#chi}_{2}^{0}")  
    graphAcc_x_Eff.GetXaxis().SetTitleOffset(1.2);
    graphAcc_x_Eff.GetYaxis().SetTitleOffset(1.3);
    graphAcc_x_Eff.GetXaxis().SetLimits(125, 350)
    graphAcc_x_Eff.GetYaxis().SetLimits(0, 90)
    l.DrawLatex(0.26, 0.85, "ATLAS #bf{#it{Internal}}")
    l.DrawLatex(0.7, 0.85, "#it{#scale[0.6]{#int} L dt = 20.3 fb^{-1}}")
    l.DrawLatex(0.7, 0.75, "#it{#sqrt{s} = 8 TeV}")
    canvasAcc_x_Eff.Update()
    graphAcc_x_Eff.SetName("accXeff_" + histoname + "_" + njets_name)
    outputfile = ROOT.TFile("/data/etp3/jwittkow/figures_acc/acceptance_efficiency.root", "update")
    graphAcc_x_Eff.Write()
    outputfile.Close()   
    canvasAcc_x_Eff.SaveAs("/data/etp3/jwittkow/figures_acc/accXeff_" + histoname + "_" + njets_name + "_29_10_14.eps")    
    #canvasAcc_x_Eff.SaveAs("/data/etp3/jwittkow/figures_acc/accXeff_" + histoname + "_" + njets_name + "_29_10_14.root")    
    graphAcc_x_Eff.GetYaxis().SetTitle("#tilde{#chi}_{1}^{0}")
    graphAcc_x_Eff.GetXaxis().SetTitle("#tilde{#chi}_{1}^{#pm}/#tilde{#chi}_{2}^{0}")
    graphAcc_x_Eff.GetXaxis().SetTitleOffset(1.2);
    graphAcc_x_Eff.GetYaxis().SetTitleOffset(1.3);
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#make TCanvas, draw TGraph2D:  
canvasProduced = ROOT.TCanvas("Produced","Produced", 600, 600)

ROOT.gStyle.SetPalette(1); 
graphProduced.SetTitle("Number of Generated Events [k]   ")
graphProduced.GetYaxis().SetTitle("#tilde{#chi}_{1}^{0}")
graphProduced.GetXaxis().SetTitle("#tilde{#chi}_{1}^{#pm}/#tilde{#chi}_{2}^{0}")  
graphProduced.Draw("COLZ")

canvasProduced.SetRightMargin(0.15)
graphProduced.GetYaxis().SetTitleOffset(1.2);

#write text for each grid point:
for r in range(0, len(rootfiles_TruthSignal)):
  if r == 0:
    print "txt_array_produced[", i_produced, "]", txt_array_produced[i_produced]
  xcoord, ycoord, xsec = getGridCoordinates(mcid_of_grid_point[r])
  text_produced.append(ROOT.TText(xcoord, ycoord, txt_array_produced[i_produced]))
  text_produced[i_produced].SetTextSize(0.03);
  text_produced[i_produced].Draw("same")
  i_produced += 1
  #end loop over grid points
  
graphProduced.GetYaxis().SetTitle("#tilde{#chi}_{1}^{0}")
graphProduced.GetXaxis().SetTitle("#tilde{#chi}_{1}^{#pm}/#tilde{#chi}_{2}^{0}")  
graphProduced.GetXaxis().SetTitleOffset(1.2);
graphProduced.GetYaxis().SetTitleOffset(1.3);
graphProduced.GetXaxis().SetLimits(125, 350)
graphProduced.GetYaxis().SetLimits(0, 90)
l.DrawLatex(0.26, 0.85, "ATLAS #bf{#it{Internal}}")
#l.DrawLatex(0.7, 0.85, "#it{#scale[0.6]{#int} L dt = 20.3 fb^{-1}}")
#l.DrawLatex(0.7, 0.75, "#it{#sqrt{s} = 8 TeV}")
canvasProduced.Update()
graphProduced.SetName("producedEvents")
outputfile = ROOT.TFile("/data/etp3/jwittkow/figures_acc/acceptance_efficiency.root", "update")
graphProduced.Write()
outputfile.Close()   
canvasProduced.SaveAs("/data/etp3/jwittkow/figures_acc/producedEvents_29_10_14.eps")    
#canvasProduced.SaveAs("/data/etp3/jwittkow/figures_acc/producedEvents_29_10_14.root")    
graphProduced.GetYaxis().SetTitle("#tilde{#chi}_{1}^{0}")
graphProduced.GetXaxis().SetTitle("#tilde{#chi}_{1}^{#pm}/#tilde{#chi}_{2}^{0}")
graphProduced.GetXaxis().SetTitleOffset(1.2);
graphProduced.GetYaxis().SetTitleOffset(1.3);

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#make TCanvas, draw TGraph2D:  
canvasXsec = ROOT.TCanvas("Xsec","Xsec", 600, 600)

ROOT.gStyle.SetPalette(1); 
graphXsec.SetTitle("#sigma [pb]   ")
graphXsec.GetYaxis().SetTitle("#tilde{#chi}_{1}^{0}")
graphXsec.GetXaxis().SetTitle("#tilde{#chi}_{1}^{#pm}/#tilde{#chi}_{2}^{0}")  
graphXsec.Draw("COLZ")

canvasXsec.SetRightMargin(0.15)
graphXsec.GetYaxis().SetTitleOffset(1.2);

#write text for each grid point:
for r in range(0, len(rootfiles_TruthSignal)):
  if r == 0:
    print "txt_array_xsec[", i_xsec, "]", txt_array_xsec[i_xsec]
  xcoord, ycoord, xsec = getGridCoordinates(mcid_of_grid_point[r])
  text_xsec.append(ROOT.TText(xcoord, ycoord, txt_array_xsec[i_xsec]))
  text_xsec[i_xsec].SetTextSize(0.03);
  text_xsec[i_xsec].Draw("same")
  i_xsec += 1
  #end loop over grid points
  
graphXsec.GetYaxis().SetTitle("#tilde{#chi}_{1}^{0}")
graphXsec.GetXaxis().SetTitle("#tilde{#chi}_{1}^{#pm}/#tilde{#chi}_{2}^{0}")  
graphXsec.GetXaxis().SetTitleOffset(1.2);
graphXsec.GetYaxis().SetTitleOffset(1.3);
graphXsec.GetXaxis().SetLimits(125, 350)
graphXsec.GetYaxis().SetLimits(0, 90)
l.DrawLatex(0.26, 0.85, "ATLAS #bf{#it{Internal}}")
#l.DrawLatex(0.7, 0.85, "#it{#scale[0.6]{#int} L dt = 20.3 fb^{-1}}")
#l.DrawLatex(0.7, 0.75, "#it{#sqrt{s} = 8 TeV}")
canvasXsec.Update()
graphXsec.GetXaxis().SetLimits(125, 350)
graphXsec.GetYaxis().SetLimits(0, 90)
graphXsec.SetName("Xsec")
outputfile = ROOT.TFile("/data/etp3/jwittkow/figures_acc/acceptance_efficiency.root", "update")
graphXsec.Write()
outputfile.Close()   
canvasXsec.SaveAs("/data/etp3/jwittkow/figures_acc/Xsec_29_10_14.eps")    
#canvasXsec.SaveAs("/data/etp3/jwittkow/figures_acc/Xsec_29_10_14.root")    
graphXsec.GetYaxis().SetTitle("#tilde{#chi}_{1}^{0}")
graphXsec.GetXaxis().SetTitle("#tilde{#chi}_{1}^{#pm}/#tilde{#chi}_{2}^{0}")
graphXsec.GetXaxis().SetTitleOffset(1.2);
graphXsec.GetYaxis().SetTitleOffset(1.3);

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#make TCanvas, draw TGraph2D:  
canvasXsec_x_BR = ROOT.TCanvas("Xsec_x_BR","Xsec_x_BR", 600, 600)

ROOT.gStyle.SetPalette(1); 
graphXsec_x_BR.SetTitle("#sigma #times BR [pb]   ")
graphXsec_x_BR.GetYaxis().SetTitle("#tilde{#chi}_{1}^{0}")
graphXsec_x_BR.GetXaxis().SetTitle("#tilde{#chi}_{1}^{#pm}/#tilde{#chi}_{2}^{0}")  
graphXsec_x_BR.Draw("COLZ")

canvasXsec_x_BR.SetRightMargin(0.15)
graphXsec_x_BR.GetYaxis().SetTitleOffset(1.2);

#write text for each grid point:
for r in range(0, len(rootfiles_TruthSignal)):
  if r == 0:
    print "txt_array_xsec_x_BR[", i_xsec_x_BR, "]", txt_array_xsec_x_BR[i_xsec_x_BR]
  xcoord, ycoord, xsec = getGridCoordinates(mcid_of_grid_point[r])
  text_xsec_x_BR.append(ROOT.TText(xcoord, ycoord, txt_array_xsec_x_BR[i_xsec_x_BR]))
  text_xsec_x_BR[i_xsec_x_BR].SetTextSize(0.03);
  text_xsec_x_BR[i_xsec_x_BR].Draw("same")
  i_xsec_x_BR += 1
  #end loop over grid points
  
graphXsec_x_BR.GetYaxis().SetTitle("#tilde{#chi}_{1}^{0}")
graphXsec_x_BR.GetXaxis().SetTitle("#tilde{#chi}_{1}^{#pm}/#tilde{#chi}_{2}^{0}")  
graphXsec_x_BR.GetXaxis().SetTitleOffset(1.2);
graphXsec_x_BR.GetYaxis().SetTitleOffset(1.3);
graphXsec_x_BR.GetXaxis().SetLimits(125, 350)
graphXsec_x_BR.GetYaxis().SetLimits(0, 90)
l.DrawLatex(0.26, 0.85, "ATLAS #bf{#it{Internal}}")
#l.DrawLatex(0.7, 0.85, "#it{#scale[0.6]{#int} L dt = 20.3 fb^{-1}}")
#l.DrawLatex(0.7, 0.75, "#it{#sqrt{s} = 8 TeV}")
canvasXsec_x_BR.Update()
graphXsec_x_BR.GetXaxis().SetLimits(125, 350)
graphXsec_x_BR.GetYaxis().SetLimits(0, 90)
graphXsec_x_BR.SetName("Xsec_x_BR")
outputfile = ROOT.TFile("/data/etp3/jwittkow/figures_acc/acceptance_efficiency.root", "update")
graphXsec_x_BR.Write()
outputfile.Close()   
canvasXsec_x_BR.SaveAs("/data/etp3/jwittkow/figures_acc/Xsec_x_BR_29_10_14.eps")    
#canvasXsec_x_BR.SaveAs("/data/etp3/jwittkow/figures_acc/Xsec_x_BR_29_10_14.root")    
graphXsec_x_BR.GetYaxis().SetTitle("#tilde{#chi}_{1}^{0}")
graphXsec_x_BR.GetXaxis().SetTitle("#tilde{#chi}_{1}^{#pm}/#tilde{#chi}_{2}^{0}")
graphXsec_x_BR.GetXaxis().SetTitleOffset(1.2);
graphXsec_x_BR.GetYaxis().SetTitleOffset(1.3);
    
    
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#for rf in rootfiles_bg:
  #rf.Close()
for rf in rootfiles_TruthSignal:
  rf.Close()
print "FINISHED"
#sys.exit(0)