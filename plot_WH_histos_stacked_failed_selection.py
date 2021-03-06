#!/usr/bin/env python
import ROOT
#import "RooStats/NumberCountingUtils.h"

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

file_cutflow_126893 = "/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_cutflow_126893_TSelector.root"
		
name_of_signal_file = [
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_177501_bgTable.root"
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_WH_177502_bgTable.root",
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_WH_177503_bgTable.root",
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_WH_177504_bgTable.root",
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_WH_177505_bgTable.root",
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_WH_177506_bgTable.root", 
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_WH_177507_bgTable.root",
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_WH_177508_bgTable.root", 
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_WH_177509_bgTable.root",
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_WH_177510_bgTable.root", 
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_WH_177511_bgTable.root",
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_WH_177512_bgTable.root", 
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_WH_177513_bgTable.root", 
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_WH_177514_bgTable.root", 
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_WH_177515_bgTable.root",
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_WH_177516_bgTable.root",
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_WH_177517_bgTable.root",
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_WH_177518_bgTable.root",
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_WH_177519_bgTable.root"
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_WH_177520_bgTable.root",
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_WH_177521_bgTable.root", 
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_WH_177522_bgTable.root", 
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_WH_177523_bgTable.root",
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_WH_177524_bgTable.root",
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_WH_177525_bgTable.root",
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_WH_177526_bgTable.root",
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_WH_177527_bgTable.root"
		       ]

name_of_contributionLegend = ["Z+Jets", "ttbarW+t", "WZ", "ZZ", "WW", "WW+Jets", "Higgs", "fake", "126893"]		
fillColors = [ROOT.kOrange-2, ROOT.kRed+1, ROOT.kSpring+1, ROOT.kGreen+3, ROOT.kBlue-2, ROOT.kAzure+8, ROOT.kYellow, ROOT.kGray+1]
name_of_contribution = ["ZPlusJets", "ttbarWPlust", "WZ", "ZZ", "WW", "WWPlusJets", "Higgs", "fake"]

name_of_variables = ["failedSignalCriteria"]#"mT2J","pTl0", "pTl1", "HT", "mll", "METrel", "mWWt", "mljj",  "mTlmax", "mTlmin", "DeltaEtall", "mlj"
#]


    
#name_of_variables = ["pTl0", "pTl1", "pTj0", "pTj1", "mll", "METrel", "MET", "HT", "mWWt", "mTlmin", "meff", "mt2", "mjj", "DeltaPhiMETll", "DeltaPhill", "NBJets", "NFJets", "NCJets", "DeltaPhijj", "pTjj", "ptll", "DeltaPhiMETl0", "DeltaPhiMETl1", "DeltaPhiMETj0", "DeltaPhiMETj1", "DeltaPhiMETjj", "DeltaRjj", "etal0", "etal1", "etaj0", "etaj1", "mTl0MET", "mTl1MET", "DeltaPhilljj", "DeltaPhil0jj", "DeltaPhil1jj", "DeltaRlljj", "DeltaEtajj", "mTll", "mMETll", "DeltaYjj", "DeltaEtall"]#, "D0_recalc_l0", "D0_recalc_l1", "D0_branch_l0", "D0_branch_l1", "D0Signif_recalc_l0", "D0Signif_recalc_l1", "D0Signif_branch_l0", "D0Signif_branch_l1", "mZTT_coll", "mZTT_mmc", "Mljj", "mTlmax", "ml0lsoft", "ml1lsoft", "mTl0lsoft", "mTl1lsoft", "DeltaRl0lsoft", "DeltaRl1lsoft", "mTlllsoft", "ml0loverlap", "ml1loverlap", "mTl0loverlap", "mTl1loverlap", "DeltaRl0loverlap", "DeltaRl1loverlap", "mTllloverlap", "ml0llost", "ml1llost", "mTl0llost", "mTl1llost", "DeltaRl0llost", "DeltaRl1llost", "mTllllost"]

x_axis_title = ["h_failedSignalCriteria"]#["mT2J", "pTl0", "pTl1", "HT", "mll", "METrel", "mWWt", "mljj", "mTlmax", "mTlmin", "DeltaEtall", "mlj"
  
