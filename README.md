# Cadastro de Pacientes - Gradio x Streamlit

Atividade da Aula 1 (prof. Francisco Fambrini).

O mesmo formulário de cadastro de pacientes feito duas vezes: uma com Gradio (roda no computador) e outra com Streamlit (publicada no Streamlit Community Cloud).

Campos: nome, idade, convênio, prioridade (1 a 5) e motivo da consulta. Cada cadastro gera uma linha no `pacientes.csv` com data e hora.

## Pastas

- `gradio_app/` - versão Gradio, grava no `pacientes.csv` local
- `streamlit_app/` - versão Streamlit, com botão para baixar o CSV
- `pacientes.csv` - exemplo gerado nos testes
- `print_gradio_local.png` - print da versão Gradio rodando

## Como rodar

```
pip install -r gradio_app/requirements.txt

cd gradio_app
python app.py
# abre em http://127.0.0.1:7860

cd streamlit_app
streamlit run app.py
```

## Link do app no Streamlit

COLE_AQUI_O_LINK.streamlit.app

## Comparação rápida

- Gradio foi mais rápido de montar e já salva direto no arquivo local. Bom para testar na própria máquina.
- Streamlit tem o `st.form`, que só envia quando clica no botão, e publicar na nuvem é bem simples pelo GitHub.
- No Streamlit Cloud o arquivo salvo no servidor some quando o app reinicia, por isso o botão de download do CSV é necessário.
