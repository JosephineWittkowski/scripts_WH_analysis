#!/usr/bin/env python
import ROOT
#import "RooStats/NumberCountingUtils.h"

ROOT.gROOT.ProcessLine("gROOT->SetBatch()")

name_of_bg_file = [
		    "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_ZPlusJets_mt2J.root", 
		    "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_ttbarWtop_mt2J.root",
		    "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_WZ_mt2J.root",  
		    "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_ZZ_mt2J.root",  
		    "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_WW_mt2J.root", 
		    "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_WWPlusJets_mt2J.root", 
		    "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_Higgs_mt2J.root",
		    "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_fakebg_mt2J.root"
		    ]
		
name_of_signal_file = [
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177501_mt2J.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177502_mt2J.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177503_mt2J.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177504_mt2J.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177505_mt2J.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177506_mt2J.root", 
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177507_mt2J.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177508_mt2J.root", 
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177509_mt2J.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177510_mt2J.root", 
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177511_mt2J.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177512_mt2J.root", 
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177513_mt2J.root", 
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177514_mt2J.root", 
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177515_mt2J.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177516_mt2J.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177517_mt2J.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177518_mt2J.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177519_mt2J.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177520_mt2J.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177521_mt2J.root", 
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177522_mt2J.root", 
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177523_mt2J.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177524_mt2J.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177525_mt2J.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177526_mt2J.root",
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177527_mt2J.root"
		       ]

name_of_contributionLegend = ["Z+Jets", "ttbarW+t", "WZ", "ZZ", "WW", "WW+Jets", "Higgs", "fake"]		
fillColors = [ROOT.kOrange-2, ROOT.kRed+1, ROOT.kSpring+1, ROOT.kGreen+3, ROOT.kBlue-2, ROOT.kAzure+8, ROOT.kYellow, ROOT.kGray+1]
name_of_contribution = ["ZPlusJets", "ttbarWPlust", "WZ", "ZZ", "WW", "WWPlusJets", "Higgs", "fake"]

name_of_variables = ["ml0l", "ml1l", "mTl0l", "mTl1l", "DeltaRl0l", "DeltaRl1l", "mTlll"]


    
#name_of_variables = ["pTl0", "pTl1", "pTj0", "pTj1", "mll", "METrel", "MET", "HT", "mWWt", "mTlmin", "meff", "mt2", "mjj", "DeltaPhiMETll", "DeltaPhill", "NBJets", "NFJets", "NCJets", "DeltaPhijj", "pTjj", "ptll", "DeltaPhiMETl0", "DeltaPhiMETl1", "DeltaPhiMETj0", "DeltaPhiMETj1", "DeltaPhiMETjj", "DeltaRjj", "etal0", "etal1", "etaj0", "etaj1", "mTl0MET", "mTl1MET", "DeltaPhilljj", "DeltaPhil0jj", "DeltaPhil1jj", "DeltaRlljj", "DeltaEtajj", "mTll", "mMETll", "DeltaYjj", "DeltaEtall"]#, "D0_recalc_l0", "D0_recalc_l1", "D0_branch_l0", "D0_branch_l1", "D0Signif_recalc_l0", "D0Signif_recalc_l1", "D0Signif_branch_l0", "D0Signif_branch_l1", "mZTT_coll", "mZTT_mmc", "ml0l", "ml1l", "mTl0l", "mTl1l", "Mljj", "mTlmax"]

x_axis_title = ["ml0l", "ml1l", "mTl0l", "mTl1l", "DeltaRl0l", "DeltaRl1l", "mTlll"]
#x_axis_title = ["p_{Tl0}","p_{Tl1}","p_{Tj0}","p_{Tj1}", "m_{ll}", "E_{T}^{miss, rel}", "E_{T}^{miss}", "H_{T}", "m_{TWW}", "min(m_{T}(l0, l1))", "m_{eff}", "m_{T2}", "m_{jj}", "#Delta#Phi(E_{T}^{miss}, ll)", "#Delta#Phi(l0,l1)", "NBJets", "NFJets", "NCJets", "#Delta#Phi(j0, j1)", "p_{T,jj}", "p_{T,ll}", "#Delta#Phi(E_{T}^{miss},l0)", "#Delta#Phi(E_{T}^{miss},l1)", "#Delta#Phi(E_{T}^{miss},j0)", "#Delta#Phi(E_{T}^{miss},j1)", "#Delta#Phi(E_{T}^{miss},jj)", "#DeltaR(j,j)", "#eta_{l0}", "#eta_{l1}", "#eta_{j0}", "#eta_{j1}", "m_{T}(l0, E_{T}^{miss})", "m_{T}(l1, E_{T}^{miss})", "#Delta#Phi(ll,jj)", "#Delta#Phi(l0,jj)", "#Delta#Phi(l1,jj)", "#DeltaR(ll,jj)", "#Delta#ta(j,j)", "m_{T,ll}", "m_{E_{T}^{miss},ll}", "#DeltaY(j,j)", "#Delta#eta(l0,l1)"]#,"d0 recalc l0", "d0 recalc l1", "d0 branch l0", "d0 branch l1", "d0/#sigmad0 recalc l0", "d0/#sigmad0 recalc l1", "d0/#sigmad0 branch l0", "d0/#sigmad0 branch l1", "m_{Z->#tau#tau} (coll)","m_{Z->#tau#tau} (mmc)", "m_{l0l}", "m_{l1l}", "m_{Tl0l}", "m_{Tl1l}", "M_{ljj}", "max(m_{T}(l0, l1))"]

