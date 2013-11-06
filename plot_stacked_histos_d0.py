#plot d0 significance and calculate cut values for 1 sigma, 2 sigma, ... for all stacked SM backgrounds (reduce fake?)

#!/usr/bin/env python
import ROOT
#import "RooStats/NumberCountingUtils.h"

#ROOT.gROOT.ProcessLine("gROOT->SetBatch()")

name_of_bg_file = [
		    "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_ZPlusJets_version16.root", 
		    "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_ttbarWtop_version16.root",
		    "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_WZ_version16.root",  
		    "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_ZZ_version16.root",  
		    "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_WW_version16.root", 
		    "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_WWPlusJets_version16.root", 
		    "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_Higgs_version16.root",
		    "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_fakebg_version16.root"
		    ]
		
name_of_signal_file = [
		       "/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177502_version16.root"
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177503_version16.root",
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177504_version16.root",
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177506_version16.root", 
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177508_version16.root", 
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177509_version16.root",
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177510_version16.root", 
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177512_version16.root", 
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177513_version16.root", 
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177514_version16.root", 
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177517_version16.root",
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177521_version16.root", 
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177522_version16.root", 
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177523_version16.root",
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177524_version16.root",
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177525_version16.root",
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177526_version16.root",
		       #"/data/etp3/jwittkow/analysis_SUSYTools_03_04/outputfiles/histos_ZN_177527_version16.root"
		       ]

		  
#name_of_contributionLegend = ["WW", "WW+Jets", "ttbarW+t", "Z+Jets", "WZ", "ZZ", "fake", "Higgs"]	
#fillColors = [ROOT.kBlue-2, ROOT.kAzure+8,  ROOT.kOrange-2, ROOT.kSpring+1, ROOT.kGreen+3, ROOT.kGray+1, ROOT.kYellow]
name_of_contributionLegend = ["Z+Jets", "ttbarW+t", "WZ", "ZZ", "WW", "WW+Jets", "Higgs", "fake"]		
fillColors = [ROOT.kOrange-2, ROOT.kRed+1, ROOT.kSpring+1, ROOT.kGreen+3, ROOT.kBlue-2, ROOT.kAzure+8, ROOT.kYellow, ROOT.kGray+1]
name_of_contribution = ["ZPlusJets", "ttbarWPlust", "WZ", "ZZ", "WW", "WWPlusJets", "Higgs", "fake"]

name_of_variables = ["D0Signif_recalc_l0", "D0Signif_recalc_l1"]
#name_of_variables = ["pTl0", "pTl1", "pTj0", "pTj1", "mll", "METrel", "MET", "HT", "mWWt", "mTlmin", "meff", "mt2", "mjj", "DeltaPhiMETll", "DeltaPhill", "NBJets", "NFJets", "NCJets", "DeltaPhijj", "pTjj", "ptll", "DeltaPhiMETl0", "DeltaPhiMETl1", "DeltaPhiMETj0", "DeltaPhiMETj1", "DeltaPhiMETjj", "DeltaRjj", "etal0", "etal1", "etaj0", "etaj1", "mTl0MET", "mTl1MET", "DeltaPhilljj", "DeltaPhil0jj", "DeltaPhil1jj", "DeltaRlljj", "DeltaEtajj", "mTll", "mMETll", "DeltaYjj", "DeltaEtall"]#, "D0_recalc_l0", "D0_recalc_l1", "D0_branch_l0", "D0_branch_l1", "D0Signif_recalc_l0", "D0Signif_recalc_l1", "D0Signif_branch_l0", "D0Signif_branch_l1", "mZTT_coll", "mZTT_mmc"]

