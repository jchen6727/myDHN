from genrn import genrn

class IN(genrn):
    def __init__(self):
        self.cellRule = {
            'secs' : {'soma': {'L': 96.0, 'nseg': 1, 'diam': 96.0, 'Ra': 100.0, 'cm': 1.0}},
            'ions' : {'k': -77.0, 'kf': -100.0, 'nat': 50.0},
            'mechs': {'im': {'gkbar': 3e-05, 'taumax': 1000.0},
                      'inak2005': {'gkfbar': 0.03, 'gnatbar': 0.3},
                      'pas': {'g': 0.0001, 'e': -70.0},
                      }
            }
        super().__init__(**self.cellRule)
        super().insert_mech('soma', 'gabaat', { 'cl': ecl })

def EX():
    cellRule = {
        'secs': {
                 'dend'   : {'L': 400 , 'diam': 3.0 , 'nseg': 1, 'Ra': 150},
                 'soma'   : {'L': 20.0, 'diam': 20.0, 'nseg': 1, 'Ra': 150},
                 'hillock': {'L': 9.0 , 'diam': 1.5 , 'nseg': 1, 'Ra': 150},
                 'axon'   : {'L': 1000, 'diam': 1.0 , 'nseg': 1, 'Ra': 150},
        },
        'ions': {'k': -84.0, 'na': 53.0, 'ca': 132.5},
        'mechs': {'pas': {'g': 4.2e-05, 'e': -65}},
        'cons': (
                 ('dend', 'soma'),
                 ('soma', 'hillock'),
                 ('hillock', 'axon')
                )}
    EX = genrn(**cellRule)
    EX>'dend'
    EX>'soma'
    EX>'hillock'
    EX>'axon'
        super().insert_mech('soma', 'gabaat', { 'cl': ecl })

class WDR(genrn):
    def __init__(self):
        self.cellRule = {
            'secs' : {'soma': {'L': 64.86, 'nseg': 1, 'diam': 70.0, 'Ra': 100.0, 'cm': 1.0}},
            'ions' : {'ca': 120.0, 'kf': -100.0, 'nat': 50.0},
            'mechs': {'cad': {'cainf': 0.00024, 'depth': 1.0, 'kt': 0.0, 'taur': 5.0},
                      'inak2005': {'gkfbar': 0.06, 'gnatbar': 0.19},
                      'it2': {'gcabar': 0.003, 'qh': 2.5, 'qm': 2.5, 'shift': 2.0, 'taubase': 85.0},
                      # 'itrecustom': {'gcabar': 0.0, 'qh': 2.5, 'qm': 2.5, 'shift': 2.0, 'taubase': 85.0},
                      'pas': {'g': 5e-05, 'e': -90.0}},
            }
        super().__init__(**self.cellRule)
        super().insert_mech('soma', 'gabaat', { 'cl': ecl })

if __name__=='__main__':
    inc = IN()
    exc = EX()
    wdrc= WDR()
    print("IN cell:\n%s"  %(inc) )
    print("EX cell:\n%s"  %(exc) )
    print("WDR cell:\n%s" %(wdrc))
    pass