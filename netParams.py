from netpyne import specs

from netStimVec import ABdelay, ADdelay, Cdelay #import NetStim start times from file netStimVec.py

import cells

try:
    from __main__ import cfg
except:
    from cfg import cfg

netParams = specs.NetParams()

###################################################################################################################################
#
#   Create Populations
#
###################################################################################################################################

netParams.popParams['ABSTIM'] = {'cellModel': 'NetStim', 'interval': 1000, 'noise': 0, 'start': 0, 'number': 20, 'numCells': 1}
netParams.popParams['ADSTIM'] = {'cellModel': 'NetStim', 'interval': 1000, 'noise': 0, 'start': 0, 'number': 20, 'numCells': 1}
netParams.popParams['CSTIM' ] = {'cellModel': 'NetStim', 'interval': 1000, 'noise': 0, 'start': 0, 'number': 20, 'numCells': 1}

netParams.popParams['STIM'] = {'cellModel': 'NetStim', 'interval': 1000, 'noise': 0, 'start': 0, 'number': 20, 'numCells': 1}

netParams.popParams['IN' ]  = {'cellType': 'IN' , 'numCells': 2, 'cellModel': '_IN' } # this is the inhibitory interneuron     (IN )
netParams.popParams['EX' ]  = {'cellType': 'EX' , 'numCells': 1, 'cellModel': '_EX' } # this is the excitatory interneuron     (EX )
netParams.popParams['WDR']  = {'cellType': 'WDR', 'numCells': 1, 'cellModel': '_WDR'} # this is the wide dynamic range neuron  (WDR)

# INcellRule = netParams.importCellParams(label='INrule' , conds={'cellType': 'IN' , 'cellModel': '_IN' }, fileName='cells.py', cellName='createIN')
# EXcellRule = netParams.importCellParams(label='EXrule' , conds={'cellType': 'EX' , 'cellModel': '_EX' }, fileName='cells.py', cellName='createEX')
# WDRcellRule= netParams.importCellParams(label='WDRrule', conds={'cellType': 'WDR', 'cellModel': '_WDR'}, fileName='cells.py', cellName='createWDR')

cells.INcellRule['conds'] = {'cellType': 'IN' , 'cellModel': '_IN' }
cells.EXcellRule['conds'] = {'cellType': 'EX' , 'cellModel': '_EX' }
cells.WDRcellRule['conds']= {'cellType': 'WDR', 'cellModel': '_WDR'}

netParams.cellParams['INRule' ] = cells.INcellRule
netParams.cellParams['EXRule' ] = cells.EXcellRule
netParams.cellParams['WDRRule'] = cells.WDRcellRule

###################################################################################################################################
#
#   Synaptic Mechanisms
#
###################################################################################################################################
netParams.defaultThreshold = -30

netParams.synMechParams['AMPA'] = {'mod': 'AMPA_DynSyn'   , 'tau_rise': 0.1, 'tau_decay': 5             }
netParams.synMechParams['NMDA'] = {'mod': 'NMDA_DynSyn'   , 'tau_rise': 2  , 'tau_decay': 100           }
netParams.synMechParams['NK13'] = {'mod': 'NK1_DynSyn'    , 'tau_rise': 100, 'tau_decay': 3000          }
netParams.synMechParams['NK23'] = {'mod': 'NK1_DynSyn'    , 'tau_rise': 200, 'tau_decay': 3000          }
netParams.synMechParams['GABA'] = {'mod': 'GABAa_DynSyn'  , 'tau_rise': 0.1, 'tau_decay': 20  , 'e': -70}
netParams.synMechParams['GLY']  = {'mod': 'Glycine_DynSyn', 'tau_rise': 0.1, 'tau_decay': 10            }

###################################################################################################################################
#
#   Weight Parameters
#
###################################################################################################################################

AB= 1.0
AD= 1.0
C = 1.0

###################################################################################################################################
#
#   Connect NetStims
#
###################################################################################################################################


