import random

nombres=("El gallo","El diablito","La dama","El catrín","El paraguas","la sirena","La escalera","La botella","El barril","El árbol","El melón","El valiente","El gorrito","La muerte","La pera","La bandera","El bandolón","El violoncello","La garza","El pájaro","La mano","La bota","La luna","El cotorro","El borracho","El negrito","El corazón","La sandía","El tambor","El camarón","Las jaras","El músico","La araña","El soldado","La estrella","El cazo","El mundo","El apache","El nopal","El alacrán","La rosa","La calavera","La campana","El cantarito","El venado","El sol","La corona","La chalupa","El pino","El pescado","La palma","La maceta","El arpa","La rana")

print(nombres[random.randrange(54)])


def impresion():
    a=1
    for i in nombres:
        print(i)

impresion()
