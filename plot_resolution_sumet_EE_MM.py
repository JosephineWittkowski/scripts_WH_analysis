#!/usr/bin/env python
import ROOT

inputfiles_EE = [ROOT.TFile("/data/etp/jwittkowski/analysis_SUSYTools_03_04/histo_Zee_pureMETxy_10GeVZwindow_data_variableBinning.root"),
		 ROOT.TFile("/data/etp/jwittkowski/analysis_SUSYTools_03_04/histo_Zee_pureMETxy_10GeVZwindow_MC_variableBinning.root")]
inputfiles_MM = [ROOT.TFile("/data/etp/jwittkowski/analysis_SUSYTools_03_04/histo_Zmm_pureMETxy_10GeVZwindow_data_variableBinning.root"),
		 ROOT.TFile("/data/etp/jwittkowski/analysis_SUSYTools_03_04/histo_Zmm_pureMETxy_10GeVZwindow_MC_variableBinning.root")]
data_type = ["data", "MC"]	     

for i_f, inputfile in enumerate(inputfiles_EE):	     
  f = open("parameters_Zee_mm_" + data_type[i_f] + "_varBins.txt", 'w')
  for i_jet in range(0,4):
    #histoname_ptel0 = "h_ptel0_" + str(i_jet) + "j"
    #histo_ptel0 = inputfile.Get(histoname_ptel0)
    #histo_ptel0.Print()
    #c1 = ROOT.TCanvas(histoname_ptel0, histoname_ptel0,  600, 600)
    #histo_ptel0.Draw()
    #c1.SaveAs("../pics/ptel0_" + str(i_jet) + " j_Zee.pdf")

    #histoname_mee = "h_mee_" + str(i_jet) + "j"
    #histo_mee = inputfile.Get(histoname_mee)
    #histo_mee.Print()
    #c1 = ROOT.TCanvas(histoname_mee, histoname_mee,  600, 600)
    #histo_mee.Draw()
    #c1.SaveAs("../pics/mee_Zee.pdf")

    #histoname_ptel1 = "h_ptel1_" + str(i_jet) + "j"
    #histo_ptel1 = inputfile.Get(histoname_ptel1)
    #histo_ptel1.Print()
    #c1 = ROOT.TCanvas(histoname_ptel1, histoname_ptel1,  600, 600)
    #histo_ptel1.Draw()
    #c1.SaveAs("../pics/ptel1_v_Zee.pdf")

    histoname_metxy_EE = "h_metxy_sumet_" + str(i_jet) + "j_EE"
    histoname_metxy_MM = "h_metxy_sumet_" + str(i_jet) + "j_MM"
    c1 = ROOT.TCanvas(histoname_metxy_EE + "_MM", histoname_metxy_EE + "_MM",  600, 600)
    histo_metxy_EE = inputfiles_EE[i_f].Get(histoname_metxy_EE)
    histo_metxy_MM = inputfiles_MM[i_f].Get(histoname_metxy_MM)
    histo_metxy_EE.Add(histo_metxy_MM)
    ROOT.gStyle.SetOptStat()
    histo_metxy_EE.Draw("col")
    histo_metxy_EE.GetYaxis().SetTitle("METx, METy")
    histo_metxy_EE.GetXaxis().SetTitle("#sum ET")
    ROOT.gStyle.SetOptStat()
    c1.SaveAs("../pics/res_met_"  + str(i_jet) + "j_Zee_mm.pdf")

    nBinsX = histo_metxy_EE.GetNbinsX()
    nBinsY = histo_metxy_EE.GetNbinsY()
    print "nBinsY = ", nBinsY
    graph = ROOT.TGraphErrors()
    

    for i_bin in range(1, nBinsX+1):
      print "bin ", i_bin, " --------------------------"
      c1 = ROOT.TCanvas(histoname_metxy_EE + "_MM" + str(i_bin), histoname_metxy_EE + "_MM" + str(i_bin),  600, 600)
      histo_metxy1D = histo_metxy_EE.ProjectionY(histoname_metxy_EE + "_MM" + "_1D_" + str(i_bin), i_bin, i_bin)
      histo_metxy1D.Draw("")
      if histo_metxy1D.Integral(0, 201)>0:
	for ebin in range(1, 99):
	  ratio = histo_metxy1D.Integral(100 - ebin, 100 + ebin) / histo_metxy1D.Integral(0, 201)
	  
	  if ratio >= 0.8:
	    print "ratio = ", ratio
	    pos_rangelimit = 100 + ebin
	    neg_rangelimit = 100 - ebin
	    break
      else:
	pos_rangelimit = 100
	neg_rangelimit = 100
      print "pos_rangelimit= ", pos_rangelimit, " neg_rangelimit= ", neg_rangelimit  
      gaussfit = ROOT.TF1("gauss", "[0] / sqrt(2.0 * TMath::Pi()) / [2] * exp(-(x-[1])*(x-[1])/2./[2]/[2])", 0, 500)
      gaussfit.SetParameters(7000.,5.,5)                                                                  
      gaussfit.SetParName(0,"A");
      gaussfit.SetParName(1,"#mu");
      gaussfit.SetParName(2,"#sigma");
      gaussfit.SetLineColor(ROOT.kRed)
      ROOT.gStyle.SetStatFontSize(0.13)
      ROOT.gStyle.SetOptFit(1)
      ROOT.gStyle.SetOptStat()    
      
      print "SetRange(", -100 + neg_rangelimit * 200/nBinsY, ", ", -100 + pos_rangelimit * 200/nBinsY
      gaussfit.SetRange(-100 + neg_rangelimit * 200/nBinsY, -100 + pos_rangelimit * 200/nBinsY)
      histo_metxy1D.Fit("gauss", "R")
      gaussfit.Draw("same")
      mu = gaussfit.GetParameter(1)
      sigma = gaussfit.GetParameter(2)
      sigma_error = gaussfit.GetParError(2)
      line = ROOT.TLine(10. ,0. , 10., histo_metxy1D.GetMaximum())
      line.SetLineWidth(5)
      line.SetLineColor(ROOT.kBlue+2)
      histo_metxy1D.Draw("")
      histo_metxy1D.SetTitle(histoname_metxy_EE + "_MM" + str(i_bin))
      
      print "entries: ", histo_metxy1D.GetEntries()
      if abs(mu) < 5. and histo_metxy1D.GetEntries() > 1000.:
	graph.SetPoint(i_bin -1, (i_bin*2000/nBinsX)-(2000/nBinsX/2), sigma)    
	graph.SetPointError(i_bin -1, 0, sigma_error)    
	print "SetPoint ", i_bin-1, " x= ", (i_bin*2000/nBinsX)-(2000/nBinsX/2), " y= ", sigma
      else:    
	print "NOT USED"
	text1 = ROOT.TText(5, histo_metxy1D.GetMaximum()/2, "NOT USED")
	text1.SetTextColor(ROOT.kRed)
	text1.Draw("same")
      print data_type[i_f]
      c1.SaveAs("../pics/gausfit_Zee_mm_" + str(i_bin) + "_" + str(i_jet) + "j_" + data_type[i_f] + "_varBins.pdf")
    c1 = ROOT.TCanvas("TGraph", "TGraph", 600, 600)
    graph.Draw("ALP")
    graph.SetTitle("Zee_mm_"+ str(i_jet) + "j_" + data_type[i_f] + "_varBins")
    fit = ROOT.TF1("myfit","[0] + [1]*sqrt(x)", 0, 2000);
    fit.SetParName(0,"p0");
    fit.SetParName(1,"p1");
    fit.SetLineColor(ROOT.kGreen)
    ROOT.gStyle.SetOptFit(1);
    ROOT.gStyle.SetOptStat()
    graph.Fit("myfit")
    p0_param = fit.GetParameter(0)
    p0_param_err = fit.GetParError(0)
    p1_param = fit.GetParameter(1)
    p1_param_err = fit.GetParError(1)
    f.write("newline " + str(i_jet) + " jets: p0 = " + str(round(p0_param,3)) + " +/- " + str(round(p0_param_err, 3)) + ", p1 = " + str(round(p1_param,3)) + " +/- " + str(round(p1_param_err, 3)) + ", \n")
    fit.Draw("same")
    ROOT.gStyle.SetOptStat()
    c1.SaveAs("../pics/gausfit_Zee_mm_profile_" + str(i_jet) + "j_" + data_type[i_f] + "_varBins.pdf")

  inputfile.Close()
  f.close()
print "FINISHED"


