import subprocess
cartas={
    'El gallo':'El que la cantó a San Pedro',
    'El diablito':'Pórtate bien cuatito, si no te lleva el coloradito ',
    'La dama':'Puliendo el paso, por toda la calle real',
    'El catrín':'Don Ferruco en la alameda, su bastón quería tirar',
    'El paraguas':'Para el sol y para el agua',
    'la sirena':'Medio cuerpo de señora se divisa en altamar',
    'La escalera':'Súbeme paso a pasito, no quieras pegar brinquitos ',
    'La botella':'La herramienta del borracho ',
    'El barril':'Tanto bebió el albañil, que quedó como barril ',
    'El árbol':'El que a buen árbol se arrima buena sombra le cobija ',
    'El melón':'Me lo das o me lo quitas ',
    'El valiente':'Por qué le corres cobarde, trayendo tan buen puñal ',
    'El gorrito':'Ponle su gorrito al nene, no se nos vaya a resfriar ',
    'La muerte':'La muerte siriqui siaca, La muerte tilica y flaca ',
    'La pera':'El que espera desespera ',
    'La bandera':'Verde blanco y colorado, la bandera del soldado ',
    'El bandolón':'Tocando su bandolón, está el mariachi Simón ',
    'El violoncello':'Creciendo se fue hasta el cielo, y como no fue violín, tuvo que ser violoncello ',
    'La garza':'Al otro lado del río tengo mi banco de arena, donde se sienta mi chata pico de garza morena ',
    'El pájaro':'Tú me traes a puros brincos, como pájaro en la rama ',
    'La mano':'La mano de un criminal, La mano de un escribano ',
    'La bota':'Una bota igual que l’otra Bótala si no te sirve ',
    'La luna':'El farol de los enamorados ',
    'El cotorro':'Cotorro cotorro saca la pata, y empiézame a platicar ',
    'El borracho':'¡Ah! qué borracho tan necio, ya no lo puedo aguantar ',
    'El negrito':'El que se comió el azúcar ',
    'El corazón':'No me extrañes corazón, que regresó en el camión ',
    'La sandía':'La barriga que Juan tenía, era empacho de sandía ',
    'El tambor':'No te arrugues cuero viejo, que te quiero pa’tambor ',
    'El camarón':'Camarón que se duerme, se lo lleva la corriente ',
    'Las jaras':'Las jaras del indio Adán, donde pegan, dan ',
    'El músico':'El músico trompa de hule, ya no me quiere tocar ',
    'La araña':'Atarántamela a palos, no me la dejes llegar ',
    'El soldado':'Uno, dos y tres el soldado p’al cuartel ',
    'La estrella':'La estrella polar del norte',
    'El cazo':'El caso que te hago es poco',
    'El mundo':'Este mundo es una bola, y nosotros un balón ',
    'El apache':'¡Ah Chihuahua! cuánto apache con pantalón y huarache ',
    'El nopal':'Al nopal lo van a ver, nomás cuando tiene tunas ',
    'El alacrán':'El que con la cola pica, le dan una paliza ',
    'La rosa':'Rosita, Rosaura, ven que te quiero ahora ',
    'La calavera':'Al pasar por el panteón, me encontré un calaverón ',
    'La campana':'Tú con la campana y yo con tu hermana ',
    'El cantarito':'El cantarito del pulque no se te vaya a quebrar pos lo quiere la patrona pa poderme enamorar ',
    'El venado':'El que brinca los peñascos ',
    'El sol':'La cobija de los pobres ',
    'La corona':'El sombrero de los reyes ',
    'La chalupa':'Rema rema va Lupita, sentada en su chalupita ',
    'El pino':'Fresco y oloroso, en todo tiempo hermoso ',
    'El pescado':'El que por la boca muere, aunque mudo fuere ',
    'La palma':'Palmero sube a la palma y bájame un coco real ',
    'La maceta':'El que nace pa’maceta, no sale del corredor ',
    'El arpa':'Arpa vieja de mi suegra, ya no sirves pa’tocar ',
    'La rana':'Al ver a la verde rana, qué brinco pegó tu hermana'
    }



variable = "echo "+str()+" | "+" termux-tts-speak"
def  speak():
    print(variable)
    subprocess.call(variable,shell=True)

speak()
for i in nombres:
    print(i)


