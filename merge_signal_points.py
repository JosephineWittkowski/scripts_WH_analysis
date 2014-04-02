import ROOT
  
Egammafile1 = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_fake_Egamma_bgTable_1.root")
Egammafile2 = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_fake_Egamma_bgTable_2.root")
Egammafile3 = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_fake_Egamma_bgTable_3.root")
Egammafile4 = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_fake_Egamma_bgTable_4.root")
Egammafile5 = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_fake_Egamma_bgTable_5.root")
Egammafile6 = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_fake_Egamma_bgTable_6.root")

Muonfile1 = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_fake_Muons_bgTable_1.root")
Muonfile2 = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_fake_Muons_bgTable_2.root")
Muonfile3 = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_fake_Muons_bgTable_3.root")
Muonfile4 = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_fake_Muons_bgTable_4.root")
Muonfile5 = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_fake_Muons_bgTable_5.root")
Muonfile6 = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_fake_Muons_bgTable_6.root")


fm = ROOT.TFileMerger(ROOT.kFALSE)
fm.OutputFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_fake_bgTable.root")
fm.AddFile(Egammafile1)
fm.AddFile(Egammafile2)
fm.AddFile(Egammafile3)
fm.AddFile(Egammafile4)
fm.AddFile(Egammafile5)
fm.AddFile(Egammafile6)
fm.AddFile(Muonfile1)
fm.AddFile(Muonfile2)
fm.AddFile(Muonfile3)
fm.AddFile(Muonfile4)
fm.AddFile(Muonfile5)
fm.AddFile(Muonfile6)
fm.PartialMerge()  

Egammafile1.Close()
Egammafile2.Close()
Egammafile3.Close()
Egammafile4.Close()
Egammafile5.Close()
Egammafile6.Close()
Muonfile1.Close()
Muonfile2.Close()
Muonfile3.Close()
Muonfile4.Close()
Muonfile5.Close()
Muonfile6.Close()


ZPlusJetsfile1 = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_ZPlusJetsNEW_bgTable_split1.root")
ZPlusJetsfile2 = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_ZPlusJetsNEW_bgTable_split2.root")
ZPlusJetsfile3 = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_ZPlusJetsNEW_bgTable_split3.root")
ZPlusJetsfile4 = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_ZPlusJetsNEW_bgTable_split4.root")


fm = ROOT.TFileMerger(ROOT.kFALSE)
fm.OutputFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04/histos_ZN_ZPlusJetsNEW_bgTable.root")

fm.AddFile(ZPlusJetsfile1)
fm.AddFile(ZPlusJetsfile2)
fm.AddFile(ZPlusJetsfile3)
fm.AddFile(ZPlusJetsfile4)

fm.PartialMerge()  

ZPlusJetsfile1.Close()
ZPlusJetsfile2.Close()
ZPlusJetsfile3.Close()
ZPlusJetsfile4.Close()

  
print "finished!"