#]
#x_axis_title = ["p_{Tl0}","p_{Tl1}","p_{Tj0}","p_{Tj1}", "m_{ll}", "E_{T}^{miss, rel}", "E_{T}^{miss}", "H_{T}", "m_{TWW}", "min(m_{T}(l0, l1))", "m_{eff}", "m_{T2}", "m_{jj}", "#Delta#Phi(E_{T}^{miss}, ll)", "#Delta#Phi(l0,l1)", "NBJets", "NFJets", "NCJets", "#Delta#Phi(j0, j1)", "p_{T,jj}", "p_{T,ll}", "#Delta#Phi(E_{T}^{miss},l0)", "#Delta#Phi(E_{T}^{miss},l1)", "#Delta#Phi(E_{T}^{miss},j0)", "#Delta#Phi(E_{T}^{miss},j1)", "#Delta#Phi(E_{T}^{miss},jj)", "#DeltaR(j,j)", "#eta_{l0}", "#eta_{l1}", "#eta_{j0}", "#eta_{j1}", "m_{T}(l0, E_{T}^{miss})", "m_{T}(l1, E_{T}^{miss})", "#Delta#Phi(ll,jj)", "#Delta#Phi(l0,jj)", "#Delta#Phi(l1,jj)", "#DeltaR(ll,jj)", "#Delta#eta(j,j)", "m_{T,ll}", "m_{E_{T}^{miss},ll}", "#DeltaY(j,j)", "#Delta#eta(l0,l1)"]#,"d0 recalc l0", "d0 recalc l1", "d0 branch l0", "d0 branch l1", "d0/#sigmad0 recalc l0", "d0/#sigmad0 recalc l1", "d0/#sigmad0 branch l0", "d0/#sigmad0 branch l1", "m_{Z->#tau#tau} (coll)","m_{Z->#tau#tau} (mmc)", "M_{ljj}", "max(m_{T}(l0, l1))"]

name_of_SR = ["el_EM"]#, "EE_SRSS2"]#, "MM_SRSS1", "MM_SRSS2", "MM_SRSS3", "MM_SRSS4", "EM_SRSS1", "EM_SRSS2", "EE_SROS1", "MM_SROS1", "EM_SROS1"]

#which bin will be used for projection:
ybinProj = 22

mcid_of_grid_point = ["177501", "177508", "177516", "177519"]
#mcid_of_grid_point = ["177501","177502", "177503", "177504","177505", "177506","177507", "177508", "177509", "177510","177511", "177512", "177513", "177514","177515","177516", "177517","177518","177519","177520", "177521", "177522", "177523", "177524", "177525", "177526", "177527"]






rootfiles_bg = []
rootfiles_gridpoints = []

for f in name_of_bg_file:
  rootfiles_bg.append(ROOT.TFile(f))
for f in name_of_signal_file:
  rootfiles_gridpoints.append(ROOT.TFile(f))