netParams.connParams['AMPA_NS->IN0'] = {
    'oneSynPerNetcon': False,
    'preConds': {'popLabel': 'STIM'},
    'postConds': {'popLabel': 'IN'},
    'weight': 0.00097067 * AB,
    'sec': 'dend',
    'delay': ABdelay, 
    'loc': 0.51,
    'synMech': 'AMPA',
    'connList': [[0, 0] for x in range(15)]}

netParams.connParams['AMPA_NS->WDR0'] = {
    'oneSynPerNetcon': False,
    'preConds': {'popLabel': 'STIM'},
    'postConds': {'popLabel': 'WDR'},
    'weight': 0.0016 * AB,
    'sec': 'dend',
    'delay': ABdelay,
    'loc': 0.50,
    'synMech': 'AMPA',
    'connList': [[0, 0] for x in range(15)]}

netParams.connParams['NMDA_NS->WDR0'] = {
    'oneSynPerNetcon': False,
    'preConds': {'popLabel': 'STIM'},
    'postConds': {'popLabel': 'WDR'},
    'weight': 6.6667e-5 * AB,
    'sec': 'dend',
    'delay': ABdelay,
    'loc': 0.50,
    'synMech': 'NMDA',
    'connList': [[0, 0] for x in range(15)]}

netParams.connParams['AMPA_NS->IN2'] = {
    'oneSynPerNetcon': False,
    'preConds': {'popLabel': 'STIM'},
    'postConds': {'popLabel': 'IN'},
    'weight': 0.0013333 * AB,
    'sec': 'dend',
    'delay': [ 2e9 ] * 15,
    'loc': 0.51,
    'synMech': 'AMPA',
    'connList': [[0, 1] for x in range(15)]}

##############################################################################################################
# For the purpose of recreating original, however, AMPA_NS->IN has no effect on simulation as is (weight is 0)
##############################################################################################################
netParams.connParams['AMPA_NS->IN1'] = {
    'oneSynPerNetcon': False,
    'preConds': {'popLabel': 'STIM'},
    'postConds': {'popLabel': 'IN'},
    'weight': 0 * AD, # AD afferent
    'sec': 'dend',
    'delay': ADdelay,
    'loc': 0.51,
    'synMech': 'AMPA',
    'connList': [[0, 0] for x in range(15)]}

netParams.connParams['AMPA_NS->WDR1'] = {
    'oneSynPerNetcon': False,
    'preConds': {'popLabel': 'STIM'},
    'postConds': {'popLabel': 'WDR'},
    'weight': 0.0016 * AD,
    'sec': 'dend',
    'delay': ADdelay,
    'loc': 0.50,
    'synMech': 'AMPA',
    'connList': [[0, 0] for x in range(15)]}

netParams.connParams['NMDA_NS->WDR1'] = {
    'oneSynPerNetcon': False,
    'preConds': {'popLabel': 'STIM'},
    'postConds': {'popLabel': 'WDR'},
    'weight': 6.6667e-5 * AD,
    'sec': 'dend',
    'delay': ADdelay,
    'loc': 0.50,
    'synMech': 'NMDA',
    'connList': [[0, 0] for x in range(15)]}

###############################################################################################################
# For the purpose of recreating original, however, AMPA_NS->IN has no effect on simulation as is (delay is 2e9)
###############################################################################################################

netParams.connParams['AMPA_NS->EX0'] = {
    'oneSynPerNetcon': False,
    'preConds': {'popLabel': 'STIM'},
    'postConds': {'popLabel': 'EX'},
    'weight': 0.008 * C,
    'sec': 'dend',
    'delay': Cdelay, 
    'loc': 0.5,
    'synMech': 'AMPA',
    'connList': [[0, 0] for x in range(30)]}

netParams.connParams['NMDA_NS->EX0'] = {
    'oneSynPerNetcon': False,
    'preConds': {'popLabel': 'STIM'},
    'postConds': {'popLabel': 'EX'},
    'weight': 0.004 * C,
    'sec': 'dend',
    'delay': Cdelay, 
    'loc': 0.5,
    'synMech': 'NMDA',
    'connList': [[0, 0] for x in range(30)]}

