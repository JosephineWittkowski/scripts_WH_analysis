{
  gROOT->LoadMacro("AtlasStyle.C");
  SetAtlasStyle();


  TFile *file_ttbar = new TFile("/data/etp/jwittkowski/analysis_SUSYTool_02_00/Aausgabe_2signalJets_105861.root");
  THnSparse *sparse_all; 
  THnSparse *sparse_trig; 
  file_ttbar.GetObject( "ths_EF_xe40wMu_den_emulated", sparse_all );
  file_ttbar.GetObject( "ths_EF_xe40wMu_num_emulated", sparse_trig );

  //	now create projections:
  //	Create one dimensional efficiency maps:

  TH1D *passed_ttbar = new TH1D();
  TH1D *trials_ttbar = new TH1D();

  TGraphAsymmErrors *gr_ttbar = new TGraphAsymmErrors();
  gr_ttbar -> SetMarkerStyle(20);
  gr_ttbar -> SetMarkerSize(1.);
  gr_ttbar -> SetMarkerColor(kRed);
  gr_ttbar -> SetLineColor(kRed);
  
  TMultiGraph *mg = new TMultiGraph();
  TCanvas canvas("canvas","canvas", 800, 600);
  int _n_dim = sparse_all->GetNdimensions();
  cout << "_n_dim= " << _n_dim << endl;
  	  

  sparse_all -> GetAxis(0) -> SetRange( 1, 5);
  sparse_trig -> GetAxis(0) -> SetRange( 1, 5);
  
  sparse_all -> GetAxis(1) -> SetRange( 3, 3);
  sparse_trig -> GetAxis(1) -> SetRange( 3, 3);
  
  passed_ttbar = sparse_trig -> Projection(0);
  trials_ttbar = sparse_all -> Projection(0);
  
  gr_ttbar -> BayesDivide(passed_ttbar, trials_ttbar);
  gr_ttbar -> GetYaxis() -> SetRangeUser( 0., 1.1 );
  gr_ttbar -> GetXaxis() -> SetTitle( "MET [MeV]" );
  gr_ttbar -> GetYaxis() -> SetTitle( "TriggerEfficiency" );
  gr_ttbar -> GetXaxis() -> SetNdivisions(1005);
//   gr_ttbar -> Draw("APZ");
  
  
  
  
  
  
  TFile *file_Zmm = new TFile("/data/etp/jwittkowski/analysis_SUSYTool_02_00/Aausgabe_2signalJets_Zmm_merged.root");
  THnSparse *sparse_all; 
  THnSparse *sparse_trig; 
  file_Zmm.GetObject( "ths_EF_xe40wMu_den_emulated", sparse_all );
  file_Zmm.GetObject( "ths_EF_xe40wMu_num_emulated", sparse_trig );

  TH1D *passed_Zmm = new TH1D();
  TH1D *trials_Zmm = new TH1D();

  TGraphAsymmErrors *gr_Zmm = new TGraphAsymmErrors();
  gr_Zmm -> SetMarkerStyle(20);
  gr_Zmm -> SetMarkerSize(1.);
  gr_Zmm -> SetMarkerColor(1);
  gr_Zmm -> SetLineColor(1);

  int _n_dim = sparse_all->GetNdimensions();
  cout << "_n_dim= " << _n_dim << endl;
		  

  sparse_all -> GetAxis(0) -> SetRange( 1, 5);
  sparse_trig -> GetAxis(0) -> SetRange( 1, 5);
  
  sparse_all -> GetAxis(1) -> SetRange( 3, 3);
  sparse_trig -> GetAxis(1) -> SetRange( 3, 3);
  
  passed_Zmm = sparse_trig -> Projection(0);
  trials_Zmm = sparse_all -> Projection(0);
  
  gr_Zmm -> BayesDivide(passed_Zmm, trials_Zmm);
  gr_Zmm -> GetYaxis() -> SetRangeUser( 0., 1.1 );
  gr_Zmm -> GetXaxis() -> SetTitle( "MET [MeV]" );
  gr_Zmm -> GetYaxis() -> SetTitle( "TriggerEfficiency" );
  gr_Zmm -> GetXaxis() -> SetNdivisions(1005);
//   gr_Zmm -> Draw("same APZ");

  


  file_Zmm -> Close();
  
   mg->Add(gr_ttbar);
   mg->Add(gr_Zmm);
   
    mg->Draw("APZ");
    mg -> GetYaxis() -> SetRangeUser( 0., 1.1 );
    
  leg = new TLegend(0.3,0.2,0.83,0.3);
  leg->SetFillColor(0);
  leg->AddEntry(gr_ttbar,"ttbar","l");
  leg->AddEntry(gr_Zmm,"Zmm","l");
  leg->SetTextSize(0.04);
  leg->Draw();
   
  canvas.Print("../pics/eff_EF_xe40wMu_THnSparse_ttbar_Zmm.pdf");
}