#====================================================================================================================================================================
#====================================================================================================================================================================
print_numbers_contributions = 1
if print_numbers_contributions:
  print '\\begin{tabular}{ l | c c | c c | c c}'
 
  #print "&  ee 1j  & &  $\\mu\\mu$ 1j & &   e$\\mu$ 1j & \\\\"
  #print "&  ee 2,3j  & &  $\\mu\\mu$ 2,3j & &   e$\\mu$ 2,3j & \\\\"
  #print "bg contribution  & before & after & before & after & before & after \\\\"
  
  print" bg contribution & 2 SS leptons & after 3rd lepton veto & 2 SS leptons & after 3rd lepton veto & 2 SS leptons & after 3rd lepton veto \\\\"

  print "\\hline  "
  sum_before_EE = 0
  sum_before_MM = 0
  sum_before_EM = 0
  sum_before_EE_err = 0
  sum_before_MM_err = 0
  sum_before_EM_err = 0
  sum_after_EE = 0
  sum_after_MM = 0
  sum_after_EM = 0
  sum_after_EE_err = 0
  sum_after_MM_err = 0
  sum_after_EM_err = 0
  #sum_total = 0
  rootfiles_cutflow = rootfiles_bg
  rootfiles_cutflow.append(ROOT.TFile(file_cutflow_126893))
  for i_rf, rf in enumerate(rootfiles_cutflow):  
    bg_histo_EE = rf.Get("cutflow_EE_ALL")	
    bg_histo_projected_EE = bg_histo_EE#.ProjectionX("cutflow_EE" + name_of_contribution[i_rf], 7, 7)
    nbins = bg_histo_projected_EE.GetNbinsX()
    bg_histo_MM = rf.Get("cutflow_MM_ALL")	
    bg_histo_projected_MM = bg_histo_MM#.ProjectionX("cutflow_MM" + name_of_contribution[i_rf], 2, 2)
    bg_histo_EM = rf.Get("cutflow_EM_ALL")	
    bg_histo_projected_EM = bg_histo_EM#.ProjectionX("cutflow_EM_ALL" + name_of_contribution[i_rf], 2, 2)
    #bg_histo_total = rf.Get("cutflow_MM_ALL")	
    if name_of_contributionLegend[i_rf]!= "126893":
      sum_before_EE = sum_before_EE + bg_histo_projected_EE.GetBinContent(22)
      sum_before_MM = sum_before_MM + bg_histo_projected_MM.GetBinContent(22)
      sum_before_EM = sum_before_EM + bg_histo_projected_EM.GetBinContent(22)
      sum_before_EE_err = sum_before_EE_err + pow(bg_histo_projected_EE.GetBinError(22),2)
      sum_before_MM_err = sum_before_MM_err + pow(bg_histo_projected_MM.GetBinError(22),2)
      sum_before_EM_err = sum_before_EM_err + pow(bg_histo_projected_EM.GetBinError(22),2)
      sum_after_EE = sum_after_EE + bg_histo_projected_EE.GetBinContent(23)
      sum_after_MM = sum_after_MM + bg_histo_projected_MM.GetBinContent(23)
      sum_after_EM = sum_after_EM + bg_histo_projected_EM.GetBinContent(23)
      sum_after_EE_err = sum_after_EE_err + pow(bg_histo_projected_EE.GetBinError(23),2)
      sum_after_MM_err = sum_after_MM_err + pow(bg_histo_projected_MM.GetBinError(23),2)
      sum_after_EM_err = sum_after_EM_err + pow(bg_histo_projected_EM.GetBinError(23),2)
    #sum_total = sum_total + bg_histo_total.GetBinContent( 1)
    before_EE = bg_histo_projected_EE.GetBinContent(22)
    before_MM = bg_histo_projected_MM.GetBinContent(22)
    before_EM = bg_histo_projected_EM.GetBinContent(22)
    after_EE = bg_histo_projected_EE.GetBinContent(23)
    after_MM = bg_histo_projected_MM.GetBinContent(23)
    after_EM = bg_histo_projected_EM.GetBinContent(23)
    before_EE_err = bg_histo_projected_EE.GetBinError(22)
    before_MM_err = bg_histo_projected_MM.GetBinError(22)
    before_EM_err = bg_histo_projected_EM.GetBinError(22)
    after_EE_err = bg_histo_projected_EE.GetBinError(23)
    after_MM_err = bg_histo_projected_MM.GetBinError(23)
    after_EM_err = bg_histo_projected_EM.GetBinError(23)
    percentage_EE = 0.00
    if after_EE > 0:
      percentage_EE = (1-(after_EE/before_EE))*100
    percentage_MM = 0.00
    if after_MM > 0:
      percentage_MM = (1-(after_MM/before_MM))*100
    #print "percentage_MM= ", percentage_MM  
    percentage_EM = 0.00
    if after_EM > 0:
      percentage_EM = (1-(after_EM/before_EM))*100
    
    if name_of_contributionLegend[i_rf]!= "126893":
      print ' ', name_of_contributionLegend[i_rf], ": &  ",round(before_EE,2), "$\pm$", round(before_EE_err,2), " &  ",round(after_EE, 2), "$\pm$", round(after_EE_err,2), "(", round(percentage_EE, 2), "\%) & ",round(before_MM,2), "$\pm$", round(before_MM_err,2), " &  ",round(after_MM, 2), "$\pm$", round(after_MM_err,2), "(", round(percentage_MM, 2), "\%) & ",round(before_EM,2), "$\pm$", round(before_EM_err,2), " &  ",round(after_EM, 2), "$\pm$", round(after_EM_err,2), "(", round(percentage_EM, 2), "\%) \\\\"
  print "\\hline"  
  print "\\hline"  
  percentage_EE_total = 0.00
  if after_EE > 0:
    percentage_EE_total = (1-(sum_after_EE/sum_before_EE))*100 
  if after_MM > 0:
    percentage_MM_total = (1-(sum_after_MM/sum_before_MM))*100 
  if after_EM > 0:
    percentage_EM_total = (1-(sum_after_EM/sum_before_EM))*100     
  print " Total &  ", round(sum_before_EE,2), "$\pm$", round(sum_before_EE_err**0.5,2), " & ", round(sum_after_EE,2), "$\pm$", round(sum_after_EE_err**0.5,2), "(", round(percentage_EE_total, 2), "\%) & ", round(sum_before_MM,2), "$\pm$", round(sum_before_MM_err**0.5,2), " & ", round(sum_after_MM,2), "$\pm$", round(sum_after_MM_err**0.5,2), "(", round(percentage_MM_total, 2), "\%) & ", round(sum_before_EM,2), "$\pm$", round(sum_before_EM_err**0.5,2), " & ", round(sum_after_EM,2), "$\pm$", round(sum_after_EM_err**0.5,2), "(", round(percentage_EM_total, 2), "\%) \\\\ "

  #print ' signal &  EE 1j &  MM 1j &  EM 1j &  EE 2j &  MM 2j &  EM 2j\\\\'
  print "\\hline  "
  for i_g, rf in enumerate(rootfiles_gridpoints):  
    bg_histo_EE = rf.Get("cutflow_EE_ALL")	
    bg_histo_projected_EE = bg_histo_EE#.ProjectionX("h_HT_2j_EE" + mcid_of_grid_point[i_g], 7, 7)
    nbins = bg_histo_projected_EE.GetNbinsX()
    bg_histo_MM = rf.Get("cutflow_MM_ALL")	
    bg_histo_projected_MM = bg_histo_MM#.ProjectionX("h_HT_MM_SRSS1" + mcid_of_grid_point[i_g], 6, 6)
    bg_histo_EM = rf.Get("cutflow_EM_ALL")	
    bg_histo_projected_EM = bg_histo_EM#.ProjectionX("h_HT_EM_SRSS1" + mcid_of_grid_point[i_g], 30, 30)
    before_EE = bg_histo_projected_EE.GetBinContent(22)
    before_MM = bg_histo_projected_MM.GetBinContent(22)
    before_EM = bg_histo_projected_EM.GetBinContent(22)
    after_EE = bg_histo_projected_EE.GetBinContent(23)
    after_MM = bg_histo_projected_MM.GetBinContent(23)
    after_EM = bg_histo_projected_EM.GetBinContent(23)
    before_EE_err = bg_histo_projected_EE.GetBinError(22)
    before_MM_err = bg_histo_projected_MM.GetBinError(22)
    before_EM_err = bg_histo_projected_EM.GetBinError(22)
    after_EE_err = bg_histo_projected_EE.GetBinError(23)
    after_MM_err = bg_histo_projected_MM.GetBinError(23)
    after_EM_err = bg_histo_projected_EM.GetBinError(23)
    percentage_EE = 0.00
    if after_EE > 0:
      percentage_EE = (1-(after_EE/before_EE))*100
    percentage_MM = 0.00
    if after_MM > 0:
      percentage_MM = (1-(after_MM/before_MM))*100
    #print "percentage_MM= ", percentage_MM  
    percentage_EM = 0.00
    if after_EM > 0:
      percentage_EM = (1-(after_EM/before_EM))*100
    print " signal: &  ",round(before_EE,2), "$\pm$", round(before_EE_err,2), " &  ",round(after_EE, 2), "$\pm$", round(after_EE_err,2), "(", round(percentage_EE, 2), "\%) & ",round(before_MM,2), "$\pm$", round(before_MM_err,2), " &  ",round(after_MM, 2), "$\pm$", round(after_MM_err,2), "(", round(percentage_MM, 2), "\%) & ",round(before_EM,2), "$\pm$", round(before_EM_err,2), " &  ",round(after_EM, 2), "$\pm$", round(after_EM_err,2), "(", round(percentage_EM, 2), "\%) \\\\"
  #rf = file_cutflow_126893
  print "\\hline"  
  print '\\end{tabular}'
  
  
   #&  ee 1j  & &  $\mu\mu$ 1j & &   e$\mu$ 1j & &  ee 2j & &  $\mu\mu$ 2j &  & e$\mu$ 2j & \\

 #bg contribution  & before & after & before & after & before & after& before & after& before & after& before & after \\
