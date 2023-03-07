import missingno as msno
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# Define dictionary
dictionary = {"Column1":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,np.nan,16,17,18,19,20],
              "Column2":[1,2,3,4,np.nan,6,7,8,np.nan,10,np.nan,12,13,14,15,16,np.nan,18,np.nan,20],
              "Column3":[1,2,3,4,np.nan,6,7,8,9,10,11,12,13,np.nan,15,16,17,18,np.nan,20]}
# Create data frame from dictionary
data_missingno = pd.DataFrame(dictionary)

# import missingno library

msno.matrix(data_missingno)
plt.show()
