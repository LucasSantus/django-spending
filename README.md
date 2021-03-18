## Controle de Gastos

*** repositório focado em estudos ***

**Clonando o Repositório**

Dentro da pasta onde o projeto irá ficar armazenado, abra o terminal PowerShell (opcional, qualquer terminal funcionará), {Shift + Botão Direito Mouse}

```
$ git init

$ git clone https://github.com/LucasSantus/controle-gastos.git
```

** Preparando Ambiente Virtual **

Com o terminal aberto, digite:

```
$ python3 -m venv myvenv

$ source myvenv/bin/activate

$ python -m pip install --upgrade pip

$ pip install -r requirements.txt
```

** Preparando o Projeto **

```
$ python manage.py migrate

$ python manage.py createsuperuser
```

** Rodando o Projeto **

```
$ python manage.ppy runserver
```

para visualizar o projeto: http://127.0.0.1:8000/
