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

## criando as colunas month, day and year and weekday
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
df["Year"] = df["Date"].dt.year
df["Weekday"] = df["Date"].dt.strftime("%A")


##### função para imput de dados


def percentil_media2(day_tip, day_date=None):
    global df  # para alterar o df global

    if day_date is None:
        date_obj = pd.to_datetime("today")
    else:
        # aceita formatos diferentes e força que o primeiro número seja o dia
        date_obj = pd.to_datetime(day_date, dayfirst=True, errors="raise")

    # Criar nova linha com colunas extras
    new_row = pd.DataFrame(
        {
            "Tip": [float(day_tip)],
            "Date": [date_obj],
            "Month": [date_obj.month],
            "Day": [date_obj.day],
            "Year": [date_obj.year],
            "Weekday": [date_obj.strftime("%A")],
        }
    )

    # Adicionar ao DataFrame
    df = pd.concat([df, new_row], ignore_index=True)

    # Recalcular média e desvio padrão
    tip_mean = df["Tip"].mean()
    tip_std = df["Tip"].std()

    # Calcular % acima/abaixo da média
    perc_diff = ((day_tip - tip_mean) / tip_mean) * 100

    # Calcular percentil (opcional, se quiser manter)
    percentil = 1 - norm.cdf(day_tip, loc=tip_mean, scale=tip_std)

    # Procurar últimas 2 entradas com o mesmo dia da semana (exceto o input atual)
    weekday = date_obj.strftime("%A")
    same_weekday = df[df["Weekday"] == weekday].iloc[
        :-1
    ]  # remove o último (input atual)
    last_two = same_weekday.tail(2)

    comparisons = {}
    for i, row in last_two.iterrows():
        diff = ((day_tip - row["Tip"]) / row["Tip"]) * 100
        comparisons[f"Comparado com{row['Date'].strftime('%d/%m/%Y')}"] = diff
    return {
        "Resumo": (
            f"Esse tip colocado é {abs(perc_diff):.2f}% "
            + ("acima" if perc_diff > 0 else "abaixo")
            + " da média"
        ),
        "Comparisons_last_two_same_weekday": {
            row["Date"].strftime("%d/%m/%Y"): (
                f"{abs(((day_tip - row['Tip']) / row['Tip']) * 100):.2f}% "
                + ("acima" if day_tip > row["Tip"] else "abaixo")
            )
            for _, row in last_two.iterrows()
        },
    }


percentil_media2(323.98, "15/08/2025")
percentil_media2(233.7, "16/08/2025")
percentil_media2(124, "19/08/2025")
percentil_media2(198, "20/08/2025")


df


df.groupby("Month")["Tip"].sum()
#####
df = df.drop(df.tail(1).index)

# Global DataFrame to store tips
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=["Date", "Tip", "Z_Score"])


def percentil_media(day_tip):
    df = st.session_state.df

    # Add new row with today's date
    new_row = pd.DataFrame(
        {"Date": [datetime.today().strftime("%Y-%m-%d")], "Tip": [float(day_tip)]}
    )

    df = pd.concat([df, new_row], ignore_index=True)

    # Calculate stats
    tip_mean = df["Tip"].mean()
    tip_std = df["Tip"].std(ddof=0)

    # Compute z-scores
    df["Z_Score"] = (df["Tip"] - tip_mean) / tip_std

    # Save back to session state
    st.session_state.df = df

    # Return the percentile of today's tip
    return norm.cdf(float(day_tip), tip_mean, tip_std)


# --- Streamlit UI ---
st.title("💰 Tip Tracker with Percentile Analysis")

# Input field
day_tip = st.number_input("Enter today's tip:", min_value=0.0, format="%.2f")

if st.button("Add Tip"):
    percentile = percentil_media(day_tip)
    st.success(f"Tip added! Today's tip is at the {percentile:.2%} percentile.")

# Show DataFrame
st.write("### Historical Data")
st.dataframe(st.session_state.df)

# Show chart
if not st.session_state.df.empty:
    st.line_chart(st.session_state.df.set_index("Date")["Tip"])
