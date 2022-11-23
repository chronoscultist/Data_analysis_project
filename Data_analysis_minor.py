
from math import*
#importerar alla functioner i pythons biblotek
import pandas as pd
#Importerarar Pandas programmet från bibloteket
    # det gör det möjligt för att python ska kunna bearbeta data från csv filer.
import matplotlib.pyplot as plt
#importerar matplotlib.pyplot graf funktionen från bibloteket så att det
    # gör det möjligt för att python ska kunna plotta datan i en graf
import numpy as np
#importerar numpy från bibloteket så att den kan användas för att beräkna medelvärdet av grupper av punkter
df = pd.read_csv('Temp_data.csv', delimiter=';', encoding='utf-8', parse_dates=['Date'], index_col='Date')
# pd.read_csv så anropar vi fuktionen read_csv som finns i pandas biblotek.
    # Temp_data.csv är sökvägen för csv filen som informationen ska extracteras från
        # delimites, bestämmer vilken delimiter, eller separerande tecken, som vi har genom att skriva
            # encoding gör det möjligt för att python och pandas att hantera svenska täcken som ÅÄÖ
                #Parse_dates pandas läser in dessa datum i ett speciellt format som görs att det kan hanteras smidigare.
                        #'DATE' är placeholder variabel som ska bytas ut med ett värde. datum.

df_lulea=df[df.Location=='Luleå'].copy()
#Skapar och binder  variabel df_lulea till data som är releterad till området av Luleå
    #copy ger oss värden av ursprunliga datan utan att modifiera den

df_lulea_temp = df_lulea.Temperature
#variabel df_lulea_temp bunden till tempraturen för ett specifikt område från tidigare commando.

interval_data = df_lulea_temp['1995-12']
#interval_data extracterar data från tidigare commando inom ett specifik intervall i det givna datum.

interval_data.plot()
#plottar intervallet av dagarna i månaden med temperatus värdet i en graf.
plt.show()
#visar den plottade grafen.

