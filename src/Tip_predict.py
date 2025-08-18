import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import poisson, expon, skew, norm
from scipy import stats
import warnings

warnings.filterwarnings("ignore")

data = {
    "Tip": [
        "235.49",
        "498.49",
        "15.46",
        "340.55",
        "370.14",
        "36.88",
        "66.97",
        "150",
        "310.68",
        "420.47",
        "301.24",
        "223.59",
        "433.16",
        "73",
    ],
    "Date": [
        "11/07/2025",
        "12/07/2025",
        "13/07/2025",
        "15/07/2025",
        "16/07/2025",
        "17/07/2025",
        "18/07/2025",
        "19/07/2025",
        "20/07/2025",
        "21/07/2025",
        "22/07/2025",
        "24/07/2025",
        "26/07/2025",
        "28/07/2025",
    ],
}

# Create DataFrame
df = pd.DataFrame(data)


print(df)

t = ["90.96", "380.54", "233.18", "272.35", "50.88", "54.71"]
m = ["01/08/2025", "02/08/2025", "04/08/2025", "05/08/2025", "06/08/2025", "08/08/2025"]

ziped = list(zip(t, m))
new_data = pd.DataFrame(ziped, columns=["Tip", "Date"])
df = pd.concat([df, new_data], ignore_index=True)


# Convert Tip to float
df["Tip"] = df["Tip"].astype(float)

# Convert Date to datetime
df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import poisson, expon, skew, norm
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

data = {
    'Tip': [
        '235.49', '498.49', '15.46', '340.55', '370.14',
        '36.88', '66.97', '150', '310.68', '420.47',
        '301.24', '223.59', '433.16', '73'
    ],
    'Date': [
        '11/07/2025', '12/07/2025', '13/07/2025', '15/07/2025', '16/07/2025',
        '17/07/2025', '18/07/2025', '19/07/2025', '20/07/2025', '21/07/2025',
        '22/07/2025', '24/07/2025', '26/07/2025', '28/07/2025'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)



print(df)

t = ['90.96','380.54','233.18','272.35','50.88','54.71']
m = [ '01/08/2025'
     ,'02/08/2025'
     ,'04/08/2025'
     ,'05/08/2025'
     ,'06/08/2025'
     ,'08/08/2025']

ziped = list(zip(t,m))
new_data = pd.DataFrame(ziped, columns=['Tip', 'Date'])
df = pd.concat([df, new_data], ignore_index=True)


# Convert Tip to float
df['Tip'] = df['Tip'].astype(float)

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')

def percentil_media(day_tip) :
  df['Tip'] = df.append(day_tip)
  df['Date'] =  today?
  tip_mean = df['Tip'].mean()
  tip_std = df['Tip'].std()
  df['Z_Score'] = (df['Tip'] - tip_mean) / tip_std
  norm.cdf(day_tip, tip_mean, tip_std)
  
  import pandas as pd
from scipy.stats import norm
from datetime import datetime

def percentil_media(day_tip, day_date=None):
    global df  # para alterar o df global

    # Se não for informada a data, usar hoje
    if day_date is None:
        day_date = datetime.today().strftime('%d/%m/%Y')

    # Criar nova linha
    #new_row = pd.DataFrame({'Tip': [float(day_tip)], 'Date': [pd.to_datetime(day_date, format='%d/%m/%Y')]})
    date_obj = pd.to_datetime(day_date, format='%d/%m/%Y')

# Criar nova linha com colunas extras
    new_row = pd.DataFrame({
      'Tip': [float(day_tip)],
      'Date': [date_obj],
      'Month': [date_obj.month],
      'Day': [date_obj.day],
      'Year': [date_obj.year],
      'Weekday': [date_obj.strftime('%A')]
})
    # Adicionar ao DataFrame
    df = pd.concat([df, new_row], ignore_index=True)

    # Recalcular média, desvio padrão e Z-score
    tip_mean = df['Tip'].mean()
    tip_std = df['Tip'].std()
    df['Z_Score'] = (df['Tip'] - tip_mean) / tip_std

    # Adicionar coluna com percentil
    percentil = 1 - norm.cdf(day_tip, loc=tip_mean, scale=tip_std)

    return percentil

# Exemplo de uso
df_atualizado = percentil_media(300)  # sem passar data → usa hoje
print(df_atualizado)

