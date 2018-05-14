

# cuts

#cuts = {}

#Update to new bTag working point -0.5884 from  -0.715
supercut = 'std_vector_lepton_pt[0]>25 && std_vector_lepton_pt[1]>20 \
            && std_vector_lepton_pt[2]<10 \
            && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*13) \
           '

# Inclusive category
#cuts['hwwhm_13TeV_of_INCL']  ='1'



#*************0-1-2-VBF-categories************************************

##------------DY----------------------

cuts['hww2l2v_13TeV_dytt_of0j']  = '( ml_score_DY>0.3) \
                && (ml_score_WW < 0.4) \
                && (ml_score_hww120_200 < 0.5) \
                && (ml_score_hww210_500 < 0.5) \
                && (ml_score_hww550_3000 < 0.5) \
                && ( std_vector_jet_pt[0] < 30 ) \
                && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.5884 ) \
                && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.5884 ) \
                && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.5884 ) \
                && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.5884 ) \
                && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.5884 ) \
                && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.5884 ) \
                && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.5884 ) \
                && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.5884 ) \
                && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.5884 ) \
                && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.5884 ) \
                '

cuts['hww2l2v_13TeV_dytt_of1j']  = '( ml_score_DY>0.3) \
                && (ml_score_Top < 0.2) \
                && (ml_score_WW < 0.4) \
                && (ml_score_hww120_200 < 0.5) \
                && (ml_score_hww210_500 < 0.5) \
                && (ml_score_hww550_3000 < 0.5) \
                && ( std_vector_jet_pt[0] >= 30 ) \
                && ( std_vector_jet_pt[1] < 30 ) \
                && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.5884 ) \
                && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.5884 ) \
                && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.5884 ) \
                && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.5884 ) \
                && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.5884 ) \
                && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.5884 ) \
                && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.5884 ) \
                && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.5884 ) \
                && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.5884 ) \
                && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.5884 ) \
                '

cuts['hww2l2v_13TeV_dytt_of2j']  = '( ml_score_DY>0.3) \
                && (ml_score_Top < 0.2) \
                && (ml_score_WW < 0.4) \
                && (ml_score_hww120_200 < 0.5) \
                && (ml_score_hww210_500 < 0.5) \
                && (ml_score_hww550_3000 < 0.5) \
                && (detajj<3.5 ||  mjj<500) \
                && ( std_vector_jet_pt[1] >= 30 ) \
                && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.5884 ) \
                && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.5884 ) \
                && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.5884 ) \
                && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.5884 ) \
                && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.5884 ) \
                && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.5884 ) \
                && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.5884 ) \
                && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.5884 ) \
                && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.5884 ) \
                && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.5884 ) \
                '

"""
cuts['hww2l2v_13TeV_dytt_of2j_vbf']  = '( mth<60) \
                && mll>30 && mll<80 \
                && ( std_vector_jet_pt[0] >= 30 ) \
                && ( std_vector_jet_pt[1] >= 30 ) \
                && (detajj>3.5 && mjj>500) \
                && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.5884 ) \
                && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.5884 ) \
                && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.5884 ) \
                && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.5884 ) \
                && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.5884 ) \
                && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.5884 ) \
                && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.5884 ) \
                && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.5884 ) \
                && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.5884 ) \
                && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.5884 ) \
                '
"""


#------------TOP----------------------


cuts['hww2l2v_13TeV_top_of0j']  = '( ml_score_DY<0.3) \
                && (ml_score_WW < 0.4) \
                && (ml_score_hww120_200 < 0.5) \
                && (ml_score_hww210_500 < 0.5) \
                && (ml_score_hww550_3000 < 0.5) \
                && ( std_vector_jet_pt[0] < 30 ) \
                && (   ( std_vector_jet_pt[0] > 20 && std_vector_jet_cmvav2[0] > -0.5884 ) \
                    || ( std_vector_jet_pt[1] > 20 && std_vector_jet_cmvav2[1] > -0.5884 ) \
                    || ( std_vector_jet_pt[2] > 20 && std_vector_jet_cmvav2[2] > -0.5884 ) \
                    || ( std_vector_jet_pt[3] > 20 && std_vector_jet_cmvav2[3] > -0.5884 ) \
                    || ( std_vector_jet_pt[4] > 20 && std_vector_jet_cmvav2[4] > -0.5884 ) \
                    || ( std_vector_jet_pt[5] > 20 && std_vector_jet_cmvav2[5] > -0.5884 ) \
                    || ( std_vector_jet_pt[6] > 20 && std_vector_jet_cmvav2[6] > -0.5884 ) \
                    || ( std_vector_jet_pt[7] > 20 && std_vector_jet_cmvav2[7] > -0.5884 ) \
                    || ( std_vector_jet_pt[8] > 20 && std_vector_jet_cmvav2[8] > -0.5884 ) \
                    || ( std_vector_jet_pt[9] > 20 && std_vector_jet_cmvav2[9] > -0.5884 ) \
                    ) \
                '


