#------------------------------------------------------------------------------
# SIMULATION CONFIGURATION
#------------------------------------------------------------------------------

from netpyne import specs

cfg = specs.SimConfig()   # object of class SimConfig to store the simulation configuration

#------------------------------------------------------------------------------
# NA CHANNEL PARAMETERS
#------------------------------------------------------------------------------

cfg.hParams['celsius'] = 36
cfg.hParams['v_init'] = -65
cfg.dt = 0.0125
cfg.duration = 21000
# Simulation parameters

cfg.checkErrors=False # True # 
cfg.verbose = False # True  # show detailed messages 

# Recording 
cfg.recordCells = [0]  # which cells to record from

cfg.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'} }

cfg.recordStim = True  # record spikes of cell stims
cfg.recordStep = 0.1 # Step size in ms to save data (eg. V traces, LFP, etc)
#cfg.cvode_active = True

# Saving
cfg.simLabel = "sim"
cfg.saveFolder = "data"
cfg.saveFileStep = 1000 # step size in ms to save data to disk
cfg.savePickle = True # Whether or not to write spikes etc. to a .mat file

cfg.analysis['plotTraces'] = {'include': ['SG', 'IN', 'WDR'], 'oneFigPer': 'trace', 'overlay': True, 'showFig' : False, 'saveFig': True} # plot recorded traces for this list of cells
cfg.analysis['plotRaster'] = {'include': ['SG', 'IN', 'WDR'], 'orderInverse': False, 'showFig' : False, 'saveFig': True} 