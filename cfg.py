#------------------------------------------------------------------------------
# SIMULATION CONFIGURATION
#------------------------------------------------------------------------------

from netpyne import specs

simConfig = specs.SimConfig()   # object of class SimConfig to store the simulation configuration

simConfig.hParams['celsius'] = 36
simConfig.hParams['v_init'] = -65
simConfig.dt = 0.0125
simConfig.duration = 1#22100
# Simulation parameters

simConfig.checkErrors=False # True # 
simConfig.verbose = False # True  # show detailed messages 

# Recording 
simConfig.recordCells = [0]  # which cells to record from

simConfig.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'} }

simConfig.recordStim = True  # record spikes of cell stims
simConfig.recordStep = 0.1 # Step size in ms to save data (eg. V traces, LFP, etc)
#simConfig.cvode_active = True

# Saving
simConfig.simLabel = "sim"
simConfig.saveFolder = "data"
simConfig.saveFileStep = 1000 # step size in ms to save data to disk
simConfig.savePickle = True # Whether or not to write spikes etc. to a .mat file

simConfig.analysis['plotTraces'] = {'include': ['SG', 'IN', 'WDR'], 'timeRange': [0, simConfig.duration], 'oneFigPer': 'trace', 'overlay': True, 'showFig' : False, 'saveFig':'./images/plotTraces.png'} # plot recorded traces for this list of cells