#!/usr/bin/env python
import ROOT
#import "RooStats/NumberCountingUtils.h"


inputfile = ROOT.TFile("/data/etp/jwittkowski/analysis_SUSYTools_03_04_neu/histos_Zmm_METresolution_merged_25GeV.root")

#histoname_ptel0 = "h_ptel0_3j_3j"
#histo_ptel0 = inputfile.Get(histoname_ptel0)
#histo_ptel0.Print()
#c1 = ROOT.TCanvas(histoname_ptel0, histoname_ptel0,  600, 600)
#histo_ptel0.Draw()
#c1.SaveAs("../pics/ptel0_3j_Zmm.pdf")

#histoname_mee = "h_mee_3j"
#histo_mee = inputfile.Get(histoname_mee)
#histo_mee.Print()
#c1 = ROOT.TCanvas(histoname_mee, histoname_mee,  600, 600)
#histo_mee.Draw()
#c1.SaveAs("../pics/mee_Zmm.pdf")

#histoname_ptel1 = "h_ptel1_3j"
#histo_ptel1 = inputfile.Get(histoname_ptel1)
#histo_ptel1.Print()
#c1 = ROOT.TCanvas(histoname_ptel1, histoname_ptel1,  600, 600)
#histo_ptel1.Draw()
#c1.SaveAs("../pics/ptel1_3j_Zmm.pdf")

histoname_metxy = "h_metxy_sumet_3j_MM"
#histoname_metxy_SS = "h_metxy_sumet_3j_SS_MM"
histo_metxy = inputfile.Get(histoname_metxy)
#histo_metxy_SS = inputfile.Get(histoname_metxy_SS)
histo_metxy.Print()
#histo_metxy.Add(histo_metxy_SS, -1)
histo_metxy.Rebin2D(20, 1)

#histo_metxy_SS.Draw("col")
#c1.SaveAs("../pics/res_met_3j_Zmm.pdf")

nBins = histo_metxy.GetNbinsX()
graph = ROOT.TGraphErrors()

for i_bin in range(1, nBins):
  c1 = ROOT.TCanvas(histoname_metxy + str(i_bin), histoname_metxy + str(i_bin),  600, 600)
  histo_metxy1D = histo_metxy.ProjectionY(histoname_metxy + "_1D_" + str(i_bin), i_bin, i_bin)
  histo_metxy1D.Rebin(5)
  histo_metxy1D.Draw("")
 
  gaussfit = ROOT.TF1("gauss", "[0] / sqrt(2.0 * TMath::Pi()) / [2] * exp(-(x-[1])*(x-[1])/2./[2]/[2])", 0, 500)
  gaussfit.SetParameters(7000.,5.,5)                                                                  
  gaussfit.SetParName(0,"A");
  gaussfit.SetParName(1,"#mu");
  gaussfit.SetParName(2,"#sigma");
  gaussfit.SetLineColor(ROOT.kRed)
  ROOT.gStyle.SetStatFontSize(0.13)
  ROOT.gStyle.SetOptFit(1)
  ROOT.gStyle.SetOptStat()
  gaussfit.SetRange(-40, 40)
  #if v=="mZTT_coll":
  #gaussfit.SetRange(40, 130)
  #if v=="mZTT_mmc":
  #gaussfit.SetRange(5, 200)
  #if v=="mZTT_missMassCalc":
  #gaussfit.SetRange(5, 200)
  histo_metxy1D.Fit("gauss", "R")
  gaussfit.Draw("same")
  mu = gaussfit.GetParameter(1)
  sigma = gaussfit.GetParameter(2)
  print "chi square= ", gaussfit.GetChisquare()
  line = ROOT.TLine(10. ,0. , 10., histo_metxy1D.GetMaximum())
  line.SetLineWidth(5)
  line.SetLineColor(ROOT.kBlue+2)
  #line.Draw("same")
  histo_metxy1D.Draw("")
  histo_metxy1D.SetTitle(histoname_metxy + str(i_bin))
  c1.SaveAs("../pics/gausfit_Zmm_" + str(i_bin) + "_3j.pdf")
  if histo_metxy1D.GetEntries() > 1000:
    graph.SetPoint(i_bin -1, (i_bin*50)-25, abs(mu))
  
    print "SetPoint ", i_bin-1, " x= ", (i_bin*50)-25, " y= ", abs(mu), " error = ", sigma
    graph.SetPointError(i_bin -1, 0, sigma)
c1 = ROOT.TCanvas("TGraphErrors", "TGraphErrors", 600, 600)
graph.Draw("ALP")
fit = ROOT.TF1("myfit","[0] + [1]*sqrt(x)", 0, 100);
fit.SetParName(0,"p0");
fit.SetParName(1,"p1");
fit.SetLineColor(ROOT.kGreen)
ROOT.gStyle.SetOptFit(1);
ROOT.gStyle.SetOptStat()
graph.Fit("myfit")
fit.Draw("same")
c1.SaveAs("../pics/gausfit_Zmm_profile_3j.pdf")

inputfile.Close()
print "FINISHED"