netParams.connParams['NK1_NS->EX0'] = {
    'oneSynPerNetcon': False,
    'preConds': {'popLabel': 'STIM'},
    'postConds': {'popLabel': 'EX'},
    'weight': 6.6667e-7 * C,
    'sec': 'dend',
    'delay': Cdelay, 
    'loc': 0.5,
    'synMech': 'NK13',
    'connList': [[0, 0] for x in range(30)]}

netParams.connParams['NK1_NS->WDR0'] = {
    'oneSynPerNetcon': False,
    'preConds': {'popLabel': 'STIM'},
    'postConds': {'popLabel': 'WDR'},  
    'weight': 4.5e-7 * C,
    'sec': 'dend',
    'delay': Cdelay, 
    'loc': 0.5,
    'synMech': 'NK23',
    'connList': [[0, 0] for x in range(30)]}

###################################################################################################################################
#
#   Connect Cells
#
###################################################################################################################################


netParams.connParams['GABA_IN->EX0'] = {
    'oneSynPerNetcon': False,
    'preConds': {'popLabel': 'IN'},
    'postConds': {'popLabel': 'EX'},
    'weight': 0.00532,
    'sec': 'dend',
    'delay': 1, 
    'loc': 0.5,
    'synMech': 'GABA',
    'connList': [[0, 0]]}

netParams.connParams['AMPA_EX->WDR'] = {
    'oneSynPerNetcon': False,
    'preConds': {'popLabel': 'EX'},
    'postConds': {'popLabel': 'WDR'},  
    'weight': 1.2e-5 * 30,
    'sec': 'dend',
    'delay': 1, 
    'loc': 0.5,
    'synMech': 'AMPA',
    'connList': [[0, 0]]}

netParams.connParams['NMDA_EX->WDR'] = {
    'oneSynPerNetcon': False,
    'preConds': {'popLabel': 'EX'},
    'postConds': {'popLabel': 'WDR'},  
    'weight': 9.6e-6 * 30,
    'sec': 'dend',
    'delay': 1, 
    'loc': 0.5,
    'synMech': 'NMDA',
    'connList': [[0, 0]]}

netParams.connParams['GLY_IN->WDR'] = {
    'oneSynPerNetcon': False,
    'preConds': {'popLabel': 'IN'},
    'postConds': {'popLabel': 'WDR'},  
    'weight': 0.00532,
    'sec': 'dend',
    'delay': 1, 
    'loc': 0.5,
    'synMech': 'GLY',
    'connList': [[0, 0]]}

netParams.connParams['GABA_IN->WDR'] = {
    'oneSynPerNetcon': False,
    'preConds': {'popLabel': 'IN'},
    'postConds': {'popLabel': 'WDR'},  
    'weight': 0.00532,
    'sec': 'dend',
    'delay': 1, 
    'loc': 0.5,
    'synMech': 'GABA',
    'connList': [[0, 0]]}

###########################################################################################################################
# For the purpose of recreating original, however, all following connParams has no effect on simulation as is (weight is 0)
###########################################################################################################################
netParams.connParams['GABA_IN1->EX'] = {
    'oneSynPerNetcon': False,
    'preConds': {'popLabel': 'IN'},
    'postConds': {'popLabel': 'EX'},
    'weight': 0,
    'sec': 'dend',
    'delay': 1, 
    'loc': 0.5,
    'synMech': 'GABA',
    'connList': [[1, 0]]}

netParams.connParams['GABA_IN1->WDR'] = {
    'oneSynPerNetcon': False,
    'preConds': {'popLabel': 'IN'},
    'postConds': {'popLabel': 'WDR'},  
    'weight': 0,
    'sec': 'dend',
    'delay': 1, 
    'loc': 0.5,
    'synMech': 'GABA',
    'connList': [[1, 0], [1, 0]]}