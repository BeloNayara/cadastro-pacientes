import os
from datetime import datetime

import gradio as gr
import pandas as pd

ARQUIVO_CSV = "pacientes.csv"
COLUNAS = ["timestamp", "nome", "idade", "convenio", "prioridade", "motivo"]
CONVENIOS = ["Particular", "Unimed", "Bradesco Saúde", "SulAmérica", "Outro"]


def ler_csv():
    # se ainda nao tem arquivo, mostra a tabela vazia
    if os.path.exists(ARQUIVO_CSV):
        return pd.read_csv(ARQUIVO_CSV)
    return pd.DataFrame(columns=COLUNAS)


def cadastrar_paciente(nome, idade, convenio, prioridade, motivo):
    if not nome or nome.strip() == "":
        return "Preencha o nome do paciente.", ler_csv().tail(5)
    if idade is None:
        return "Preencha a idade.", ler_csv().tail(5)
    if not convenio:
        return "Escolha o convênio.", ler_csv().tail(5)

    linha = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "nome": nome.strip(),
        "idade": int(idade),
        "convenio": convenio,
        "prioridade": int(prioridade),
        "motivo": motivo.strip(),
    }
    novo = pd.DataFrame([linha], columns=COLUNAS)

    # primeira vez cria o arquivo com cabecalho, depois so acrescenta linhas
    if os.path.exists(ARQUIVO_CSV):
        novo.to_csv(ARQUIVO_CSV, mode="a", header=False, index=False)
    else:
        novo.to_csv(ARQUIVO_CSV, mode="w", header=True, index=False)

    return f"Paciente {linha['nome']} cadastrado com sucesso!", ler_csv().tail(5)


with gr.Blocks(title="Cadastro de Pacientes") as demo:
    gr.Markdown("## Cadastro de Pacientes")
    gr.Markdown("Recepção do consultório")

    # tudo em uma coluna so, pra ficar bom no celular
    nome = gr.Textbox(label="Nome do paciente")
    idade = gr.Number(label="Idade", minimum=0, maximum=120, precision=0)
    convenio = gr.Dropdown(CONVENIOS, label="Convênio")
    prioridade = gr.Slider(1, 5, step=1, value=1,
                           label="Prioridade do atendimento (5 = urgente)")
    motivo = gr.Textbox(label="Motivo da consulta / observações", lines=3)

    botao = gr.Button("Cadastrar", variant="primary")

    saida_msg = gr.Textbox(label="Status", interactive=False)
    tabela = gr.Dataframe(value=ler_csv().tail(5),
                          label="Últimos pacientes cadastrados")

    botao.click(
        cadastrar_paciente,
        [nome, idade, convenio, prioridade, motivo],
        [saida_msg, tabela],
    )

if __name__ == "__main__":
    demo.launch()
