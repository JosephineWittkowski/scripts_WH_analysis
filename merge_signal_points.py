import ROOT
#from gridCoord import getGridCoordinates, reqidByMc1Mn1

#doMerge = 1

#names_of_merged_grid_points = [1765700, 1765800, 1765900, 1766000, 1766100, 1766200, 1766300]
#number_of_points = [0, 0, 0, 0, 0, 0, 0]
#filenames = []
#mcids = []
#for mcid in range(176574, 176641):
  #if mcid == 176585 or mcid == 176614:
    #continue
  #filenames.append(ROOT.TFile("/data/etp/jwittkowski/outputfiles/histos_ZN_signal_" + str(mcid) + ".root"))
  #mcids.append(mcid)
  
##print filenames

#if doMerge:
  #print "MERGING MERGING MERGING"
  #filemergers = []
  #for r in range(0,7):
    #filemerger = ROOT.TFileMerger(ROOT.kFALSE)
    #filemerger.OutputFile("/data/etp/jwittkowski/outputfiles/histos_ZN_signal_merged_" + str(r+1) + ".root")
    #filemergers.append(filemerger)
  
#bincontent = [0., 0., 0., 0., 0., 0., 0.] 
#for i_f, filename in enumerate(filenames):
  ##if i_f == 11 or i_f == 40:
    ##continue
  
  ##filename.Print()
  ##histo = filename.Get("h_N_events_MM")
  #mcid = mcids[i_f]
  
  

  ##print "mcid= ", mcid
  #xcoord, ycoord, xsec = getGridCoordinates(mcid)
  #r = reqidByMc1Mn1(xcoord, ycoord)
  #print "r= ", r, ", mcid= ", mcid
  ##bincontent[r] += histo.Integral(mcid-99999, mcid-99999, 1, 1)
  ##print getGridCoordinates(mcid)
  ##openedFile = ROOT.TFile(filename)
  ##filename.Print()
  #number_of_points[r] += 1
  #if doMerge:
    #filemergers[r].AddFile(filename)
#if doMerge:
  #for r in range(0,7):
    #filemergers[r].PartialMerge()
  
#for filename in (filenames):
  #filename.Close()
#print number_of_points

#filenames_merged = []
#for r in range(0,7):
  #print "bincontent= ", bincontent[r]
  #filename_merged = ROOT.TFile("/data/etp/jwittkowski/outputfiles/histos_ZN_signal_merged_" + str(r+1) + ".root")
  #filenames_merged.append(filename_merged)
  #histo = filenames_merged[r].Get("h_N_events_MM")
  #print "r= ", r, ", content= ", histo.Integral(0, 99999, 1, 1)
  
Egammafile1 = ROOT.TFile("/data/etp/jwittkowski/outputfiles/histos_fake_Egamma_woJOR_1.root")
Egammafile2 = ROOT.TFile("/data/etp/jwittkowski/outputfiles/histos_fake_Egamma_woJOR_2.root")
Egammafile3 = ROOT.TFile("/data/etp/jwittkowski/outputfiles/histos_fake_Muons_woJOR_3.root")

Muonfile1 = ROOT.TFile("/data/etp/jwittkowski/outputfiles/histos_fake_Muons_woJOR_1.root")
Muonfile2 = ROOT.TFile("/data/etp/jwittkowski/outputfiles/histos_fake_Muons_woJOR_2.root")
Muonfile3 = ROOT.TFile("/data/etp/jwittkowski/outputfiles/histos_fake_Muons_woJOR_3.root")


fm = ROOT.TFileMerger(ROOT.kFALSE)
fm.OutputFile("/data/etp/jwittkowski/outputfiles/histos_ZN_fakebg_woJOR.root")
fm.AddFile(Egammafile1)
fm.AddFile(Egammafile2)
fm.AddFile(Egammafile3)
fm.AddFile(Muonfile1)
fm.AddFile(Muonfile2)
fm.AddFile(Muonfile3)
fm.PartialMerge()  

Egammafile1.Close()
Egammafile2.Close()
Egammafile3.Close()
Muonfile1.Close()
Muonfile2.Close()
Muonfile3.Close()
  
print "finished!"