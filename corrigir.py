import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")


def corrigir_codigo(codigo_usuario, descricao_exercicio):
    try:
        prompt = f"""
        O seguinte código foi escrito por um aluno como solução para o exercício: "{descricao_exercicio}"
        Avalie o código, corrija erros, sugira melhorias e forneça um feedback detalhado.

        Código do aluno:
        ```python
        {codigo_usuario}
        ```

        Informe:
        1. Se o código está correto.
        2. Quais erros foram encontrados.
        3. Versão corrigida do código, se necessário.
        """

        # Chamada para a API do ChatGPT
        response = model.generate_content(prompt)

        # Extrai e retorna a resposta
        return response.text

    except FileNotFoundError:
        return "Erro: O arquivo especificado não foi encontrado."
    except Exception as e:
        return f"Ocorreu um erro: {str(e)}"


def processar_pasta(caminho_pasta, descricao_exercicio, arquivo_saida):
    # Abre o arquivo de saída em modo de escrita
    with open(arquivo_saida, 'w', encoding='utf-8') as arquivo_resultado:
        # Percorre todos os arquivos .py na pasta especificada
        for nome_arquivo in os.listdir(caminho_pasta):
            if nome_arquivo.endswith('.py'):
                caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)

                with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo_codigo:
                    codigo_usuario = arquivo_codigo.read()

                # Corrige o código utilizando a função corrigir_codigo
                feedback = corrigir_codigo(codigo_usuario, descricao_exercicio)

                # Escreve o feedback no arquivo de saída
                arquivo_resultado.write(f"### Feedback para {
                                        nome_arquivo} ###\n")
                arquivo_resultado.write(feedback + "\n\n")
                arquivo_resultado.write("="*80 + "\n\n")


if __name__ == "__main__":
    caminho_da_pasta = 'tarefas/'  # Substitua pelo caminho correto da sua pasta

    with open('enunciado.txt', 'r', encoding='utf-8') as file:
        descricao_exercicio = file.read()

    arquivo_saida = 'resultado_correcao.txt'

    processar_pasta(caminho_da_pasta, descricao_exercicio, arquivo_saida)
    print(f"Correções concluídas! Confira o arquivo {arquivo_saida}")
