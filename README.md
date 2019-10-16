# genericDatabase
Conjunto genérico para conexão com Bancos de dados relacionais

# utilities
Nesta pasta estão presentes auxiliares para leitura de arquivo de configuração para conexão com banco de Dados.

## contants
Contempla constantes e enums utilizados pela aplicação.

## exception
Contempla alguns tratamentos simples de exceção. Ainda há muito o que melhorar nesta parte.

## GenConfigFile
Contempla rotinas para leitura de arquivo de configuração, bem como para a criação de um genérico. A extenção dos arquivos que podem ser
lidos ou criados e a '.ini'

## DatabaseClass
Contempla a classe genérica para conexão a banco de dados relacional, que se apoia em alguns métodos dos arquivos acima. As informações
para conexão junto a um banco desejado devem ser realizadas via arquivo de configuração.

# domain
Possui duas classes exemplo, as quais representam tabelas no banco de dados. Nelas não é necessário o espelhamento manual de cada coluna
das tabelas em questão, devido à forma de conexão atualmente realizada pela classe DatabaseClass, que tem espelhamento automático da
estrutura existente no banco a ser acessado.

# dependencies
Atualmente possui um único arquivo de dependência para o funcionamento específico da ORM utilizada neste projeto.

# config
Onde ficam os arquivos de configuração. Existe um de exemplo.

# searches
Possui o arquivo da classe genérica, e um exemplo de implementação de pesquisa por tabela

# Example.py
Exemplo de main cliente que utiliza as classes implementadas. Para a inicialização correta, por perfil de desenvolvedor,
basta passar como parêmetro de execução a chave do perfil. Um exemplo de comando seria:

                                python Example.py dev
## Perfis de usuário
No arquivo de constants.py, existe um enum que recebe "key = 'archive.ini'". Para adicionar um novo perfil, basta criar
um arquivo '.ini' e direcioná-lo neste enum. De forma genérica, a execução da aplicação se dá por:

                                python Example.py key