name_of_SR = ["MM_SRSS1", "EE_SRSS1", "EM_SRSS1"]#, "EE_SRSS2"]#, "MM_SRSS1", "MM_SRSS2", "MM_SRSS3", "MM_SRSS4", "EM_SRSS1", "EM_SRSS2", "EE_SROS1", "MM_SROS1", "EM_SROS1"]

mcid_of_grid_point = ["177501","177502", "177503", "177504","177505", "177506","177507", "177508", "177509", "177510","177511", "177512", "177513", "177514","177515","177516", "177517","177518","177519","177520", "177521", "177522", "177523", "177524", "177525", "177526", "177527"]






rootfiles_bg = []
rootfiles_gridpoints = []

for f in name_of_bg_file:
  rootfiles_bg.append(ROOT.TFile(f))
for f in name_of_signal_file:
  rootfiles_gridpoints.append(ROOT.TFile(f))

#====================================================================================================================================================================
#====================================================================================================================================================================
print_numbers_contributions = 0
if print_numbers_contributions:
  print 'bg contribution & events processed & MMSRSS1 & MMSRSS2 & MMSRSS3\\\\'
  print "\hline  "
  sum_EE = 0
  sum_MM = 0
  sum_EM = 0
  sum_total = 0
  for i_rf, rf in enumerate(rootfiles_bg):  
    bg_histo_EE = rf.Get("h_HT_MM_SRSS1")	
    bg_histo_projected_EE = bg_histo_EE.ProjectionX("h_HT_MM_SRSS1" + name_of_contribution[i_rf], 46, 46)
    nbins = bg_histo_projected_EE.GetNbinsX()
    bg_histo_MM = rf.Get("h_HT_MM_SRSS2")	
    bg_histo_projected_MM = bg_histo_MM.ProjectionX("h_HT_MM_SRSS2" + name_of_contribution[i_rf], 45, 45)
    bg_histo_EM = rf.Get("h_HT_MM_SRSS3")	
    bg_histo_projected_EM = bg_histo_EM.ProjectionX("h_HT_MM_SRSS3" + name_of_contribution[i_rf], 46, 46)
    bg_histo_total = rf.Get("cutflow_MM")	
    sum_EE = sum_EE + bg_histo_projected_EE.Integral(0, nbins + 2)
    sum_MM = sum_MM + bg_histo_projected_MM.Integral(0, nbins + 2)
    sum_EM = sum_EM + bg_histo_projected_EM.Integral(0, nbins + 2)
    sum_total = sum_total + bg_histo_total.GetBinContent( 1)
    print name_of_contributionLegend[i_rf], ": & ", round(bg_histo_total.GetBinContent( 1),2), " & ",round(bg_histo_projected_EE.Integral(0, nbins + 2),2), " & ", round(bg_histo_projected_MM.Integral(0, nbins + 2),2), " & ",round(bg_histo_projected_EM.Integral(0, nbins + 2),2), "\\\\"
  print "\hline"  
  print "\hline"  
  print "Total &  ", round(sum_total, 2), " & ", round(sum_EE,2),  " & ", round(sum_MM,2),  " & ", round(sum_EM,2),  "\\\\"

  print 'WH mass point & events processed & MMSRSS1 & MMSRSS2 & MMSRSS3\\\\'
  print "\hline  "
  for i_g, rf in enumerate(rootfiles_gridpoints):  
    bg_histo_EE = rf.Get("h_HT_MM_SRSS1")	
    bg_histo_projected_EE = bg_histo_EE.ProjectionX("h_HT_MM_SRSS1" + mcid_of_grid_point[i_g], 27, 27)
    nbins = bg_histo_projected_EE.GetNbinsX()
    bg_histo_MM = rf.Get("h_HT_MM_SRSS1")	
    bg_histo_projected_MM = bg_histo_MM.ProjectionX("h_HT_MM_SRSS1" + mcid_of_grid_point[i_g], 27, 27)
    bg_histo_EM = rf.Get("h_HT_MM_SRSS1")	
    bg_histo_projected_EM = bg_histo_EM.ProjectionX("h_HT_MM_SRSS1" + mcid_of_grid_point[i_g], 27, 27)
    bg_histo_total = rf.Get("cutflow_MM")	
    print mcid_of_grid_point[i_g], ": & ", round(bg_histo_total.GetBinContent( 1),2), " & ",round(bg_histo_projected_EE.Integral(0, nbins + 2),2), " & ", round(bg_histo_projected_MM.Integral(0, nbins + 2),2), " & ",round(bg_histo_projected_EM.Integral(0, nbins + 2),2), "\\\\"
  print "\hline"  
