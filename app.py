import xml.etree.ElementTree as Xet
import pandas as pd
import os

path='data'

cols = ['ANO_CONCESSAO_BOLSA','CODIGO_EMEC_IES_BOLSA','NOME_IES_BOLSA','TIPO_BOLSA','MODALIDADE_ENSINO_BOLSA','NOME_CURSO_BOLSA','NOME_TURNO_CURSO_BOLSA','CPF_BENEFICIARIO_BOLSA','SEXO_BENEFICIARIO_BOLSA','RACA_BENEFICIARIO_BOLSA','DT_NASCIMENTO_BENEFICIARIO','BENEFICIARIO_DEFICIENTE_FISICO','REGIAO_BENEFICIARIO_BOLSA','SIGLA_UF_BENEFICIARIO_BOLSA','MUNICIPIO_BENEFICIARIO_BOLSA']
rows = []

for file in os.listdir(path):
    if file[-3:] == 'csv':
        with open(f"{path}/{file}", encoding="utf8", errors='ignore') as fr:
            lines = fr.readlines()
            with open("data.csv","a", encoding="utf8") as fw:
                fw.writelines(lines)


    # if file[-3:] == 'xml':
    #     xmlparse = Xet.parse(f'{path}/{file}')
    #     root = xmlparse.getroot()
    #     for i in root:
    #         ano_concessao_bolsa = i.find("ano_concessao_bolsa").text
    #         codigo_emec_ies_bolsa = i.find("codigo_emec_ies_bolsa").text
    #         nome_ies_bolsa = i.find("nome_ies_bolsa").text
    #         tipo_bolsa = i.find("tipo_bolsa").text
    #         modalidade_ensino_bolsa = i.find("modalidade_ensino_bolsa").text
    #         nome_curso_bolsa = i.find("nome_curso_bolsa").text
    #         nome_turno_curso_bolsa = i.find("nome_turno_curso_bolsa").text
    #         cpf_beneficiario_bolsa = i.find("cpf_beneficiario_bolsa").text
    #         sexo_beneficiario_bolsa = i.find("sexo_beneficiario_bolsa").text
    #         raca_beneficiario_bolsa = i.find("raca_beneficiario_bolsa").text
    #         dt_nascimento_beneficiario = i.find("dt_nascimento_beneficiario").text
    #         beneficiario_deficiente_fisico = i.find("beneficiario_deficiente_fisico").text
    #         regiao_beneficiario_bolsa = i.find("regiao_beneficiario_bolsa").text
    #         sigla_uf_beneficiario_bolsa = i.find("sigla_uf_beneficiario_bolsa").text
    #         municipio_beneficiario_bolsa = i.find("municipio_beneficiario_bolsa").text

    #         rows.append(
    #             {
    #                 'ano_concessao_bolsa': ano_concessao_bolsa,
    #                 'codigo_emec_ies_bolsa': codigo_emec_ies_bolsa,
    #                 'nome_ies_bolsa': nome_ies_bolsa,
    #                 'tipo_bolsa': tipo_bolsa,
    #                 'modalidade_ensino_bolsa': modalidade_ensino_bolsa,
    #                 'nome_curso_bolsa': nome_curso_bolsa,
    #                 'nome_turno_curso_bolsa': nome_turno_curso_bolsa,
    #                 'cpf_beneficiario_bolsa': cpf_beneficiario_bolsa,
    #                 'sexo_beneficiario_bolsa': sexo_beneficiario_bolsa,
    #                 'raca_beneficiario_bolsa': raca_beneficiario_bolsa,
    #                 'dt_nascimento_beneficiario': dt_nascimento_beneficiario,
    #                 'beneficiario_deficiente_fisico': beneficiario_deficiente_fisico,
    #                 'regiao_beneficiario_bolsa': regiao_beneficiario_bolsa,
    #                 'sigla_uf_beneficiario_bolsa': sigla_uf_beneficiario_bolsa,
    #                 'municipio_beneficiario_bolsa': municipio_beneficiario_bolsa,
    #             }
    #         )
    #     df = pd.DataFrame(rows, columns=cols)

    #     df.to_csv(file[:-3]+"csv")