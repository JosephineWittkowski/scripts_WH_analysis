#!/usr/bin/env python
import ROOT
import sys
#import "RooStats/NumberCountingUtils.h"

from gridCoord import getGridCoordinates, reqidByMc1Mn1

#ROOT.gROOT.ProcessLine("gROOT->SetBatch()")

name_of_bg_file = [
  		    "/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_ZPlusJetsNEW_bgTable.root", 
		    "/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_ttbarWtop_bgTable.root",
		    "/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_WZ_bgTable.root",
		    "/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_ZZ_bgTable.root",  
		    "/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_WW_bgTable.root", 
		    "/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_WWPlusJets_bgTable.root", 
		    "/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_Higgs_bgTable.root",
		    "/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_fake_bgTable.root"
		   ]
	

name_of_SR = ["EE_SRSS1"]#, "EE_SRSS2", "MM_SRSS1", "MM_SRSS2", "MM_SRSS3", "MM_SRSS4",2 "EM_SRSS1", "EM_SRSS2", "EE_SROS1", "MM_SROS1", "EM_SROS1"]
#name_of_SR = ["EE_SRSS1"]#, "EE_SRSS2", "MM_SRSS1", "MM_SRSS2", "MM_SRSS3", "MM_SRSS4", "EM_SRSS1", "EM_SRSS2", "EE_SROS1", "MM_SROS1", "EM_SROS1"]
mcid_of_grid_point = [177501, 177502, 177503, 177504, 177505, 177506, 177507, 177508, 177509, 177510, 177511, 177512, 177513, 177514, 177515, 177516, 177517, 177518, 177519, 177520, 177521, 177522, 177523, 177524, 177525, 177526, 177527]

#which bin will be used for projection:
ybinProj_EE_SRSS1 = 32
ybinProj_EE_SRSS2 = 31

ybinProj_MM_SRSS1 = 42
ybinProj_MM_SRSS2 = 127
ybinProj_MM_SRSS3 = 58
ybinProj_MM_SRSS4 = 58

ybinProj_EM_SRSS1 = 49
ybinProj_EM_SRSS2 = 66
ybinProj_EE_SROS1 = 51
ybinProj_MM_SROS1 = 51
ybinProj_EM_SROS1 = 51
ybinProj_list = [ybinProj_MM_SRSS1, ybinProj_MM_SRSS2, ybinProj_MM_SRSS3]
#ybinProj_list = [ybinProj_EE_SRSS1, ybinProj_EE_SRSS2, ybinProj_MM_SRSS1, ybinProj_MM_SRSS2, ybinProj_MM_SRSS3, ybinProj_MM_SRSS4, ybinProj_EM_SRSS1, ybinProj_EM_SRSS2, ybinProj_EE_SROS1, ybinProj_MM_SROS1, ybinProj_EM_SROS1]
	  
rootfiles_bg = []
rootfiles_sg = []

for f in name_of_bg_file:
  rootfiles_bg.append(ROOT.TFile(f))

name_of_signal_file = [
		      "/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_177501_bgTable.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_177502_bgTable.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_177503_bgTable.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_177504_bgTable.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_177505_bgTable.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_177506_bgTable.root", 
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_177507_bgTable.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_177508_bgTable.root", 
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_177509_bgTable.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_177510_bgTable.root", 
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_177511_bgTable.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_177512_bgTable.root", 
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_177513_bgTable.root", 
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_177514_bgTable.root", 
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_177515_bgTable.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_177516_bgTable.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_177517_bgTable.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_177518_bgTable.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_177519_bgTable.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_177520_bgTable.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_177521_bgTable.root", 
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_177522_bgTable.root", 
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_177523_bgTable.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_177524_bgTable.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_177525_bgTable.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_177526_bgTable.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_177527_bgTable.root"
		       ]
for f in name_of_signal_file:
  rootfiles_sg.append(ROOT.TFile(f))

