from netpyne import specs
from netpyne import sim

from netStimVec import starts #import NetStim start times from file netStimVec.py

netParams = specs.NetParams()

###################################################################################################################################
#
#   Create Populations
#
###################################################################################################################################

#for i, start in enumerate(starts):
#    netParams.popParams['NS' + str(i)] = {'cellModel': 'NetStim', 'interval': 1000, 'noise': 0, 'start': starts[i], 'number': 20, 'numCells': 1}

#DOESN'T WORK
#cellList = [ {'start': start} for start in starts ]
#netParams.popParams['NS'] = {'cellModel': 'NetStim', 'interval': 1000, 'noise': 0, 'number': 20, 'cellList': cellList}

netParams.popParams['NS' ] = {'cellModel': 'NetStim', 'interval': 1000, 'noise': 0, 'start': 0, 'number': 20, 'numCells': 1}

netParams.popParams['SG' ] = {'cellType': 'SG', 'numCells': 1 }
netParams.popParams['IN' ] = {'cellType': 'IN', 'numCells': 1 }
netParams.popParams['WDR'] = {'cellType': 'WDR', 'numCells': 1 }

SGcellRule  = netParams.importCellParams(label='SGrule' , conds={'cellType': 'SG' }, fileName='SG.tem' , cellName='SG')
INcellRule  = netParams.importCellParams(label='INrule' , conds={'cellType': 'IN' }, fileName='IN.tem' , cellName='IN')
WDRcellRule = netParams.importCellParams(label='WDRrule', conds={'cellType': 'WDR'}, fileName='WDR.tem', cellName='WDR')

netParams.cellParams['SGRule' ] = SGcellRule
netParams.cellParams['INRule' ] = INcellRule
netParams.cellParams['WDRRule'] = WDRcellRule

###################################################################################################################################
#   NS->Cell Synaptic Mechanisms
###################################################################################################################################




netParams.synMechParams['NK1'] = {'mod': 'NK1_DynSyn', 'tau_rise': 100, 'tau_decay': 3000}

###################################################################################################################################
#   Cell->Cell Synaptic Mechanisms
###################################################################################################################################

netParams.synMechParams['GABA_0.1_20_70'] = {'mod': 'GABAa_DynSyn', 'tau_rise': 0.1, 'tau_decay': 20, 'e': -70}
netParams.synMechParams['AMPA_0.1_5'] = {'mod': 'AMPA_DynSyn', 'tau_rise': 0.1, 'tau_decay': 5}
netParams.synMechParams['NMDA_2_100'] = {'mod': 'NMDA_DynSyn', 'tau_rise': 2, 'tau_decay': 100}
netParams.synMechParams['GLY'] = {'mod': 'Glycine_DynSyn', 'tau_rise': 0.1, 'tau_decay': 10}
#netParams.synMechParams['GABA_0.1_20_70'] = {'mod': 'GABAa_DynSyn', 'tau_rise': 0.1, 'tau_decay': 20, 'e': -70}

###################################################################################################################################
#
#   Connect NetStims
#
###################################################################################################################################


netParams.connParams['NK1_NS->IN'] = {
    'nonLinear': True,
    'preConds': {'popLabel': 'SG'}, 
    'postConds': {'popLabel': 'IN'},  
    'weight': 4.5e-7,
    'sec': 'dend',
    'delay': starts[196:226], 
    'loc': 0.5,
    'threshold': 0,
    'synMech': ['NK1'] * 30,
    'connList': [ [0, 0] ]}


###################################################################################################################################
#
#   Connect Cells
#
###################################################################################################################################

connList = [ [ 0, 0 ] for x in range(30) ]

netParams.connParams['GABA_SG->IN'] = {
    'nonLinear': True,
    'preConds': {'popLabel': 'SG'}, 
    'postConds': {'popLabel': 'IN'},  
    'weight': 0.00532,
    'sec': 'dend',
    'delay': 1, 
    'loc': 0.5,
    'threshold': 0,
    'synMech': 'GABA_0.1_20_70',
    'connList': [ [0, 0] ]}

netParams.connParams['AMPA_IN->WDR'] = {
    'nonLinear': True,
    'preConds': {'popLabel': 'IN'}, 
    'postConds': {'popLabel': 'WDR'},  
    'weight': 1.2e-5,
    'sec': 'dend',
    'delay': 1, 
    'loc': 0.5,
    'threshold': 0,
    'synMech': 'AMPA_0.1_5',
    'connList': connList}

netParams.connParams['NMDA_IN->WDR'] = {
    'nonLinear': True,
    'preConds': {'popLabel': 'IN'}, 
    'postConds': {'popLabel': 'WDR'},  
    'weight': 9.6e-6,
    'sec': 'dend',
    'delay': 1, 
    'loc': 0.5,
    'threshold': 0,
    'synMech': 'NMDA_2_100',
    'connList': connList}

netParams.connParams['GLY_IN->WDR'] = {
    'nonLinear': True,
    'preConds': {'popLabel': 'SG'}, 
    'postConds': {'popLabel': 'WDR'},  
    'weight': 0.00532,
    'sec': 'dend',
    'delay': 1, 
    'loc': 0.5,
    'threshold': 0,
    'synMech': 'GLY',
    'connList': [ [0, 0] ]}

netParams.connParams['GABA_IN->WDR'] = {
    'nonLinear': True,
    'preConds': {'popLabel': 'SG'}, 
    'postConds': {'popLabel': 'IN'},  
    'weight': 0.00532,
    'sec': 'dend',
    'delay': 1, 
    'loc': 0.5,
    'threshold': 0,
    'synMech': 'GABA_0.1_20_70',
    'connList': [ [0, 0] ]}


##netcon = "%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % ( nc.precell(), nc.postcell(), nc.syn(), nc.syn().tau_rise, nc.syn().tau_decay, nc.syn().e, nc.postseg(), nc.weight[0], nc.delay )
##
##[[x.precell(), x.syn(), x.postcell(), x.postseg()] for x in ncl]