#cut_list = [2, 50, 50, 80, 40, 50, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
x_axis_title = ["d0/#sigmad0 recalc l0", "d0/#sigmad0 recalc l1"]
#x_axis_title = ["p_{Tl0}","p_{Tl1}","p_{Tj0}","p_{Tj1}", "m_{ll}", "E_{T}^{miss, rel}", "E_{T}^{miss}", "H_{T}", "m_{TWW}", "min(m_{T}(l0, l1))", "m_{eff}", "m_{T2}", "m_{jj}", "#Delta#Phi(E_{T}^{miss}, ll)", "#Delta#Phi(l0,l1)", "NBJets", "NFJets", "NCJets", "#Delta#Phi(j0, j1)", "p_{T,jj}", "p_{T,ll}", "#Delta#Phi(E_{T}^{miss},l0)", "#Delta#Phi(E_{T}^{miss},l1)", "#Delta#Phi(E_{T}^{miss},j0)", "#Delta#Phi(E_{T}^{miss},j1)", "#Delta#Phi(E_{T}^{miss},jj)", "#DeltaR(j,j)", "#eta_{l0}", "#eta_{l1}", "#eta_{j0}", "#eta_{j1}", "m_{T}(l0, E_{T}^{miss})", "m_{T}(l1, E_{T}^{miss})", "#Delta#Phi(ll,jj)", "#Delta#Phi(l0,jj)", "#Delta#Phi(l1,jj)", "#DeltaR(ll,jj)", "#Delta#ta(j,j)", "m_{T,ll}", "m_{E_{T}^{miss},ll}", "#DeltaY(j,j)", "#Delta#eta(l0,l1)"]#,"d0 recalc l0", "d0 recalc l1", "d0 branch l0", "d0 branch l1", "d0/#sigmad0 recalc l0", "d0/#sigmad0 recalc l1", "d0/#sigmad0 branch l0", "d0/#sigmad0 branch l1", "m_{Z->#tau#tau} (coll)","m_{Z->#tau#tau} (mmc)"]
name_of_SR = ["MM_SRSS1"]#, "EE_SRSS2"]#, "MM_SRSS1", "MM_SRSS2", "MM_SRSS3", "MM_SRSS4", "EM_SRSS1", "EM_SRSS2", "EE_SROS1", "MM_SROS1", "EM_SROS1"]
#name_of_SR = ["EE_SRSS1", "EE_SRSS2", "MM_SRSS1", "MM_SRSS2", "MM_SRSS3", "MM_SRSS4", "EM_SRSS1", "EM_SRSS2", "EE_SROS1", "MM_SROS1", "EM_SROS1"]
#mcid_of_grid_point = ["177502", "177504", "177508", "177513", "177523", "177525"]
#mcid_of_grid_point = ["177508", "177513"]
mcid_of_grid_point = ["177502", "177503", "177504", "177506", "177508", "177509", "177510", "177512", "177513", "177514", "177517", "177521", "177522", "177523", "177524", "177525", "177526", "177527"]






rootfiles_bg = []
rootfiles_gridpoints = []

for f in name_of_bg_file:
  rootfiles_bg.append(ROOT.TFile(f))
for f in name_of_signal_file:
  rootfiles_gridpoints.append(ROOT.TFile(f))

print 'bg contribution & events processed & EE & MM & EM\\\\'
print "\hline  "
sum_EE = 0
sum_MM = 0
sum_EM = 0
sum_total = 0
for i_rf, rf in enumerate(rootfiles_bg):  
  bg_histo_EE = rf.Get("h_HT_EE_SRSS1")	
  bg_histo_projected_EE = bg_histo_EE.ProjectionX("h_HT_EE_SRSS1" + name_of_contribution[i_rf], 32, 32)
  nbins = bg_histo_projected_EE.GetNbinsX()
  bg_histo_MM = rf.Get("h_HT_MM_SRSS1")	
  bg_histo_projected_MM = bg_histo_MM.ProjectionX("h_HT_MM_SRSS1" + name_of_contribution[i_rf], 31, 31)
  bg_histo_EM = rf.Get("h_HT_EM_SRSS1")	
  bg_histo_projected_EM = bg_histo_EM.ProjectionX("h_HT_EM_SRSS1" + name_of_contribution[i_rf], 31, 31)
  bg_histo_total = rf.Get("cutflow_EM")	
  sum_EE = sum_EE + bg_histo_projected_EE.Integral(0, nbins + 2)
  sum_MM = sum_MM + bg_histo_projected_MM.Integral(0, nbins + 2)
  sum_EM = sum_EM + bg_histo_projected_EM.Integral(0, nbins + 2)
  sum_total = sum_total + bg_histo_total.GetBinContent( 1)
  print name_of_contributionLegend[i_rf], ": & ", round(bg_histo_total.GetBinContent( 1),2), " & ",round(bg_histo_projected_EE.Integral(0, nbins + 2),2), " & ", round(bg_histo_projected_MM.Integral(0, nbins + 2),2), " & ",round(bg_histo_projected_EM.Integral(0, nbins + 2),2), "\\\\"
