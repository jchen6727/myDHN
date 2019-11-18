from netpyne import specs
from netpyne.batch import Batch

params = specs.ODict()

params['perc'] = [ 30, 60, 90] 
params['erev'] = [ 40 ]

b = Batch(params = params, cfgFile = 'cfg.py', netParamsFile = 'netParams.py')

b.batchLabel = 'DHN'
b.saveFolder = 'batch_data'
b.method = 'grid'
b.runCfg = {'type': 'mpi_bulletin', 'script': 'init.py', 'skip': True}

b.run()