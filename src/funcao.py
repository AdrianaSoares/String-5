import pandas as pd


def dropar_na(df, coluna, limite_dados_faltantes):
    print('olá')
    if df[coluna].isna().mean() > limite_dados_faltantes:
        df = df.dropna(subset=[coluna])
    return df


def limpar_outlier(df, coluna):
    print('olá')
    media = df[coluna].mean()  # calculo da média
    dp = df[coluna].std()  # desvio padrão
    # limite superior (como não é uma curva normal fez a multiplicação por 2)
    ls = media + 2*dp
    li = media - 2*dp  # limite inferior
    df = df[(df[coluna] > li) & (df[coluna] < ls)]

    return df
