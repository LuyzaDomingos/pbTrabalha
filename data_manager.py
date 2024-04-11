import pandas as pd
import numpy as np

big_group = {
    'Administração Pública, Defesa e Seguridade Social': 'Serviços',
    'Agricultura, Pecuária, Produção Florestal, Pesca e AqÜIcultura': 'Agropecuária',
    'Alojamento e Alimentação': 'Serviços',
    'Artes, Cultura, Esporte e Recreação': 'Serviços',
    'Atividades Administrativas e Serviços Complementares': 'Serviços',
    'Atividades Financeiras, de Seguros e Serviços Relacionados': 'Serviços',
    'Atividades Imobiliárias': 'Serviços',
    'Atividades Profissionais, Científicas e Técnicas': 'Serviços',
    'Comércio, Reparação de Veículos Automotores e Motocicletas': 'Comércio',
    'Construção': 'Construção',
    'Educação': 'Serviços',
    'Eletricidade e Gás': 'Indústria',
    'Indústrias Extrativas': 'Indústria',
    'Indústrias de Transformação': 'Indústria',
    'Informação e Comunicação': 'Serviços',
    'Não identificado': 'Não Identificado',
    'Organismos Internacionais e Outras Instituições Extraterritoriais': 'Serviços',
    'Outras Atividades de Serviços': 'Serviços',
    'Saúde Humana e Serviços Sociais': 'Serviços',
    'Serviços Domésticos': 'Serviços',
    'Transporte, Armazenagem e Correio': 'Serviços',
    'Água, Esgoto, Atividades de Gestão de Resíduos e Descontaminação': 'Indústria'
}

data = pd.read_csv("data/caged_agregado.csv", index_col=0)
data["competênciamov"] = pd.to_datetime(data["competênciamov"])
data["Grupo"] = data["seção"].apply(lambda x: big_group[x] if x in big_group else np.nan)

cities = data["município"].apply(lambda x: x.split("Pb-")[1]).unique()


def get_adm_layoffs_series(df):
    g = df.groupby(["competênciamov", "saldomovimentação"], as_index=False).sum()
    g["admissao"] = g["saldomovimentação"] * g["graudeinstrução"]
    g["demissao"] = g["saldomovimentação"] * g["graudeinstrução"] * -1

    for col in ["admissao", "demissao"]:
        g[col] = g[col].apply(lambda x: x if x > 0 else np.nan)

    g["admissao"].fillna(method="bfill", inplace=True)
    g["demissao"].fillna(method="ffill", inplace=True)

    g = g[["competênciamov", "demissao", "admissao"]].drop_duplicates(keep="first").reset_index(drop=True)
    g = g.astype({"demissao": int, "admissao": int})

    return g


adm_layoffs = get_adm_layoffs_series(data)

g2 = data.astype({"competênciamov": str}).groupby(["competênciamov",
                                                   "saldomovimentação"], as_index=False).sum()
g2["graudeinstrução"] = g2["graudeinstrução"] * g2["saldomovimentação"]

net = g2.groupby("competênciamov").sum()["graudeinstrução"]
net_dict = net.to_dict()

sectors_stats = data[data["competênciamov"] == "2024-02-01"].groupby([
                        "saldomovimentação", "Grupo"
                    ], as_index=True).sum().to_dict()["graudeinstrução"]