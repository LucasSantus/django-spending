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
git init

git clone git@github.com:LucasSantus/controle-gastos.git

cd controle-gastos
```

> **Clonando via HTTPS:**

```
git init

git clone https://github.com/LucasSantus/controle-gastos.git

cd controle-gastos
```

**Preparando Ambiente Virtual**

Com o terminal aberto, digite:

```
python3 -m venv env

source env/bin/activate

python -m pip install --upgrade pip

pip install -r requirements.txt
```
**Instalalando o Mysql Server**

> Para instalar o MySQL, primeiramente atualize o APT:

```
sudo apt update
```

> Instalar os cabeçalhos e bibliotecas de desenvolvimento Python e MySQL necessários:

```
sudo apt install mysql-server python3-dev libmysqlclient-dev default-libmysqlclient-dev
```

> Execute o script de segurança, salve a senha escolhida:
```
sudo mysql_secure_installation
```

> Feche do Terminal de segurança do Mysql:

```
exit
```

> Abra o terminal do Mysql:

```
sudo mysql
```

> Para visualizar os usuários já criados do MySql:

```
SELECT user,authentication_string,plugin,host FROM mysql.user;
```

> Caso já tenha um usuário root cadastrado:

```
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Password!123';
```

> Visualize novamente os usuários criados:

```
SELECT user,authentication_string,plugin,host FROM mysql.user;
```

> Feche do Terminal do Mysql:

```
exit
```

> Abra novamente o terminal do Mysql com esse comando:

```
sudo mysql -u root -p
```

> Crie um novo usuário Mysql:

> Observação, admin: é o nome do usuário, troque caso prefira.
> Observação, Admin!@123: é senha do usuário, troque caso prefira.

```
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'Admin!@123';
```

> Dê previlégios ao novo usuário:

```
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost' WITH GRANT OPTION;
```

> Crie um novo banco de dados:
```
CREATE DATABASE AACC;
```

> Feche do Terminal de segurança do Mysql:

```
exit
```

> Para Visualizar se o MySql Server está ativo:

```
systemctl status mysql.service
```

**Configurando Settings do Projeto**

> Observação, 'NAME": AACC, o nome do Banco de Dados criado no MySql.
> Observação, 'USER": admin, o nome do usuário criado no MySql.
> Observação, 'PASSWORD": Admin!@123, a senha do usuário criado no MySql.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'AACC',
        'USER': 'admin',
        'PASSWORD': 'Admin!@123',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

para exportar um banco de dados mysql:
mysqldump -u [username] -p [database name] > [database name].sql
mysqldump -u admin -p AACC > AACC.sql

para importar um banco de dados:
CREATE DATABASE AACC;
mysql -u [username] -p newdatabase < [database name].sql
mysql -u admin -p newdatabase < AACC.sql

**Preparando o Projeto**

```
python manage.py makemigrations contas

python manage.py migrate

python manage.py createsuperuser
```

**Rodando o Projeto**

```
python manage.py runserver
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
python -m venv env

env\Scripts\activate

python -m pip install --upgrade pip

pip install -r requirements.txt
```

**Preparando o Projeto**

```
python manage.py makemigrations usuarios

python manage.py migrate

python manage.py createsuperuser
```

**Rodando o Projeto**

```
python manage.py runserver
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

### Autor(es)
 
