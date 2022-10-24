import requests

'''Programa em Python desenvolvido para postar conteúdos 
e consultar informações de páginas corportativas do instagram'''
''''Autor: Gustavo Pita Bersaneti'''

pageID = "110544383863225"
access_token = "EAAPl1L0LH7wBALZCq6WA7IuZC9w4Tt9hNxdsbSL5vLS5AvZBCobIMKNBYgdMXt3qH6ZCzkdX5GuXRPKwq2s4i1ly6chRlzxyBiPZAHGvjZC0bQgt8z1gCZCFSBripPsXe4yXaL4h2dhKh41hg0owaSrqatGQ2H6PAe6av2Bz7fMSgGf0ZCSPjdwjZAA2XJPDxVeo7iGU6anME8w8aAmAQ187TGSiWd9jY0kYZD"

opção = "SIM"
while opção == "SIM":

    link_foto = str(input("Digite o link da foto que deseja postar: "))
    legenda = str(input("Digite a legenda da foto: "))
    
    request = requests.get(f"https://graph.facebook.com/v15.0/{pageID}?fields=instagram_business_account&access_token={access_token}")
    instagramID = request.json()["instagram_business_account"]["id"]
    request = requests.get(f"https://graph.facebook.com/v14.0/{instagramID}?fields=media%2Cfollowers_count%2Cfollows_count%2Cusername%2Cname&access_token={access_token}")
        
    def get_info():
        resposta_infos = request.json()
        if request.status_code == 200:
            nome_usuario = resposta_infos["name"]
            nome_conta = resposta_infos["username"]
            seguidores = resposta_infos["followers_count"]
            seguindo = resposta_infos["follows_count"]

            print(f"\nInformações da página do instagram:\n")
            print(f"Nome de usuário: {nome_usuario}")
            print(f"Nome da conta: {nome_conta}")
            print(f"Número de seguidores: {seguidores}")
            print(f"Número de pessoas seguindo:{seguindo}")
        else:
            print(f" ERRO - STATUS CODE: {request.status_code} " )

    def post_content():
        request = requests.post(f"https://graph.facebook.com/v14.0/{instagramID}/media?image_url={link_foto}&caption={legenda}&access_token={access_token}")
        imageID = request.json()["id"]
        request2 = requests.post(f"https://graph.facebook.com/v14.0/{instagramID}/media_publish?creation_id={imageID}&access_token={access_token}")
        resposta = request2.json()

    get_info()
    post_content()

    opção = input("Digite SIM para fazer mais uma consulta/postagem ou NÃO para sair: ").upper()
