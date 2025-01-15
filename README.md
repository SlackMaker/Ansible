# IaC - (Infraestrura como Código)

# Conceito
A **IaC** tem o conceito de provisionar e dar suporte à infraestrutura de computação usando código em vez de configurações e processos manuais. Todo ambiente de aplicações requer muitos componentes de infraestrutura, como sistemas operacionais, conexões de banco de dados e armazenamento.

**Como trabalhar com seus códigos:**
- Iremos conectar o servidor 192.168.0.X com seu usuario, em seguida iremos criar um ambiente virtual no python trabalhando assim de forma segura, usaremos um ambiente virtual do python para trabalhar com ansible;

1. `# python3 -m venv venv` - Criando o ambiente virtual
2. `# source venv/bin/activate` - Ativando o ambiente virtual
3. `# pip install -r requirements.txt` - Instalando os requerimentos para trabalhar com o ambiente
4. `# ansible-galaxy install -r requirements.yml` - Instalando as dependências necessárias para rodar os módulos do ansible

**Seguem os passos abaixo para realizar o clone**


1. `# git clone https://github.com/SlackMaker/Ansible.git` - Clonar o repositório
2. `# cd iac` - Entrar no diretório clonado
3. `# git checkout -b nome-da-nova-branch` - Crie uma nova branch, exemplo: feature/nova-funcionalidade ou bugfix/corrigir-erro, faça suas alterações, funcionalidades, etc...
4. `# git add .` - Adiciona os arquivos na stage
5. `# git commit -m` - Descrição das alterações realizadas" - Adicione os arquivos, descrevendo suas funcionalidades
6. `git push origin nome-da-nova-branch` - Faça um push para nova branch

7. Abra um pull request no Gitlab e aguarde a revisão, se forem feitos comentários ou solicitações de alterações, atualize sua branch conforme necessário e faça novos commits, após a aprovação do pull request a sua branch será mesclada para a master

8. Atualize sua branch principal local, depois que sua branch for mesclada, atualize sua branch principal local para  garantir que você tenha as alterações mais recentes.

9. `# git checkout main`

10. `# git pull origin main`
