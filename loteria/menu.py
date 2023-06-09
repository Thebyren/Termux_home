#========-------variables-------========#
ESC= '\x1b'
tab="\t"
esp="\n"
margen="\n\n\n"
red_color=ESC + '[31m'
blue_color=ESC + '[34m'
green_color=ESC + '[32m'
cian_color=ESC + '[36m'
intermitente = '\x1b[5;32m'
#=======-------funciones--------========#

def menu():
     print(
        blue_color+" ██████████████████████████████████████████████████████████"
        ,margen
        ,blue_color+
        """
            _____  _______ _______  ______ _____ _______
    |      |     |    |    |______ |_____/   |   |_____|
    |_____ |_____|    |    |______ |    \_ __|__ |     |
        """
        ,margen
        ,esp,tab, green_color+"iniciar juego"+   blue_color+tab+tab+"["+red_color+" 1 "+blue_color+"]"
        ,esp,tab, green_color+"record"+          blue_color+tab+tab+tab+"["+red_color+" 2 "+blue_color+"]"
        ,esp,tab, green_color+"creditos"+        blue_color+tab+tab+"["+red_color+" 3 "+blue_color+"]"
        ,intermitente+"hola"

        ,margen,margen
        ,blue_color+"██████████████████████████████████████████████████████████"
        )

menu()




