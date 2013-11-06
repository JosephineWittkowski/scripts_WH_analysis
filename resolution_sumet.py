#!/usr/bin/env python
import ROOT
import numpy 

n = 44
x = numpy.array([108., 130., 150., 170., 195., 205., 228., 251., 275., 292., 302., 337., 
350., 365., 392., 410., 430., 450., 475., 488., 515., 530., 
550., 565., 590., 610., 630., 650., 670., 688., 708., 730., 750., 770., 
797., 810., 835., 850., 870., 895., 910., 930., 950., 965.
], 'd')
y = numpy.array([8.65, 10.05, 10.95, 10.95, 11.4, 11.95, 11.95, 12.5, 13.0, 13.0, 13.5, 13.8, 
14.1, 14.0, 14.6, 14.6, 14.9, 15.3, 15.8, 15.9, 16.15, 16.45, 
16.45, 16.95, 16.90, 17.55, 18.1, 18.05, 18.50, 19.0, 19.0, 20.05, 19.5, 19.6, 
20.5, 20.8, 20.6, 21.8, 21.0, 22.60, 22.8, 22.6, 23.15, 22.7
], 'd')

graph = ROOT.TGraph(n, x, y)

graph.SetMarkerStyle(ROOT.kFullCircle)
#graph.SetMarkerSize(1)
graph.SetLineColor(ROOT.kBlack)
graph.SetLineWidth(2)
canvas=ROOT.TCanvas("canvas","Guckmal!")
graph.GetXaxis().SetRange(0, 1200)
graph.Draw("ALP")
graph.GetXaxis().SetTitle("sumET")

graph.GetYaxis().SetTitle("resolution")

fit = ROOT.TF1("myfit","[0] + [1]*sqrt(x)", 0, 100);
fit.SetParName(0,"p0");
fit.SetParName(1,"p1");
fit.SetLineColor(ROOT.kRed)
gStyle.SetOptFit(1011);
ROOT.gStyle.SetOptStat()
graph.Fit("myfit")
fit.Draw("same")


canvas.SaveAs("../pics/res_sumet.pdf")
