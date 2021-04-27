## Controle de Gastos

Se você quiser dar uma olhada em todas as telas do aplicativo, elas estão [aqui] (link). Imagens Indisponiveis!

--------------------------------------------------------------------------------------

### Sobre o Projeto

A ideia é:

_"Criar uma aplicação de Controle de Gastos onde a mesma tenha um design simples e belo, com intuito de promover o aprendizado utilizando o framework Django"_

Este repositório tem foco, na criação de uma aplicação de Controle de Gastos, interligado a um banco de dados provido pelo próprio Django Framework facilitando dessa forma a manipulação de dados.

--------------------------------------------------------------------------------------

### Por Que?

Este projeto faz parte do meu portfólio pessoal, então, ficarei feliz caso você fornecer algum feedback, código, estrutura, funcionalidade ou qualquer coisa que você possa relatar para melhora-lo.

Você pode usar este projeto como quiser, seja para estudar, fazer melhorias, você que manda!

Este é um projeto totalmente grátis!

--------------------------------------------------------------------------------------

### Instalando o Projeto

**Clonando o Repositório**

Dentro da pasta onde o projeto irá ficar armazenado, abra o terminal PowerShell (opcional, qualquer terminal funcionará), {Shift + Botão Direito Mouse}

```
$ git init

$ git clone git@github.com:LucasSantus/controle-gastos.git

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

--------------------------------------------------------------------------------------

### Autor(es)
 
- **Lucas Santos:** [GitHub](https://github.com/LucasSantus)

Siga-me no github!

Obrigado por me visitar e boa codificação!

--------------------------------------------------------------------------------------

### License

Este projeto está licenciado sob a Licença MIT License - veja o [LICENSE.md](https://github.com/LucasSantus/controle-gastos/blob/master/LICENSE) para melhores detalhes.

Tutorial Install Mysql:

> Para instalar o MySQL, atualize o APT:

sudo apt update

> Instalar os cabeçalhos e bibliotecas de desenvolvimento Python e MySQL necessários:

sudo apt install mysql-server python3-dev libmysqlclient-dev default-libmysqlclient-dev

> Execute o script de segurança:

sudo mysql_secure_installation

sudo mysql

SELECT user,authentication_string,plugin,host FROM mysql.user;

caso tenha um user root já cadastrado!

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Password!123';

SELECT user,authentication_string,plugin,host FROM mysql.user;

sudo mysql -u root

CREATE USER 'admin'@'localhost' IDENTIFIED BY 'Admin!@123';

GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost' WITH GRANT OPTION;

CREATE DATABASE AACC;

systemctl status mysql.service
