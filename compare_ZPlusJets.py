#!/usr/bin/env python
import ROOT
ROOT.gROOT.ProcessLine("gROOT->SetBatch()")



names_of_old_file = ["/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_ZPlusJetsOLD_bgTable.root"]
names_of_new_file = ["/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_ZPlusJetsNEW_bgTable.root"]		
		
		  
name_of_variables = ["pTl0", "pTl1", "HT", "mll", "METrel", "mWWt", "mT2J", "Mljj", "Mlj", "mTlmax", "mTlmin", "DeltaEtall", "Mlj"]
name_of_SR = ["MM_SRSS1"]

x_axis_title = ["pTl0", "pTl1", "HT", "mll", "METrel", "mWWt", "mT2J", "Mljj", "Mlj", "mTlmax", "mTlmin", "DeltaEtall", "Mlj"]

#which bin will be used for projection:
ybinProj = 17

ybinProj_list = [ybinProj]

fillColors = [ROOT.kBlue-2, ROOT.kRed+1, ROOT.kOrange-2, ROOT.kSpring+1, ROOT.kGray+1, ROOT.kRed-1, ROOT.kRed-4,  ROOT.kCyan-2]

rootfiles_old = []
rootfiles_new = []

for f in names_of_old_file:
  rootfiles_old.append(ROOT.TFile(f))
for f in names_of_new_file:
  rootfiles_new.append(ROOT.TFile(f))

#loop over signal regions:  
for i_s, s in enumerate(name_of_SR):
  #loop over variables  
  for i_v, v in enumerate(name_of_variables):
    histoname = "h_" + v + "_" + s
    print "histoname", histoname
    
    histo_new = rootfiles_new[0].Get(histoname)
    histo_new.Print()
    
    histo_old = rootfiles_old[0].Get(histoname)

    
    c1 = ROOT.TCanvas("data_old_" + histoname, "data_old_" + histoname, 600, 600)
    pad1 = ROOT.TPad("pad1","pad1",0.0,0.3,1.0,1.0,21)
    pad1.Draw()
    pad1.SetLogy(1)
    pad1.SetRightMargin(0.1)
    pad1.SetFillColor(ROOT.kWhite)
    pad1.SetBottomMargin(0.01)


    pad2 = ROOT.TPad("pad2","pad2",0.0,0.0,1.0,0.3,22)
    pad2.SetRightMargin(0.1)
    pad2.Draw()
    pad2.SetFillColor(ROOT.kWhite)
    pad2.SetTopMargin(0.05)
    pad2.SetBottomMargin(0.5)
    pad1.cd()
    #draw here your data and old
    histo_old_1D = histo_old.ProjectionX(histoname + "_old_1D_", ybinProj_list[i_s], ybinProj_list[i_s])
    histo_old_1D.Rebin(2)
    histo_new_1D = histo_new.ProjectionX(histoname + "_new_1D_", ybinProj_list[i_s], ybinProj_list[i_s])
    histo_new_1D.Rebin(2)
    #histo_old_1D.Rebin(5)
    #histo_new.Rebin(5)
    #histo_old_1D.SetFillColor(ROOT.kBlue)
    #histo_old_1D.GetXaxis().SetRangeUser(0, 200)
    histo_old_1D.Draw("")
    histo_old_1D.SetTitle(x_axis_title[i_v] + " " + s)
    histo_new_1D.SetLineColor(ROOT.kRed)
    histo_new_1D.Draw("samel")
    #histo_new_1D.GetXaxis().SetTitle(x_axis_title[i_v])
    #histo_new_1D.SetTitle(x_axis_titlei_v[i_h])

    leg1 = ROOT.TLegend(0.5,0.6,0.99,0.9)
    leg1.SetFillColor(0)
    leg1.SetTextSize(0.025)
    leg1.AddEntry(histo_new_1D,"new","l")
    leg1.AddEntry(histo_old_1D,"old","l")
    leg1.Draw("same")

    pad2.cd()
    histo_ratio = histo_new_1D.Clone();
    histo_ratio.Divide(histo_old_1D)
    histo_ratio.GetYaxis().SetRangeUser(0, 2)
    histo_ratio.GetYaxis().SetTitle("new / old")
    #histo_ratio.GetXaxis().SetRangeUser(0, 200)
    histo_ratio.SetLineColor(ROOT.kBlack)
    ROOT.gStyle.SetOptStat(0)
    histo_ratio.SetTitle("")
    histo_ratio.Draw("e")
    print "histo_ratio.GetXaxis().GetXmax()", histo_ratio.GetXaxis().GetXmax()
    line1 = ROOT.TLine(0 ,1.0 , histo_ratio.GetXaxis().GetXmax(), 1.0)
    line1.SetLineWidth(1)
    line1.SetLineStyle(9)
    line1.SetLineColor(ROOT.kRed)
    line1.Draw("same")
    
    c1.SaveAs("../pics/compare_new_old_ZPlusJets_" + v + "_" + s + ".pdf")



  #here I draw the pad with new/old plot. what you will probably have to adapt is the histograms, which are for me histo_new and histo_mc (histogram with sum of all SM backgrounds)
    
  #c1.update()
  

for f in rootfiles_old:
  f.Close()
for f in rootfiles_new:
  f.Close()
  #print "FINISHED"