for b in range(42, 43):  
  #loop over signal regions:
  for i_s, s in enumerate(name_of_SR):
    ybinProj_list[i_s] = b
    binX = ybinProj_list[i_s]
    print "binX= ", binX
    B = 0.
    #loop over bg rootfiles:
    for i_rf, rf in enumerate(rootfiles_bg):
      rf.Print()
      histoname = "h_mll_" + s
      bg_histo = rf.Get(histoname)
      nBinsX = bg_histo.GetNbinsX()
      print "bg_histo.Integral(0, nBinsX+2, binX, binX)= ", bg_histo.Integral(0, nBinsX+2, binX, binX)  
      B += bg_histo.Integral(0, nBinsX+2, binX, binX)
      #end loop over bg rootfiles

    #define array with entry for every grid point:  
    S = [0., 0., 0., 0. ,0. ,0. ,0. ,0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]
    Z_N = [0., 0., 0., 0. ,0. ,0. ,0. ,0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]
    N = [0., 0., 0., 0. ,0. ,0. ,0. ,0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]
    graph = ROOT.TGraph2D()
    text_array = []
    
    N_points=0
    M = 0
    text_Z_N = []
    
    #loop over grid points:
    for r in range(0, len(rootfiles_sg)):
	
      #print "mcid= ", mcid_of_grid_point[r], ", xcoord= ", xcoord, ", ycoord= ", ycoord, ", r= ", r
      sg_histo = rootfiles_sg[r].Get(histoname)
      #projection on x of bin of interest
      signal_histo_1D = sg_histo.ProjectionX(histoname + "_1D_signal", ybinProj_list[i_s], ybinProj_list[i_s])

      nBinsX = signal_histo_1D.GetNbinsX()
      
      #get N events in this bin over whole x-range:  
      S[r] = signal_histo_1D.Integral(0, nBinsX+2)

      #calc Z_N for this, for all grid points [r]:
      Z_N[r] = ROOT.RooStats.NumberCountingUtils.BinomialExpZ(S[r], B, 0.25)
      if Z_N[r]<0 or B==0 or S[r]==0:
	Z_N[r] = 0.

      #get grid coordinates for this grid point:
      xcoord, ycoord, xsec = getGridCoordinates(mcid_of_grid_point[r])
      
      graph.SetPoint(N_points, xcoord, ycoord, Z_N[r])
      N_points += 1
      
      text_array.append(str(round(Z_N[r],2)))
      print "mcid= ", mcid_of_grid_point[r], " S[r]= ", S[r], ", B= ", B, ", xcoord= ", xcoord, ", ycoord= ", ycoord, ", Z_N[r]= ", Z_N[r], ", N[r]= ", N[r]
      #end loop over grid points
      
    #make TCanvas, draw TGraph2D:  
    c1 = ROOT.TCanvas("c_"+ s,"c_"+ s, 600, 600)
    ROOT.gStyle.SetPalette(1); 
    #graph.SetTitle("Z_{N} " + s + " bin " +  str(ybinProj_list[i_s]))
    graph.SetTitle("")
    #graph.SetMaximum(3.0);
    graph.Draw("COLZ")
    graph.GetYaxis().SetTitle("#tilde{#chi}_{1}^{0}");
    graph.GetXaxis().SetTitle("#tilde{#chi}_{1}^{#pm}/#tilde{#chi}_{2}^{0}");    
    #end loop over grid points
    
    for r in range(0, len(rootfiles_sg)):
      xcoord, ycoord, xsec = getGridCoordinates(mcid_of_grid_point[r])
      text_Z_N.append(ROOT.TText(xcoord, ycoord, text_array[M]))
      text_Z_N[M].SetTextSize(0.04);
      text_Z_N[M].Draw("same")
      M += 1
    #end loop over grid points
      
    #c1.SaveAs("../pics/significance_Z_N_" + s + "_bin" + str(ybinProj_list[i_s]) + "_PRcheck.pdf")    
    #c1.SaveAs("../pics/grid_mcids_new2.pdf")  
    #c1.SaveAs("/data/etp/jwittkowski/int_note_whss/figures/signalregions/EM/EM_1j_ZN.eps")


for rf in rootfiles_bg:
  rf.Close()
for rf in rootfiles_sg:
  rf.Close()
print "FINISHED"
#sys.exit(0)