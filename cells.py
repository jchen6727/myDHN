from genrn import genrn

def createIN():
    cellRule = {
        'secs': {
                 'soma'   : {'L': 10.0, 'diam': 10.0, 'nseg': 1, 'Ra': 150},
                 'dend'   : {'L': 1371, 'diam': 1.4 , 'nseg': 1, 'Ra': 150},
                 'hillock': {'L': 30  , 'diam': 1.5 , 'nseg': 1, 'Ra': 150},
        },
        'ions': {'k': -84.0, 'na': 60, 'ca': 132.5},
        'mechs': {'pas': {'g': 1.1e-05, 'e': -70}},
        'cons': (
                 ('dend', 'soma'),
                 ('soma', 'hillock')
                )}
    IN = genrn(**cellRule)
    IN/'soma'<{'B_Na': {'gnabar': 0.008},
               'B_A': {}, 'B_DR': {}, 'KDR': {},
               'KDRI': {'gkbar': 0.0043}}
    IN/'hillock'<{'B_Na': {'gnabar': 3.45},
                  'B_A': {}, 'B_DR': {}, 'KDR': {},
                  'KDRI': {'gkbar': 0.076}}
    IN/'dend'<{'SS': {'gnabar':0},
               'B_DR': {},
               'KDR': {},
               'KDRI': {'gkbar':0.034}}
    IN.init_nernsts()
    return IN

def createEX():
    cellRule = {
        'secs': {
                 'dend'   : {'L': 400 , 'diam': 3.0 , 'nseg': 1, 'Ra': 150},
                 'soma'   : {'L': 20.0, 'diam': 20.0, 'nseg': 1, 'Ra': 150},
                 'hillock': {'L': 9.0 , 'diam': 1.5 , 'nseg': 1, 'Ra': 150},
                 'axon'   : {'L': 1000, 'diam': 1.0 , 'nseg': 1, 'Ra': 150},
        },
        'ions': {'k': -70.0, 'na': 53.0, 'ca': 132.5},
        'mechs': {'pas': {'g': 4.2e-05, 'e': -65}},
        'cons': (
                 ('dend', 'soma'),
                 ('soma', 'hillock'),
                 ('hillock', 'axon')
                )}
    EX = genrn(**cellRule)
    EX/'dend'<{'HH2': {'gnabar': 0, 'gkbar': 0.036},
               'CaIntraCellDyn': {'depth': 0.1, 'cai_tau': 2.0, 'cai_inf': 50e-6},
               'iKCa': {'gbar': 0.002}}
    EX/'soma'<{'HH2': {'gnabar': 0, 'gkbar': 0.001075, 'vtraub': -55},
               'CaIntraCellDyn': {'depth': 0.1, 'cai_tau': 1.0, 'cai_inf': 50e-6},
               'iKCa': {'gbar': 0.002}}
    EX/'hillock'<{'HH2': {'gnabar': 3.45, 'gkbar': 0.076, 'vtraub': -55}}
    # axon only has one mechanism besides pas, with 0 ion conductance
    EX.init_nernsts()
    return EX

def createWDR():
    cellRule = {
        'secs': {
                 'soma'   : {'L': 20.0, 'diam': 20.0, 'nseg': 1, 'Ra': 150},
                 'dend'   : {'L': 350 , 'diam': 2.5 , 'nseg': 1, 'Ra': 150},
                 'hillock': {'L': 9.0 , 'diam': 1.5 , 'nseg': 1, 'Ra': 150},
                 'axon'   : {'L': 1000, 'diam': 1.0 , 'nseg': 1, 'Ra': 150},
        },
        'ions': {'k': -70.0, 'na': 53.0, 'ca': 132.5},
        'mechs': {'pas': {'g': 4.2e-05, 'e': -65}},
        'cons': (
                 ('dend', 'soma'),
                 ('soma', 'hillock'),
                 ('hillock', 'axon')
                )}
    WDR = genrn(**cellRule)
    WDR/'soma'<{'HH2': {'gnabar': 0, 'gkbar': 0.001075, 'vtraub': -55},
                'CaIntraCellDyn': {'depth': 0.1, 'cai_tau': 1.0, 'cai_inf': 50e-6},
                'iCaL': {'pcabar': 0.001},
                'iKCa': {'gbar': 0.0001},
                'iNaP': {'gnabar': 0.0001}}
    WDR/'dend'<{'HH2': {'gnabar': 0, 'gkbar': 0.036},
                'CaIntraCellDyn': {'depth': 0.1, 'cai_tau': 2.0, 'cai_inf':50e-6},
                'iCaL': {'pcabar': 3e-5},
                'iKCa': {'gbar': 0.001}}
    WDR/'hillock'<{'HH2': {'gnabar': 3.45, 'gkbar': 0.076, 'vtraub': -55}}
    return WDR

if __name__=='__main__':
    inc = createIN()
    exc = createEX()
    wdrc= createWDR()
    print("IN cell:\n%s"  %(inc) )
    print("EX cell:\n%s"  %(exc) )
    print("WDR cell:\n%s" %(wdrc))
    pass