#exaclty one b-tag jet pT>30 GeV
cuts['hww2l2v_13TeV_top_of1j']  = '( ml_score_DY<0.3) \
                && (ml_score_Top > 0.2) \
                && (ml_score_WW < 0.4) \
                && (ml_score_hww120_200 < 0.5) \
                && (ml_score_hww210_500 < 0.5) \
                && (ml_score_hww550_3000 < 0.5) \
                && ( std_vector_jet_pt[0] >= 30 ) \
                && ( std_vector_jet_pt[1] < 30 ) \
                '


#NEW in 2jet region: taken from Moriond analysis (but modified...)
#https://github.com/latinos/PlotsConfigurations/blob/master/Configurations/ggH2j/Moriond/cuts.py#L14
#ortogonal to VBF control region
cuts['hww2l2v_13TeV_top_of2j']  = '( ml_score_DY<0.3) \
                && (ml_score_Top > 0.2) \
                && (ml_score_WW < 0.4) \
                && (ml_score_hww120_200 < 0.5) \
                && (ml_score_hww210_500 < 0.5) \
                && (ml_score_hww550_3000 < 0.5) \
                && (detajj<3.5 ||  mjj<500) \
                && ( std_vector_jet_pt[0] >= 30 ) \
                && ( std_vector_jet_pt[1] >= 30 ) \
                '



"""
#NEW: VBF Top Ctrl region: only 2 jets and one b-jet with p T > 30 GeV. Plus detajj>3.5 && mjj>500
#https://github.com/latinos/PlotsConfigurations/blob/master/Configurations/VBF/Moriond/cuts.py#L59
cuts['hww2l2v_13TeV_top_VBF']  = ' mll>50 \
                && ( std_vector_jet_pt[0] >= 30 ) \
                && ( std_vector_jet_pt[1] >= 30 ) \
                && (detajj>3.5 && mjj>500) \
                && ( std_vector_jet_cmvav2[0]>-0.5884 || std_vector_jet_cmvav2[1]>-0.5884 ) \
                '
"""



# 11 = e
# 13 = mu
# 15 = tau


##------------SIGNAL REGION----------------------

#0 jet:
# low mass:
cuts['hwwhm_low_13TeV_of_0j'] = '( ml_score_DY<0.3) \
                && (ml_score_WW < 0.4) \
                && (ml_score_hww210_500 < 0.5)\
                && (ml_score_hww550_3000 < 0.5) \
                && ( std_vector_jet_pt[0] < 30 ) \
                && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.5884 ) \
                && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.5884 ) \
                && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.5884 ) \
                && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.5884 ) \
                && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.5884 ) \
                && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.5884 ) \
                && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.5884 ) \
                && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.5884 ) \
                && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.5884 ) \
                && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.5884 ) \
                '

# medium mass:
cuts['hwwhm_medium_13TeV_of_0j'] = '( ml_score_DY<0.3) \
                && (ml_score_WW < 0.4) \
                && (ml_score_hww120_200 < 0.5)\
                && (ml_score_hww550_3000 < 0.5) \
                && ( std_vector_jet_pt[0] < 30 ) \
                && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.5884 ) \
                && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.5884 ) \
                && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.5884 ) \
                && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.5884 ) \
                && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.5884 ) \
                && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.5884 ) \
                && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.5884 ) \
                && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.5884 ) \
                && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.5884 ) \
                && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.5884 ) \
                '
# high mass:
cuts['hwwhm_high_13TeV_of_0j'] = '( ml_score_DY<0.3) \
                && (ml_score_WW < 0.4) \
                && (ml_score_hww210_500 < 0.5)\
                && (ml_score_hww120_200 < 0.5) \
                && ( std_vector_jet_pt[0] < 30 ) \
                && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.5884 ) \
                && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.5884 ) \
                && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.5884 ) \
                && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.5884 ) \
                && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.5884 ) \
                && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.5884 ) \
                && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.5884 ) \
                && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.5884 ) \
                && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.5884 ) \
                && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.5884 ) \
                '