#====================================================================================================================================================================  
#====================================================================================================================================================================

#which bin will be used for projection:
ybinProj_EE_SRSS1 = 27
ybinProj_EE_SRSS2 = 38

ybinProj_MM_SRSS1 = 27
ybinProj_MM_SRSS2 = 45
ybinProj_MM_SRSS3 = 46
#ybinProj_MM_SRSS4 = 37

ybinProj_EM_SRSS1 = 27
ybinProj_EM_SRSS2 = 45

#ybinProj_EE_SROS1 = 51
#ybinProj_MM_SROS1 = 51
#ybinProj_EM_SROS1 = 51

ybinProj_list = [ybinProj_EE_SRSS1, ybinProj_MM_SRSS1, ybinProj_EM_SRSS1]
#ybinProj_list = [ybinProj_EE_SRSS1, ybinProj_EE_SRSS2, ybinProj_MM_SRSS1, ybinProj_MM_SRSS2, ybinProj_MM_SRSS3, ybinProj_MM_SRSS4, ybinProj_EM_SRSS1, ybinProj_EM_SRSS2, ybinProj_EE_SROS1, ybinProj_MM_SROS1, ybinProj_EM_SROS1]

#loop over variables:  
for i_v, v in enumerate(name_of_variables):
  if v == "DeltaPhiMETll" or v == "DeltaPhijj" or v == "DeltaPhiMETl0" or v == "DeltaPhiMETl1" or v == "DeltaPhiMETj0" or v == "DeltaPhiMETj1" or v == "DeltaPhiMETjj" or v == "DeltaRjj" or v == "etal0" or v == "etal1" or v == "etaj0" or v == "etaj1" or v == "DeltaPhilljj" or v == "DeltaPhil0jj" or v == "DeltaPhil1jj" or v == "DeltaRlljj" or v == "DeltaEtajj" or v == "DeltaYjj"  or v == "DeltaPhill" or v == "DeltaEtall" or v == "Mljj":
    cut_if_value_higher = True
    cut_if_value_smaller = False
  else:
    cut_if_value_higher = False
    cut_if_value_smaller = True
  #loop over signal regions:  
  for i_s, s in enumerate(name_of_SR):
    #histoname as defined in histos_ZN_tauveto.C
    histoname = "h_" + v + "_" + s
    print "histoname ", histoname
    #define stack to add all bg samples:
    stack = ROOT.THStack("stack_" + v + "_" + s, "stack_" + v + "_" + s)
    #define corresponding leg_stack
    leg_stack = ROOT.TLegend(0.7,0.55,0.85,0.89)
    leg_stack.SetFillColor(0)

    #loop over TFiles for bg contributions:
    for i_rf, rf in enumerate(rootfiles_bg):	
      #get individual histo for each bg root file:
      #print histoname
      #bg_histo = rf.Get(histoname)
      
      bg_histo = rf.Get("h_" + v +  "soft" + "_" + s)
      bg_histo_overlap = rf.Get("h_" + v +  "overlap" + "_" + s)
      bg_histo.Add(bg_histo_overlap)
      #projection of TH2F:
      bg_histo_projected = bg_histo.ProjectionX(histoname + "_1D_" + name_of_contribution[i_rf], ybinProj_list[i_s], ybinProj_list[i_s])
      
      
      #depending on bins of histo, do rebin:
      nbins = bg_histo.GetNbinsX()
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
	binning = 25
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
      
      bg_histo_projected.SetMarkerStyle(21)
      bg_histo_projected.SetMarkerColor(fillColors[i_rf])
      bg_histo_projected.SetFillStyle(1001) 
      bg_histo_projected.SetFillColor(fillColors[i_rf])
      
      leg_stack.AddEntry(bg_histo_projected,name_of_contributionLegend[i_rf],"F")
      #add projection of bg histo to stack for lower plot:
      stack.Add(bg_histo_projected)
      
      #if it is the first bg histo, define individual h_sum_bg for every signal grid point i_g:
      if i_rf == 0:
	h_sum_bg = ROOT.TH1D(histoname+ "_sumbg", histoname + "_sumbg", nbins, first_bin, last_bin)
	h_sum_bg.Rebin(nbins/binning)	  
      #add projection of bg histo to h_sum_bg for upper plot:
      h_sum_bg.Add(bg_histo_projected)
      ##end of loop over rootfiles_bg   
      #draw stack if it the last bg contribution:
      #if i_rf == 7:
	#print "bin content ", h_sum_bg.GetBinContent(10)
    #loop over signal grid point root files:
    for i_g, grid_point_file in enumerate(rootfiles_gridpoints):
      #for merged signal grid point: just draw histogram:	
      
      grid_point_file_histo = grid_point_file.Get("h_" + v +  "soft" + "_" + s)
      grid_point_file_histo_overlap = grid_point_file.Get("h_" + v +  "overlap" + "_" + s)
      grid_point_file_histo.Add(grid_point_file_histo_overlap)
      
      grid_point_file_histo.Print()
      grid_point_file_histo_projected = grid_point_file_histo.ProjectionX(histoname + "_1D_signal_" + name_of_contribution[i_rf], ybinProj_list[i_s], ybinProj_list[i_s])
      #make sure to use the same binning:
      grid_point_file_histo_projected.Rebin(nbins/binning)
      
      #find a factor for scaling signal to make it visible:
      signal_max = grid_point_file_histo_projected.GetMaximum()
      if signal_max == 0:
	scale_for_signal = 0
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
      print "bin content ", grid_point_file_histo_projected.GetBinContent(10)
      
      #define TCanvas and TPads:
      c1 = ROOT.TCanvas("c_" + v + "_" + s + "_" + str(i_g), "c_" + v + "_" + s + "_" + str(i_g), 600, 600)
      c1.SetLogy()
      pad1 = ROOT.TPad("pad1","pad1", 0.0, 0.0, 1.0, 0.85, 0, 0, 0)
      pad1.Draw()
      pad1.SetLogy(1)
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
      stack.GetYaxis().SetTitle("Events / " + str((last_bin+0.0)/(binning+0.0)) + " units ")    
      stack.GetYaxis().SetTitleOffset(2.5)
      stack.GetXaxis().SetTitle(x_axis_title[i_v]) 
      ROOT.gStyle.SetTitleFontSize(0.5)
      stack.SetTitle(s + " bin " + str(ybinProj_list[i_s]) + " mcid " + mcid_of_grid_point[i_g] + " scaled by " + str(scale))
      
      #draw signal in same TPad as stack:
      grid_point_file_histo_projected.SetLineColor(ROOT.kPink-2)
      grid_point_file_histo_projected.SetMarkerColor(ROOT.kPink-2)
      grid_point_file_histo_projected.SetMarkerSize(0.5)
      grid_point_file_histo_projected.SetLineWidth(2)
      grid_point_file_histo_projected.SetMarkerStyle(20)
      
      grid_point_file_histo_projected.Draw("p same")
      if (i_g == 0):
	leg_stack.AddEntry(grid_point_file_histo_projected,"signal")
      #draw legend     
      #leg_stack.SetHeader(s)
      leg_stack.SetTextSize(0.025)
      leg_stack.Draw("same")
      #leg_stack.GetListOfPrimitives().Remove(grid_point_file_histo_projected)
      pad1.cd().Update()
      #c1.SaveAs("/data/etp/jwittkowski/pics/cumulative_pdf_" + v + "_" + s + "_" + mcid_of_grid_point[i_g] + "_bin" + str(ybinProj_list[i_s]) + "_test.pdf")
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
	#grid_point_file_histo = grid_point_file.Get(histoname)

	
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
      c1.SaveAs("/data/etp/jwittkowski/pics/cumulative_pdf_" + v + "added_" + s + "_" + mcid_of_grid_point[i_g] + "_bin" + str(ybinProj_list[i_s]) + "_mt2J.pdf")
      #end loop over mass points
  #end loop over signal regions
#end loop over variables
for rf in rootfiles_bg:
  rf.Close()
print "FINISHED"