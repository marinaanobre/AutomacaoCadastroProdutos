Automação de Cadastro de Produtos

Projeto desenvolvido durante estudos de automação com Python.

Este projeto é uma ferramenta de automação desenvolvida em Python para facilitar o cadastro em massa de produtos em um sistema. Utilizando scripts de automação de interface, o sistema lê uma base de dados externa e preenche os campos automaticamente.

Tecnologias utilizadas:

- Python: Linguagem principal
- PyAutoGUI: Para controlar o mouse e o teclado e interagir com o navegador
- Pandas: Para a manipulação e leitura da base de dados produtos.csv
- Time: Para os intervalos de carregamento entre as páginas

Como executar o projeto?

1. Instale as bibliotecas necessárias:
pip install pyautogui pandas

2. Certifique-se de que o arquivo "produtos.csv" está na mesma pasta do script.

3. Execute o script principal:
python codigo.py

Observação: o projeto utiliza automação de interface com PyAutoGUI. Pode ser necessário ajustar as coordenadas do mouse de acordo com a resolução da sua tela.
