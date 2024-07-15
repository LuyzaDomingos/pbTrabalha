# import pandas as pd
# import numpy as np

# big_group = {
#     'Administração Pública, Defesa e Seguridade Social': 'Serviços',
#     'Agricultura, Pecuária, Produção Florestal, Pesca e AqÜIcultura': 'Agropecuária',
#     'Alojamento e Alimentação': 'Serviços',
#     'Artes, Cultura, Esporte e Recreação': 'Serviços',
#     'Atividades Administrativas e Serviços Complementares': 'Serviços',
#     'Atividades Financeiras, de Seguros e Serviços Relacionados': 'Serviços',
#     'Atividades Imobiliárias': 'Serviços',
#     'Atividades Profissionais, Científicas e Técnicas': 'Serviços',
#     'Comércio, Reparação de Veículos Automotores e Motocicletas': 'Comércio',
#     'Construção': 'Construção',
#     'Educação': 'Serviços',
#     'Eletricidade e Gás': 'Indústria',
#     'Indústrias Extrativas': 'Indústria',
#     'Indústrias de Transformação': 'Indústria',
#     'Informação e Comunicação': 'Serviços',
#     'Não identificado': 'Não Identificado',
#     'Organismos Internacionais e Outras Instituições Extraterritoriais': 'Serviços',
#     'Outras Atividades de Serviços': 'Serviços',
#     'Saúde Humana e Serviços Sociais': 'Serviços',
#     'Serviços Domésticos': 'Serviços',
#     'Transporte, Armazenagem e Correio': 'Serviços',
#     'Água, Esgoto, Atividades de Gestão de Resíduos e Descontaminação': 'Indústria'
# }

