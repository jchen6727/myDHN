from netpyne import specs
from netpyne import sim

from netStimVec import starts #import NetStim start times from file netStimVec.py

netParams = specs.NetParams()

###################################################################################################################################
#
#   Create Populations
#
###################################################################################################################################

netParams.popParams['NS' ] = {'cellModel': 'NetStim', 'interval': 1000, 'noise': 0, 'start': 0, 'number': 20, 'numCells': 1}
netParams.popParams['SG' ] = {'cellType': 'SG' , 'numCells': 2 , 'cellModel': '_SG' } # this is the inhibitory interneuron     (IN )
netParams.popParams['IN' ] = {'cellType': 'IN' , 'numCells': 1 , 'cellModel': '_IN' } # this is the excitatory interneuron     (EX )
netParams.popParams['WDR'] = {'cellType': 'WDR', 'numCells': 1 , 'cellModel': '_WDR'} # this is the wide dynamic range neuron  (WDR)

SGcellRule  = netParams.importCellParams(label='SGrule' , conds={'cellType': 'SG'  ,'cellModel': '_SG' }, fileName='SG.tem' , cellName='SG')
INcellRule  = netParams.importCellParams(label='INrule' , conds={'cellType': 'IN'  ,'cellModel': '_IN' }, fileName='IN.tem' , cellName='IN')
WDRcellRule = netParams.importCellParams(label='WDRrule', conds={'cellType': 'WDR' ,'cellModel': '_WDR'}, fileName='WDR.tem', cellName='WDR')

netParams.cellParams['SGRule' ] = SGcellRule
netParams.cellParams['INRule' ] = INcellRule
netParams.cellParams['WDRRule'] = WDRcellRule

###################################################################################################################################
#
#   Synaptic Mechanisms
#
###################################################################################################################################
netParams.defaultThreshold = -30

netParams.synMechParams['AMPA'] = {'mod': 'AMPA_DynSyn'   , 'tau_rise': 0.1, 'tau_decay': 5              }
netParams.synMechParams['NMDA'] = {'mod': 'NMDA_DynSyn'   , 'tau_rise': 2  , 'tau_decay': 100            }
netParams.synMechParams['NK13'] = {'mod': 'NK1_DynSyn'    , 'tau_rise': 100, 'tau_decay': 3000           }
netParams.synMechParams['NK23'] = {'mod': 'NK1_DynSyn'    , 'tau_rise': 200, 'tau_decay': 3000           }
netParams.synMechParams['GABA'] = {'mod': 'GABAa_DynSyn'  , 'tau_rise': 0.1, 'tau_decay': 20   , 'e': -70}
netParams.synMechParams['GLY']  = {'mod': 'Glycine_DynSyn', 'tau_rise': 0.1, 'tau_decay': 10             }

###################################################################################################################################
#
#   Weight Parameters
#
###################################################################################################################################

AB = 1.0
AD = 1.0
C  = 1.0

###################################################################################################################################
#
#   Connect NetStims
#
###################################################################################################################################

netParams.connParams['AMPA_NS->SG0'] = {
    'nonLinear': True,
    'preConds': {'popLabel': 'NS'}, 
    'postConds': {'popLabel': 'SG'},  
    'weight': 0.00097067 * AB,
    'sec': 'dend',
    'delay': starts[0:15], 
    'loc': 0.51,
    'synMech': 'AMPA',
    'connList': [ [0, 0] for x in range(15) ] }

netParams.connParams['AMPA_NS->WDR0'] = {
    'nonLinear': True,
    'preConds': {'popLabel': 'NS'}, 
    'postConds': {'popLabel': 'WDR'},  
    'weight': 0.0016 * AB,
    'sec': 'dend',
    'delay': starts[15:30], 
    'loc': 0.50,
    'synMech': 'AMPA',
    'connList': [ [0, 0] for x in range(15) ] }

netParams.connParams['NMDA_NS->WDR0'] = {
    'nonLinear': True,
    'preConds': {'popLabel': 'NS'}, 
    'postConds': {'popLabel': 'WDR'},  
    'weight': 6.6667e-5 * AB,
    'sec': 'dend',
    'delay': starts[30:45], 
    'loc': 0.50,
    'synMech': 'NMDA',
    'connList': [ [0, 0] for x in range(15) ] }

##############################################################################################################
# For the purpose of recreating original, however, AMPA_NS->SG has no effect on simulation as is (weight is 0)
##############################################################################################################
netParams.connParams['AMPA_NS->SG1'] = {
    'nonLinear': True,
    'preConds': {'popLabel': 'NS'}, 
    'postConds': {'popLabel': 'SG'},  
    'weight': 0 * AB,
    'sec': 'dend',
    'delay': starts[45:60], 
    'loc': 0.51,
    'synMech': 'AMPA',
    'connList': [ [0, 0] for x in range(15) ] }

netParams.connParams['AMPA_NS->WDR1'] = {
    'nonLinear': True,
    'preConds': {'popLabel': 'NS'}, 
    'postConds': {'popLabel': 'WDR'},  
    'weight': 0.0016 * AD,
    'sec': 'dend',
    'delay': starts[60:75], 
    'loc': 0.50,
    'synMech': 'AMPA',
    'connList': [ [0, 0] for x in range(15) ] }

netParams.connParams['NMDA_NS->WDR1'] = {
    'nonLinear': True,
    'preConds': {'popLabel': 'NS'}, 
    'postConds': {'popLabel': 'WDR'},  
    'weight': 6.6667e-5 * AD,
    'sec': 'dend',
    'delay': starts[75:90], 
    'loc': 0.50,
    'synMech': 'NMDA',
    'connList': [ [0, 0] for x in range(15) ] }