# 1 jet:
# low mass:
cuts['hwwhm_low_13TeV_of_1j']  = '( ml_score_DY<0.3) \
                && (ml_score_WW < 0.4) \
                && (ml_score_Top < 0.2) \
                && (ml_score_hww210_500 < 0.5)\
                && (ml_score_hww550_3000 < 0.5) \
                && ( std_vector_jet_pt[0] >= 30 ) \
                && ( std_vector_jet_pt[1] < 30 ) \
                && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.5884 ) \
                && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.5884 ) \
                && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.5884 ) \
                && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.5884 ) \
                && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.5884 ) \
                && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.5884 ) \
                && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.5884 ) \
                && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.5884 ) \
                && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.5884 ) \
                && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.5884 ) \
                '

# medium mass:
cuts['hwwhm_medium_13TeV_of_1j']  = '( ml_score_DY<0.3) \
                && (ml_score_WW < 0.4) \
                && (ml_score_Top < 0.2) \
                && (ml_score_hww120_200 < 0.5)\
                && (ml_score_hww550_3000 < 0.5) \
                && ( std_vector_jet_pt[0] >= 30 ) \
                && ( std_vector_jet_pt[1] < 30 ) \
                && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.5884 ) \
                && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.5884 ) \
                && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.5884 ) \
                && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.5884 ) \
                && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.5884 ) \
                && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.5884 ) \
                && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.5884 ) \
                && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.5884 ) \
                && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.5884 ) \
                && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.5884 ) \
                '
# high mass:
cuts['hwwhm_high_13TeV_of_1j']  = '( ml_score_DY<0.3) \
                && (ml_score_WW < 0.4) \
                && (ml_score_Top < 0.2) \
                && (ml_score_hww210_500 < 0.5)\
                && (ml_score_hww120_200 < 0.5) \
                && ( std_vector_jet_pt[0] >= 30 ) \
                && ( std_vector_jet_pt[1] < 30 ) \
                && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.5884 ) \
                && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.5884 ) \
                && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.5884 ) \
                && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.5884 ) \
                && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.5884 ) \
                && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.5884 ) \
                && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.5884 ) \
                && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.5884 ) \
                && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.5884 ) \
                && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.5884 ) \
                '

#New: 2jet
#https://github.com/latinos/PlotsConfigurations/blob/master/Configurations/ggH2j/Moriond/cuts.py#L48
# low mass:
cuts['hwwhm_low_13TeV_of2j']  = '( ml_score_DY<0.3) \
                && (ml_score_WW < 0.4) \
                && (ml_score_Top < 0.2) \
                && (ml_score_hww210_500 < 0.5)\
                && (ml_score_hww550_3000 < 0.5) \
                && (detajj<3.5 ||  mjj<500) \
                && ( std_vector_jet_pt[0] >= 30 && std_vector_jet_pt[1] >= 30 ) \
                && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.5884 ) \
                && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.5884 ) \
                && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.5884 ) \
                && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.5884 ) \
                && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.5884 ) \
                && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.5884 ) \
                && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.5884 ) \
                && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.5884 ) \
                && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.5884 ) \
                && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.5884 ) \
                '
# medium mass:
cuts['hwwhm_medium_13TeV_of2j']  = '( ml_score_DY<0.3) \
                && (ml_score_WW < 0.4) \
                && (ml_score_Top < 0.2) \
                && (ml_score_hww120_200 < 0.5)\
                && (ml_score_hww550_3000 < 0.5) \
                && (detajj<3.5 ||  mjj<500) \
                && ( std_vector_jet_pt[0] >= 30 && std_vector_jet_pt[1] >= 30 ) \
                && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.5884 ) \
                && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.5884 ) \
                && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.5884 ) \
                && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.5884 ) \
                && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.5884 ) \
                && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.5884 ) \
                && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.5884 ) \
                && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.5884 ) \
                && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.5884 ) \
                && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.5884 ) \
                '

#high mass:
cuts['hwwhm_high_13TeV_of2j']  = '( ml_score_DY<0.3) \
                && (ml_score_WW < 0.4) \
                && (ml_score_Top < 0.2) \
                && (ml_score_hww210_500 < 0.5)\
                && (ml_score_hww120_200 < 0.5) \
                && (detajj<3.5 ||  mjj<500) \
                && ( std_vector_jet_pt[0] >= 30 && std_vector_jet_pt[1] >= 30 ) \
                && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.5884 ) \
                && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.5884 ) \
                && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.5884 ) \
                && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.5884 ) \
                && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.5884 ) \
                && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.5884 ) \
                && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.5884 ) \
                && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.5884 ) \
                && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.5884 ) \
                && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.5884 ) \
                '