# sectors_stats = {
# ('2023-01-01', -1, 'Agropecuária'): 617,
#  ('2023-01-01', -1, 'Comércio'): 4399,
#  ('2023-01-01', -1, 'Construção'): 2179,
#  ('2023-01-01', -1, 'Indústria'): 2835,
#  ('2023-01-01', -1, 'Serviços'): 6221,
#  ('2023-01-01', 1, 'Agropecuária'): 290,
#  ('2023-01-01', 1, 'Comércio'): 3858,
#  ('2023-01-01', 1, 'Construção'): 2417,
#  ('2023-01-01', 1, 'Indústria'): 1427,
#  ('2023-01-01', 1, 'Serviços'): 6536,
#  ('2023-02-01', -1, 'Agropecuária'): 439,
#  ('2023-02-01', -1, 'Comércio'): 3835,
#  ('2023-02-01', -1, 'Construção'): 2373,
#  ('2023-02-01', -1, 'Indústria'): 2211,
#  ('2023-02-01', -1, 'Serviços'): 5628,
#  ('2023-02-01', 1, 'Agropecuária'): 160,
#  ('2023-02-01', 1, 'Comércio'): 3695,
#  ('2023-02-01', 1, 'Construção'): 2897,
#  ('2023-02-01', 1, 'Indústria'): 1840,
#  ('2023-02-01', 1, 'Serviços'): 6408,
#  ('2023-03-01', -1, 'Agropecuária'): 1196,
#  ('2023-03-01', -1, 'Comércio'): 4017,
#  ('2023-03-01', -1, 'Construção'): 2563,
#  ('2023-03-01', -1, 'Indústria'): 4067,
#  ('2023-03-01', -1, 'Serviços'): 6198,
#  ('2023-03-01', 1, 'Agropecuária'): 306,
#  ('2023-03-01', 1, 'Comércio'): 4804,
#  ('2023-03-01', 1, 'Construção'): 2921,
#  ('2023-03-01', 1, 'Indústria'): 2056,
#  ('2023-03-01', 1, 'Serviços'): 7139,
#  ('2023-04-01', -1, 'Agropecuária'): 1663,
#  ('2023-04-01', -1, 'Comércio'): 3490,
#  ('2023-04-01', -1, 'Construção'): 2398,
#  ('2023-04-01', -1, 'Indústria'): 4360,
#  ('2023-04-01', -1, 'Serviços'): 5230,
#  ('2023-04-01', 1, 'Agropecuária'): 366,
#  ('2023-04-01', 1, 'Comércio'): 3712,
#  ('2023-04-01', 1, 'Construção'): 2537,
#  ('2023-04-01', 1, 'Indústria'): 1485,
#  ('2023-04-01', 1, 'Serviços'): 5860,
#  ('2023-05-01', -1, 'Agropecuária'): 404,
#  ('2023-05-01', -1, 'Comércio'): 3505,
#  ('2023-05-01', -1, 'Construção'): 2196,
#  ('2023-05-01', -1, 'Indústria'): 2512,
#  ('2023-05-01', -1, 'Serviços'): 5750,
#  ('2023-05-01', 1, 'Agropecuária'): 329,
#  ('2023-05-01', 1, 'Comércio'): 4581,
#  ('2023-05-01', 1, 'Construção'): 3154,
#  ('2023-05-01', 1, 'Indústria'): 2292,
#  ('2023-05-01', 1, 'Serviços'): 6879,
#  ('2023-06-01', -1, 'Agropecuária'): 232,
#  ('2023-06-01', -1, 'Comércio'): 3508,
#  ('2023-06-01', -1, 'Construção'): 2970,
#  ('2023-06-01', -1, 'Indústria'): 2171,
#  ('2023-06-01', -1, 'Não Identificado'): 1,
#  ('2023-06-01', -1, 'Serviços'): 5949,
#  ('2023-06-01', 1, 'Agropecuária'): 326,
#  ('2023-06-01', 1, 'Comércio'): 3889,
#  ('2023-06-01', 1, 'Construção'): 2753,
#  ('2023-06-01', 1, 'Indústria'): 1713,
#  ('2023-06-01', 1, 'Serviços'): 5927,
#  ('2023-07-01', -1, 'Agropecuária'): 211,
#  ('2023-07-01', -1, 'Comércio'): 3890,
#  ('2023-07-01', -1, 'Construção'): 2438,
#  ('2023-07-01', -1, 'Indústria'): 1743,
#  ('2023-07-01', -1, 'Não Identificado'): 1,
#  ('2023-07-01', -1, 'Serviços'): 5687,
#  ('2023-07-01', 1, 'Agropecuária'): 353,
#  ('2023-07-01', 1, 'Comércio'): 3935,
#  ('2023-07-01', 1, 'Construção'): 3082,
#  ('2023-07-01', 1, 'Indústria'): 3966,
#  ('2023-07-01', 1, 'Serviços'): 6111,
#  ('2023-08-01', -1, 'Agropecuária'): 229,
#  ('2023-08-01', -1, 'Comércio'): 3893,
#  ('2023-08-01', -1, 'Construção'): 2579,
#  ('2023-08-01', -1, 'Indústria'): 2005,
#  ('2023-08-01', -1, 'Serviços'): 5796,
#  ('2023-08-01', 1, 'Agropecuária'): 2919,
#  ('2023-08-01', 1, 'Comércio'): 4409,
#  ('2023-08-01', 1, 'Construção'): 3374,
#  ('2023-08-01', 1, 'Indústria'): 4531,
#  ('2023-08-01', 1, 'Serviços'): 8051,
#  ('2023-09-01', -1, 'Agropecuária'): 262,
#  ('2023-09-01', -1, 'Comércio'): 3358,
#  ('2023-09-01', -1, 'Construção'): 2635,
#  ('2023-09-01', -1, 'Indústria'): 1504,
#  ('2023-09-01', -1, 'Não Identificado'): 2,
#  ('2023-09-01', -1, 'Serviços'): 5812,
#  ('2023-09-01', 1, 'Agropecuária'): 844,
#  ('2023-09-01', 1, 'Comércio'): 4301,
#  ('2023-09-01', 1, 'Construção'): 3042,
#  ('2023-09-01', 1, 'Indústria'): 1997,
#  ('2023-09-01', 1, 'Serviços'): 7582,
#  ('2023-10-01', -1, 'Agropecuária'): 249,
#  ('2023-10-01', -1, 'Comércio'): 3582,
#  ('2023-10-01', -1, 'Construção'): 2356,
#  ('2023-10-01', -1, 'Indústria'): 1526,
#  ('2023-10-01', -1, 'Serviços'): 5315,
#  ('2023-10-01', 1, 'Agropecuária'): 501,
#  ('2023-10-01', 1, 'Comércio'): 4617,
#  ('2023-10-01', 1, 'Construção'): 3302,
#  ('2023-10-01', 1, 'Indústria'): 1867,
#  ('2023-10-01', 1, 'Serviços'): 6514,
#  ('2023-11-01', -1, 'Agropecuária'): 263,
#  ('2023-11-01', -1, 'Comércio'): 3365,
#  ('2023-11-01', -1, 'Construção'): 2632,
#  ('2023-11-01', -1, 'Indústria'): 1453,
#  ('2023-11-01', -1, 'Serviços'): 5107,
#  ('2023-11-01', 1, 'Agropecuária'): 207,
#  ('2023-11-01', 1, 'Comércio'): 4591,
#  ('2023-11-01', 1, 'Construção'): 3021,
#  ('2023-11-01', 1, 'Indústria'): 1582,
#  ('2023-11-01', 1, 'Serviços'): 7076,
#  ('2023-12-01', -1, 'Agropecuária'): 319,
#  ('2023-12-01', -1, 'Comércio'): 3368,
#  ('2023-12-01', -1, 'Construção'): 1773,
#  ('2023-12-01', -1, 'Indústria'): 1690,
#  ('2023-12-01', -1, 'Serviços'): 6308,
#  ('2023-12-01', 1, 'Agropecuária'): 162,
#  ('2023-12-01', 1, 'Comércio'): 3723,
#  ('2023-12-01', 1, 'Construção'): 1835,
#  ('2023-12-01', 1, 'Indústria'): 1120,
#  ('2023-12-01', 1, 'Serviços'): 5114,
#  ('2024-01-01', -1, 'Agropecuária'): 649,
#  ('2024-01-01', -1, 'Comércio'): 4657,
#  ('2024-01-01', -1, 'Construção'): 2588,
#  ('2024-01-01', -1, 'Indústria'): 2017,
#  ('2024-01-01', -1, 'Serviços'): 6996,
#  ('2024-01-01', 1, 'Agropecuária'): 339,
#  ('2024-01-01', 1, 'Comércio'): 4001,
#  ('2024-01-01', 1, 'Construção'): 3574,
#  ('2024-01-01', 1, 'Indústria'): 1698,
#  ('2024-01-01', 1, 'Serviços'): 7627,
#  ('2024-02-01', -1, 'Agropecuária'): 1123,
#  ('2024-02-01', -1, 'Comércio'): 4271,
#  ('2024-02-01', -1, 'Construção'): 3009,
#  ('2024-02-01', -1, 'Indústria'): 3209,
#  ('2024-02-01', -1, 'Serviços'): 6264,
#  ('2024-02-01', 1, 'Agropecuária'): 231,
#  ('2024-02-01', 1, 'Comércio'): 4160,
#  ('2024-02-01', 1, 'Construção'): 3662,
#  ('2024-02-01', 1, 'Indústria'): 1911,
#  ('2024-02-01', 1, 'Serviços'): 7903,
#  ('2024-03-01', -1, 'Agropecuária'): 2443,
#  ('2024-03-01', -1, 'Comércio'): 4182,
#  ('2024-03-01', -1, 'Construção'): 2901,
#  ('2024-03-01', -1, 'Indústria'): 2530,
#  ('2024-03-01', -1, 'Serviços'): 6567,
#  ('2024-03-01', 1, 'Agropecuária'): 207,
#  ('2024-03-01', 1, 'Comércio'): 5006,
#  ('2024-03-01', 1, 'Construção'): 3546,
#  ('2024-03-01', 1, 'Indústria'): 2002,
#  ('2024-03-01', 1, 'Serviços'): 8125,
#  ('2024-04-01', -1, 'Agropecuária'): 565,
#  ('2024-04-01', -1, 'Comércio'): 4508,
#  ('2024-04-01', -1, 'Construção'): 3074,
#  ('2024-04-01', -1, 'Indústria'): 3717,
#  ('2024-04-01', -1, 'Serviços'): 6327,
#  ('2024-04-01', 1, 'Agropecuária'): 358,
#  ('2024-04-01', 1, 'Comércio'): 4905,
#  ('2024-04-01', 1, 'Construção'): 3630,
#  ('2024-04-01', 1, 'Indústria'): 2417,
#  ('2024-04-01', 1, 'Não Identificado'): 1,
#  ('2024-04-01', 1, 'Serviços'): 7619
# }

