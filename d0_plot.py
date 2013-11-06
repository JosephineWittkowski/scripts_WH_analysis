import ROOT

c1 = ROOT.TCanvas("D0 ", " D0", 600, 600)
#enum LEP_TYPE{PR=0, CONV, HF, LF, TYPE_Undef};
#bin 2: PR
#bin 3: CONV
#bin 4: HF
#bin 5: LF

D0_array = ["D0Signif"]
#D0_array = ["D0", "D0Signif"]
for i_d0, d0signif in enumerate(D0_array):
  DeltaR_array = ["06"]
  #DeltaR_array = ["02", "04", "06", "08"]
  for i_d, DeltaRPosition in enumerate(DeltaR_array):
    i_d = 0
    in_file = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_ttbar_validate_d0_wOSSW_wIP_requirements_DeltaRClosestJet" + DeltaR_array[i_d] +".root")
    #in_file = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_ttbar_validate_d0_2SS_DeltaRClosestJet" + DeltaR_array[i_d] +".root")
    lepton_array = ["elec"]
    #lepton_array = ["elec", "muon"]
    DeltaRdecimal_array = ["0.6"]
    #DeltaRdecimal_array = ["0.2", "0.4", "0.6", "0.8"]

    for i_l, lepton in enumerate(lepton_array):
      print lepton_array[i_l]
      histoname_jetTruth = "h_jetTruthInfo_" + lepton_array[i_l]
      #print histoname_jetTruth
      histo_jetTruth = in_file.Get(histoname_jetTruth) #histo_2D_PR.ProjectionX(histoname_PR + "_1D", 2, 2)
      histo_jetTruth.SetTitle("jetTruthInfo #DeltaR closest Jet <" + DeltaRdecimal_array[i_d] +"")
      ROOT.gStyle.SetOptStat()
      histo_jetTruth.Draw("hist")
      #c1.SaveAs("../pics/JetTruthInfo_" +  lepton_array[i_l] + ".pdf")

      c1.SetLogy()
      histoname_PR = "h_" + D0_array[i_d0] + "_recalc_PR_" +  lepton_array[i_l] + ""
      histo_PR = in_file.Get(histoname_PR)

      histo_PR.SetMarkerStyle(20)
      histo_PR.SetLineColor(ROOT.kBlue)
      histo_PR.Rebin(10)
      
      nbins= histo_PR.GetNbinsX()
      #print "nbins= ", nbins
      all_leptons = histo_PR.Integral(1, nbins+1)      
      zero = histo_PR.GetNbinsX()/2
      
      for i_bin1s in range(1,(nbins/2)+1):
	if((histo_PR.Integral(zero-i_bin1s, zero+i_bin1s) / all_leptons) > 0.682689492):
	  break
      
      for i_bin2s in range(1,(nbins/2)+1):
	if((histo_PR.Integral(zero-i_bin2s, zero+i_bin2s) / all_leptons) > 0.954499736):
	  break
	  
      for i_bin3s in range(1,(nbins/2)+1):
	if((histo_PR.Integral(zero-i_bin3s, zero+i_bin3s) / all_leptons) > 0.997300204):
	  break
	  
      for i_bin4s in range(1,(nbins/2)+1):
	if((histo_PR.Integral(zero-i_bin4s, zero+i_bin4s) / all_leptons) > 0.99993666):
	  break
      
      for i_bin5s in range(1,(nbins/2)+1):
	#print histo_PR.Integral(zero-i_bin5s, zero+i_bin5s), " / ", all_leptons, " ratio= ", (histo_PR.Integral(zero-i_bin5s, zero+i_bin5s) / all_leptons)
	if((histo_PR.Integral(zero-i_bin5s, zero+i_bin5s) / all_leptons) > 0.999999426697):
	  break	  
	
      print "Prompt " + lepton_array[i_l], ", cut at $|d0/\sigma d0|<$\\\\"
      range_xaxis = abs(histo_PR.GetXaxis().GetXmax()) + abs(histo_PR.GetXaxis().GetXmin()) + 0.0
      #print range_xaxis
      _1sigma = i_bin1s * ((range_xaxis)/(nbins+0.0))
      print "1 $\sigma$: ", _1sigma, "\\\\"
      _2sigma = i_bin2s * ((range_xaxis)/(nbins+0.0))
      print "2 $\sigma$: ", _2sigma, "\\\\"
      _3sigma = i_bin3s * ((range_xaxis)/(nbins+0.0))
      print "3 $\sigma$: ", _3sigma, "\\\\"
      _4sigma = i_bin4s * ((range_xaxis)/(nbins+0.0))
      #print "4 $\sigma$: ", _4sigma, "\\\\"
      _5sigma = i_bin5s * ((range_xaxis)/(nbins+0.0))
      #print "5 $\sigma$: ", _5sigma, "\\\\"
      
      histo_PR.Scale(1/histo_PR.Integral(0,histo_PR.GetNbinsX()))

      histo_PR.SetTitle("h_" + D0_array[i_d0] + "_recalc " +  lepton_array[i_l] + " #DeltaR closest Jet <" + DeltaRdecimal_array[i_d] +"")
      histo_PR.Draw("hist")
      histo_PR.GetXaxis().SetTitle(D0_array[i_d0])
      max_bin_content = histo_PR.GetMaximum()
      
      linePlus_1sigma_PR = ROOT.TLine(_1sigma, 0, _1sigma, max_bin_content*1.1);
      linePlus_1sigma_PR.SetLineColor(ROOT.kBlue)
      linePlus_1sigma_PR.SetLineWidth(2)
      
      lineMinus_1sigma_PR = ROOT.TLine(-_1sigma, 0, -_1sigma, max_bin_content*1.1);
      lineMinus_1sigma_PR.SetLineColor(ROOT.kBlue)
      lineMinus_1sigma_PR.SetLineWidth(2)

      
      linePlus_2sigma_PR = ROOT.TLine(_2sigma, 0, _2sigma, max_bin_content*1.1);
      linePlus_2sigma_PR.SetLineColor(ROOT.kBlue)
      linePlus_2sigma_PR.SetLineWidth(2)
      linePlus_2sigma_PR.SetLineStyle(2)
      
      lineMinus_2sigma_PR = ROOT.TLine(-_2sigma, 0, -_2sigma, max_bin_content*1.1);
      lineMinus_2sigma_PR.SetLineColor(ROOT.kBlue)
      lineMinus_2sigma_PR.SetLineWidth(2)
      lineMinus_2sigma_PR.SetLineStyle(2)

      
      linePlus_3sigma_PR = ROOT.TLine(_3sigma, 0, _3sigma, max_bin_content*1.1);
      linePlus_3sigma_PR.SetLineColor(ROOT.kBlue)
      linePlus_3sigma_PR.SetLineWidth(2)
      linePlus_3sigma_PR.SetLineStyle(10)
      
      lineMinus_3sigma_PR = ROOT.TLine(-_3sigma, 0, -_3sigma, max_bin_content*1.1);
      lineMinus_3sigma_PR.SetLineColor(ROOT.kBlue)
      lineMinus_3sigma_PR.SetLineWidth(2)
      lineMinus_3sigma_PR.SetLineStyle(10)
      
      linePlus_4sigma_PR = ROOT.TLine(_4sigma, 0, _4sigma, max_bin_content*1.1);
      linePlus_4sigma_PR.SetLineColor(ROOT.kBlue)
      linePlus_4sigma_PR.SetLineWidth(2)
      linePlus_4sigma_PR.SetLineStyle(7)
      
      lineMinus_4sigma_PR = ROOT.TLine(-_4sigma, 0, -_4sigma, max_bin_content*1.1);
      lineMinus_4sigma_PR.SetLineColor(ROOT.kBlue)
      lineMinus_4sigma_PR.SetLineWidth(2)
      lineMinus_4sigma_PR.SetLineStyle(7)

      linePlus_5sigma_PR = ROOT.TLine(_5sigma, 0, _5sigma, max_bin_content*1.1);
      linePlus_5sigma_PR.SetLineColor(ROOT.kBlue)
      linePlus_5sigma_PR.SetLineWidth(2)
      linePlus_5sigma_PR.SetLineStyle(8)
      
      lineMinus_5sigma_PR = ROOT.TLine(-_5sigma, 0, -_5sigma, max_bin_content*1.1);
      lineMinus_5sigma_PR.SetLineColor(ROOT.kBlue)
      lineMinus_5sigma_PR.SetLineWidth(2)
      lineMinus_5sigma_PR.SetLineStyle(8)
      
      #linePlus_1sigma_PR.Draw("same")
      #lineMinus_1sigma_PR.Draw("same")
      #linePlus_2sigma_PR.Draw("same")
      #lineMinus_2sigma_PR.Draw("same")
      #linePlus_3sigma_PR.Draw("same")
      #lineMinus_3sigma_PR.Draw("same")
      #linePlus_4sigma_PR.Draw("same")
      #lineMinus_4sigma_PR.Draw("same")
      #linePlus_5sigma_PR.Draw("same")
      #lineMinus_5sigma_PR.Draw("same")
      
