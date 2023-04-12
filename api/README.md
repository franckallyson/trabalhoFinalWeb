<div align="center" id="cabecalho">
    <h1>BackEnd TrabalhoFinal</h1>
    <h3>Franck Allyson da Silva Rocha </h3>
    <h4>4º Período | BSI | IFNMG Campus Salinas</h4>
</div>

<hr>

1. [Linguagem e Framework](#ling_frame)
2. [Banco de Dados Escolhido](#bd)
3. [DBaaS Escolhido](#dbaas)
4. [Documentação do projeto](#doc)

    4.1. [Descrição e Objetivos](#desc_obj)
    
    4.2. [Tecnologias utilizadas](#tec)
    
    4.3. [Como replicar o Projeto](#replica)
    
    4.4. [Deploy de uma API](#deploy)
    
    4.5. [Endpoints Disponíveis](#endpoints)
5. [Utilização DBaaS](#utilizardbaas)
6. [Creditos](#credits)
7. [Licença](#licenca)

<hr>

<ul style="list-style: none;">
    <li>
        <h3 id="ling_frame">1. Linguagem e Framework Escolhido</h3>
        <div style="padding-left: 30px;">
            Para este exercício, foi escolhido a linguagem Python e o Framework <a href="https://www.djangoproject.com/">Django</a>.<br> O Django disponibiliza a utilização de outro framework, o <i>Django Rest Framework</i>, e com isso a implementação fica <b>extremamente</b> fácil! Vamos continuar!
        </div>
    </li>
    <hr>
    <li>
        <h3 id="bd">2. Banco de Dados Escolhido</h3>
        <div style="padding-left: 30px;">
            O banco de dados escolhido foi o <b>PostgreSQL</b>. <br>
            Pela versatilidade e integração facilitada com o Django. 
        </div>
    </li>
    <hr>
    <li>
        <h3 id="dbaas">3. DBaaS escolhido</h3>
        <div style="padding-left: 30px;">
            Utilizamos o Bit.io para fornecer o Banco de Dados como Serviço. <br>
            O site é bem prático e fácil de ser utilizado. 
        </div>
    </li>
    <hr>
    <li>
        <h3 id="doc">4. Documentação do Projeto</h3>
        <ul style="list-style:none;">
            <li>
                <h4 id="desc_obj">4.1. Descrição e Objetivos</h4>
                <div style="padding-left: 30px;">
                    Este projeto é um Back-End para um site de cabeleireiro, disponibilizamos Imagens, Comentários, Serviços e Pacotes de serviços. No mais, padrão, as requisições entregam dados em JSON. <br>
                    O principal Objetivo com a execução desse projeto é aprender conceitos de API, Backend e também do próprio Django. Eu particularmente pretendo trabalhar  focado na parte do back-end então pra mim é de grande valia. 
                     <br>Vale ressaltar que fizemos a integração dos dados da API com o Front. 
               </div>
            </li>
            <hr>
            <li>
                <h4 id="tec">4.2. Tecnologias e Ferramentas Utilizadas</h4>
                <div style="padding-left: 30px;">
                    <ul>
                        <li>  
                            <h5><a href="https://www.postman.com/">PostMan</a> - ( Execução de testes das requisições )</h5>
                        </li>
                        <li>  
                            <h5>PyCharm - ( Ambiente de Desenvolvimento )</h5>
                        </li>
                        <li>  
                            <h5>PythonAnywhere - ( Serviço de Deploy )</h5>
                        </li>
                        <li>  
                            <h5>Django - ( Framework )</h5>
                        </li>
                        <li>  
                            <h5>Django Rest Framework - ( Framework para Desenvolvimento de API )</h5>
                        </li>
                        <li>  
                            <h5>Dependências e versões: </h5>
                            <div style="padding-left: 30px;">
                                <table>
                                <thead>
                                    <tr>
                                        <th>Dependência</th>
                                        <th>Versão</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>
                                            Python
                                        </td>
                                        <td>
                                            3.10.4
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>
                                            Django
                                        </td>
                                        <td>
                                            4.1.7
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>
                                            djangorestframework
                                        </td>
                                        <td>
                                            3.14.0
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>
                                            psycopg2
                                        </td>
                                        <td>
                                            2.9.6
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>
                                            Pillow
                                        </td>
                                        <td>
                                            9.5.0
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>
                                            django-cors-headers
                                        </td>
                                        <td>
                                            3.14.0
                                        </td>
                                    </tr>
                                </tbody>
                                </table>
                            </div>
                        </li>
                    </ul>
                </div>
            </li>
            <hr>
            <li>
                <h4 id="replica">4.3. Como Replicar o projeto</h4>
                <div style="padding-left: 30px;">
                    Neste momento iremos ver um passo a passo de como replicar o projeto feito nessa atividade. Irei lhe ensinar minuciosamente cada passo até chegar ao Deploy e testagem. 
                </div>
                <ol style="list-style: none;">
                    <li>
                        <h4>4.3.1. Preparação do ambiente</h4>
                        <div style="padding-left: 30px;">
                            <ul>
                                <li>
                                Tenha o Python instalado em sua máquina. Para isso, basta entrar neste link: <a href="https://www.python.org/downloads/">Download Python</a>.
                                </li>
                                <br>
                                <li>
                                Tenha um Editor de Código instalado em sua máquina. Recomendo tanto o <a href="https://www.jetbrains.com/pycharm/">PyCharm</a>, quanto o <a href="https://code.visualstudio.com/">VsCode</a>. Para esse tutorial, recomendamos o PyCharm, por ter sido o usado para o desenvolvimento dessa API. 
                                </li>
                                <br>
                                <li>
                                    <h5>Criação do Projeto</h5>
                                    <div style="padding-left: 30px;">
                                        Primeiramente você precisa entender o que é <b>ambiente virtual</b>. O ambiente virtual é nada mais do que uma forma de encapsular o que tudo o que o seu projeto terá: Dependências, Bibliotecas, etc. Ele permite que você isole todas as necessidades do projeto X e que ao criar um projeto Y, você não tenha as necessidades do X já instaladas, afinal, pode ser que você não precise de nenhuma. 
                                        <br><br>
                                        Para criar um projeto, basta ir no canto superior direito da sua IDE, clicar em <b>File</b>, e procurar por algo parecido com <b>New Project</b>, siga as instruções. 
                                        <br><br>
                                        Eu vou criar o meu projeto com o nome de <i>api</i>. Para alterar o nome, mude o último nome na localização do seu projeto.
                                        <img src="https://img001.prntscr.com/file/img001/fVA65jZzSKCkxLDsh1wI2w.png">
                                        <img src="https://img001.prntscr.com/file/img001/hREm_EQERRKYT80QLS6T7A.png">
                                        <br><br>
                                        O PyCharm na aba de criação, já permite que você crie um ambiente virtual na criação do projeto, veja: 
                                        <img src="https://img001.prntscr.com/file/img001/wMi2CP6tQtS3iQv4j7AHVw.png">
                                        <br>
                                        Caso você selecione a segunda opção: <i>Previously Cofigured interpreter</i>, você não irá criar um ambiente virtual e terá que fazer isso manualmente via terminal. Iremos explicar a você como executar isso. 
                                        <br><br>
                                        Após criar seu projeto, caso não tenha o Ambiente virtual já definido, abra o terminal e digite os seguintes comandos:<br><br>
                                        <kbd style="background-color: grey; color: white;"> 
                                            python -m venv NOME_DO_AMBIENTE_VIRTUAL
                                        </kbd><br><br>
                                        Lembrando que NOME_DO_AMBIENTE_VIRTUAL é uma variável que você escolhe o nome. <br>
                                        Para ativar o Ambiente virtual, basta digitar: <br><br>
                                        <kbd style="background-color: grey; color: white;"> 
                                            NOME_DO_AMBIENTE_VIRTUAL/Scripts/activate
                                        </kbd><br><br>
                                        Pronto! Para verificar se foi ativo ou não, basta observar a linha de inserção do terminal, á esqueda dela você terá o nome do ambiente virtual entre parênteses. Exemplo:
                                        <br><br>
                                        <kbd style="background-color: grey; color: white;"> 
                                            (NOME_DO_AMBIENTE_VIRTUAL)  PS C:\Users\Franck\Faculdade\api_rest_django> 
                                        </kbd><br><br>
                                        <b>Pronto! Estamos prontos para começar, o nosso ambiente de desenvolvimento está preparado!</b>
                                    </div>
                                </li>
                                <li>
                                    <h5>Instalação das dependências</h5>
                                    <div style="padding-left: 30px;">
                                          Para instalar as dependências basta navegar até a pasta API e digitar o seguinte comando.
                                        <kbd style="background-color: grey; color: white;"> 
                                            pip install -r requirements.txt
                                        </kbd><br>
                                        O <a href="https://www.djangoproject.com/">Django</a> é um framework para desenvolvimento Web utilizando a linguagem python, iremos usar ele pois a estrutura e a forma como ele trabalha torna o nosso trabalho muito fácil. <br><br>
                                        O <a href="https://www.django-rest-framework.org/">Django Rest Framework</a> é outra ferramenta que utilizaremos, ela tem como principal função auxiliar na produção de APIs Rest. 
                                        O Pillow é uma biblioteca responsável pelo gerenciamento de imagens da nossa API.
                                        O Cors é uma ferramenta responsável por autorizar os hosts que poderão fazer solicitações á API. 
                                        O Psycopg2 é o Driver do Postgres responsável por fazer a integração da Aplicação Django com o BD PostgreSQL.
                                    </div>
                                </li>
                            </ul>
                        </div>
                    </li>
                    <li>
                        <h4>4.3.2. Inicio da Produção</h4>
                        <div style="padding-left: 30px;">
                        <ul>
                        <li>
                        <h5>Criando um projeto</h5>
                                    <div style="padding-left: 30px;">
                                        Com as dependências instaladas, iremos começar a produção. <br><br>
                                        O primeiro comando que daremos ao terminal é:<br><br>
                                        <kbd style="background-color: grey; color: white;"> 
                                            django-admin startproject NOME_DO_PROJETO .
                                        </kbd><br>
                                        Este comando irá criar uma pasta que contem arquivos de configuração do seu site, portanto, escolhemos o nome backend_trabalho_final para ele. Colocamos um PONTO no final, pois isso faz com que ele não crie uma pasta config dentro de outra pasta ambiente_trabalho_final. Veja a estrutura gerada:
                                        <img src="https://img001.prntscr.com/file/img001/31ciEphARK6H5ZaQG8CRhg.png"><br>
                                        <b>Obs: </b><i>ambiente_trabalho_final</i> é o nome do nosso ambiente virtual. 
                                        <br><br>
                                        Cada um destes arquivos tem um significado, veja: 
                                        <ul>
                                        <li>
                                        <var>manage.py</var>: Um utilitário de linha de comando que permite que você interaja com isso Projeto Django de várias maneiras. Você pode ler todos os detalhes sobre em django-admin e manage.py.
                                        </li>
                                        <li>
                                        <var>backend_trabalho_final/__init__.py</var>: Um arquivo vazio que informa ao Python que isso diretório deve ser considerado um pacote Python. Se você é um iniciante em Python,<a href="https://docs.python.org/3/tutorial/modules.html#tut-packages"> leia mais sobre pacotes </a> nos documentos oficiais do Python.
                                        </li>
                                        <li>
                                        <var>backend_trabalho_final/settings.py</var>: Configurações/configuração para este Django projeto.<a href="https://docs.djangoproject.com/en/4.1/topics/settings/"> As configurações do Django </a> informarão tudo sobre como as configurações trabalho.
                                        </li>
                                        <li>
                                        <var>backend_trabalho_final/urls.py</var>: As declarações de URL para este projeto Django; um "sumário" do seu site com tecnologia Django. Você pode ler mais sobre URLs no <a href="https://docs.djangoproject.com/en/4.1/topics/http/urls/">dispatcher de URL</a>.
                                        </li>
                                        <li>
                                        <var>backend_trabalho_final/asgi.py</var>: Um ponto de entrada para servidores Web compatíveis com ASGI para sirva o seu projeto. <a href="https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/">Consulte Como implantar com ASGI</a> para obter mais detalhes.
                                        </li>
                                        <li>
                                        <var>backend_trabalho_final/wsgi.py</var>: Um ponto de entrada para servidores Web compatíveis com WSGI para sirva o seu projeto. <a href="https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/">Consulte Como implantar com o WSGI</a> para obter mais detalhes.
                                        </li>
                                        </ul>
                                        <br><br>
                                        Para o nosso tutorial, se preocupe apenas com o <var>Manage.py, setting.py e urls.py</var>.
                                    </div>
                        </li>
                        <ul>
                            <h5>Criação de um App</h5>
                                <div style="padding-left: 30px;">
                                    Nesse momento o seu projeto ja está rodando localmente. Para verificar isso digite no terminal: 
                                    <br><br>
                                    <kbd style="background-color: grey; color: white;"> 
                                            py manage.py runserver
                                    </kbd><br><br>
                                    E você terá como resposta algo próximo a isso: <br>
                                    <img src="https://img001.prntscr.com/file/img001/e4iSgB7lTGONy6tVjumh0A.png"><br><br>
                                    Ao clicar no link, você irá para a página principal do Django: <br>
                                    <img src="https://img001.prntscr.com/file/img001/Tg0ojiPNRgyR5b9yJkYWjA.png"><br><br>
                                    Agora que você já viu que o seu Projeto está rodando, vamos iniciar a criação do App.<br><br>
                                    Começe digitando no terminal: <br>
                                    <kbd style="background-color: grey; color: white;">py manage.py startapp NOME_DO_APP </kbd><br><br>
                                    Escolhemos o nome api_trabalho_final para o app. Este comando irá gerar os seguintes diretórios e arquivos: <br><br>
                                    <img src="https://img001.prntscr.com/file/img001/Oh8djl-QRueQJTm3ypdzrA.png"><br><br>
                                    Não iremos explicar uma por uma nesse momento, você irá entender no decorrer do desenvolvimento. <br><br>
                                    Vamos registrar o App criado no arquivo <var>settings.py</var>.
                                    <br><br>
                                    Adicione as três últimas linhas da lista INSTALLED_APPS: 
                                    <br>
                                    <var>api_trabalho_final</var> è o nome do App que criamos. <br>
                                    <var>rest_framework</var> é a ferramenta que instalamos no início do desenvolvimento, ela será usada na produção da nossa API e o django pede para você registrar aí caso for usa-la. 
                                    <var>corsheaders</var> é a ferramenta responsável pela autorização das hosts solicitarem á API.<br> Além disso você precisará adicionar á lista de MiDDLEWARES: "corsheaders.middleware.CorsMiddleware", e criar seguinte lista CORS_ALLOWED_ORIGINS = [
    (HOSTS_AUTORIZADAS)
] 
</div>
                                <li>
                                <h5>Construindo os Models</h5>
                                    <div style="padding-left: 30px;">
                                    Vamos começar criando os nossos Models. Segue uma explicação sobre eles: Um modelo no Django é um tipo especial de objeto -- ele é salvo em um banco de dados. Um banco de dados é uma coleção de dados. Ele é um local em que você vai salvar dados sobre usuários, suas postagens, etc. Usaremos um banco de dados chamado postgreSQL para armazenar as nossas informações.<br><br>
                                    <br><br>
                                    Para alterar o banco de dados, vá até settings e na área DATA BASE faça o seguinte:
                                    <img src="https://img001.prntscr.com/file/img001/JawNj8mmQqGFOjeCl0DD5w.png" alt="">
<br><br>
                                    Agora vou facilitar pra você, os models são as tabelas do nosso banco de dados!
                                    <br><br>
                                    Vamos começar!
                                    <pre>
                                        <code>
from django.db import models
<br>
class Comentario(models.Model):
    nome_usuario = models.CharField(max_length=100)
    comentario = models.TextField()
        <br>
class Image(models.Model):
    descricao = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='images/')
        <br>
class PacotePromocional(models.Model):
    nomepacotepromocional = models.CharField(max_length=100)
<br>
class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    valor = models.FloatField()
    marcada = models.BooleanField()
    picture = models.ImageField(upload_to='images/', null=True) <br>
<br>
    
class ServicoPacotePromocional(models.Model):
    fk_id_servico = models.ForeignKey(Servico, models.DO_NOTHING, db_column='fk_id_servico', blank=True, null=True)
    fk_id_pacotes_promocionais = models.ForeignKey(PacotePromocional, models.DO_NOTHING, db_column='fk_id_pacotes_promocionais', blank=True, null=True)

<br>
                                        </code>
                                    </pre>
                                    <br><br>
                                    Estes são os models, os termos usados ai são baseados em conceitos de banco de dados. Veja que os atributos recebem funções como:<br><code> charField, TextField, ForeignKey, DateField
                                    </code>.
                                    <br><br>São auto explicativos, ou seja, representam colunas da tabela com o tipo especificado, Text, Char, Date, etc.
                                    <br><br>
                                    Para aprender mais sobre banco de dados, <a href="https://www.devmedia.com.br/conceitos-fundamentais-de-banco-de-dados/1649">Clique Aqui</a>
                                    </div>  
                                </li>
                        </ul>
                        </div>
                    </li>
                    <li>
                        <h4>4.3.3. Criando os Serializers</h4>
                        <div style="padding-left: 30px;">
                        Serialização é o processo de transformar dados em um formato que pode ser armazenado ou transmitido e, então, reconstruído. Ele é usado em todas as partes do desenvolvimento de aplicações, ou quando estamos armazenando dados numa base de dados, na memória ou convertendo-os em arquivos.
                        <a href="https://labcodes.com.br/blog/pt-br/development/como-usar-serializers-de-django-rest-framework/#:~:text=Django%20vem%20com%20um%20m%C3%B3dulo%20de%20serializers%20que,as%20aplica%C3%A7%C3%B5es%20web%2C%20como%20JSON%2C%20YAML%20e%20XML.">Leia mais...</a>
                        <br><br>
                        Crie uma pasta dentro do seu diretório <code>NOME_DO_APP</code>, que no nosso exemplo é biblioteca, a pasta deve se chamar <code>serializer.py</code>
                        <br><br>
                        Faça o seguinte código:
                        <pre>
                        <code>
from rest_framework import serializers
from api_trabalho_final.models import Comentario, Image, PacotePromocional, ServicoPacotePromocional, Servico


class ComentariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'


class ImagesSerializer(serializers.ModelSerializer):
    imagem = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Image
        fields = ('id', 'descricao', 'imagem')


class PacotesPromocionaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = PacotePromocional
        fields = '__all__'


class ServicosPacotesPromocionaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicoPacotePromocional
        fields = '__all__'


class ServicosSerializer(serializers.ModelSerializer):
    picture = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Servico
        fields = '__all__'
                        </code>
                        </pre>
                        <br><br>
                        Veja, começamos importando o módulo <code>serializers</code> disponibilizado pelo nosso <b>Django Rest Framework.</b> Depois disso importe as tabelas que você quer serializar, no nosso caso são todas. 
                        <br><br>
                        Para cada tabela você precisará criar um serializer. Extenda cada classe de <code>serializers.ModelSerializer</code>, defina o model utilizado e os campos que você quer serializar. De resto, o Django faz todo o trabalho!
                        <br><br>
                        Esses códigos irão permitir que transformemos os dados da tabela em um Json, para que retornemos isso ao usuário da nossa API. 
                        </div>
                    </li>
                    <li>
                    <h4>4.3.4. Criando as Views</h4>
                    <div style="padding-left: 30px;">
                    Uma função view, ou view para abreviar, é uma função Python que usa um solicitação da Web e retorna uma resposta da Web. Esta resposta pode ser o conteúdo HTML de uma página da Web, ou um redirecionamento, ou um erro 404, ou um documento XML, ou uma imagem . . . ou qualquer coisa, na verdade. A visão em si contém qualquer lógica arbitrária necessário para devolver essa resposta. Este código pode viver em qualquer lugar que você quiser, desde que como está no seu caminho Python. Não há outro requisito – nenhuma "magia", então para falar. Por uma questão de colocar o código em algum lugar, a convenção é colocar modos de exibição em um arquivo chamado , colocado em seu projeto ou diretório do <b>aplicativo.views.py</b>.
                    <a href="https://docs.djangoproject.com/en/4.1/topics/http/views/">Aprenda mais...</a>
                    <br><br>
                    As nossas views ficarão assim:
                    <pre>
                    <code>
from rest_framework import viewsets
from api_trabalho_final.models import Comentario, Image, Servico, ServicoPacotePromocional, PacotePromocional
from api_trabalho_final.serializer import ComentariosSerializer, ImagesSerializer, ServicosSerializer, ServicosPacotesPromocionaisSerializer, PacotesPromocionaisSerializer


class ComentariosViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentariosSerializer


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImagesSerializer


class ServicosViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicosSerializer


class ServicosPacotesPromocionaisViewSet(viewsets.ModelViewSet):
    queryset = ServicoPacotePromocional.objects.all()
    serializer_class = ServicosPacotesPromocionaisSerializer


class PacotesPromocionaisViewSet(viewsets.ModelViewSet):
    queryset = PacotePromocional.objects.all()
    serializer_class = PacotesPromocionaisSerializer
                    </code>
                    </pre>
                    <ul>
                    <li>
                    <h5>ViewSets</h5>
                    No Django Rest Framework, <b>Viewsets</b> são classes que agrupam a lógica relacionada à exibição de objetos em uma API.
                    <br><br>
                    Eles fornecem uma maneira rápida e fácil de definir as visualizações CRUD (criar, ler, atualizar e excluir) comuns em uma API RESTful.
                    <br><br>
                    Os Viewsets geralmente funcionam em conjunto com os Routers do DRF, que mapeiam automaticamente as rotas HTTP para as funções CRUD do Viewset.
                    <br><br>
                    Existem vários tipos de Viewsets disponíveis no DRF, cada um oferecendo diferentes níveis de controle sobre o comportamento da API e a serialização dos dados.
                    <br><br>
                    Por exemplo, os ModelViewSet e ReadOnlyModelViewSet são Viewsets que se baseiam em modelos Django, enquanto o ViewSet padrão fornece a maior flexibilidade e controle para criar visualizações personalizadas.
                    <br><br>
                    Em resumo, os Viewsets do DRF são uma abstração útil que ajuda a simplificar a criação de APIs RESTful no Django, fornecendo um conjunto padronizado de funcionalidades para CRUD e mapeando as rotas HTTP automaticamente.</li><br>
                    <li>
                    <h5>query_sets</h5>
                    Já os <b>Querysets</b> são objetos do Django que representam uma consulta ao banco de dados. Eles permitem que você faça consultas complexas ao banco de dados e manipule os resultados. Quando você executa uma consulta no Django, ela retorna um queryset que contém todos os objetos correspondentes aos critérios da consulta.
<br><br>
Os querysets são bastante flexíveis e permitem que você faça operações como filtrar, ordenar e limitar os resultados da consulta. Eles também permitem que você aplique funções agregadas, como contar ou somar os valores de um campo.</li>
                    </ul>
                    <br><br>
                    Depois de entender isso, basta implementar, definimos o query_set e em seguida a classe de serialização, que recebe a classe Serializer que criamos no arquivo <code>Serializer.py</code>.
                    </div>
                    </li>
                    <li>
                    <h4>4.3.4. Indicando as Urls</h4>
                    <div style="padding-left: 30px;">
                    Após todas as views definidas, devemos informar quais serão as urls referentes á elas. Vamos fazer isso no arquivo <code>NOME_DO_PROJETO/urls.py</code>. No nosso caso, <code>config/urls.py</code>.
                    <br><br>
                    <pre>
                    <code>
"""
URL configuration for backend_trabalho_final project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from api_trabalho_final.views import ComentariosViewSet, ImagesViewSet, ServicosViewSet, PacotesPromocionaisViewSet, ServicosPacotesPromocionaisViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'comentarios', ComentariosViewSet)
router.register(r'images', ImagesViewSet, basename="Images")
router.register(r'servicos', ServicosViewSet)
router.register(r'pacotes', PacotesPromocionaisViewSet)
router.register(r'servicos_pacotes', ServicosPacotesPromocionaisViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)"""
                    </code>
                    </pre>
                    <br><br>
                    O mais importante nesse momento é entender o pacote <code>routers</code> que o rest_framework disponibiliza. 
                    <br><br>
                    Como estamos usando classes Viewset em vez de classes View, na verdade não precisamos criar a URL conf nós mesmos. As convenções para conectar recursos em exibições e urls podem ser manipuladas automaticamente, usando uma classe Router. Tudo o que precisamos fazer é registrar os conjuntos de exibição apropriados com um roteador e deixá-lo fazer o resto. <a href="https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/">Aprenda mais sobre routers.</a>
                    <br><br>
                    Já a rota de admin, é disponibilizada pelo próprio Django, para você ter acesso á página de administração do sistema. Para logar nela coloque <code>/admin</code> ao fim da url e digite login e senha do SuperUser. Parar criar o SuperUser digite no terminal: <br>
                    <kbd>py manage.py createsuperuser</kbd>
                    <br>Depois disso siga as instruções. 
                    <br><br>
                    Você verá uma tela próxima á isso: 
                    <img src="https://img001.prntscr.com/file/img001/Df-fDAAhSqqR9LpcscWivg.png">
                    </div>
                    </li>
                </ol>
            </li>
            <br>
            <li>
            <h4 id="deploy">4.4. Deploy de uma API</h4>
            <div style="padding-left: 30px;">
            Para efetuar o deploy na plataforma PythonAnywhere eu segui os tutoriais do site <a href="https://img001.prntscr.com/file/img001/lWx0B7mIRZmUpQ-8jfSUoQ.png">Acervo Lima</a>. Ele ensina de forma detalhada como executar o Deploy, siga o passo-a-passo e dará tudo certo!
            Porém vale lembrar que para fazer o deploy de uma API que usa um banco de dados que está hospedado em outro local é um serviço pago. 
         </div>
            </li>
            <li>
            <h4 id="endpoints">4.5. Endpoints Disponíveis</h4>
            <div style="padding-left:30px;">
            Para cada tabela criada nós temos dois Endpoints possíveis, genéricamente falando, já que para cada dado criado surge um Endpoint novo. Vamos lá, para cada model NOME_DO_MODEL criado nós teremos os endpoints: <code>https://URL_BASE/NOME_DO_MODEL/</code> e <code>https://URL_BASE/NOME_DO_MODEL/ID_DO_DADO/</code>.
            <br><br>
            Em nosso projeto temos quatro tabelas, logo teremos os seguintes endpoints: 
            <ul>
            <li>Servico: <ul><li>"http://franckallyson.pythonanywhere.com/servicos/"</li><li>"http://franckallyson.pythonanywhere.com/servicos/id_do_servico/"</li></ul>
            </li>
            <li>Pacotes: <ul><li>"http://franckallyson.pythonanywhere.com/pacotes/"</li><li>"http://franckallyson.pythonanywhere.com/pacotes/id_do_pacotes/"</li></ul></li>
            <li>Imagens: <ul><li>"http://franckallyson.pythonanywhere.com/imagens/"</li><li>"http://franckallyson.pythonanywhere.com/imagens/id_da_imagem/"</li></ul></li>
            <li>Serviços do Pacote: <ul><li>"http://franckallyson.pythonanywhere.com/languages/"</li><li>"http://franckallyson.pythonanywhere.com/servicos_pacotes/id/"</li></ul></li>
            <li>Comentários: <ul><li>"http://franckallyson.pythonanywhere.com/comentarios/"</li><li>"http://franckallyson.pythonanywhere.com/comentarios/id/"</li></ul></li>
            </ul>
            <br><br>
        </ul>
    </li>
   <li>
   <h3 id="utilizardbaas">5. Utilizando DBaaS</h3>
<div style="padding-left: 30px;">
As alterações que fazemos pela API são enviadas diretamente para o Banco de Dados Remoto. 
<img src="https://img001.prntscr.com/file/img001/NK3727o0QUuWtTd4CVzEDg.png" alt="">
</div>
</li>
    <li>
    <h3 id="credits">6. Créditos</h3>
    <div style="padding-left: 30px;">
    <ul>
    <li><a href="https://www.django-rest-framework.org/">Django Rest Framework</a></li>
    <li><a href="https://www.djangoproject.com/">Django</a></li>
    <li><a href="https://www.youtube.com/watch?v=BKChTO8GADk&feature=youtu.be&ab_channel=Alura">Video ensinando criar uma API</a></li>
    <li><a href="https://acervolima.com/como-implantar-o-projeto-django-no-pythonanywhere/#:~:text=python3%20-m%20venv%20env%20%23%20criar%20ambiente%20virtual,instalou%20no%20bash%20Digite%20o%20comando%20no%20bash">Artigo ensinando fazer o deploy</a>/</li>
    </ul>
    </div>
    </li>
    <li>
    <h3 id="licenca">7. Licença</h3>
    <div style="padding-left: 30px;">GNU 3.0</div>
    </li>
    <hr>
</ul>
