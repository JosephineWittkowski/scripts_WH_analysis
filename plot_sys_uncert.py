import ROOT
#file = ROOT.TFile("/data/etp/jwittkowski/outputfiles/histos_ZN_WZ_tauWZ.root")


file_NtSys_Nom          = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_0.root")
file_NtSys_EES_Z_UP     = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_1.root") 
file_NtSys_EES_Z_DN     = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_2.root") 
file_NtSys_EES_MAT_UP   = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_3.root") 
file_NtSys_EES_MAT_DN   = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_4.root") 
file_NtSys_EES_PS_UP    = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_5.root") 
file_NtSys_EES_PS_DN    = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_6.root") 
file_NtSys_EES_LOW_UP   = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_7.root") 
file_NtSys_EES_LOW_DN   = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_8.root") 
file_NtSys_EER_UP       = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_9.root") 
file_NtSys_EER_DN       = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_10.root")
file_NtSys_MS_UP        = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_11.root")
file_NtSys_MS_DN        = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_12.root")
file_NtSys_ID_UP        = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_13.root")
file_NtSys_ID_DN        = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_14.root")
file_NtSys_JES_UP       = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_15.root")
file_NtSys_JES_DN       = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_16.root")
file_NtSys_JER          = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_17.root")
file_NtSys_SCALEST_UP   = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_18.root")
file_NtSys_SCALEST_DN   = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_19.root")
file_NtSys_RESOST       = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_20.root")
file_NtSys_TRIGSF_EL_UP = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_21.root")
file_NtSys_TRIGSF_EL_DN = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_22.root")
file_NtSys_TRIGSF_MU_UP = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_23.root")
file_NtSys_TRIGSF_MU_DN = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_24.root")
file_NtSys_TES_UP       = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_25.root")
file_NtSys_TES_DN       = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_26.root")
file_BTag_BJet_DN       = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_27.root")
file_BTag_CJet_DN       = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_28.root")
file_BTag_LJet_DN       = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_29.root")
file_BTag_BJet_UP       = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_30.root")
file_BTag_CJet_UP       = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_31.root")
file_BTag_LJet_UP       = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_32.root")
file_BKGMETHOD_UP       = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_33.root")
file_BKGMETHOD_DN       = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_34.root")
file_SYS_EL_RE_UP       = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_35.root")
file_SYS_EL_RE_DOWN     = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_36.root")
file_SYS_EL_FR_UP       = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_37.root")
file_SYS_EL_FR_DOWN     = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_38.root")
file_SYS_MU_RE_UP       = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_39.root")
file_SYS_MU_RE_DOWN     = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_40.root")
file_SYS_MU_FR_UP       = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_41.root")
file_SYS_MU_RE_DOWN     = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_42.root")
file_el_eff_up          = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_43.root")
file_el_eff_dn          = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_44.root")
file_mu_eff_up          = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_45.root")
file_mu_eff_dn          = ROOT.TFile("/data/etp3/jwittkow/analysis_SUSYTools_03_04_SusyNt_01_16/histos_ZN_177501_n0150_sysUncert_46.root")







histoname_EE = "cutflow_EE_sysUncert"
histoname_MM = "cutflow_MM_sysUncert"
histoname_EM = "cutflow_EM_sysUncert"

