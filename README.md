# Sistema de correção automática de atividades de alunos.

O sistema de correção automatizada de exercícios de programação é uma solução robusta e eficiente, projetada para auxiliar educadores e instituições no processo de avaliação de códigos desenvolvidos por alunos. Focado na linguagem Python, o sistema oferece uma abordagem automatizada que analisa e corrige múltiplos arquivos de código armazenados em uma pasta, utilizando a inteligência artificial do Google Gemini (modelo 1.5 Flash). O feedback gerado é completo e detalhado, fornecendo insights valiosos sobre erros encontrados, sugestões de melhorias, e práticas recomendadas.

A principal característica do sistema é a capacidade de processar todos os arquivos Python de uma pasta específica, corrigindo cada um de forma individual. Cada código é submetido à API do Gemini, onde é avaliado com base em critérios predefinidos, como correção lógica, clareza e eficiência. O sistema então salva o feedback detalhado em um arquivo .txt, organizado de forma estruturada, permitindo que educadores revisem as análises com facilidade.

Além disso, o sistema adota práticas seguras, como o uso de variáveis de ambiente armazenadas em um arquivo .env para proteger a chave de acesso à API. Isso garante a confidencialidade das credenciais e facilita a configuração em diferentes ambientes.

Este sistema automatizado economiza tempo, aumenta a consistência nas correções e proporciona feedback personalizado para cada aluno, incentivando o aprendizado contínuo. É ideal para cursos de programação, bootcamps e plataformas de ensino online, onde a avaliação manual pode ser demorada e inconsistente. Ao integrar a inteligência artificial com um processo de correção automatizada, o sistema eleva o padrão de ensino de programação, promovendo uma experiência educacional mais eficiente e enriquecedora.

## Utilização
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