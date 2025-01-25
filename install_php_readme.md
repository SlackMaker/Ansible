# Detalhes do Playbook do PHP


## Componentes:

- **`hosts: all`**: Indica que o playbook deve ser executado em todos os servidores definidos no arquivo de inventário.
- **`become: yes`**: O playbook utiliza privilégios de superusuário (sudo) para instalar pacotes e iniciar serviços.
- **`php_version`**: Variável que define a versão do PHP a ser instalada (exemplo: `php8.1`).
- **`php_extensions`**: Uma lista de extensões PHP necessárias para o ambiente.
- **`apt`**: Usado para instalar pacotes no Ubuntu/Debian. Se for preciso usar alguma outra distribuição (como CentOS): substitua por `yum` ou `dnf` conforme necessário.
- **`php-fpm`**: Este é o serviço de PHP para rodar em servidores web (como Nginx ou Apache) que não utilizam mod_php.
- **`service`**: A tarefa para garantir que o serviço PHP-FPM esteja em execução e configurado para iniciar automaticamente.
- **`command`** e **`debug`**: Usadas para verificar e exibir a versão do PHP instalada.

### Observações:

- Este playbook usa o **apt** para pacotes do Ubuntu/Debian. Se for preciso usar alguma distribuição baseada em RHEL (CentOS, Fedora): então, será preciso alterar para o **yum** ou **dnf**.
- O **PHP-FPM** é uma das formas mais comuns de rodar PHP em servidores de produção, especialmente com servidores web como Nginx.
- As extensões PHP incluídas no playbook são comuns para ambientes web: porém, seria possível modificar a lista conforme as necessidades de cada projeto.

### Personalização:
- **Versão do PHP**: Caso for preciso empregar alguma versão específica: então, substitua a variável `php_version` por outra versão do PHP.
- **Extensões**: Se for preciso usar outras extensões: então, adicione-as à variável `php_extensions`.