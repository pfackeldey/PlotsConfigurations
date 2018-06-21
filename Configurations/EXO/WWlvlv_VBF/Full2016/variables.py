# variables

#variables = {}

#'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
"""
variables['mTi_scaled'] = {'name': 'mTi_scaled',  # variable name
                           # variable range
                           'range': ([0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 900, 1000, 2000],),
                           #'range' : (40,0,2000),    #   variable range
                           'xaxis': 'm_{T,i} scaled [GeV]',  # x axis name
                           'fold': 3,
                           'divideByBinWidth': 1,
                           }
"""
variables['ml_sig_score'] = {'name': 'ml_sig_score',  # variable name
                             'range': ([0.0, 0.5, 0.6, 0.7, 0.75, 0.775, 0.8, 0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1.0],),
                             'xaxis': 'NN score',
                             'fold': 3,
                             'divideByBinWidth': 1,
                             }

variables['ml_max_score'] = {'name': 'ml_max_score',  # variable name
                             'range': (50, 0, 1),
                             'xaxis': 'NN score',
                             'fold': 3,
                             'divideByBinWidth': 1,
                             }

"""
variables['events'] = {'name': '1',
                       'range': (1, 0, 2),
                       'xaxis': 'events',
                       'fold': 3,
                       'divideByBinWidth': 1,
                       }

variables['mTi'] = {'name': 'mTi',  # variable name
                    # variable range
                    'range': ([0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 800, 900, 1000, 2000],),
                    #'range' : (40,0,2000),    #   variable range
                    'xaxis': 'm_{T,i} [GeV]',  # x axis name
                    'fold': 3,
                    'divideByBinWidth': 1,
                    }


variables['mTi_VBF'] = {'name': 'mTi',  # variable name
                        # variable range
                        'range': ([0, 50, 100, 150, 200, 250, 300, 350, 400, 500, 700, 1000, 2000],),
                        'xaxis': 'm_{T,i} [GeV]',  # x axis name
                        'fold': 3,
                        'divideByBinWidth': 1,
                        }
"""
"""
variables['ml_score_hww120_200']  = {   'name': 'ml_score_hww120_200',            #   variable name
                        'range' : (30,0,1),
                        'xaxis' : 'NN score ggH (120 - 200 GeV)',
                        'fold' : 3,
                        'divideByBinWidth': 0,
                        }

variables['ml_score_hww210_500']  = {   'name': 'ml_score_hww210_500',            #   variable name
                        'range' : (30,0,1),
                        'xaxis' : 'NN score ggH (210 - 500 GeV)',
                        'fold' : 3,
                        'divideByBinWidth': 0,
                        }

variables['ml_score_hww550_3000']  = {   'name': 'ml_score_hww550_3000',            #   variable name
                        'range' : (30,0,1),
                        'xaxis' : 'NN score ggH (550 - 3000 GeV)',
                        'fold' : 3,
                        'divideByBinWidth': 0,
                        }


variables['ml_score_Top']  = {   'name': 'ml_score_Top',            #   variable name
                        'range' : (30,0,1),
                        'xaxis' : 'NN score Top',
                        'fold' : 3,
                        'divideByBinWidth': 0,
                        }

variables['ml_score_DY']  = {   'name': 'ml_score_DY',            #   variable name
                        'range' : (30,0,1),
                        'xaxis' : 'NN score DY',
                        'fold' : 3,
                        'divideByBinWidth': 0,
                        }

variables['ml_score_WW']  = {   'name': 'ml_score_WW',            #   variable name
                        'range' : (30,0,1),
                        'xaxis' : 'NN score WW',
                        'fold' : 3,
                        'divideByBinWidth': 0,
                        }

variables['ml_score_misc']  = {   'name': 'ml_score_misc',            #   variable name
                        'range' : (30,0,1),
                        'xaxis' : 'NN score misc',
                        'fold' : 3,
                        'divideByBinWidth': 0,
                        }

"""
"""
#variables['mth_VBF']  = {   'name': 'mth',            #   variable name
#                        'range' : ([100,150,200,250,300,350,400,500,700,1000,2000,3000],),    #   variable range
#                        'xaxis' : 'm_{T,i} [GeV]',  #   x axis name
#                        'fold' : 3,
#                        'divideByBinWidth': 1,
# }
#
#variables['mth']  = {   'name': 'mth',            #   variable name
#                        'range' : (60,0,600),    #   variable range
#                        'xaxis' : 'm_{TH} [GeV]',  #   x axis name
#                        'fold' : 3,
#                        'divideByBinWidth': 1,
#                        }
#
#
#variables['mth_DY']  = {   'name': 'mth',            #   variable name
#                        'range' : (20,0,200),    #   variable range
#                        'xaxis' : 'm_{TH} [GeV]',  #   x axis name
#                        'fold' : 3,
#                        'divideByBinWidth': 1,
#                        }
#
#variables['ptll']  = {   'name': 'ptll',            #   variable name
#                        'range' : (20,0,200),    #   variable range
#                        'xaxis' : 'pT_{ll} [GeV]',  #   x axis name
#                        'fold' :3,
#                        'divideByBinWidth': 1,
#                        }


variables['mll'] = {'name': 'mll',  # variable name
                    'range': (30, 0, 300),  # variable range
                    'xaxis': 'm_{ll} [GeV]',  # x axis name
                    'fold': 3,
                    'divideByBinWidth': 1,
                    }

variables['mll_DY']  = {   'name': 'mll',            #   variable name
                        'range' : (25,0,120),    #   variable range
                        'xaxis' : 'm_{ll} [GeV]',  #   x axis name
                        'fold' :3,
                        'divideByBinWidth': 0,
                        }
#
#

variables['mjj']  = {   'name': 'mjj',            #   variable name
                        'range' : (80,0,800),    #   variable range
                        'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                        'fold' :3,
                        'divideByBinWidth': 0,
                        }
#
#


#variables['mjj_DY_VBF']  = {   'name': 'mjj',            #   variable name
#                        'range' : (30,500,1500),    #   variable range
#                        'xaxis' : 'm_{jj} [GeV]',  #   x axis name
#                        'fold' :3,
#                        'divideByBinWidth': 1,
#                        }
#
#variables['std_vector_lepton_pt[0]']  = {   'name': 'std_vector_lepton_pt[0]',            #   variable name
#                        'range' : (20,0,200),    #   variable range
#                        'xaxis' : 'pT_{1l} [GeV]',  #   x axis name
#                        'fold' :3,
#                        'divideByBinWidth': 1,
#                        }
#
#variables['std_vector_lepton_pt[1]']  = {   'name': 'std_vector_lepton_pt[1]',            #   variable name
#                        'range' : (20,0,200),    #   variable range
#                        'xaxis' : 'pT_{2l} [GeV]',  #   x axis name
#                        'fold' :3,
#                        'divideByBinWidth': 1,
#                        }
#
#variables['std_vector_lepton_eta[0]']  = {   'name': 'std_vector_lepton_eta[0]',            #   variable name
#                        'range' : (20,-5,5),    #   variable range
#                        'xaxis' : 'eta_{1l} [GeV]',  #   x axis name
#                        'fold' :3,
#                        'divideByBinWidth': 1,
#                        }
#
#variables['std_vector_lepton_eta[1]']  = {   'name': 'std_vector_lepton_eta[1]',            #   variable name
#                        'range' : (20,-5,5),    #   variable range
#                        'xaxis' : 'eta_{2l} [GeV]',  #   x axis name
#                        'fold' :3,
#                        'divideByBinWidth': 1,
#                        }
#
#
#variables['metPfType1']  = {   'name': 'metPfType1',            #   variable name
#                        'range' : (25,0,250),    #   variable range
#                        'xaxis' : 'MET [GeV]',  #   x axis name
#                        'fold' :3,
#                        'divideByBinWidth': 1,
#                        }
#
#
#
#variables['njet']  = {   'name': 'njet',            #   variable name
#                        'range' : (10,0,10),    #   variable range
#                        'xaxis' : 'njet',  #   x axis name
#                        'fold' :3,
#                        'divideByBinWidth': 1,
#                        }
#
#
#
#


variables['mR']  = {   'name': 'mR',            #   variable name
                        'range' : ([100,150,200,250,300,350,400,450,500,600,700,1000],),    #   variable range
                        'xaxis' : 'mR [GeV]',  #   x axis name
                        'fold' : 3
                        }
variables['mTe']  = {   'name': 'mTe',            #   variable name
                        'range' : ([100,150,200,250,300,350,400,450,500,600,700,1000],),    #   variable range
                        'xaxis' : 'mTe [GeV]',  #   x axis name
                        'fold' : 3
                        }

variables['mcoll']  = {   'name': 'mcoll',            #   variable name
                        'range' : ([100,150,200,250,300,350,400,450,500,600,700,1000],),    #   variable range
                        'xaxis' : 'mcoll [GeV]',  #   x axis name
                        'fold' : 3
                        }

variables['mcollWW']  = {   'name': 'mcollWW',            #   variable name
                        'range' : ([100,150,200,250,300,350,400,450,500,600,700,1000],),    #   variable range
                        'xaxis' : 'mcollWW [GeV]',  #   x axis name
                        'fold' : 3
                        }


variables['std_vector_lepton_phi[0]']  = {   'name': 'std_vector_lepton_phi[0]',            #   variable name
                        'range' : (20,-5,5),    #   variable range
                        'xaxis' : 'phi_{1l} [GeV]',  #   x axis name
                        'fold' :3
                        }

variables['std_vector_lepton_phi[1]']  = {   'name': 'std_vector_lepton_phi[1]',            #   variable name
                        'range' : (20,-5,5),    #   variable range
                        'xaxis' : 'phi_{2l} [GeV]',  #   x axis name
                        'fold' :3
                        }



"""


# variables['mTi_test_BIN50GeV']  = {   'name': 'mTi',            #   variable name
#                        'range' : (60,0,3000),
#                        'xaxis' : 'm_{T,i} [GeV]',  #   x axis name
#                        'fold' : 3,
#                        #'divideByBinWidth': 1,
#                        }
#
