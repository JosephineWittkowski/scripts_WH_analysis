import ROOT

c1 = ROOT.TCanvas("D0 ", " D0", 600, 600)
#enum LEP_TYPE{PR=0, CONV, HF, LF, TYPE_Undef};
#bin 2: PR
#bin 3: CONV
#bin 4: HF
#bin 5: LF

#D0_array = ["D0", "D0Signif"]
D0_array = ["D0Signif"]
for i_d0, d0signif in enumerate(D0_array):
  #DeltaR_array = ["02", "04", "06", "08"]
  DeltaR_array = ["06"]
  for i_d, DeltaRPosition in enumerate(DeltaR_array):
    i_d = 0
    in_file = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_ttbar_validate_d0_2SS_DeltaRClosestJet" + DeltaR_array[i_d] +".root")
    in_file.Print()
    #lepton_array = ["elec", "muon"]
    lepton_array = ["elec"]

    #DeltaRdecimal_array = ["0.2", "0.4", "0.6", "0.8"]
    DeltaRdecimal_array = ["0.6"]

    for i_l, lepton in enumerate(lepton_array):
      print lepton_array[i_l]
      #histoname_jetTruth = "h_jetTruthInfo_" + lepton_array[i_l]
      #print histoname_jetTruth
      #histo_jetTruth = in_file.Get(histoname_jetTruth) #histo_2D_PR.ProjectionX(histoname_PR + "_1D", 2, 2)
      #histo_jetTruth.SetTitle("jetTruthInfo #DeltaR closest Jet <" + DeltaRdecimal_array[i_d] +"")
      #ROOT.gStyle.SetOptStat()
      #histo_jetTruth.Draw("hist")
      #c1.SaveAs("../pics/JetTruthInfo02_" +  lepton_array[i_l] + ".pdf")

      c1.SetLogy()
      histoname_PR = "h_" + D0_array[i_d0] + "_recalc_" +  lepton_array[i_l]
      print histoname_PR
      #histo_2D_PR = in_file.Get(histoname_PR)
      histo_d0signif = in_file.Get(histoname_PR) #histo_2D_PR.ProjectionX(histoname_PR + "_1D", 2, 2)
      histo_d0signif.Print()
      print histo_d0signif.GetEntries()
      histo_d0signif.SetMarkerStyle(20)
      histo_d0signif.SetLineColor(ROOT.kBlue)
      histo_d0signif.Rebin(200)
      nbins= histo_d0signif.GetNbinsX()
      #print "nbins= ", nbins
      all_leptons = histo_d0signif.Integral(1, nbins+1)      
      zero = histo_d0signif.GetNbinsX()/2
      
      for i_bin1s in range(1,(nbins/2)+1):
	if((histo_d0signif.Integral(zero-i_bin1s, zero+i_bin1s) / all_leptons) > 0.682689492):
	  break
      
      for i_bin2s in range(1,(nbins/2)+1):
	if((histo_d0signif.Integral(zero-i_bin2s, zero+i_bin2s) / all_leptons) > 0.954499736):
	  break
	  
      for i_bin3s in range(1,(nbins/2)+1):
	if((histo_d0signif.Integral(zero-i_bin3s, zero+i_bin3s) / all_leptons) > 0.997300204):
	  break
	  
      for i_bin4s in range(1,(nbins/2)+1):
	if((histo_d0signif.Integral(zero-i_bin4s, zero+i_bin4s) / all_leptons) > 0.99993666):
	  break
      
      for i_bin5s in range(1,(nbins/2)+1):
	#print histo_d0signif.Integral(zero-i_bin5s, zero+i_bin5s), " / ", all_leptons, " ratio= ", (histo_d0signif.Integral(zero-i_bin5s, zero+i_bin5s) / all_leptons)
	if((histo_d0signif.Integral(zero-i_bin5s, zero+i_bin5s) / all_leptons) > 0.999999426697):
	  break	  
	  
      print "No truth classifiation " + lepton_array[i_l], ", cut at $|d0/\sigma d0|<$\\\\"
      range_xaxis = abs(histo_d0signif.GetXaxis().GetXmax()) + abs(histo_d0signif.GetXaxis().GetXmin()) + 0.0
      print range_xaxis
      _1sigma = i_bin1s * ((range_xaxis)/(nbins+0.0))
      print "1 $\sigma$: ", _1sigma, "\\\\"
      _2sigma = i_bin2s * ((range_xaxis)/(nbins+0.0))
      print "2 $\sigma$: ", _2sigma, "\\\\"
      _3sigma = i_bin3s * ((range_xaxis)/(nbins+0.0))
      print "3 $\sigma$: ", _3sigma, "\\\\"
      _4sigma = i_bin4s * ((range_xaxis)/(nbins+0.0))
      #print "4 $\sigma$: ", _4sigma, "\\\\"
      _5sigma = i_bin5s * ((range_xaxis)/(nbins+0.0))	  
      
      histo_d0signif.Scale(1/histo_d0signif.Integral(0,histo_d0signif.GetNbinsX()))

      histo_d0signif.SetTitle("h_" + D0_array[i_d0] + "_recalc " +  lepton_array[i_l] + " #DeltaR closest Jet <" + DeltaRdecimal_array[i_d] +"")
      histo_d0signif.Draw("hist")
      histo_d0signif.GetXaxis().SetTitle(D0_array[i_d0])
      max_bin_content = histo_d0signif.GetMaximum()
      
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
      
      linePlus_1sigma_PR.Draw("")
      lineMinus_1sigma_PR.Draw("same")
      linePlus_2sigma_PR.Draw("same")
      lineMinus_2sigma_PR.Draw("same")
      linePlus_3sigma_PR.Draw("same")
      lineMinus_3sigma_PR.Draw("same")
      #linePlus_4sigma_PR.Draw("same")
      #lineMinus_4sigma_PR.Draw("same")
      #linePlus_5sigma_PR.Draw("same")
      #lineMinus_5sigma_PR.Draw("same")
      
      histo_d0signif.SetTitle(D0_array[i_d0] + " "+  lepton_array[i_l] + " #DeltaR closest Jet <" + DeltaRdecimal_array[i_d]  )
      #histo_d0signif.SetTextSize(0.02)
      ROOT.gStyle.SetTitleSize(0.05); 
      histo_d0signif.Draw("histsame")
      #histo_d0signif.GetXaxis().SetRangeUser(-0.5, 0.5)
      histo_d0signif.GetXaxis().SetTitle(D0_array[i_d0])
      #draw legend for upper plot:
      #leg_ZN = ROOT.TLegend(0.65,0.8,0.9,0.9)
      #leg_ZN.SetFillColor(0)
      #leg_ZN.SetHeader("leptons: " + str(round(all_leptons,2)) + " in 3 #sigma: " + str(round(_3sigma_events,2)) + " in 5 #sigma: " + str(round(_5sigma_events,2)) )
      #leg_ZN.AddEntry(h_ZN,"Z_{N}","l")
      #leg_ZN.AddEntry(h_cut_eff_signal,"signal cut #epsilon","l")
      #leg_ZN.AddEntry(h_cut_eff_bg,"bg cut #epsilon","l")
      #leg_ZN.SetTextSize(0.03)
      #leg_ZN.Draw("same")

      #histoname_HF = "h_" + D0_array[i_d0] + "_recalc_HF_" +  lepton_array[i_l] + ""
      ##histo_2D_HF = in_file.Get(histoname_HF)
      #histo_HF = in_file.Get(histoname_HF) #histo_2D_HF.ProjectionX(histoname_HF + "_1D", 4, 4)
      #print histo_HF.GetEntries()
      #histo_HF.SetMarkerStyle(20)
      #histo_HF.SetLineColor(ROOT.kRed)
      #histo_HF.Scale(1/histo_HF.Integral(0,histo_HF.GetNbinsX()))
      #histo_HF.Rebin(200)
      #histo_HF.Draw("histsame")


      #histoname_LF = "h_" + D0_array[i_d0] + "_recalc_LF_" +  lepton_array[i_l] + ""
      ##histo_2D_LF = in_file.Get(histoname_LF)
      #histo_LF = in_file.Get(histoname_LF) #histo_2D_LF.ProjectionX(histoname_LF + "_1D", 5, 5)
      #print histo_LF.GetEntries()
      #histo_LF.SetMarkerStyle(20)
      #histo_LF.SetLineColor(ROOT.kOrange)
      #histo_LF.Scale(1/histo_LF.Integral(0,histo_LF.GetNbinsX()))
      #histo_LF.Rebin(200)
      #histo_LF.Draw("histsame")

      leg_stack = ROOT.TLegend(0.7,0.7,0.8,0.8)
      leg_stack.SetFillColor(0)
      leg_stack.AddEntry(histo_d0signif,"PR","l")
      #leg_stack.AddEntry(histo_HF,"HF","l")
      #leg_stack.AddEntry(histo_LF,"LF","l")
      leg_stack.SetTextSize(0.025)
      #leg_stack.Draw("same")
      ROOT.gStyle.SetOptStat(0)

      max_bin_content = histo_d0signif.GetMaximum()
      line = ROOT.TLine(0,0,0,max_bin_content*1.1);
      line.SetLineColor(ROOT.kGreen)
      line.SetLineWidth(2)
      #line.Draw("same")

      line2 = ROOT.TLine(3,0,3,max_bin_content*1.1);
      line2.SetLineColor(2)
      line2.SetLineWidth(2)
      line2.Draw("same")
      line3 = ROOT.TLine(-3,0,-3,max_bin_content*1.1);
      line3.SetLineColor(2)
      line3.SetLineWidth(2)
      line3.Draw("same")
      line4 = ROOT.TLine(-5,0,-5,max_bin_content*1.1);
      line4.SetLineColor(5)
      line4.SetLineWidth(2)
      line4.Draw("same")

      line5 = ROOT.TLine(5,0,5,max_bin_content*1.1);
      line5.SetLineColor(5)
      line5.SetLineWidth(2)
      line5.Draw("same")

      c1.SaveAs("../pics/h_" + D0_array[i_d0] + "_tightSel_2SS_DeltaRClosestJet" + DeltaR_array[i_d] + "_" +  lepton_array[i_l] + ".pdf")
