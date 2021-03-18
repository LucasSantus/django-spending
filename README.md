## Controle de Gastos

![Languages](https://img.shields.io/github/languages/count/LucasSantus/Annotations)

--------------------------------------------------------------------------------------

### Sobre o Projeto

A ideia é:

_"Criar uma aplicação minimalista de anotações onde a mesma tenha um design simples e belo, com intuito de armazenar informações&dados que o próprio usuário deseja inserir."_

Este repositório tem foco, na criação de uma aplicação de anotações utilizando o padrão CRUD(Create, Read, Update, Delete), interligado a um banco de dados que seja armazenado no próprio dispositivo móvel do usuário.

--------------------------------------------------------------------------------------

### Instalando o Projeto

**Clonando o Repositório**

Dentro da pasta onde o projeto irá ficar armazenado, abra o terminal PowerShell (opcional, qualquer terminal funcionará), {Shift + Botão Direito Mouse}

```
$ git init

$ git clone https://github.com/LucasSantus/Annotations.git
```

**Inserindo o Dart**

Com o Android Studio aberto, abra o projeto "annotations". Vá em (File > Settings > Languages&Frameworks > Dart) do IDE, selecionando (Enable Dart support fot the project 'annotations'), clique em ... para inserir o local onde o Dart está armazenado, redirecione-se para a pasta onde o flutter foi instalado, a pasta do Dart está localizada juntamente do flutter.

Exemplo: D:\ProgramFiles\AndroidStudio\flutter\bin\cache\dart-sdk

**Selecionando o Android**

Com o Android Studio aberto, abra o projeto "Annotations". Abra o Project Structure(Control+Alt+Shift+S), selecionando (No SDK) irá abrir uma caixa de seleção, selecione a versão de android instalada em sua máquina. 

**Instalando Dependências**

Com o projeto aberto, abra o arquivo pubspec.yaml e selecione "Pub get".