###############################################################################################################
# For the purpose of recreating original, however, AMPA_NS->SG has no effect on simulation as is (delay is 2e9)
###############################################################################################################
netParams.connParams['AMPA_NS->SG2'] = {
    'nonLinear': True,
    'preConds': {'popLabel': 'NS'}, 
    'postConds': {'popLabel': 'SG'},  
    'weight': 0.0013333 * AB,
    'sec': 'dend',
    'delay': starts[90:105], 
    'loc': 0.51,
    'synMech': 'AMPA',
    'connList': [ [0, 1] for x in range(15) ] }

netParams.connParams['AMPA_NS->IN0'] = {
    'nonLinear': True,
    'preConds': {'popLabel': 'NS'}, 
    'postConds': {'popLabel': 'IN'},  
    'weight': 0.008 * C,
    'sec': 'dend',
    'delay': starts[105:135], 
    'loc': 0.5,
    'synMech': 'AMPA',
    'connList': [ [0, 0] for x in range(30) ] }

netParams.connParams['NMDA_NS->IN0'] = {
    'nonLinear': True,
    'preConds': {'popLabel': 'NS'}, 
    'postConds': {'popLabel': 'IN'},  
    'weight': 0.004 * C,
    'sec': 'dend',
    'delay': starts[135:165], 
    'loc': 0.5,
    'synMech': 'NMDA',
    'connList': [ [0, 0] for x in range(30) ] }

netParams.connParams['NK1_NS->IN0'] = {
    'nonLinear': True,
    'preConds': {'popLabel': 'NS'}, 
    'postConds': {'popLabel': 'IN'},  
    'weight': 6.6667e-7 * C,
    'sec': 'dend',
    'delay': starts[165:195], 
    'loc': 0.5,
    'synMech': 'NK13',
    'connList': [ [0, 0] for x in range(30) ] }

netParams.connParams['NK1_NS->WDR0'] = {
    'nonLinear': True,
    'preConds': {'popLabel': 'NS'}, 
    'postConds': {'popLabel': 'WDR'},  
    'weight': 4.5e-7 * C,
    'sec': 'dend',
    'delay': starts[195:225], 
    'loc': 0.5,
    'synMech': 'NK23',
    'connList': [ [0, 0] for x in range(30) ] }

###################################################################################################################################
#
#   Connect Cells
#
###################################################################################################################################


netParams.connParams['GABA_SG->IN0'] = {
    'nonLinear': True,
    'preConds': {'popLabel': 'SG'}, 
    'postConds': {'popLabel': 'IN'},  
    'weight': 0.00532,
    'sec': 'dend',
    'delay': 1, 
    'loc': 0.5,
    'synMech': 'GABA',
    'connList': [ [0, 0] ]}

netParams.connParams['AMPA_IN->WDR'] = {
    'nonLinear': True,
    'preConds': {'popLabel': 'IN'}, 
    'postConds': {'popLabel': 'WDR'},  
    'weight': 1.2e-5,
    'sec': 'dend',
    'delay': 1, 
    'loc': 0.5,
    'synMech': 'AMPA',
    'connList': [ [0, 0] for x in range(30) ]}

netParams.connParams['NMDA_IN->WDR'] = {
    'nonLinear': True,
    'preConds': {'popLabel': 'IN'}, 
    'postConds': {'popLabel': 'WDR'},  
    'weight': 9.6e-6,
    'sec': 'dend',
    'delay': 1, 
    'loc': 0.5,
    'synMech': 'NMDA',
    'connList': [ [0, 0] for x in range(30) ]}

netParams.connParams['GLY_SG->WDR'] = {
    'nonLinear': True,
    'preConds': {'popLabel': 'SG'}, 
    'postConds': {'popLabel': 'WDR'},  
    'weight': 0.00532,
    'sec': 'dend',
    'delay': 1, 
    'loc': 0.5,
    'synMech': 'GLY',
    'connList': [ [0, 0] ]}

netParams.connParams['GABA_SG->IN1'] = {
    'nonLinear': True,
    'preConds': {'popLabel': 'SG'}, 
    'postConds': {'popLabel': 'IN'},  
    'weight': 0.00532,
    'sec': 'dend',
    'delay': 1, 
    'loc': 0.5,
    'synMech': 'GABA',
    'connList': [ [0, 0] ]}

netParams.connParams['GABA_SG->WDR'] = {
    'nonLinear': True,
    'preConds': {'popLabel': 'SG'}, 
    'postConds': {'popLabel': 'WDR'},  
    'weight': 0.00532,
    'sec': 'dend',
    'delay': 1, 
    'loc': 0.5,
    'synMech': 'GABA',
    'connList': [ [0, 0] ]}

###########################################################################################################################
# For the purpose of recreating original, however, all following connParams has no effect on simulation as is (weight is 0)
###########################################################################################################################
netParams.connParams['GABA_SG1->IN'] = {
    'nonLinear': True,
    'preConds': {'popLabel': 'SG'}, 
    'postConds': {'popLabel': 'IN'},  
    'weight': 0,
    'sec': 'dend',
    'delay': 1, 
    'loc': 0.5,
    'synMech': 'GABA',
    'connList': [ [1, 0] ]}

netParams.connParams['GABA_SG1->WDR'] = {
    'nonLinear': True,
    'preConds': {'popLabel': 'SG'}, 
    'postConds': {'popLabel': 'WDR'},  
    'weight': 0,
    'sec': 'dend',
    'delay': 1, 
    'loc': 0.5,
    'synMech': 'GABA',
    'connList': [ [1, 0], [1, 0] ]}

