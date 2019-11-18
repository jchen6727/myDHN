from netpyne import sim  # import netpyne init module

cfg, netParams = sim.readCmdLineArgs(simConfigDefault='cfg.py', netParamsDefault='netParams.py')
###############################################################################
# create, simulate, and analyse network
###############################################################################
sim.createSimulateAnalyze(netParams = netParams, simConfig = cfg)