# data = pd.read_csv("data/caged_agregado.csv", index_col=0)
# # data["competênciamov"] = pd.to_datetime(data["competênciamov"])
# data["Grupo"] = data["seção"].apply(lambda x: big_group[x] if x in big_group else np.nan)

# cities = data["município"].apply(lambda x: x.split("Pb-")[1]).unique()


# def get_adm_layoffs_series(df: pd.DataFrame = data, group: str = None) -> pd.DataFrame:
#     if group is not None:
#         g = df[df["Grupo"] == group].groupby(["competênciamov", "saldomovimentação"], as_index=False).sum()
#     else:
#         g = df.groupby(["competênciamov", "saldomovimentação"], as_index=False).sum()

#     g["admissao"] = g["saldomovimentação"] * g["graudeinstrução"]
#     g["demissao"] = g["saldomovimentação"] * g["graudeinstrução"] * -1

#     for col in ["admissao", "demissao"]:
#         g[col] = g[col].apply(lambda x: x if x > 0 else np.nan)

#     g["admissao"].fillna(method="bfill", inplace=True)
#     g["demissao"].fillna(method="ffill", inplace=True)

#     g = g[["competênciamov", "demissao", "admissao"]].drop_duplicates(keep="first").reset_index(drop=True)
#     g = g.astype({"demissao": int, "admissao": int})

#     return g


# def get_net_series(df: pd.DataFrame = data, group: str = None) -> pd.DataFrame:
#     if group is not None:
#         g2 = df[df["Grupo"] == group].astype({"competênciamov": str}).groupby(["competênciamov",
#                                                          "saldomovimentação"], as_index=False).sum()
#     else:
#         g2 = df.astype({"competênciamov": str}).groupby(["competênciamov",
#                                                          "saldomovimentação"], as_index=False).sum()

#     g2["graudeinstrução"] = g2["graudeinstrução"] * g2["saldomovimentação"]

#     return g2.groupby("competênciamov").sum()["graudeinstrução"]


# adm_layoffs_series = get_adm_layoffs_series(data)
# net_series = get_net_series(data)

# net_dict = net_series.to_dict()


# # sectors_stats = data[data["competênciamov"] == "2024-02-01"].groupby([
# #                         "saldomovimentação", "Grupo"
# #                     ], as_index=True).sum().to_dict()["graudeinstrução"]

# # sectors_stats = data.groupby([
# #     "competênciamov", "saldomovimentação","Grupo"]).sum().to_dict()["graudeinstrução"]