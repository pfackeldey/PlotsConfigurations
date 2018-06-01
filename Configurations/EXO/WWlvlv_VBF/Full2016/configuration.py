# example of configuration file

tag = 'HWWhighMass2016_OF'
# V3 fix nuisance to SM H
# V4 con SBI (+V3)


# used by mkShape to define output directory for root files
outputDir = '/net/scratch_cms3b/fackeldey/shapes/Full2016_shapes_peter/rootFile_OF/plots_HWWhighMass2016_OF_with_mTi.root'


# file with list of variables
variablesFile = 'variables.py'

# file with list of cuts
cutsFile = 'cuts_dnn.py'  # 'cuts_dnn.py'

# file with list of samples
samplesFile = 'samples_dnn.py'
#samplesFile ='samples_genericFormulas.py'

# file with list of samples
plotFile = 'plot_dnn.py'


# luminosity to normalize to (in 1/fb)
# RIMETTERE baswW se lumi !=1 !!!!
#lumi = 1.0
#lumi = 35.867

lumi = 35.9

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = '/net/scratch_cms3b/fackeldey/shapes/Full2016_shapes_peter/plotHWWhighMass_OF'


# used by mkDatacards to define output directory for datacards
outputDirDatacard = '/net/scratch_cms3b/fackeldey/shapes/Full2016_shapes_peter/datacards_test_OF'


# structure file for datacard
structureFile = 'structure.py'


# nuisances file for mkDatacards and for mkShape
nuisancesFile = 'nuisances.py'

#nuisancesFile = 'nuisances_vuoto.py'
