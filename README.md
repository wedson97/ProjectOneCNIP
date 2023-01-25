<h1>Projeto 1 - Protocolo de Interconexão de Redes de Computadores</h1>

<h2>Descrição</h2>

> Projeto desenvolvido como atividade referente a matéria Protocolo de Interconexão de Redes de Computadores do curso Tecnologia em Sistemas para internet - IFPB Guarabira.
> O projeto consiste em uma aplicação cliente-servidor utilizando a API de Sockets do Python. 
> A aplicação é capaz de responder mais de um cliente ao mesmo tempo, e atende à requisições dos mesmos por meio de "palavras-chaves" digitadas no terminal.

<h3>Pré - Requisitos</h3>

> * Biblioteca Requests instalado
> * Digite `pip install requests` no terminal para instalar

<h3>Aplicação</h3>

> Protocolo de transporte de dados utilizada:
>
> * IPv4
> * TCP
>
> Funcionalidades do servidor:
>
> * Cotação atual do Bitcoin
> * Cotação atual do Dolar
> * Cotação atual do Euro
> * Localizar endereço através do CEP
> * Desconectar e/ou Finalizar Servidor
>
> APIs:
>
> * https://docs.awesomeapi.com.br/api-de-moedas
> * https://docs.awesomeapi.com.br/api-cep
>
> Bibliotecas:
>
> * Socket
> * Threading
> * Requests
> * Json

<h3>Execução</h3>

> A execução da aplicação é feita completamente no terminal.
> No terminal e no diretório da aplicação, o usuário deverá executar o arquivo `servidor.py` para ativar o servidor e tornar possível as conexões.
> Com o servidor ativo, o usuário executa em outra aba do terminal o arquivo `cliente.py` para iniciar uma conexão ao servidor *(Repita esse processo para ativar mais conexões)*.
> Feito isso, o cliente-servidor poderá trocar mensagens, o cliente informa as palavras-chave e o servidor responderá à requisição disponível.
>
> Palavras-chaves atualmente disponíveis:
> * bitcoin
> * cep
> * dolar
> * euro
> * fechar
> * sair

<h2>Estruturação do código</h2>

<h3> Servidor</h3>

> * Ele começa importando algumas bibliotecas como "socket", "threading", "requests" e "json".
> 
> * Em seguida, é definido o host e a porta por onde as comunicações serão realizadas.
> 
> * É definida a função handle_client, nela estão estruturadas todas as funcionalidades do servidor, como por exemplo mostrar se o cliente está ou não conectado, fazer > uso da API
> para ver a cotação do dólar, euro, bitcoin e consultar o CEP. Englobando todas essas funcionalidades, há um tratamento de erro (try/except), e um tratamento de erro 
> exclusivo na consulta de CEP, com a finalidade de evitar possíveis erros que possam surgir.
> 
> * Depois que a função de funcionalidade do servidor foi definida, é então que é feita a parte que dar vida ao servidor, com um código curto, com apenas 15 linhas, onde 
> é chamada a função anteriormente criada.

<h3>Cliente</h3>

> * O código do cliente inicializa importando as bibliotecas "socket" e "threading".
> 
> * Da mesma forma que o servidor, em seguida vem a definição do host e da porta por onde as comunicações serão realizadas.
> 
> * É criada então a função que dará os comandos ao servidor, mostrando que a conexão foi estabelecida. Em seguida, é mostrado um menu de 
> funcionalidades onde o cliente pode escolher o que deseja fazer entre consultar o dólar, euro, bitcoin ou consultar um CEP. Dentre as funcionalidades, há também as 
> opções de fechar a tela do cliente com o comando "sair" ou fechar o servidor com o comando "fechar", mas o servidor só poderá ser fechado se apenas um cliente 
> estiver conectado.
> 
> * Englobando toda a função, também há um tratamento de erro que indicará que o cliente não está conectado.

<h2>Code structure</h2>
<h3>Server</h3>

> * It starts by importing some libraries such as "socket", "threading", "requests" and "json".
> 
> * Next, the host and port for communications are defined.
> 
> * The handle_client function is defined, which structures all the server's functionality, such as showing whether the client is connected or not, using the API to 
> check the dollar, euro, bitcoin exchange rate and check the zip code. Encompassing all these functionality, there is an error handling (try/except), and a specific 
> error handling in the zip code check, in order to avoid possible errors that may arise.
> 
> * Once the server's functionality function has been defined, the server is brought to life with a short code, with only 15 lines, where the previously created 
> function is called.

<h3>Client</h3>

> * The client code starts by importing the "socket" and "threading" libraries.
> 
> * Similarly to the server, the host and port for communications are defined next.
> 
> * Then the function that will give commands to the server is created, showing that the connection has been established. Next, a menu of functionalities is 
> shown where the client can choose what they want to do, check the dollar, euro, bitcoin exchange rate or check a zip code. Among the functionalities, there 
> are also options to close the client screen with the "exit" command or close the server with the "close" command, but the server can only be closed if only one 
> client is connected.
> 
> * Encompassing the entire function, there is also an error handling that will indicate that the client is not connected.