#\hline
  #Z+Jets : &   0.36  &  0.36 &   0.0  &   0.0 & 0.01  &  0.01 &   0.47 &   0.47 &   0.0  &   0.0 &   0.0  &   0.0\\
  #ttbarW+t : &   0.13  &   0.13 &  0.01   &  0.01 &   0.08  &  0.08 &   0.08 &   0.08 &   0.02 &   0.02 &   0.05 &   0.05\\
  #WZ : &   1.78 & 1.72  &   5.35  & 3.56 &   2.78   & 2.3 &   0.81  &   0.73 &   1.95  &   1.33 &   0.75 &   0.7  \\
  #ZZ : &   0.01 & 0.01 &   0.35 & 0.24 &   0.13  & 0.1 &   0.02 &   0.02  &   0.16  & 0.07 &   0.06 & 0.05\\
  #WW : &   0.2  & 0.2 &   0.05  &  0.05 &  0.16   & 0.15 &   0.07  &   0.07 &   0.03 &   0.03  &   0.05 &   0.05\\
  #WW+Jets : &   0.17  & 0.17 &   0.19  &   0.19 & 0.11  & 0.11 &   0.27 &   0.27 &   0.36  &   0.36 &   0.14 &   0.14\\
  #Higgs : &   0.0  &   0.0 &   0.13 &   0.13 &   0.07  &   0.07 &   0.04  &   0.04 &   0.04 &   0.04  &   0.02  &   0.02\\
  #fake : &   2.95 &   2.99 &   0.15  &   0.01 &   1.54  &   1.45 &   1.95 &   1.95 &   -0.03  &   -0.00 &   0.22 &   0.22\\
 
#\hline
#\hline
 #Total &   5.61  & 5.59 & 6.23  & 4.18 &  4.87  &  4.27 &   3.71 &   3.63  &  2.53 &  1.83 &  1.29 &  1.23 \\ 

#\hline  
#signal : &   2.37 & 2.37  &   4.55 & 4.43  &  4.4 &  4.39 &   2.45  &   2.45 &   3.46 &   3.41 &  3.2 &  3.2 \\
#\hline
#====================================================================================================================================================================  
#====================================================================================================================================================================




