*** Criando ambiente virtual ***
    *Ativando o ambiente visual* 
        pithon -m venv flask_env
    *Iniciando e/ou ambiente*
        .\flask\Scripts\activate 
        deactivate - encerrando o ambiente
    *Fazendo e carregando lista dos pacotes e instalando*
      pip freeze > requirements.txt (copiar pacotes e colocar em um arquivo requirements.txt) 
      pip  install -r requirements.txt

*** Instalando o Flask ***
    pip install flask

*** Instalando pacote para variaveis de ambiente ***
    pip install python-dotenv

*** Startando o projeto ***
    flask run --debug