- **Lucas Santos:** [GitHub](https://github.com/LucasSantus)

Siga-me no github!

Obrigado por me visitar e boa codificação!

--------------------------------------------------------------------------------------

### License

Este projeto está licenciado sob a Licença MIT License - veja o [LICENSE.md](https://github.com/LucasSantus/controle-gastos/blob/master/LICENSE) para melhores detalhes.


<h1 align="center">CRemédios</h1>

<p align="center">
	<a href="#sobre">Sobre</a> &nbsp;|&nbsp;
	<a href="#porque">Por Que</a> &nbsp;|&nbsp;
	<a href="#tecnologias">Tecnologias</a> &nbsp;|&nbsp;
	<a href="#funcionalidades">Funcionalidades</a> &nbsp;|&nbsp;
	<a href="#instalando">Instalando</a> &nbsp;|&nbsp;
	<a href="#rodando">Rodando</a> &nbsp;|&nbsp;
	<a href="#autor">Autor</a> &nbsp;|&nbsp;
	<a href="#license">Licença</a>
</p>

<h6 align="center"> 
	Se você quiser visualizar as imagens do aplicativo, clique <a href="github/images/README.md">aqui</a>.
</h6>

<h3 id="sobre">:information_source: Sobre</h3>

> Este projeto foi desenvolvido utilizando o Django como framework back-end e o Materialize como framework front-end. 

A ideia é:

_"Criar um Sistema de Remédios onde o mesmo tenha um design simples e belo, com intuito de promover o aprendizado e gerar um projeto completo utilizando o Django framework."_

--------------------------------------------------------------------------------------

<h3 id="porque">:question: Por Que</h3>

Este projeto faz parte do meu portfólio pessoal, ficarei feliz caso você forneça algum feedback, código, estrutura, funcionalidade ou qualquer funcionalidade&melhoria que você possa relatar para melhora-lo.

Você pode usar este projeto como quiser, seja para estudar, fazer melhorias, você que manda!

Este é um projeto totalmente grátis!

--------------------------------------------------------------------------------------

<h3 id="tecnologias">:rocket: Tecnologias</h3>

As seguintes ferramentas foram usadas na construção do projeto:

- [Django Framework](https://www.djangoproject.com/)
- [Materialize](https://materializecss.com/)

--------------------------------------------------------------------------------------

<h3 id="funcionalidades">:sparkles: Funcionalidades</h3>

:construction: - As Funcionalidades será construída em breve...

--------------------------------------------------------------------------------------

<h3 id="instalando">:computer: Instalando o Projeto</h3>

**Clonando o Repositório**

```
git clone git@github.com:LucasSantus/c-remedios.git

cd c-remedios
```

#### Preparando o Projeto

#### Windows

> **Observação:** Foi utilizado o Windows(versão 10), caso ocorra algum problema na instalação, pesquise por conta própria a resolução do mesmo!

**Preparando Ambiente Virtual**

```
python -m venv env

env\Scripts\activate

python -m pip install --upgrade pip

pip install -r requirements.txt
```

#### Linux

> **Observação:** Foi utilizado a distro Linux Mint(versão 20.1), caso ocorra algum problema na instalação, pesquise por conta própria a resolução do mesmo!

**Instalando Ambiente Virtual**

Caso não tenha um ambiente virtual instalado, digite no terminal:

```
sudo apt-get install python3-venv
```

**Preparando Ambiente Virtual**

Com o terminal aberto, digite no terminal:

```
python3 -m venv env

source env/bin/activate

python -m pip install --upgrade pip

pip install -r requirements.txt
```

<h3 id="rodando">:zap: Rodando</h3>

**Iniciando**

```
python manage.py makemigrations home

python manage.py makemigrations usuarios

python manage.py makemigrations receitas

python manage.py makemigrations automated_logging

python manage.py migrate

python manage.py shell

exec(open('apps/scripts/main.py').read())

exit()

python manage.py runserver
```

**Criando Super Usuário**

```
python manage.py createsuperuser
```
**Acessando o Projeto**

para visualizar o projeto: http://127.0.0.1:8000/


**Acessando o Admin**

Com o projeto rodando, adicione o 'admin/' dps da URL:

http://127.0.0.1:8000/admin/

--------------------------------------------------------------------------------------

<h3 id="autor">:bust_in_silhouette: Autor</h3>

<div align="left"> 
	<a href="https://github.com/LucasSantus">
		<img style="border-radius: 50%;" src="https://github.com/LucasSantus.png" width="100px;" alt=""/>
		<br />
		Lucas Santus
	</a>
</div>
<br />
Feito com ❤️ por Lucas Santus!<br />
Obrigado por visitar e boa codificação!<br />

--------------------------------------------------------------------------------------

<h3 id="license">:memo: License</h3>

Este projeto está licenciado sob a Licença MIT License - veja o [LICENSE.md](https://github.com/LucasSantus/c-remedios/blob/master/LICENSE) para melhores detalhes.

