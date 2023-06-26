import pandas_ta as pta
import pandas as pd
import numpy as np
    
names = pd.Series(np.random.randint(0, 10, 20))

oes =pta.rsi(names, timeperiod=14)

print(oes)
