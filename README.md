<h1>Estruturação do código</h1>
<h1> Servidor</h1>

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

<h1>Cliente</h1>

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

<h1>Code structure</h1>
<h1>Server</h1>

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

<h1>Client</h1>

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
