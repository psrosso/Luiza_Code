# Luiza_Code
Atividades realizadas para a 5ª edição do Luiza Code, programa de formação e capacitação de mulheres na linguagem Python. 
<p align="center">
  <img src="https://d2q79iu7y748jz.cloudfront.net/s/_customcontent/33c719969dae78ef0936904a59011b1f">
</p>

## Desenvolvedora :octocat:

[<img src="https://avatars.githubusercontent.com/u/79259481?s=400&u=e9f8f346fe341894c69cde41e8e79cd952fbfcce&v=4" width=115><br><sub>Rafaela Rosso</sub>](https://github.com/beebones) 
| :---: | 

> Status do Projeto: Em andamento ████▒▒▒▒▒ 40%:

<!-- ### Tópicos 

:small_blue_diamond: [Descrição do projeto](#descrição-do-projeto-star)

:small_blue_diamond: [O que a plataforma é capaz de fazer](#o-que-a-plataforma-é-capaz-de-fazer-checkered_flag)

:small_blue_diamond: [Deploy da Aplicação com Netlify](#deploy-da-aplicação-com-netlify-dash)

:small_blue_diamond: [Pré-requesitos](#pré-requesitos)

:small_blue_diamond: [Como rodar a aplicação](#como-rodar-a-aplicação-arrow_forward)

:small_blue_diamond: [JSON](#json-floppy_disk)

:small_blue_diamond: [Páginas](#páginas)

:small_blue_diamond: [CRUD](#crud)

:small_blue_diamond: [Linguagens, dependencias e libs utilizadas ](#linguagens-dependencias-e-libs-utilizadas-books)

:small_blue_diamond: [Dependência externa](#dependência-externa-incoming_envelope)

## Descrição do projeto :star:

<p align="justify">
Desenvolver uma plataforma capaz de gerar certificados em PDF de eventos e cursos para enviá-los por e-mail aos participantes.
</p>

<p align="center">
<img src="https://user-images.githubusercontent.com/46378210/80231326-9a603980-8629-11ea-8798-eabacda99982.png"/>
</p>

## O que a plataforma é capaz de fazer :checkered_flag:

:trophy: Gerar PDF do certificado com as informações preenchidas no formulário para cada participantes para envio de e-mail 

:trophy: Check-list de participantes, permitindo selecionar quem irá receber os certificados 

:trophy: Permite que o organizador do evento escreva sua assinatura digital dentro da plataforma

:trophy: Oferece layout responsivo 

:trophy: Cadastrar organizadores 

:trophy: Cadastrar eventos 

:trophy: Cadastrar participantes para cada evento

## Deploy da Aplicação com Netlify :dash:

> https://certificates-for-everyone-womakerscode.netlify.app/

## Pré-requesitos

:warning: [Node](https://nodejs.org/en/download/)

:warning: [Yarn](https://classic.yarnpkg.com/pt-BR/docs/install/#windows-stable) 

## Como rodar a aplicação :arrow_forward:

No terminal, clone o projeto: 

```
git clone https://github.com/React-Bootcamp-WoMarkersCode/certificate-generator
```

Entre na pasta do projeto:  

```
cd certificate-generator
```

Instale as dependecias:

```
yarn install
```

Execute a aplicação:

```
yarn start
```

Pronto, agora é possível acessar a aplicação a partir da rota http://localhost:3000/ 

## JSON :floppy_disk:

A nossa simulação de banco de dados foi feita com JSON. Foram separados um para [usuarios](https://github.com/React-Bootcamp-WoMarkersCode/certificate-generator/blob/DianaRegina/certificate/src/services/users.json), [participantes](https://github.com/React-Bootcamp-WoMarkersCode/certificate-generator/blob/DianaRegina/certificate/src/services/participantes.json) e [eventos](https://github.com/React-Bootcamp-WoMarkersCode/certificate-generator/blob/DianaRegina/certificate/src/services/events.json):

### Usuário: 

|name|email|password|token|avatar|
| -------- |-------- |-------- |-------- |-------- |
|Lais Lima|laislima98@hotmail.com|lais123|true|https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcS9-U_HbQAipum9lWln3APcBIwng7T46hdBA42EJv8Hf6Z4fDT3&usqp=CAU|

### Evento: 

|user|company|course|startDate|finishDate|workload|logo|
| -------- |-------- |-------- |-------- |-------- |-------- |-------- |
|Lais Lima|WomakersCode|Bootcamp React|01/02/2020|28/03/2020|56|https://miro.medium.com/max/478/1*jriufqYKgJTW4DKrBizU5w.png|https://upload.wikimedia.org/wikipedia/commons/7/7f/Assinatura_Jos%C3%A9_Saramago.png|

### Participante: 

|name|email|present|receiveCertificate|course|
| -------- |-------- |-------- |-------- |-------- |
|Chaiana Hermes|chaiana_hermes@yahoo.com.br|true|false|Bootcamp React|

## Páginas

[Aqui](https://github.com/React-Bootcamp-WoMarkersCode/certificate-generator/blob/DianaRegina/README_PAGES.md) é possível visualizar a **proposta** de layout do projeto.  

## CRUD

### Usuários

:heavy_check_mark: O usuário pode ser **criado** na pagina Sign-up a partir de um formulário ou com uma conta existente no Google.

:heavy_check_mark: Os dados do usuário podem ser **acessados** em Login e perfil. 

:heavy_check_mark: Os dados do usuário podem ser **atualizados** em seu perfil a partir de um formulário.

:heavy_check_mark: A conta do usuário pode ser **deletada** em seu perfil.

### Eventos

:heavy_check_mark: Podem ser **criados** a partir de um formulário na lista de eventos.

:heavy_check_mark: Podem ser **acessados** na lista de eventos 

:heavy_check_mark: Podem ser **atualizados**  na lista de eventos a partir de um formulário.

:heavy_check_mark: Podem ser **deletados** na lista de eventos

### Participantes

:heavy_check_mark: Podem ser **criados** a partir de um formulário na lista de participantes.

:heavy_check_mark: Podem ser **acessados** em uma lista na lista de participantes.

:heavy_check_mark: Podem ser **atualizados**, indicando se aquele participante poderá ou não receber um certificado na lista de participantes.

:heavy_check_mark: Podem ser **deletados** na lista de participantes.

## Linguagens, dependencias e libs utilizadas :books:

- [React](https://pt-br.reactjs.org/docs/create-a-new-react-app.html)
- [React PDF](https://react-pdf.org/)
- [React Router](https://reacttraining.com/react-router/web/guides/quick-start)

Framework para layouts prontos:
- [AntDesign](https://ant.design/docs/react/introduce) 

Autenticação com Google
- [Login com Google](https://www.npmjs.com/package/react-google-login)

Para mandar PDF por email
- [jspdf](https://www.npmjs.com/package/jspdf) 

Para inserir HTML no corpo do email
- [html2canvas](https://www.npmjs.com/package/html2canvas)

Para desenvolver a assinatura digital:

- [Reactjs-Popup](https://react-popup.elazizi.com/getting-started/)
- [react-signature-canvas](https://www.npmjs.com/package/react-signature-canvas)

Permite visualizar uma animação enquanto o usuário espera o e-mail ser enviado:
- [React-Spinkit](https://github.com/KyleAMathews/react-spinkit)

## Dependência externa :incoming_envelope:
[Server Mailjet](https://github.com/beebones/server-mailjet) - Back-end feito em **Golang** utiizado para consumir api **mailjet** e enviar os emails com o certificado.
<hr/> -->
