import netParams # import parameters file
import cfg

from netpyne import sim  # import netpyne init module
from neuron import h

###############################################################################
# create, simulate, and analyse network
###############################################################################
sim.createSimulateAnalyze(netParams = netParams.netParams, simConfig = cfg.simConfig)

ncl = h.List('NetCon')
fp = open('netcons_netpyne.csv', "w")
for nc in ncl:
    netcon = "%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % ( nc.precell(), nc.postseg(), nc.syn(), nc.syn().tau_rise, nc.syn().tau_decay, nc.syn().e, nc.threshold, nc.weight[0], nc.delay )
    fp.write(netcon)

fp.close()