##################################################################################################################################
##################################################################################################################################

      histoname_HF = "h_" + D0_array[i_d0] + "_recalc_HF_" +  lepton_array[i_l] + ""
      #histo_2D_HF = in_file.Get(histoname_HF)
      histo_HF = in_file.Get(histoname_HF) #histo_2D_HF.ProjectionX(histoname_HF + "_1D", 4, 4)
      #print histo_HF.GetEntries()
      histo_HF.SetMarkerStyle(20)
      histo_HF.SetLineColor(ROOT.kRed)
      histo_HF.Rebin(10)
      nbins= histo_HF.GetNbinsX()
      #print "nbins= ", nbins
      all_leptons = histo_HF.Integral(1, nbins+1)      
      zero = histo_HF.GetNbinsX()/2
      
      for i_bin1s in range(1,(nbins/2)+1):
	if((histo_HF.Integral(zero-i_bin1s, zero+i_bin1s) / all_leptons) > 0.682689492):
	  break
      
      for i_bin2s in range(1,(nbins/2)+1):
	if((histo_HF.Integral(zero-i_bin2s, zero+i_bin2s) / all_leptons) > 0.954499736):
	  break
	  
      for i_bin3s in range(1,(nbins/2)+1):
	if((histo_HF.Integral(zero-i_bin3s, zero+i_bin3s) / all_leptons) > 0.997300204):
	  break
	  
      for i_bin4s in range(1,(nbins/2)+1):
	if((histo_HF.Integral(zero-i_bin4s, zero+i_bin4s) / all_leptons) > 0.99993666):
	  break
      
      for i_bin5s in range(1,(nbins/2)+1):
	#print histo_HF.Integral(zero-i_bin5s, zero+i_bin5s), " / ", all_leptons, " ratio= ", (histo_HF.Integral(zero-i_bin5s, zero+i_bin5s) / all_leptons)
	if((histo_HF.Integral(zero-i_bin5s, zero+i_bin5s) / all_leptons) > 0.999999426697):
	  break	  
	
      print "HF " + lepton_array[i_l], ", cut at $|d0/\sigma d0|<$\\\\"
      range_xaxis = abs(histo_HF.GetXaxis().GetXmax()) + abs(histo_HF.GetXaxis().GetXmin()) + 0.0
      _1sigma = i_bin1s * ((range_xaxis)/(nbins+0.0))
      print "1 $\sigma$: ", _1sigma, "\\\\"
      _2sigma = i_bin2s * ((range_xaxis)/(nbins+0.0))
      print "2 $\sigma$: ", _2sigma, "\\\\"
      _3sigma = i_bin3s * ((range_xaxis)/(nbins+0.0))
      print "3 $\sigma$: ", _3sigma, "\\\\"
      _4sigma = i_bin4s * ((range_xaxis)/(nbins+0.0))
      #print "4 $\sigma$: ", _4sigma, "\\\\"
      _5sigma = i_bin5s * ((range_xaxis)/(nbins+0.0))
      #print "5 $\sigma$: ", _5sigma, "\\\\"
      
      histo_HF.Scale(1/histo_HF.Integral(0,histo_HF.GetNbinsX()))

      histo_HF.SetTitle("h_" + D0_array[i_d0] + "_recalc " +  lepton_array[i_l] + " #DeltaR closest Jet <" + DeltaRdecimal_array[i_d] +"")
      histo_HF.Draw("histsame")
      histo_HF.GetXaxis().SetTitle(D0_array[i_d0])
      max_bin_content = histo_HF.GetMaximum()
      
      linePlus_1sigma_HF = ROOT.TLine(_1sigma, 0, _1sigma, max_bin_content*1.1);
      linePlus_1sigma_HF.SetLineColor(ROOT.kRed)
      linePlus_1sigma_HF.SetLineWidth(2)
      
      lineMinus_1sigma_HF = ROOT.TLine(-_1sigma, 0, -_1sigma, max_bin_content*1.1);
      lineMinus_1sigma_HF.SetLineColor(ROOT.kRed)
      lineMinus_1sigma_HF.SetLineWidth(2)

      
      linePlus_2sigma_HF = ROOT.TLine(_2sigma, 0, _2sigma, max_bin_content*1.1);
      linePlus_2sigma_HF.SetLineColor(ROOT.kRed)
      linePlus_2sigma_HF.SetLineWidth(2)
      linePlus_2sigma_HF.SetLineStyle(2)
      
      lineMinus_2sigma_HF = ROOT.TLine(-_2sigma, 0, -_2sigma, max_bin_content*1.1);
      lineMinus_2sigma_HF.SetLineColor(ROOT.kRed)
      lineMinus_2sigma_HF.SetLineWidth(2)
      lineMinus_2sigma_HF.SetLineStyle(2)

      
      linePlus_3sigma_HF = ROOT.TLine(_3sigma, 0, _3sigma, max_bin_content*1.1);
      linePlus_3sigma_HF.SetLineColor(ROOT.kRed)
      linePlus_3sigma_HF.SetLineWidth(2)
      linePlus_3sigma_HF.SetLineStyle(10)
      
      lineMinus_3sigma_HF = ROOT.TLine(-_3sigma, 0, -_3sigma, max_bin_content*1.1);
      lineMinus_3sigma_HF.SetLineColor(ROOT.kRed)
      lineMinus_3sigma_HF.SetLineWidth(2)
      lineMinus_3sigma_HF.SetLineStyle(10)
      
      linePlus_4sigma_HF = ROOT.TLine(_4sigma, 0, _4sigma, max_bin_content*1.1);
      linePlus_4sigma_HF.SetLineColor(ROOT.kRed)
      linePlus_4sigma_HF.SetLineWidth(2)
      linePlus_4sigma_HF.SetLineStyle(7)
      
      lineMinus_4sigma_HF = ROOT.TLine(-_4sigma, 0, -_4sigma, max_bin_content*1.1);
      lineMinus_4sigma_HF.SetLineColor(ROOT.kRed)
      lineMinus_4sigma_HF.SetLineWidth(2)
      lineMinus_4sigma_HF.SetLineStyle(7)

      linePlus_5sigma_HF = ROOT.TLine(_5sigma, 0, _5sigma, max_bin_content*1.1);
      linePlus_5sigma_HF.SetLineColor(ROOT.kRed)
      linePlus_5sigma_HF.SetLineWidth(2)
      linePlus_5sigma_HF.SetLineStyle(8)
      
      lineMinus_5sigma_HF = ROOT.TLine(-_5sigma, 0, -_5sigma, max_bin_content*1.1);
      lineMinus_5sigma_HF.SetLineColor(ROOT.kRed)
      lineMinus_5sigma_HF.SetLineWidth(2)
      lineMinus_5sigma_HF.SetLineStyle(8)
      
      #linePlus_1sigma_HF.Draw("same")
      #lineMinus_1sigma_HF.Draw("same")
      #linePlus_2sigma_HF.Draw("same")
      #lineMinus_2sigma_HF.Draw("same")
      #linePlus_3sigma_HF.Draw("same")
      #lineMinus_3sigma_HF.Draw("same")
      #linePlus_4sigma_HF.Draw("same")
      #lineMinus_4sigma_HF.Draw("same")
      #linePlus_5sigma_HF.Draw("same")
      #lineMinus_5sigma_HF.Draw("same")
      
      #histo_HF.Draw("histsame")