ybinProj_list = [ybinProj]
#ybinProj_list = [ybinProj_EE_SRSS1, ybinProj_EE_SRSS2, ybinProj_MM_SRSS1, ybinProj_MM_SRSS2, ybinProj_MM_SRSS3, ybinProj_MM_SRSS4, ybinProj_EM_SRSS1, ybinProj_EM_SRSS2, ybinProj_EE_SROS1, ybinProj_MM_SROS1, ybinProj_EM_SROS1]

#loop over variables:  
for i_v, v in enumerate(name_of_variables):
  if v == "DeltaPhiMETll" or v == "DeltaPhijj" or v == "DeltaPhiMETl0" or v == "DeltaPhiMETl1" or v == "DeltaPhiMETj0" or v == "DeltaPhiMETj1" or v == "DeltaPhiMETjj" or v == "DeltaRjj" or v == "etal0" or v == "etal1" or v == "etaj0" or v == "etaj1" or v == "DeltaPhilljj" or v == "DeltaPhil0jj" or v == "DeltaPhil1jj" or v == "DeltaRlljj" or v == "DeltaEtajj" or v == "DeltaYjj"  or v == "DeltaPhill" or v == "DeltaEtall" or v == "mljj" or v == "mlj":
    cut_if_value_higher = True
    cut_if_value_smaller = False
  else:
    cut_if_value_higher = False
    cut_if_value_smaller = True
  #loop over signal regions:  
  for i_s, s in enumerate(name_of_SR):
    #histoname as defined in histos_ZN_tauveto.C
    histoname = "h_" + v + "_" + s
    #histoname = "h_failedSignalCriteria_l0_EE"
    print "histoname ", histoname
    #define stack to add all bg samples:
    stack = ROOT.THStack("stack_" + v + "_" + s, "stack_" + v + "_" + s)
    #define corresponding leg_stack
    leg_stack = ROOT.TLegend(0.75,0.55,0.9,0.89)
    leg_stack.SetFillColor(0)

    #loop over TFiles for bg contributions:
    for i_rf, rf in enumerate(rootfiles_bg):	
      #get individual histo for each bg root file:
      #rf.Print()
      
      #bg_histo_1 = rf.Get("h_failedSignalCriteria_l1_EE")
      #bg_histo.Print()
      #projection of TH2F:
      #bg_histo_projected_1 = bg_histo_1.ProjectionX(histoname + "_1_1D_" + name_of_contribution[i_rf]+"_1", ybinProj_list[i_s], ybinProj_list[i_s])
      
      bg_histo = rf.Get(histoname)
      bg_histo.Print()
      #projection of TH2F:
      bg_histo_projected = bg_histo.ProjectionX(histoname + "_1D_" + name_of_contribution[i_rf], ybinProj_list[i_s], ybinProj_list[i_s])
      print "bg_histo_projected= ", bg_histo_projected.Print()
      #bg_histo_projected.Add(bg_histo_projected_1)
      #print "bg_histo_projected= ", bg_histo_projected.Print()
      
      #depending on bins of histo, do rebin:
      nbins = bg_histo.GetNbinsX()
      #print "nbins", nbins
      if "ICl" in v:
	#print "ICl0llost"
	first_bin = -0.5
	last_bin = 1.5
	binning = 2
      elif "ptcone30" in v:
	first_bin = 0
	last_bin = 1
	binning = 50	
      elif "d0Sig" in v:
	first_bin = 0
	last_bin = 10
	binning = 100
      elif "z0SinTheta" in v:
	first_bin = 0
	last_bin = 1
	binning = 50			
      elif "etcone" in v:
	first_bin = 0
	last_bin = 1
	binning = 100		
      elif "failedSignalCriteria" in v:
	first_bin = -0.5
	last_bin = 14.5
	binning = 15	
      else:
	if nbins == 2 or nbins == 11:
	  first_bin = -0.5
	else:
	  first_bin = 0.	  
	if nbins == 2:
	  last_bin = 2.5
	  binning = 2	  
	if nbins == 11:
	  last_bin = 10.5
	  binning = 11	  
	if nbins == 70:
	  last_bin = 7
	  binning = 35	  
	if nbins == 1000:
	  last_bin = 1000.
	  binning = 25	  
	if nbins == 500.:
	  last_bin = 500.
	  binning = 25	  
	if nbins == 100.:
	  last_bin = 500.
	  binning = 100
	if nbins == 200.:
	  last_bin = 10.
	  first_bin = -10.
	  binning = 200
	if nbins == 1200.:
	  last_bin = 1.5
	  first_bin = -1.5
	  binning = 120

      #do a rebinning :
      bg_histo_projected.Rebin(nbins/binning)
      #print "after rebin", bg_histo_projected.GetNbinsX()
      
      bg_histo_projected.SetMarkerStyle(21)
      bg_histo_projected.SetMarkerColor(fillColors[i_rf])
      bg_histo_projected.SetFillStyle(1001) 
      bg_histo_projected.SetFillColor(fillColors[i_rf])
      #print "item ", name_of_contribution[i_rf], round(bg_histo_projected.Integral(),1)
      
      leg_stack.AddEntry(bg_histo_projected,name_of_contributionLegend[i_rf],"F")
      #add projection of bg histo to stack for lower plot:
      stack.Add(bg_histo_projected)
      
      #if it is the first bg histo, define individual h_sum_bg for every signal grid point i_g:
      if i_rf == 0:
	#print "nbins", nbins, "first_bin", first_bin, "last_bin", last_bin
	h_sum_bg = ROOT.TH1D(histoname+ "_sumbg", histoname + "_sumbg", nbins, first_bin, last_bin)
	h_sum_bg.Rebin(nbins/binning)	  
      #add projection of bg histo to h_sum_bg for upper plot:
      #print "before"
      h_sum_bg.Add(bg_histo_projected)
      #print "after"
      ##end of loop over rootfiles_bg   
      #draw stack if it the last bg contribution:
      #if i_rf == 7:
	#print "bin content ",h_sum_bg.GetBinContent(2) +  2* h_sum_bg.GetBinContent(3)
    #loop over signal grid point root files:
    for i_g, grid_point_file in enumerate(rootfiles_gridpoints):
      #for merged signal grid point: just draw histogram:	
      print histoname
      grid_point_file_histo = grid_point_file.Get(histoname)
      #grid_point_file_histo.Print()
      grid_point_file_histo_projected = grid_point_file_histo.ProjectionX(histoname + "_1D_signal_" + name_of_contribution[i_rf], ybinProj_list[i_s], ybinProj_list[i_s])
      #make sure to use the same binning:
      grid_point_file_histo_projected.Rebin(nbins/binning)
      #print "signal masspoint ", mcid_of_grid_point[i_s]
      #print "integral", round(grid_point_file_histo_projected.Integral(),1)
      
      #find a factor for scaling signal to make it visible:
      signal_max = grid_point_file_histo_projected.GetMaximum()
      #print "signal_max", signal_max
      if signal_max == 0.0:
	scale_for_signal = 0
	scale = 0
      else:
	scale_for_signal = stack.GetMaximum()/signal_max/2
      if scale_for_signal > 100000.:
	scale = 100000
      elif scale_for_signal > 10000:
	scale = 10000
      elif scale_for_signal > 1000:
	scale = 1000
      elif scale_for_signal > 100:
	scale = 100
      elif scale_for_signal > 0:
	scale = 10
      grid_point_file_histo_projected.Scale(scale)
      
      #define TCanvas and TPads:
      c1 = ROOT.TCanvas("c_" + v + "_" + s + "_" + str(i_g), "c_" + v + "_" + s + "_" + str(i_g), 600, 600)
      pad1 = ROOT.TPad("pad1","pad1", 0.0, 0.0, 1.0, 0.85, 0, 0, 0)
      pad1.Draw()
      #if (not "mT2J" in v) and (not "Mljj" in v):
	#c1.SetLogy()
	#pad1.SetLogy(1)
      
      pad1.SetFillColor(ROOT.kWhite)

      draw_pad2 = False
      if draw_pad2:
	pad2 = ROOT.TPad("pad2","pad2", 0.0, 0.85, 1.0, 1.0, 0, 0)
	pad2.Draw()
	pad2.SetFillColor(ROOT.kWhite)
      
      #enter first TPad for stack plot:
      pad1.cd()
      pad1.SetBottomMargin(0.15)
      pad1.SetLeftMargin(0.2)
      pad1.SetRightMargin(0.05)
      pad1.SetTopMargin(0.0)  
      stack.Draw("HIST")   
      stack.GetYaxis().SetTitle("")    
      #stack.GetYaxis().SetTitleOffset(2.5)
      if not "failedSignalCriteria" in v:
	stack.GetXaxis().SetTitle(x_axis_title[i_v]) 
      stack.SetTitle("")
      #stack.SetTitle(s + " bin " + str(ybinProj_list[i_s]) + " mcid " + mcid_of_grid_point[i_g] + " scaled by " + str(scale))
      
      if "failedSignalCriteria" in v:
  	stack.GetXaxis().SetBinLabel(2,"N leptons");
	stack.GetXaxis().SetBinLabel(3,"too soft");
	stack.GetXaxis().SetBinLabel(4,"#eta too large");
	stack.GetXaxis().SetBinLabel(5,"failed pTCone30 iso");
	stack.GetXaxis().SetBinLabel(6,"failed eTCone30 iso");
	stack.GetXaxis().SetBinLabel(7,"failed d0Significance");
	stack.GetXaxis().SetBinLabel(8,"failed Z0Significance");
	stack.GetXaxis().SetBinLabel(9,"failed medium quality");
	stack.GetXaxis().SetBinLabel(10,"failed tight quality");
	stack.GetXaxis().SetBinLabel(11,"failed OR or Mll cut");
	stack.GetXaxis().SetBinLabel(12,"not Prompt");
      
      #draw signal in same TPad as stack:
      grid_point_file_histo_projected.SetLineColor(ROOT.kPink-2)
      grid_point_file_histo_projected.SetMarkerColor(ROOT.kPink-2)
      grid_point_file_histo_projected.SetMarkerSize(0.5)
      grid_point_file_histo_projected.SetLineWidth(2)
      grid_point_file_histo_projected.SetMarkerStyle(20)
      
      #grid_point_file_histo_projected.Draw("p same")
      if "ml0" in v or "ml1" in v:
	line = ROOT.TLine(91.2 ,0. , 91.2, h_sum_bg.GetMaximum())
	line.SetLineWidth(5)
	line.SetLineColor(6)
	line.Draw("same")
      #if (i_g == 0):
	#leg_stack.AddEntry(grid_point_file_histo_projected,"signal")
      #draw legend     
      #leg_stack.SetHeader(s)
      leg_stack.SetTextSize(0.025)
      leg_stack.Draw("same")
      #leg_stack.GetListOfPrimitives().Remove(grid_point_file_histo_projected)
      pad1.cd().Update()
      #c1.SaveAs("/data/etp/jwittkowskiski/pics/cumulative_pdf_" + v + "_" + s + "_" + mcid_of_grid_point[i_g] + "_bin" + str(ybinProj_list[i_s]) + "_test.pdf")
      if draw_pad2:
	#access second TPad for Z_N, cut efficiency plots:
	pad2.cd()
	pad2.SetBottomMargin(0.0)
	pad2.SetLeftMargin(0.2)
	pad2.SetRightMargin(0.05)
	
	#define histos for pad2 and do rebinning:
	h_ZN = ROOT.TH1D(histoname + "_" + mcid_of_grid_point[i_g] + "_ZN", histoname + "_" + mcid_of_grid_point[i_g] + "_ZN", nbins, first_bin, last_bin)
	h_ZN.Rebin(nbins/binning)
	h_cut_eff_bg = ROOT.TH1D(histoname + "_" + mcid_of_grid_point[i_g] + "_cut_eff_bg", histoname + "_" + mcid_of_grid_point[i_g] + "_cut_eff_bg", nbins, first_bin, last_bin)
	h_cut_eff_bg.Rebin(nbins/binning)
	h_cut_eff_signal = ROOT.TH1D(histoname + "_" + mcid_of_grid_point[i_g] + "_cut_eff_signal", histoname + "_" + mcid_of_grid_point[i_g] + "_cut_eff_signal", nbins, first_bin, last_bin)
	h_cut_eff_signal.Rebin(nbins/binning)
	grid_point_file_histo = grid_point_file.Get(histoname)
	
	#projection of signal contribution to read bin content for Z_N
	signal_histo_1D = grid_point_file.Get(histoname).ProjectionX(histoname + "_1D_signal", ybinProj_list[i_s], ybinProj_list[i_s])      
	
	signal_histo_1D.Rebin(nbins/binning)
	n_bins = h_sum_bg.GetNbinsX()

	#define ratios etc:
	Z_N_max_bin = 0
	Z_N_max = 0.
	pos_line_Z_N_max = 0.
	diff_eff_max_bin = 0
	diff_eff_max = 0.
	eff_max = 0.
	pos_line_diff_eff_max = 0.
	
	#loop over all bins in 1D-histo for particular variable:
	for it_bins in range(1, n_bins+1):
	  #get N events bg & signal:
	  if cut_if_value_higher:
	    bg_events = h_sum_bg.Integral(0, it_bins-1)    
	    signal_events = signal_histo_1D.Integral(0, it_bins-1)
	  else:
	    bg_events = h_sum_bg.Integral(it_bins, n_bins+2)   
	    signal_events = signal_histo_1D.Integral(it_bins, n_bins+2)
	    
	  #calc Z_N:
	  Z_N = ROOT.RooStats.NumberCountingUtils.BinomialExpZ(signal_events, bg_events, 0.25)
	  #set Z_N to 0 if bad return value:
	  if Z_N<0 or bg_events==0 or Z_N > 1000.:
	    Z_N = 0.
	  h_ZN.SetBinContent(it_bins, Z_N)
	  
	  #calculate max Z_N and corresponding bin:
	  if Z_N > Z_N_max:
	    Z_N_max_bin = it_bins
	    Z_N_max = Z_N
	  #print "Z_N_max= ", Z_N_max, " Z_N_max_bin= ", Z_N_max_bin
	    
	  #calculate cut efficiency bg:
	  content_below_x_bg = h_sum_bg.Integral(0, it_bins-1)
	  content_with_and_above_x_bg = h_sum_bg.Integral(it_bins, n_bins+2)
	  content_bg = h_sum_bg.Integral(0, n_bins+2)
	  cut_efficiency_bg = 0.
	  if content_bg>0:
	    if cut_if_value_higher:
	    #else you cut on values SMALLER than x
	      cut_efficiency_bg = content_below_x_bg / content_bg
	    else:
	      cut_efficiency_bg = content_with_and_above_x_bg / content_bg
	      
	  h_cut_eff_bg.SetBinContent(it_bins, cut_efficiency_bg)  
	  
	  #calculate cut efficiency signal:
	  content_below_x_s = signal_histo_1D.Integral(0, it_bins-1)
	  content_with_and_above_x_s = signal_histo_1D.Integral(it_bins, n_bins+2)
	  content_s = signal_histo_1D.Integral(0, n_bins+2)
	  cut_efficiency_s = 0.
	  if content_s>0:
	    if cut_if_value_higher:
	      cut_efficiency_s = content_below_x_s / content_s
	    else:
	      cut_efficiency_s = content_with_and_above_x_s / content_s
	  h_cut_eff_signal.SetBinContent(it_bins, cut_efficiency_s)  
	  
	  #where is the difference between the two efficiencies at maximum -> most recommended cut?:
	  diff_eff = abs(cut_efficiency_bg - cut_efficiency_s)
	  if diff_eff > diff_eff_max:
	    diff_eff_max = diff_eff
	    diff_eff_max_bin = it_bins
	  if max(cut_efficiency_bg, cut_efficiency_s) > eff_max:
	      eff_max = max(cut_efficiency_bg, cut_efficiency_s)  
	
	#end loop over bins
	
	#draw cut efficiencies signal and bg:
	h_cut_eff_signal.GetYaxis().SetTitle("significance")
	h_cut_eff_signal.GetYaxis().SetTitleOffset(0.5)
	h_cut_eff_signal.GetYaxis().SetTitleSize(0.15)
	h_cut_eff_signal.SetTitle("")
	h_cut_eff_bg.SetLineColor(1)
	h_cut_eff_bg.SetTitle("")
	h_cut_eff_signal.SetLineColor(ROOT.kRed)
	h_cut_eff_signal.Draw("l")
	ROOT.gStyle.SetOptStat(0)
	h_cut_eff_bg.Draw("lsame")
	
	#draw line for max difference in efficiencies:
	pos_line_diff_eff_max = last_bin / binning * (diff_eff_max_bin - 0.5)

	line_diff_eff = ROOT.TLine(pos_line_diff_eff_max ,0. , pos_line_diff_eff_max, eff_max)
	line_diff_eff.SetLineWidth(5)
	line_diff_eff.SetLineColor(ROOT.kBlack)
	line_diff_eff.Draw("same")
	
	#draw Z_N, cut efficiencies + legend:
	h_ZN.SetLineColor(ROOT.kBlue)
	h_ZN.SetLineStyle(2)
	h_ZN.SetTitle("")
	h_ZN.Draw("lsame")
	pos_line_Z_N_max = (last_bin+0.0) / (binning+0.0) * ((Z_N_max_bin+0.0) - 0.5)
	#print "pos_line_Z_N_max= ", pos_line_Z_N_max, "last_bin= ", last_bin, " binning= ", binning, "Z_N_max_bin= ", Z_N_max_bin

	line_Z = ROOT.TLine(pos_line_Z_N_max ,0. , pos_line_Z_N_max, Z_N_max)
	line_Z.SetLineWidth(5)
	line_Z.SetLineColor(ROOT.kBlue)
	line_Z.Draw("same")
	
	#draw legend for upper plot:
	leg_ZN = ROOT.TLegend(0.45,0.6,0.9,0.99)
	leg_ZN.SetFillColor(0)
	leg_ZN.SetHeader("Z_{N} " + str(round(Z_N_max,2)) + " at " + str(round(pos_line_Z_N_max,2)) + ", #Delta #epsilon: " + str(round(diff_eff_max,2)) + " at " + str(round(pos_line_diff_eff_max,2)) + " mcid " + str(mcid_of_grid_point[i_g]) )
	leg_ZN.SetTextSize(0.15)
	leg_ZN.Draw("same")

	pad2.cd().Update()
	#end draw_pad2      
      #c1.SaveAs("/data/etp/jwittkowski/pics_reoptimization/cumulative_pdf_" + v + "_" + s + "_" + mcid_of_grid_point[i_g] + "_bin" + str(ybinProj_list[i_s]) + ".eps")
      #c1.SaveAs("../int_note_whss/figures/background/WZ/pic_failedSignalCriteria_el_EM_WZ.eps")

      #end loop over mass points
  #end loop over signal regions
#end loop over variables
for rf in rootfiles_bg:
  rf.Close()
print "FINISHED"