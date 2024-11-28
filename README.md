#Sistema de correção automática de atividades de alunos.

##Utilização
1. Clonar o repositório
2. Criar a chave de API (https://aistudio.google.com/u/2/apikey)
3. Copiar o arquivo env-sample para a raiz do projeto
4. Renomear o arquivo env-sample para .env
5. Colar a sua chave de API para o arquivo .env substituindo a frase: adicionar a sua chave de API do google
6. Criar uma pasta tarefas onde serão colocadas as atividades dos alunos, um arquivo para cada estudante, o nome do arquivo deve ser o nome do estudante (não é obrigatório mas fica mais fácil encontrar de quem é a correção ao final da execução)
7. Criar um documento enunciado.txt onde deverá ser colada a instrução da tarefa que foi passada ao aluno.
8. Rodar o programa

```console
git clone https://github.com/clebersfonseca/coretorAtividades.git
mv contrib/env-sample .env
mkdir tarefas
touch enunciado.txt
python corrigir.py
```