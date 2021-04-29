## Controle de Gastos

Se você quiser dar uma olhada em todas as telas do aplicativo, elas estão [aqui] (link). Imagens Indisponiveis!

--------------------------------------------------------------------------------------

### Sobre o Projeto

A ideia é:

_"Criar uma aplicação de Controle de Gastos onde a mesma tenha um design simples e belo, com intuito de promover o aprendizado utilizando o framework Django"_

Este repositório tem foco, na criação de uma aplicação de Controle de Gastos, interligado a um banco de dados provido pelo próprio Django Framework facilitando dessa forma a manipulação de dados.

--------------------------------------------------------------------------------------

### Por Que?

Este projeto faz parte do meu portfólio pessoal, então, ficarei feliz caso você forneça algum feedback, código, estrutura, funcionalidade ou qualquer funcionalidade/melhoria que você possa relatar para melhora-lo.

Você pode usar este projeto como quiser, seja para estudar, fazer melhorias, você que manda!

Este é um projeto totalmente grátis!

--------------------------------------------------------------------------------------

### Instalando o Projeto

#### Linux

> **Observação:** Foi utilizado a distro Linux Mint(versão 20.1), caso ocorra algum problema na instalação, pesquise por conta própria a resolução do mesmo!

**Clonando o Repositório**

> **Observação:** Caso não tenha configurado chave SSH, clone o projeto via HTTPS:

Dentro da pasta onde o projeto ficará armazenado, abra o terminal.

> **Clonando via SSH:** 

```
$ git init

$ git clone git@github.com:LucasSantus/controle-gastos.git

$ cd controle-gastos
```

> **Clonando via HTTPS:**

```
$ git init

$ git clone https://github.com/LucasSantus/controle-gastos.git

$ cd controle-gastos
```

**Preparando Ambiente Virtual**

Com o terminal aberto, digite:

```
$ python3 -m venv env

$ source env/bin/activate

$ python -m pip install --upgrade pip

$ pip install -r requirements.txt
```

**Preparando o Projeto**

```
$ python manage.py makemigrations contas

$ python manage.py migrate

$ python manage.py createsuperuser
```

**Rodando o Projeto**

```
$ python manage.py runserver
```

**Visualizando o Projeto**
```
http://127.0.0.1:8000/
```

**Acessando o Admin**

Com o projeto rodando, adicione o 'admin/' dps da URL:
```
http://127.0.0.1:8000/admin/
```

#### Windows

> **Observação:** Foi utilizado o Windows(versão 10), caso ocorra algum problema na instalação, pesquise por conta própria a resolução do mesmo!

**Preparando Ambiente Virtual**

```
$ python -m venv env

$ env\Scripts\activate

$ python -m pip install --upgrade pip

$ pip install -r requirements.txt
```

**Preparando o Projeto**

```
$ python manage.py makemigrations usuarios

$ python manage.py migrate

$ python manage.py createsuperuser
```

**Rodando o Projeto**

```
$ python manage.py runserver
```

**Acessando o Projeto**

Visualize o projeto no navegador: 

```
http://127.0.0.1:8000/
```

**Acessando o Admin**

Adicione 'admin/' há URL:

```
http://127.0.0.1:8000/admin/
```

--------------------------------------------------------------------------------------

### Instalalando o Mysql Server:

> Para instalar o MySQL, primeiramente atualize o APT:

```
$ sudo apt update
```

> Instalar os cabeçalhos e bibliotecas de desenvolvimento Python e MySQL necessários:

```
$ sudo apt install mysql-server python3-dev libmysqlclient-dev default-libmysqlclient-dev
```

> Execute o script de segurança, salve a senha escolhida:
```
$ sudo mysql_secure_installation
```

> feche do Terminal de segurança do Mysql:

```
$ exit
```

> Abra o terminal do Mysql:

```
$ sudo mysql
```

> Para visualizar os usuários já criados do MySql:

```
$ SELECT user,authentication_string,plugin,host FROM mysql.user;
```

> Caso já tenha um usuário root cadastrado:

```
$ ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Password!123';
```

> Visualie novamente os usuários criados:

```
$ SELECT user,authentication_string,plugin,host FROM mysql.user;
```

> feche do Terminal do Mysql:

```
$ exit
```

> Abra novamente o terminal do Mysql com esse comando:

```
$ sudo mysql -u root
```

> Crie um novo usuário Mysql:

> Observações, : 

```
$ CREATE USER 'admin'@'localhost' IDENTIFIED BY 'Admin!@123';
```


GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost' WITH GRANT OPTION;

CREATE DATABASE AACC;

systemctl status mysql.service

--------------------------------------------------------------------------------------

### Autor(es)
 
- **Lucas Santos:** [GitHub](https://github.com/LucasSantus)

Siga-me no github!

Obrigado por me visitar e boa codificação!

--------------------------------------------------------------------------------------

### License

Este projeto está licenciado sob a Licença MIT License - veja o [LICENSE.md](https://github.com/LucasSantus/controle-gastos/blob/master/LICENSE) para melhores detalhes.