"""
#VBF case, form 2015 analysis
cuts['hwwhm_13TeV_of_VBF']  = '( mth>=60) \
                && ( mTi > 100 ) \
                && ( mjj>500 ) \
                && ( detajj>3.5  ) \
                && ( std_vector_jet_pt[1] >= 30 ) \
                && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.5884 ) \
                && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.5884 ) \
                && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.5884 ) \
                && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.5884 ) \
                && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.5884 ) \
                && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.5884 ) \
                && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.5884 ) \
                && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.5884 ) \
                && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.5884 ) \
                && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.5884 ) \
                '
"""




#*************INCLUSIVE************************************

'''
#DY For Inclusive study
cuts['hww2l2v_13TeV_dytt_of_INCL']  = '( mth<60) \
                && mll>30 && mll<80 \
                && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.5884 ) \
                && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.5884 ) \
                && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.5884 ) \
                && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.5884 ) \
                && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.5884 ) \
                && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.5884 ) \
                && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.5884 ) \
                && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.5884 ) \
                && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.5884 ) \
                && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.5884 ) \
                '

#Top For Inclusive study
#exaclty 2 jets b-tag
cuts['hww2l2v_13TeV_top_of_exaclty_2bj_INCL']  = ' (mll>50 \
                && ( std_vector_jet_pt[0] >= 30 && std_vector_jet_cmvav2[0]>-0.5884) \
                && ( std_vector_jet_pt[1] >= 30 && std_vector_jet_cmvav2[1]>-0.5884) ) \
               '

cuts['hww2l2v_13TeV_top_of_exaclty_2bj_VBF_INCL']  = ' (mll>50 \
                && ( mjj>500 ) \
                && ( detajj>3.5  ) \
                && ( std_vector_jet_pt[0] >= 30 && std_vector_jet_cmvav2[0]>-0.5884) \
                && ( std_vector_jet_pt[1] >= 30 && std_vector_jet_cmvav2[1]>-0.5884) ) \
               '


#Signal case: ORTOGONAL to VBF
#               VBF:
#                or ( mjj<500 ) \
#                or ( detajj<3.5  ) \

cuts['hwwhm_13TeV_of_INCL']  ='( mth>=60) \
                && ( mTi > 100 ) \
                && ( ( mjj<500 ) || ( detajj<3.5) ) \
                && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.5884 ) \
                && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.5884 ) \
                && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.5884 ) \
                && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.5884 ) \
                && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.5884 ) \
                && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.5884 ) \
                && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.5884 ) \
                && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.5884 ) \
                && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.5884 ) \
                && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.5884 ) \
                              '



#TOP control region OLD

#OLD
cuts['hww2l2v_13TeV_top_of2j_OLD']  = 'mll>50 \
                && ( std_vector_jet_pt[1] >= 30 ) \
                && (   ( std_vector_jet_pt[0] > 20 && std_vector_jet_cmvav2[0] > -0.5884 ) \
                    || ( std_vector_jet_pt[1] > 20 && std_vector_jet_cmvav2[1] > -0.5884 ) \
                    || ( std_vector_jet_pt[2] > 20 && std_vector_jet_cmvav2[2] > -0.5884 ) \
                    || ( std_vector_jet_pt[3] > 20 && std_vector_jet_cmvav2[3] > -0.5884 ) \
                    || ( std_vector_jet_pt[4] > 20 && std_vector_jet_cmvav2[4] > -0.5884 ) \
                    || ( std_vector_jet_pt[5] > 20 && std_vector_jet_cmvav2[5] > -0.5884 ) \
                    || ( std_vector_jet_pt[6] > 20 && std_vector_jet_cmvav2[6] > -0.5884 ) \
                    || ( std_vector_jet_pt[7] > 20 && std_vector_jet_cmvav2[7] > -0.5884 ) \
                    || ( std_vector_jet_pt[8] > 20 && std_vector_jet_cmvav2[8] > -0.5884 ) \
                    || ( std_vector_jet_pt[9] > 20 && std_vector_jet_cmvav2[9] > -0.5884 ) \
                    ) \
               '
'''