###################################################################################################################################
###################################################################################################################################

      histoname_LF = "h_" + D0_array[i_d0] + "_recalc_LF_" +  lepton_array[i_l] + ""
      #histo_2D_LF = in_file.Get(histoname_LF)
      histo_LF = in_file.Get(histoname_LF) #histo_2D_LF.ProjectionX(histoname_LF + "_1D", 5, 5)
      #print histo_LF.GetEntries()
      histo_LF.SetMarkerStyle(20)
      histo_LF.SetLineColor(ROOT.kOrange)
      histo_LF.Rebin(10)
      nbins= histo_LF.GetNbinsX()
      #print "nbins= ", nbins
      all_leptons = histo_LF.Integral(1, nbins+1)      
      zero = histo_LF.GetNbinsX()/2
      
      for i_bin1s in range(1,(nbins/2)+1):
	if((histo_LF.Integral(zero-i_bin1s, zero+i_bin1s) / all_leptons) > 0.682689492):
	  break
      
      for i_bin2s in range(1,(nbins/2)+1):
	if((histo_LF.Integral(zero-i_bin2s, zero+i_bin2s) / all_leptons) > 0.954499736):
	  break
	  
      for i_bin3s in range(1,(nbins/2)+1):
	if((histo_LF.Integral(zero-i_bin3s, zero+i_bin3s) / all_leptons) > 0.997300204):
	  break
	  
      for i_bin4s in range(1,(nbins/2)+1):
	if((histo_LF.Integral(zero-i_bin4s, zero+i_bin4s) / all_leptons) > 0.99993666):
	  break
      
      for i_bin5s in range(1,(nbins/2)+1):
	#print histo_LF.Integral(zero-i_bin5s, zero+i_bin5s), " / ", all_leptons, " ratio= ", (histo_LF.Integral(zero-i_bin5s, zero+i_bin5s) / all_leptons)
	if((histo_LF.Integral(zero-i_bin5s, zero+i_bin5s) / all_leptons) > 0.999999426697):
	  break	  
	
      print "LF " + lepton_array[i_l], ", cut at $|d0/\sigma d0|<$\\\\"
      range_xaxis = abs(histo_LF.GetXaxis().GetXmax()) + abs(histo_LF.GetXaxis().GetXmin()) + 0.0
      _1sigma = i_bin1s * ((range_xaxis)/(nbins+0.0))
      print "1 $\sigma$: ", _1sigma, "\\\\"
      _2sigma = i_bin2s * ((range_xaxis)/(nbins+0.0))
      print "2 $\sigma$: ", _2sigma, "\\\\"
      _3sigma = i_bin3s * ((range_xaxis)/(nbins+0.0))
      print "3 $\sigma$: ", _3sigma, "\\\\"
      _4sigma = i_bin4s * ((range_xaxis)/(nbins+0.0))
      #print "4 $\sigma$: ", _4sigma, "\\\\"
      _5sigma = i_bin5s * ((range_xaxis)/(nbins+0.0))
      #print "5 $\sigma$: ", _5sigma, "\\\\"
      
      histo_LF.Scale(1/histo_LF.Integral(0,histo_LF.GetNbinsX()))

      histo_LF.SetTitle("h_" + D0_array[i_d0] + "_recalc " +  lepton_array[i_l] + " #DeltaR closest Jet <" + DeltaRdecimal_array[i_d] +"")
      histo_LF.Draw("histsame")
      histo_LF.GetXaxis().SetTitle(D0_array[i_d0])
      max_bin_content = histo_LF.GetMaximum()
      
      linePlus_1sigma_LF = ROOT.TLine(_1sigma, 0, _1sigma, max_bin_content*1.1);
      linePlus_1sigma_LF.SetLineColor(ROOT.kOrange)
      linePlus_1sigma_LF.SetLineWidth(2)
      
      lineMinus_1sigma_LF = ROOT.TLine(-_1sigma, 0, -_1sigma, max_bin_content*1.1);
      lineMinus_1sigma_LF.SetLineColor(ROOT.kOrange)
      lineMinus_1sigma_LF.SetLineWidth(2)

      
      linePlus_2sigma_LF = ROOT.TLine(_2sigma, 0, _2sigma, max_bin_content*1.1);
      linePlus_2sigma_LF.SetLineColor(ROOT.kOrange)
      linePlus_2sigma_LF.SetLineWidth(2)
      linePlus_2sigma_LF.SetLineStyle(2)
      
      lineMinus_2sigma_LF = ROOT.TLine(-_2sigma, 0, -_2sigma, max_bin_content*1.1);
      lineMinus_2sigma_LF.SetLineColor(ROOT.kOrange)
      lineMinus_2sigma_LF.SetLineWidth(2)
      lineMinus_2sigma_LF.SetLineStyle(2)

      
      linePlus_3sigma_LF = ROOT.TLine(_3sigma, 0, _3sigma, max_bin_content*1.1);
      linePlus_3sigma_LF.SetLineColor(ROOT.kOrange)
      linePlus_3sigma_LF.SetLineWidth(2)
      linePlus_3sigma_LF.SetLineStyle(10)
      
      lineMinus_3sigma_LF = ROOT.TLine(-_3sigma, 0, -_3sigma, max_bin_content*1.1);
      lineMinus_3sigma_LF.SetLineColor(ROOT.kOrange)
      lineMinus_3sigma_LF.SetLineWidth(2)
      lineMinus_3sigma_LF.SetLineStyle(10)
      
      linePlus_4sigma_LF = ROOT.TLine(_4sigma, 0, _4sigma, max_bin_content*1.1);
      linePlus_4sigma_LF.SetLineColor(ROOT.kOrange)
      linePlus_4sigma_LF.SetLineWidth(2)
      linePlus_4sigma_LF.SetLineStyle(7)
      
      lineMinus_4sigma_LF = ROOT.TLine(-_4sigma, 0, -_4sigma, max_bin_content*1.1);
      lineMinus_4sigma_LF.SetLineColor(ROOT.kOrange)
      lineMinus_4sigma_LF.SetLineWidth(2)
      lineMinus_4sigma_LF.SetLineStyle(7)

      linePlus_5sigma_LF = ROOT.TLine(_5sigma, 0, _5sigma, max_bin_content*1.1);
      linePlus_5sigma_LF.SetLineColor(ROOT.kOrange)
      linePlus_5sigma_LF.SetLineWidth(2)
      linePlus_5sigma_LF.SetLineStyle(8)
      
      lineMinus_5sigma_LF = ROOT.TLine(-_5sigma, 0, -_5sigma, max_bin_content*1.1);
      lineMinus_5sigma_LF.SetLineColor(ROOT.kOrange)
      lineMinus_5sigma_LF.SetLineWidth(2)
      lineMinus_5sigma_LF.SetLineStyle(8)
      
      #linePlus_1sigma_LF.Draw("same")
      #lineMinus_1sigma_LF.Draw("same")
      #linePlus_2sigma_LF.Draw("same")
      #lineMinus_2sigma_LF.Draw("same")
      #linePlus_3sigma_LF.Draw("same")
      #lineMinus_3sigma_LF.Draw("same")
      #linePlus_4sigma_LF.Draw("same")
      #lineMinus_4sigma_LF.Draw("same")
      #linePlus_5sigma_LF.Draw("same")
      #lineMinus_5sigma_LF.Draw("same")
      #histo_LF.Draw("histsame")
      


      leg_stack = ROOT.TLegend(0.7,0.7,0.8,0.8)
      leg_stack.SetFillColor(0)
      leg_stack.AddEntry(histo_PR,"PR","l")
      leg_stack.AddEntry(histo_HF,"HF","l")
      leg_stack.AddEntry(histo_LF,"LF","l")
      leg_stack.SetTextSize(0.025)
      leg_stack.Draw("same")
      ROOT.gStyle.SetOptStat(0)

      #line = ROOT.TLine(0,0,0,max_bin_content*1.1);
      #line.SetLineColor(ROOT.kGreen)
      #line.SetLineWidth(2)
      #line.Draw("same")


      #line4 = ROOT.TLine(-35,0.0001,35,0.0001);
      #line4.SetLineColor(ROOT.kGray+2)
      #line4.SetLineWidth(2)
      #line4.Draw("same")

      #line5 = ROOT.TLine(-35,0.0003,35,0.0003);
      #line5.SetLineColor(ROOT.kGray+2)
      #line5.SetLineWidth(2)
      #line5.Draw("same")

      c1.SaveAs("../pics/h_" + D0_array[i_d0] + "_wOSSW_wIP_requirements" + DeltaR_array[i_d] + "_" +  lepton_array[i_l] + ".pdf")