print "\hline"  
print "\hline"  
print "Total &  ", round(sum_total, 2), " & ", round(sum_EE,2),  " & ", round(sum_MM,2),  " & ", round(sum_EM,2),  "\\\\"
  

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

ybinProj_list = [ybinProj_MM_SRSS1]
#ybinProj_list = [ybinProj_EE_SRSS1, ybinProj_EE_SRSS2, ybinProj_MM_SRSS1, ybinProj_MM_SRSS2, ybinProj_MM_SRSS3, ybinProj_MM_SRSS4, ybinProj_EM_SRSS1, ybinProj_EM_SRSS2, ybinProj_EE_SROS1, ybinProj_MM_SROS1, ybinProj_EM_SROS1]

#loop over signal grid point root files:
for i_g, grid_point_file in enumerate(rootfiles_gridpoints):
  #loop over variables:  
  for i_v, v in enumerate(name_of_variables):
    if v == "DeltaPhiMETll" or v == "DeltaPhijj" or v == "DeltaPhiMETl0" or v == "DeltaPhiMETl1" or v == "DeltaPhiMETj0" or v == "DeltaPhiMETj1" or v == "DeltaPhiMETjj" or v == "DeltaRjj" or v == "etal0" or v == "etal1" or v == "etaj0" or v == "etaj1" or v == "DeltaPhilljj" or v == "DeltaPhil0jj" or v == "DeltaPhil1jj" or v == "DeltaRlljj" or v == "DeltaEtajj" or v == "DeltaYjj"  or v == "DeltaPhill" or v == "DeltaEtall":
      cut_if_value_higher = True
      cut_if_value_smaller = False
    else:
      cut_if_value_higher = False
      cut_if_value_smaller = True
    #loop over signal regions:  
    for i_s, s in enumerate(name_of_SR):
      #histoname as defined in histos_ZN_tauveto.C
      histoname = "h_" + v + "_" + s
      #print "histoname ", histoname
      #define stack to add all bg samples:
      stack = ROOT.THStack("stack_" + v + "_" + s, "stack_" + v + "_" + s)
      #define corresponding leg_stack
      leg_stack = ROOT.TLegend(0.65,0.65,0.99,0.99)
      leg_stack.SetFillColor(0)

      #loop over TFiles for bg contributions:
      for i_rf, rf in enumerate(rootfiles_bg):	
	#get individual histo for each bg root file:
	bg_histo = rf.Get(histoname)
	
	#projection of TH2F:
	bg_histo_projected = bg_histo.ProjectionX(histoname + "_1D_" + name_of_contribution[i_rf] + "_" + str(i_g), ybinProj_list[i_s], ybinProj_list[i_s])
	
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
	  binning = 20
	if nbins == 200.:
	  last_bin = 10.
	  first_bin = -10.
	  binning = 200
	if nbins == 1200.:
	  last_bin = 1.5
	  first_bin = -1.5
	  binning = 120

	#do a rebinning :
	#print "rebin with nbins/binning = ", nbins, "/", binning, " = ", nbins/binning
	bg_histo_projected.Rebin(nbins/binning)
	
	bg_histo_projected.SetMarkerStyle(21)
	bg_histo_projected.SetMarkerColor(fillColors[i_rf])
	bg_histo_projected.SetFillStyle(1001) 
	bg_histo_projected.SetFillColor(fillColors[i_rf])
	
	#-------------------------------------------------------------
	#-------------------------------------------------------------
	nbins= bg_histo_projected.GetNbinsX()
	
	zero = bg_histo_projected.GetNbinsX()/2
	range_xaxis = abs(bg_histo_projected.GetXaxis().GetXmax()) + abs(bg_histo_projected.GetXaxis().GetXmin())

	lower_limit = int(zero-(3/((range_xaxis)/(nbins))))
	upper_limit = int(zero+(3/((range_xaxis)/(nbins))))
	all_leptons = bg_histo_projected.Integral(lower_limit, upper_limit)      
	rage_xaxis = range_xaxis + 0.0
      
	for i_bin1s in range(1,(nbins/2)+1):
	  if((bg_histo_projected.Integral(zero-i_bin1s, zero+i_bin1s) / all_leptons) > 0.682689492):
	    break
	for i_bin2s in range(1,(nbins/2)+1):
	  if((bg_histo_projected.Integral(zero-i_bin2s, zero+i_bin2s) / all_leptons) > 0.954499736):
	    break
	  
	for i_bin3s in range(1,(nbins/2)+1):
	  if((bg_histo_projected.Integral(zero-i_bin3s, zero+i_bin3s) / all_leptons) > 0.997300204):
	    break	
	    
	print name_of_contributionLegend[i_rf], ":\\\\"
	_1sigma = i_bin1s * ((range_xaxis)/(nbins+0.0))
	print "1 $\sigma$: ", _1sigma, "\\\\"
	_2sigma = i_bin2s * ((range_xaxis)/(nbins+0.0))
	print "2 $\sigma$: ", _1sigma, "\\\\"
	_3sigma = i_bin3s * ((range_xaxis)/(nbins+0.0))
	print "3 $\sigma$: ", _3sigma, "\\\\"
	#-------------------------------------------------------------
	#-------------------------------------------------------------
	
	leg_stack.AddEntry(bg_histo_projected,name_of_contributionLegend[i_rf],"F")
	#add projection of bg histo to stack for lower plot:
	stack.Add(bg_histo_projected)
	#print "       ", bg_histo_projected.Integral(0, nbins + 2)
	
	#if it is the first bg histo, define individual h_sum_bg for every signal grid point i_g:
	if i_rf == 0:
	  h_sum_bg = ROOT.TH1D(histoname + "_" + str(i_g) + "_sumbg", histoname + "_" + str(i_g) + "_sumbg", nbins, first_bin, last_bin)
	  h_sum_bg.Rebin(nbins/binning)	  
	#add projection of bg histo to h_sum_bg for upper plot:
	h_sum_bg.Add(bg_histo_projected)
	
	#draw stack if it the last bg contribution:
	if i_rf == 7:
	  #define TCanvas and TPads:
	  c1 = ROOT.TCanvas("c_" + v + "_" + s + "_" + mcid_of_grid_point[i_g] + "_" + str(i_rf), "c_" + v + "_" + s + "_" + mcid_of_grid_point[i_g] + "_" + str(i_rf), 600, 600)
	  c1.SetLogy()
	  pad1 = ROOT.TPad("pad1","pad1", 0.0, 0.0, 1.0, 0.85, 0, 0, 0)
	  pad1.Draw()
	  pad1.SetLogy(1)
	  pad1.SetFillColor(ROOT.kWhite)
  
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
	  stack.SetTitle(s + " bin " + str(ybinProj_list[i_s]))
	  #for merged signal grid point: just draw histogram:	
	  #print histoname
	  grid_point_file_histo = grid_point_file.Get(histoname)
	  #grid_point_file_histo.Print()
	  grid_point_file_histo_projected = grid_point_file_histo.ProjectionX(histoname + "_1D_signal_" + name_of_contribution[i_rf], ybinProj_list[i_s], ybinProj_list[i_s])
	  #print str(mcid_of_grid_point[i_g]), "      ", grid_point_file_histo_projected.Integral(0, nbins + 2)
	  #grid_point_file_histo_projected.Print()
	  #make sure to use the same binning:
	  grid_point_file_histo_projected.Rebin(nbins/binning)
	  
		
	  #-------------------------------------------------------------
	  #-------------------------------------------------------------
	  nbins= grid_point_file_histo_projected.GetNbinsX()
	  
	  zero = grid_point_file_histo_projected.GetNbinsX()/2
	  range_xaxis = abs(grid_point_file_histo_projected.GetXaxis().GetXmax()) + abs(grid_point_file_histo_projected.GetXaxis().GetXmin())

	  lower_limit = int(zero-(3/((range_xaxis)/(nbins))))
	  upper_limit = int(zero+(3/((range_xaxis)/(nbins))))
	  all_leptons = grid_point_file_histo_projected.Integral(lower_limit, upper_limit)      
	  rage_xaxis = range_xaxis + 0.0
	
	  for i_bin1s in range(1,(nbins/2)+1):
	    if((grid_point_file_histo_projected.Integral(zero-i_bin1s, zero+i_bin1s) / all_leptons) > 0.682689492):
	      break
	  for i_bin2s in range(1,(nbins/2)+1):
	    if((grid_point_file_histo_projected.Integral(zero-i_bin2s, zero+i_bin2s) / all_leptons) > 0.954499736):
	      break
	  
	  for i_bin3s in range(1,(nbins/2)+1):
	    if((grid_point_file_histo_projected.Integral(zero-i_bin3s, zero+i_bin3s) / all_leptons) > 0.997300204):
	      break		      

	  print mcid_of_grid_point[i_g], ":\\\\"
	  _1sigma = i_bin1s * ((range_xaxis)/(nbins+0.0))
	  print "1 $\sigma$: ", _1sigma, "\\\\"
	  _2sigma = i_bin2s * ((range_xaxis)/(nbins+0.0))
	  print "2 $\sigma$: ", _1sigma, "\\\\"
	  _3sigma = i_bin3s * ((range_xaxis)/(nbins+0.0))
	  print "3 $\sigma$: ", _3sigma, "\\\\"
	  #-------------------------------------------------------------
	  #-------------------------------------------------------------
	  
	  #find a factor for scaling signal to make it visible:
	  signal_max = grid_point_file_histo_projected.GetMaximum()
	  if signal_max == 0:
	    scale_for_signal = 0
	  else:
	    scale_for_signal = stack.GetMaximum()/signal_max/2
	  #print "scale_for_signal= ", scale_for_signal
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
	  #draw signal in same TPad as stack:
	  grid_point_file_histo_projected.SetMarkerColor(ROOT.kPink-2)
	  grid_point_file_histo_projected.SetMarkerStyle(29)
	  grid_point_file_histo_projected.Draw("histpsame")
	  leg_stack.AddEntry(grid_point_file_histo_projected,"mcid " + str(mcid_of_grid_point[i_g]) + " scaled by " + str(scale),"p")
	  
	#end of loop over rootfiles_bg        
	
	
      #draw legend, cut line:
      leg_stack.SetHeader(s)
      leg_stack.SetTextSize(0.025)
      leg_stack.Draw("same")
    

      pad1.cd().Update()
      c1.SaveAs("/data/etp/jwittkowski/pics/stack_" + v + "_" + s + "_" + mcid_of_grid_point[i_g] + "_bin" + str(ybinProj_list[i_s]) + "_d0_wOSSW_wIP_requirements.pdf")
    #end loop over signal regions
  #end loop over variables
for rf in rootfiles_bg:
  rf.Close()
print "FINISHED"