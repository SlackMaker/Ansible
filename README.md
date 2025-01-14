IaC - (Infraestrura como Código)

Conceito
A IaC tem o conceito de provisionar e dar suporte à infraestrutura de computação usando código em vez de configurações e processos manuais. Todo ambiente de aplicações requer muitos componentes de infraestrutura, como sistemas operacionais, conexões de banco de dados e armazenamento.
Como trabalhar com seus códigos:

Iremos conectar o servidor 192.168.0.23 com seu DATAXXXXX, em seguida iremos criar um ambiente virtual no python trabalhando assim de forma segura, usaremos um ambiente virtual do python para trabalhar com ansible;



# python3 -m venv venv - Criando o ambiente virtual

# source venv/bin/activate - Ativando o ambiente virtual

# pip install -r requirements.txt - Instalando os requerimentos para trabalhar com o ambiente

# ansible-galaxy install -r requirements.yml - Instalando as dependências necessárias para rodar os módulos do ansible

Seguem os passos abaixo para realizar o clone


# - Clonar o repositório
# cd iac - Entrar no diretório clonado
# git checkout -b nome-da-nova-branch - Crie uma nova branch, exemplo: feature/nova-funcionalidade ou bugfix/corrigir-erro, faça suas alterações, funcionalidades, etc...
# git add . - Adiciona os arquivos na stage
# git commit -m - Descrição das alterações realizadas" - Adicione os arquivos, descrevendo suas funcionalidades

git push origin nome-da-nova-branch - Faça um push para nova branch
Abra um pull request no Gitlab e aguarde a revisão, se forem feitos comentários ou solicitações de alterações, atualize sua branch conforme necessário e faça novos commits, após a aprovação do pull request a sua branch será mesclada para a master
Atualize sua branch principal local, depois que sua branch for mesclada, atualize sua branch principal local para  garantir que você tenha as alterações mais recentes.

# git checkout main


# git pull origin main