print " =================================================      EE ========================================================== "
print "NtSys_NOM          ", round(file_NtSys_Nom         .Get(histoname_EE).Integral(34,34, 1 , 1 ), 4), round(file_NtSys_Nom         .Get(histoname_EE).Integral(42,42, 1 , 1 ), 4)
print "NtSys_EES_Z_UP     ", round(file_NtSys_EES_Z_UP    .Get(histoname_EE).Integral(34,34, 2 , 2 ), 4), round(file_NtSys_EES_Z_UP    .Get(histoname_EE).Integral(42,42, 2 , 2 ), 4)
print "NtSys_EES_Z_DN     ", round(file_NtSys_EES_Z_DN    .Get(histoname_EE).Integral(34,34, 3 , 3 ), 4), round(file_NtSys_EES_Z_DN    .Get(histoname_EE).Integral(42,42, 3 , 3 ), 4)
print "NtSys_EES_MAT_UP   ", round(file_NtSys_EES_MAT_UP  .Get(histoname_EE).Integral(34,34, 4 , 4 ), 4), round(file_NtSys_EES_MAT_UP  .Get(histoname_EE).Integral(42,42, 4 , 4 ), 4)
print "NtSys_EES_MAT_DN   ", round(file_NtSys_EES_MAT_DN  .Get(histoname_EE).Integral(34,34, 5 , 5 ), 4), round(file_NtSys_EES_MAT_DN  .Get(histoname_EE).Integral(42,42, 5 , 5 ), 4)
print "NtSys_EES_PS_UP    ", round(file_NtSys_EES_PS_UP   .Get(histoname_EE).Integral(34,34, 6 , 6 ), 4), round(file_NtSys_EES_PS_UP   .Get(histoname_EE).Integral(42,42, 6 , 6 ), 4)
print "NtSys_EES_PS_DN    ", round(file_NtSys_EES_PS_DN   .Get(histoname_EE).Integral(34,34, 7 , 7 ), 4), round(file_NtSys_EES_PS_DN   .Get(histoname_EE).Integral(42,42, 7 , 7 ), 4)
print "NtSys_EES_LOW_UP   ", round(file_NtSys_EES_LOW_UP  .Get(histoname_EE).Integral(34,34, 8 , 8 ), 4), round(file_NtSys_EES_LOW_UP  .Get(histoname_EE).Integral(42,42, 8 , 8 ), 4)
print "NtSys_EES_LOW_DN   ", round(file_NtSys_EES_LOW_DN  .Get(histoname_EE).Integral(34,34, 9 , 9 ), 4), round(file_NtSys_EES_LOW_DN  .Get(histoname_EE).Integral(42,42, 9 , 9 ), 4)
print "NtSys_EER_UP       ", round(file_NtSys_EER_UP      .Get(histoname_EE).Integral(34,34, 10, 10), 4), round(file_NtSys_EER_UP      .Get(histoname_EE).Integral(42,42, 10, 10), 4)
print "NtSys_EER_DN       ", round(file_NtSys_EER_DN      .Get(histoname_EE).Integral(34,34, 11, 11), 4), round(file_NtSys_EER_DN      .Get(histoname_EE).Integral(42,42, 11, 11), 4)
print "NtSys_MS_UP        ", round(file_NtSys_MS_UP       .Get(histoname_EE).Integral(34,34, 12, 12), 4), round(file_NtSys_MS_UP       .Get(histoname_EE).Integral(42,42, 12, 12), 4)
print "NtSys_MS_DN        ", round(file_NtSys_MS_DN       .Get(histoname_EE).Integral(34,34, 13, 13), 4), round(file_NtSys_MS_DN       .Get(histoname_EE).Integral(42,42, 13, 13), 4)
print "NtSys_ID_UP        ", round(file_NtSys_ID_UP       .Get(histoname_EE).Integral(34,34, 14, 14), 4), round(file_NtSys_ID_UP       .Get(histoname_EE).Integral(42,42, 14, 14), 4)
print "NtSys_ID_DN        ", round(file_NtSys_ID_DN       .Get(histoname_EE).Integral(34,34, 15, 15), 4), round(file_NtSys_ID_DN       .Get(histoname_EE).Integral(42,42, 15, 15), 4)
print "NtSys_JES_UP       ", round(file_NtSys_JES_UP      .Get(histoname_EE).Integral(34,34, 16, 16), 4), round(file_NtSys_JES_UP      .Get(histoname_EE).Integral(42,42, 16, 16), 4)
print "NtSys_JES_DN       ", round(file_NtSys_JES_DN      .Get(histoname_EE).Integral(34,34, 17, 17), 4),  round(file_NtSys_JES_DN      .Get(histoname_EE).Integral(42,42,17, 17 ), 4)
print "NtSys_JER          ", round(file_NtSys_JER         .Get(histoname_EE).Integral(34,34, 18, 18), 4),  round(file_NtSys_JER         .Get(histoname_EE).Integral(42,42,18, 18 ), 4)
print "NtSys_SCALEST_UP   ", round(file_NtSys_SCALEST_UP  .Get(histoname_EE).Integral(34,34, 19, 19), 4),  round(file_NtSys_SCALEST_UP  .Get(histoname_EE).Integral(42,42,19, 19 ), 4)
print "NtSys_SCALEST_DN   ", round(file_NtSys_SCALEST_DN  .Get(histoname_EE).Integral(34,34,20, 20 ), 4),  round(file_NtSys_SCALEST_DN  .Get(histoname_EE).Integral(42,42, 20, 20 ), 4)
print "NtSys_RESOST       ", round(file_NtSys_RESOST      .Get(histoname_EE).Integral(34,34, 21, 21), 4),  round(file_NtSys_RESOST      .Get(histoname_EE).Integral(42,42,21, 21 ), 4)
print "NtSys_TRIGSF_EL_UP ", round(file_NtSys_TRIGSF_EL_UP.Get(histoname_EE).Integral(34,34, 22, 22), 4),  round(file_NtSys_TRIGSF_EL_UP.Get(histoname_EE).Integral(42,42,22, 22 ), 4)
print "NtSys_TRIGSF_EL_DN ", round(file_NtSys_TRIGSF_EL_DN.Get(histoname_EE).Integral(34,34, 23, 23), 4),  round(file_NtSys_TRIGSF_EL_DN.Get(histoname_EE).Integral(42,42,23, 23 ), 4)
print "NtSys_TRIGSF_MU_UP ", round(file_NtSys_TRIGSF_MU_UP.Get(histoname_EE).Integral(34,34, 24, 24), 4),  round(file_NtSys_TRIGSF_MU_UP.Get(histoname_EE).Integral(42,42,24, 24 ), 4)
print "NtSys_TRIGSF_MU_DN ", round(file_NtSys_TRIGSF_MU_DN.Get(histoname_EE).Integral(34,34, 25, 25), 4),  round(file_NtSys_TRIGSF_MU_DN.Get(histoname_EE).Integral(42,42,25, 25 ), 4)
print "NtSys_TES_UP       ", round(file_NtSys_TES_UP      .Get(histoname_EE).Integral(34,34, 26, 26), 4),  round(file_NtSys_TES_UP      .Get(histoname_EE).Integral(42,42,26, 26 ), 4)
print "NtSys_TES_DN       ", round(file_NtSys_TES_DN      .Get(histoname_EE).Integral(34,34, 27, 27), 4),  round(file_NtSys_TES_DN      .Get(histoname_EE).Integral(42,42,27, 27 ), 4)
print "BTag_BJet_DN       ", round(file_BTag_BJet_DN      .Get(histoname_EE).Integral(34,34, 28, 28), 4),  round(file_BTag_BJet_DN      .Get(histoname_EE).Integral(42,42,28, 28 ), 4)
print "BTag_CJet_DN       ", round(file_BTag_CJet_DN      .Get(histoname_EE).Integral(34,34, 29, 29), 4),  round(file_BTag_CJet_DN      .Get(histoname_EE).Integral(42,42,29, 29 ), 4)
print "BTag_LJet_DN       ", round(file_BTag_LJet_DN      .Get(histoname_EE).Integral(34,34, 30, 30), 4),  round(file_BTag_LJet_DN      .Get(histoname_EE).Integral(42,42,30, 30 ), 4)
print "BTag_BJet_UP       ", round(file_BTag_BJet_UP      .Get(histoname_EE).Integral(34,34, 31, 31), 4),  round(file_BTag_BJet_UP      .Get(histoname_EE).Integral(42,42,31, 31 ), 4)
print "BTag_CJet_UP       ", round(file_BTag_CJet_UP      .Get(histoname_EE).Integral(34,34, 32, 32), 4),  round(file_BTag_CJet_UP      .Get(histoname_EE).Integral(42,42,32, 32 ), 4)
print "BTag_LJet_UP       ", round(file_BTag_LJet_UP      .Get(histoname_EE).Integral(34,34, 33, 33), 4),  round(file_BTag_LJet_UP      .Get(histoname_EE).Integral(42,42,33, 33 ), 4)
print "BKGMETHOD_UP       ", round(file_BKGMETHOD_UP      .Get(histoname_EE).Integral(34,34, 34, 34), 4),  round(file_BKGMETHOD_UP      .Get(histoname_EE).Integral(42,42,34, 34 ), 4)
print "BKGMETHOD_DN       ", round(file_BKGMETHOD_DN      .Get(histoname_EE).Integral(34,34, 35, 35), 4),  round(file_BKGMETHOD_DN      .Get(histoname_EE).Integral(42,42,35, 35 ), 4)




                                                                                                                                          
print " "
print " "
print " =================================================      MM ========================================================== "
print "NtSys_NOM          ", round(file_NtSys_Nom         .Get(histoname_MM).Integral(32,32, 1 , 1 ), 4), round(file_NtSys_Nom         .Get(histoname_MM).Integral(41,41, 1 , 1 ), 4)
print "NtSys_EES_Z_UP     ", round(file_NtSys_EES_Z_UP    .Get(histoname_MM).Integral(32,32, 2 , 2 ), 4), round(file_NtSys_EES_Z_UP    .Get(histoname_MM).Integral(41,41, 2 , 2 ), 4)
print "NtSys_EES_Z_DN     ", round(file_NtSys_EES_Z_DN    .Get(histoname_MM).Integral(32,32, 3 , 3 ), 4), round(file_NtSys_EES_Z_DN    .Get(histoname_MM).Integral(41,41, 3 , 3 ), 4)
print "NtSys_EES_MAT_UP   ", round(file_NtSys_EES_MAT_UP  .Get(histoname_MM).Integral(32,32, 4 , 4 ), 4), round(file_NtSys_EES_MAT_UP  .Get(histoname_MM).Integral(41,41, 4 , 4 ), 4)
print "NtSys_EES_MAT_DN   ", round(file_NtSys_EES_MAT_DN  .Get(histoname_MM).Integral(32,32, 5 , 5 ), 4), round(file_NtSys_EES_MAT_DN  .Get(histoname_MM).Integral(41,41, 5 , 5 ), 4)
print "NtSys_EES_PS_UP    ", round(file_NtSys_EES_PS_UP   .Get(histoname_MM).Integral(32,32, 6 , 6 ), 4), round(file_NtSys_EES_PS_UP   .Get(histoname_MM).Integral(41,41, 6 , 6 ), 4)
print "NtSys_EES_PS_DN    ", round(file_NtSys_EES_PS_DN   .Get(histoname_MM).Integral(32,32, 7 , 7 ), 4), round(file_NtSys_EES_PS_DN   .Get(histoname_MM).Integral(41,41, 7 , 7 ), 4)
print "NtSys_EES_LOW_UP   ", round(file_NtSys_EES_LOW_UP  .Get(histoname_MM).Integral(32,32, 8 , 8 ), 4), round(file_NtSys_EES_LOW_UP  .Get(histoname_MM).Integral(41,41, 8 , 8 ), 4)
print "NtSys_EES_LOW_DN   ", round(file_NtSys_EES_LOW_DN  .Get(histoname_MM).Integral(32,32, 9 , 9 ), 4), round(file_NtSys_EES_LOW_DN  .Get(histoname_MM).Integral(41,41, 9 , 9 ), 4)
print "NtSys_EER_UP       ", round(file_NtSys_EER_UP      .Get(histoname_MM).Integral(32,32, 10, 10), 4), round(file_NtSys_EER_UP      .Get(histoname_MM).Integral(41,41, 10, 10), 4)
print "NtSys_EER_DN       ", round(file_NtSys_EER_DN      .Get(histoname_MM).Integral(32,32, 11, 11), 4), round(file_NtSys_EER_DN      .Get(histoname_MM).Integral(41,41, 11, 11), 4)
print "NtSys_MS_UP        ", round(file_NtSys_MS_UP       .Get(histoname_MM).Integral(32,32, 12, 12), 4), round(file_NtSys_MS_UP       .Get(histoname_MM).Integral(41,41, 12, 12), 4)
print "NtSys_MS_DN        ", round(file_NtSys_MS_DN       .Get(histoname_MM).Integral(32,32, 13, 13), 4), round(file_NtSys_MS_DN       .Get(histoname_MM).Integral(41,41, 13, 13), 4)
print "NtSys_ID_UP        ", round(file_NtSys_ID_UP       .Get(histoname_MM).Integral(32,32, 14, 14), 4), round(file_NtSys_ID_UP       .Get(histoname_MM).Integral(41,41, 14, 14), 4)
print "NtSys_ID_DN        ", round(file_NtSys_ID_DN       .Get(histoname_MM).Integral(32,32, 15, 15), 4), round(file_NtSys_ID_DN       .Get(histoname_MM).Integral(41,41, 15, 15), 4)
print "NtSys_JES_UP       ", round(file_NtSys_JES_UP      .Get(histoname_MM).Integral(32,32, 16, 16), 4), round(file_NtSys_JES_UP      .Get(histoname_MM).Integral(41,41, 16, 16), 4)
print "NtSys_JES_DN       ", round(file_NtSys_JES_DN      .Get(histoname_MM).Integral(32,32, 17, 17), 4),  round(file_NtSys_JES_DN      .Get(histoname_MM).Integral(41,41,17, 17 ), 4)
print "NtSys_JER          ", round(file_NtSys_JER         .Get(histoname_MM).Integral(32,32, 18, 18), 4),  round(file_NtSys_JER         .Get(histoname_MM).Integral(41,41,18, 18 ), 4)
print "NtSys_SCALEST_UP   ", round(file_NtSys_SCALEST_UP  .Get(histoname_MM).Integral(32,32, 19, 19), 4),  round(file_NtSys_SCALEST_UP  .Get(histoname_MM).Integral(41,41,19, 19 ), 4)
print "NtSys_SCALEST_DN   ", round(file_NtSys_SCALEST_DN  .Get(histoname_MM).Integral(32,32,20, 20 ), 4),  round(file_NtSys_SCALEST_DN  .Get(histoname_MM).Integral(41,41, 20, 20 ), 4)
print "NtSys_RESOST       ", round(file_NtSys_RESOST      .Get(histoname_MM).Integral(32,32, 21, 21), 4),  round(file_NtSys_RESOST      .Get(histoname_MM).Integral(41,41,21, 21 ), 4)
print "NtSys_TRIGSF_EL_UP ", round(file_NtSys_TRIGSF_EL_UP.Get(histoname_MM).Integral(32,32, 22, 22), 4),  round(file_NtSys_TRIGSF_EL_UP.Get(histoname_MM).Integral(41,41,22, 22 ), 4)
print "NtSys_TRIGSF_EL_DN ", round(file_NtSys_TRIGSF_EL_DN.Get(histoname_MM).Integral(32,32, 23, 23), 4),  round(file_NtSys_TRIGSF_EL_DN.Get(histoname_MM).Integral(41,41,23, 23 ), 4)
print "NtSys_TRIGSF_MU_UP ", round(file_NtSys_TRIGSF_MU_UP.Get(histoname_MM).Integral(32,32, 24, 24), 4),  round(file_NtSys_TRIGSF_MU_UP.Get(histoname_MM).Integral(41,41,24, 24 ), 4)
print "NtSys_TRIGSF_MU_DN ", round(file_NtSys_TRIGSF_MU_DN.Get(histoname_MM).Integral(32,32, 25, 25), 4),  round(file_NtSys_TRIGSF_MU_DN.Get(histoname_MM).Integral(41,41,25, 25 ), 4)
print "NtSys_TES_UP       ", round(file_NtSys_TES_UP      .Get(histoname_MM).Integral(32,32, 26, 26), 4),  round(file_NtSys_TES_UP      .Get(histoname_MM).Integral(41,41,26, 26 ), 4)
print "NtSys_TES_DN       ", round(file_NtSys_TES_DN      .Get(histoname_MM).Integral(32,32, 27, 27), 4),  round(file_NtSys_TES_DN      .Get(histoname_MM).Integral(41,41,27, 27 ), 4)
print "BTag_BJet_DN       ", round(file_BTag_BJet_DN      .Get(histoname_MM).Integral(32,32, 28, 28), 4),  round(file_BTag_BJet_DN      .Get(histoname_MM).Integral(41,41,28, 28 ), 4)
print "BTag_CJet_DN       ", round(file_BTag_CJet_DN      .Get(histoname_MM).Integral(32,32, 29, 29), 4),  round(file_BTag_CJet_DN      .Get(histoname_MM).Integral(41,41,29, 29 ), 4)
print "BTag_LJet_DN       ", round(file_BTag_LJet_DN      .Get(histoname_MM).Integral(32,32, 30, 30), 4),  round(file_BTag_LJet_DN      .Get(histoname_MM).Integral(41,41,30, 30 ), 4)
print "BTag_BJet_UP       ", round(file_BTag_BJet_UP      .Get(histoname_MM).Integral(32,32, 31, 31), 4),  round(file_BTag_BJet_UP      .Get(histoname_MM).Integral(41,41,31, 31 ), 4)
print "BTag_CJet_UP       ", round(file_BTag_CJet_UP      .Get(histoname_MM).Integral(32,32, 32, 32), 4),  round(file_BTag_CJet_UP      .Get(histoname_MM).Integral(41,41,32, 32 ), 4)
print "BTag_LJet_UP       ", round(file_BTag_LJet_UP      .Get(histoname_MM).Integral(32,32, 33, 33), 4),  round(file_BTag_LJet_UP      .Get(histoname_MM).Integral(41,41,33, 33 ), 4)
print "BKGMETHOD_UP       ", round(file_BKGMETHOD_UP      .Get(histoname_MM).Integral(32,32, 34, 34), 4),  round(file_BKGMETHOD_UP      .Get(histoname_MM).Integral(41,41,34, 34 ), 4)
print "BKGMETHOD_DN       ", round(file_BKGMETHOD_DN      .Get(histoname_MM).Integral(32,32, 35, 35), 4),  round(file_BKGMETHOD_DN      .Get(histoname_MM).Integral(41,41,35, 35 ), 4)
print " "
print " "
print " =================================================      EM ========================================================== "
print "NtSys_NOM          ", round(file_NtSys_Nom         .Get(histoname_EM).Integral(32,32, 1 , 1 ), 4), round(file_NtSys_Nom         .Get(histoname_EM).Integral(41,41, 1 , 1 ), 4)
print "NtSys_EES_Z_UP     ", round(file_NtSys_EES_Z_UP    .Get(histoname_EM).Integral(32,32, 2 , 2 ), 4), round(file_NtSys_EES_Z_UP    .Get(histoname_EM).Integral(41,41, 2 , 2 ), 4)
print "NtSys_EES_Z_DN     ", round(file_NtSys_EES_Z_DN    .Get(histoname_EM).Integral(32,32, 3 , 3 ), 4), round(file_NtSys_EES_Z_DN    .Get(histoname_EM).Integral(41,41, 3 , 3 ), 4)
print "NtSys_EES_MAT_UP   ", round(file_NtSys_EES_MAT_UP  .Get(histoname_EM).Integral(32,32, 4 , 4 ), 4), round(file_NtSys_EES_MAT_UP  .Get(histoname_EM).Integral(41,41, 4 , 4 ), 4)
print "NtSys_EES_MAT_DN   ", round(file_NtSys_EES_MAT_DN  .Get(histoname_EM).Integral(32,32, 5 , 5 ), 4), round(file_NtSys_EES_MAT_DN  .Get(histoname_EM).Integral(41,41, 5 , 5 ), 4)
print "NtSys_EES_PS_UP    ", round(file_NtSys_EES_PS_UP   .Get(histoname_EM).Integral(32,32, 6 , 6 ), 4), round(file_NtSys_EES_PS_UP   .Get(histoname_EM).Integral(41,41, 6 , 6 ), 4)
print "NtSys_EES_PS_DN    ", round(file_NtSys_EES_PS_DN   .Get(histoname_EM).Integral(32,32, 7 , 7 ), 4), round(file_NtSys_EES_PS_DN   .Get(histoname_EM).Integral(41,41, 7 , 7 ), 4)
print "NtSys_EES_LOW_UP   ", round(file_NtSys_EES_LOW_UP  .Get(histoname_EM).Integral(32,32, 8 , 8 ), 4), round(file_NtSys_EES_LOW_UP  .Get(histoname_EM).Integral(41,41, 8 , 8 ), 4)
print "NtSys_EES_LOW_DN   ", round(file_NtSys_EES_LOW_DN  .Get(histoname_EM).Integral(32,32, 9 , 9 ), 4), round(file_NtSys_EES_LOW_DN  .Get(histoname_EM).Integral(41,41, 9 , 9 ), 4)
print "NtSys_EER_UP       ", round(file_NtSys_EER_UP      .Get(histoname_EM).Integral(32,32, 10, 10), 4), round(file_NtSys_EER_UP      .Get(histoname_EM).Integral(41,41, 10, 10), 4)
print "NtSys_EER_DN       ", round(file_NtSys_EER_DN      .Get(histoname_EM).Integral(32,32, 11, 11), 4), round(file_NtSys_EER_DN      .Get(histoname_EM).Integral(41,41, 11, 11), 4)
print "NtSys_MS_UP        ", round(file_NtSys_MS_UP       .Get(histoname_EM).Integral(32,32, 12, 12), 4), round(file_NtSys_MS_UP       .Get(histoname_EM).Integral(41,41, 12, 12), 4)
print "NtSys_MS_DN        ", round(file_NtSys_MS_DN       .Get(histoname_EM).Integral(32,32, 13, 13), 4), round(file_NtSys_MS_DN       .Get(histoname_EM).Integral(41,41, 13, 13), 4)
print "NtSys_ID_UP        ", round(file_NtSys_ID_UP       .Get(histoname_EM).Integral(32,32, 14, 14), 4), round(file_NtSys_ID_UP       .Get(histoname_EM).Integral(41,41, 14, 14), 4)
print "NtSys_ID_DN        ", round(file_NtSys_ID_DN       .Get(histoname_EM).Integral(32,32, 15, 15), 4), round(file_NtSys_ID_DN       .Get(histoname_EM).Integral(41,41, 15, 15), 4)
print "NtSys_JES_UP       ", round(file_NtSys_JES_UP      .Get(histoname_EM).Integral(32,32, 16, 16), 4), round(file_NtSys_JES_UP      .Get(histoname_EM).Integral(41,41, 16, 16), 4)
print "NtSys_JES_DN       ", round(file_NtSys_JES_DN      .Get(histoname_EM).Integral(32,32, 17, 17), 4),  round(file_NtSys_JES_DN      .Get(histoname_EM).Integral(41,41,17, 17 ), 4)
print "NtSys_JER          ", round(file_NtSys_JER         .Get(histoname_EM).Integral(32,32, 18, 18), 4),  round(file_NtSys_JER         .Get(histoname_EM).Integral(41,41,18, 18 ), 4)
print "NtSys_SCALEST_UP   ", round(file_NtSys_SCALEST_UP  .Get(histoname_EM).Integral(32,32, 19, 19), 4),  round(file_NtSys_SCALEST_UP  .Get(histoname_EM).Integral(41,41,19, 19 ), 4)
print "NtSys_SCALEST_DN   ", round(file_NtSys_SCALEST_DN  .Get(histoname_EM).Integral(32,32,20, 20 ), 4),  round(file_NtSys_SCALEST_DN  .Get(histoname_EM).Integral(41,41, 20, 20), 4)
print "NtSys_RESOST       ", round(file_NtSys_RESOST      .Get(histoname_EM).Integral(32,32, 21, 21), 4),  round(file_NtSys_RESOST      .Get(histoname_EM).Integral(41,41,21, 21 ), 4)
print "NtSys_TRIGSF_EL_UP ", round(file_NtSys_TRIGSF_EL_UP.Get(histoname_EM).Integral(32,32, 22, 22), 4),  round(file_NtSys_TRIGSF_EL_UP.Get(histoname_EM).Integral(41,41,22, 22 ), 4)
print "NtSys_TRIGSF_EL_DN ", round(file_NtSys_TRIGSF_EL_DN.Get(histoname_EM).Integral(32,32, 23, 23), 4),  round(file_NtSys_TRIGSF_EL_DN.Get(histoname_EM).Integral(41,41,23, 23 ), 4)
print "NtSys_TRIGSF_MU_UP ", round(file_NtSys_TRIGSF_MU_UP.Get(histoname_EM).Integral(32,32, 24, 24), 4),  round(file_NtSys_TRIGSF_MU_UP.Get(histoname_EM).Integral(41,41,24, 24 ), 4)
print "NtSys_TRIGSF_MU_DN ", round(file_NtSys_TRIGSF_MU_DN.Get(histoname_EM).Integral(32,32, 25, 25), 4),  round(file_NtSys_TRIGSF_MU_DN.Get(histoname_EM).Integral(41,41,25, 25 ), 4)
print "NtSys_TES_UP       ", round(file_NtSys_TES_UP      .Get(histoname_EM).Integral(32,32, 26, 26), 4),  round(file_NtSys_TES_UP      .Get(histoname_EM).Integral(41,41,26, 26 ), 4)
print "NtSys_TES_DN       ", round(file_NtSys_TES_DN      .Get(histoname_EM).Integral(32,32, 27, 27), 4),  round(file_NtSys_TES_DN      .Get(histoname_EM).Integral(41,41,27, 27 ), 4)
print "BTag_BJet_DN       ", round(file_BTag_BJet_DN      .Get(histoname_EM).Integral(32,32, 28, 28), 4),  round(file_BTag_BJet_DN      .Get(histoname_EM).Integral(41,41,28, 28 ), 4)
print "BTag_CJet_DN       ", round(file_BTag_CJet_DN      .Get(histoname_EM).Integral(32,32, 29, 29), 4),  round(file_BTag_CJet_DN      .Get(histoname_EM).Integral(41,41,29, 29 ), 4)
print "BTag_LJet_DN       ", round(file_BTag_LJet_DN      .Get(histoname_EM).Integral(32,32, 30, 30), 4),  round(file_BTag_LJet_DN      .Get(histoname_EM).Integral(41,41,30, 30 ), 4)
print "BTag_BJet_UP       ", round(file_BTag_BJet_UP      .Get(histoname_EM).Integral(32,32, 31, 31), 4),  round(file_BTag_BJet_UP      .Get(histoname_EM).Integral(41,41,31, 31 ), 4)
print "BTag_CJet_UP       ", round(file_BTag_CJet_UP      .Get(histoname_EM).Integral(32,32, 32, 32), 4),  round(file_BTag_CJet_UP      .Get(histoname_EM).Integral(41,41,32, 32 ), 4)
print "BTag_LJet_UP       ", round(file_BTag_LJet_UP      .Get(histoname_EM).Integral(32,32, 33, 33), 4),  round(file_BTag_LJet_UP      .Get(histoname_EM).Integral(41,41,33, 33 ), 4)
print "BKGMETHOD_UP       ", round(file_BKGMETHOD_UP      .Get(histoname_EM).Integral(32,32, 34, 34), 4),  round(file_BKGMETHOD_UP      .Get(histoname_EM).Integral(41,41,34, 34 ), 4)
print "BKGMETHOD_DN       ", round(file_BKGMETHOD_DN      .Get(histoname_EM).Integral(32,32, 35, 35), 4),  round(file_BKGMETHOD_DN      .Get(histoname_EM).Integral(41,41,35, 35 ), 4)