import tkinter
import tkinter.ttk
import winsound
#creacion y titulacion de la ventana
v = tkinter.Tk()
v.title("Super Mario Game")
#inicializacion de variables de los enemigos y mario ademas de otras funcionalidades como sus limites en saltos, entre otras
posxm = 400
final=0
finall=0
both=0
nombres=[]
parejas=False
posym = 520
limite = False
estadopow=0
nivel=0
counterxm=0
counterym=0
estadom=0
estadoizdem=0
posxl = 400
posyl = 520
limite1 = False
counterxl=0
counteryl=0
estadol=0
estadoizdel=0
nombre1=""
nombre2=""
estadoe=0
estadoe1=0
estadoe2=0
estadoe3=0
estadoe4=1
estadoe5=0
estadoe6=0
estadoe7=0
estadoe8=0
estadoe9=0
estadoe10=0
estadoe11=0
estadoe12=1
estadoe13=0
estadoe14=0
estadoe15=0
estadoe16=0
posxe=790
posye=210
posxe1=790
posye1=210
posxe2=20
posye2=210
posxe3=20
posye3=210
posxe4=820
posye4=210
posxe5=820
posye5=210
posxe6=-20
posye6=210
posxe7=-20
posye7=210
posxe8=820
posye8=520
posxe9=820
posye9=520
posxe10=-20
posye10=520
posxe11=-20
posye11=520
posxe12=820
posye12=520
posxe13=820
posye13=520
posxe14=-20
posye14=520
posxe15=-20
posye15=520
posxe16=400
posye16=520
estadov1=1
estadov2=1
estadov3=1
estadov11=1
estadov21=1
estadov31=1
points=0
pointsl=0
presionado = [0,0,0,0,0,0,0]
#reproduccion del audio
winsound.PlaySound('track.wav',winsound.SND_ASYNC)
winsound.SND_LOOP
#funciones que permiten mover al personaje de mario
def saltar():
    """
funcion que permite saltar al personaje mario sin realizar ningun cambio en su posicion en x, determinando hacia que direccion esta orientado el personaje para realizarlo, tambien determinado por el limite de salto y un contador
    """
    global canvas,lemario,posxm,posym,limite,counterym,estadoizdem
    if estadoizdem==1:
        if (limite!=True) and(counterym<=150):
            canvas.delete(lemario)
            counterym=counterym+5
            posym=posym-5
            lemario = canvas.create_image(posxm,posym, image=mario4)
            v.after(10,saltar)
            if (counterym>=150)or((posym==460)and(((posxm>=0)and(posxm<=300))or((posxm>=500)and(posxm<=800))))or((posym==340)and(((posxm>=220)and(posxm<=580))))or((posym==240)and(((posxm>=480)or(posxm<=320)))):
                limite=True
        if (limite==True)and (counterym>0):
            canvas.delete(lemario)
            counterym=counterym-5
            posym=posym+5
            lemario = canvas.create_image(posxm,posym, image=mario4)
            if ((posym==450)and(((posxm>=0)and(posxm<=300))or((posxm>=500)and(posxm<=800))))or((posym==330)and(((posxm>=220)and(posxm<=580)))):
                posym=450
                counterym=0
            v.after(10,saltar)
    elif estadoizdem==0:
        if (limite!=True) and(counterym<=150):
            canvas.delete(lemario)
            counterym=counterym+5
            posym=posym-5
            lemario = canvas.create_image(posxm,posym, image=mario14)
            v.after(10,saltar)
            if (counterym>=150) or((posym==460)and(((posxm>=0)and(posxm<=300))or((posxm>=500)and(posxm<=800))))or((posym==340)and(((posxm>=220)and(posxm<=580))))or((posym==240)and(((posxm>=480)or(posxm<=320)))):
                limite=True
        if (limite==True)and (counterym>0):
            canvas.delete(lemario)
            counterym=counterym-5
            posym=posym+5
            lemario = canvas.create_image(posxm,posym, image=mario14)
            if ((posym==450)and(((posxm>=0)and(posxm<=300))or((posxm>=500)and(posxm<=800))))or((posym==330)and(((posxm>=220)and(posxm<=580)))):
                posym=450
                counterym=0
            v.after(10,saltar)
def saltar2():
    """
    Procedimiento que realiza el salto en parabola a la derecha, realizando un cambio positivo en la posicion en x,  tambien determinado por el limite de salto y un contador
    """
    global canvas,lemario,posxm,posym,limite,counterym,counterxm
    if (limite!=True) and(counterym<=150):
        canvas.delete(lemario)
        counterym=counterym+5
        posym=posym-5
        posxm=posxm+3
        lemario = canvas.create_image(posxm,posym, image=mario4)
        v.after(10,saltar2)
        if (counterym>=150) or((posym==460)and(((posxm>=0)and(posxm<=300))or((posxm>=500)and(posxm<=800))))or((posym==340)and(((posxm>=220)and(posxm<=580))))or((posym==80)and(((posxm>=0)and(posxm<=800))))or((posym==240)and(((posxm>=480)or(posxm<=320)))):
            limite=True
    if (limite==True)and (counterym>0):
        canvas.delete(lemario)
        counterym=counterym-5
        posym=posym+5
        posxm=posxm+3
        lemario = canvas.create_image(posxm,posym, image=mario4)
        v.after(10,saltar2)
        if ((posym==420)and(((posxm>=0)and(posxm<=300))or((posxm>=500)and(posxm<=800)))):
                posym=420
                counterym=0
        elif(posym==310)and(((posxm>=220)and(posxm<=580))):
            posym=310
            counterym=0
        elif ((posym==210)and(((posxm>=0)and(posxm<=330))or((posxm>=480)and(posxm<=800)))):
            posym=210
            counterym=0
def saltar3():
    """
    Procedimiento que realiza el salto en parabola a la izquierda, realizando un cambio negativo en la posicion en x,  tambien determinado por el limite de salto y un contador
    """
    global canvas,lemario,posxm,posym,limite,counterym,counterxm
    if (limite!=True) and(counterym<=150):
        canvas.delete(lemario)
        counterym=counterym+5
        posym=posym-5
        posxm=posxm-3
        counterxm=counterxm+3
        lemario = canvas.create_image(posxm,posym, image=mario14)
        v.after(10,saltar3)
        if (counterym>=150) or((posym==460)and(((posxm>=0)and(posxm<=300))or((posxm>=500)and(posxm<=800))))or((posym==340)and((posxm>=220)and(posxm<=580)))or((posym==240)and(((posxm>=480)or(posxm<=320)))):
            limite=True
    if (limite==True)and (counterym>0):
        canvas.delete(lemario)
        counterym=counterym-5
        posym=posym+5
        posxm=posxm-3
        lemario = canvas.create_image(posxm,posym, image=mario14)
        v.after(10,saltar3)
        if ((posym==420)and(((posxm>=0)and(posxm<=300))or((posxm>=500)and(posxm<=800)))):
                posym=420
                counterym=0
        elif(posym==310)and(((posxm>=220)and(posxm<=580))):
            posym=310
            counterym=0
        elif ((posym==210)and(((posxm>=0)and(posxm<=330))or((posxm>=480)and(posxm<=800)))):
            posym=210
            counterym=0
def saltar11():
    """
funcion que permite saltar al personaje luigi sin realizar ningun cambio en su posicion en x, determinando hacia que direccion esta orientado el personaje para realizarlo, tambien determinado por el limite de salto y un contador
    """
    global canvas,leluigi,posxl,posyl,limite1,counteryl,estadoizdel
    if estadoizdel==1:
        if (limite1!=True) and(counteryl<=150):
            canvas.delete(leluigi)
            counteryl=counteryl+5
            posyl=posyl-5
            leluigi = canvas.create_image(posxl,posyl, image=luigi4)
            v.after(10,saltar11)
            if (counteryl>=150)or((posyl==460)and(((posxl>=0)and(posxl<=300))or((posxl>=500)and(posxl<=800))))or((posyl==340)and(((posxl>=220)and(posxl<=580))))or((posyl==240)and(((posxl>=480)or(posxl<=320)))):
                limite1=True
        if (limite1==True)and (counteryl>0):
            canvas.delete(leluigi)
            counteryl=counteryl-5
            posyl=posyl+5
            leluigi = canvas.create_image(posxl,posyl, image=luigi4)
            if ((posyl==450)and(((posxl>=0)and(posxl<=300))or((posxl>=500)and(posxl<=800))))or((posyl==330)and(((posxl>=220)and(posxl<=580)))):
                posyl=450
                counteryl=0
            v.after(10,saltar11)
    elif estadoizdel==0:
        if (limite1!=True) and(counteryl<=150):
            canvas.delete(leluigi)
            counteryl=counteryl+5
            posyl=posyl-5
            leluigi = canvas.create_image(posxl,posyl, image=luigi14)
            v.after(10,saltar11)
            if (counteryl>=150) or((posyl==460)and(((posxl>=0)and(posxl<=300))or((posxl>=500)and(posxl<=800))))or((posyl==340)and(((posxl>=220)and(posxl<=580))))or((posyl==240)and(((posxl>=480)or(posxl<=320)))):
                limite1=True
        if (limite1==True)and (counteryl>0):
            canvas.delete(leluigi)
            counteryl=counteryl-5
            posyl=posyl+5
            leluigi = canvas.create_image(posxl,posyl, image=luigi14)
            if ((posyl==450)and(((posxl>=0)and(posxl<=300))or((posxl>=500)and(posxl<=800))))or((posyl==330)and(((posxl>=220)and(posxl<=580)))):
                posyl=450
                counteryl=0
            v.after(10,saltar11)
def saltar21():
    """
    Procedimiento que realiza el salto en parabola a la izquierda
    """
    global canvas,leluigi,posxl,posyl,limite1,counteryl,counterxl
    if (limite1!=True) and(counteryl<=150):
        canvas.delete(leluigi)
        counteryl=counteryl+5
        posyl=posyl-5
        posxl=posxl+3
        leluigi = canvas.create_image(posxl,posyl, image=luigi4)
        v.after(3,saltar21)
        if (counteryl>=150) or((posyl==460)and(((posxl>=0)and(posxl<=300))or((posxl>=500)and(posxl<=800))))or((posyl==340)and(((posxl>=220)and(posxl<=580))))or((posyl==80)and(((posxl>=0)and(posxl<=800))))or((posyl==240)and(((posxl>=480)or(posxl<=320)))):
            limite1=True
    if (limite1==True)and (counteryl>0):
        canvas.delete(leluigi)
        counteryl=counteryl-5
        posyl=posyl+5
        posxl=posxl+3
        leluigi = canvas.create_image(posxl,posyl, image=luigi4)
        v.after(3,saltar21)
        if ((posyl==420)and(((posxl>=0)and(posxl<=300))or((posxl>=500)and(posxl<=800)))):
                posyl=420
                counteryl=0
        elif(posyl==310)and(((posxl>=220)and(posxl<=580))):
            posyl=310
            counteryl=0
        elif ((posyl==210)and(((posxl>=0)and(posxl<=330))or((posxl>=480)and(posxl<=800)))):
            posyl=210
            counteryl=0
def saltar31():
    """
    Procedimiento que realiza el salto en parabola a la derecha acordarse de acomodar el pinche codigo
    """
    global canvas,leluigi,posxl,posyl,limite1,counteryl,counterxl
    if (limite1!=True) and(counteryl<=150):
        canvas.delete(leluigi)
        counteryl=counteryl+5
        posyl=posyl-5
        posxl=posxl-3
        counterxl=counterxl+3
        leluigi = canvas.create_image(posxl,posyl, image=luigi14)
        v.after(3,saltar31)
        if (counteryl>=150) or((posyl==460)and(((posxl>=0)and(posxl<=300))or((posxl>=500)and(posxl<=800))))or((posyl==340)and(((posxl>=220)and(posxl<=580))))or((posyl==240)and(((posxl>=480)or(posxl<=320)))):
            limite1=True
    if (limite1==True)and (counteryl>0):
        canvas.delete(leluigi)
        counteryl=counteryl-5
        posyl=posyl+5
        posxl=posxl-3
        leluigi = canvas.create_image(posxl,posyl, image=luigi14)
        v.after(6,saltar31)
        if ((posyl==420)and(((posxl>=0)and(posxl<=300))or((posxl>=500)and(posxl<=800)))):
                posyl=420
                counteryl=0
        elif(posyl==310)and(((posxl>=220)and(posxl<=580))):
            posyl=310
            counteryl=0
        elif ((posyl==210)and(((posxl>=0)and(posxl<=330))or((posxl>=480)and(posxl<=800)))):
            posyl=210
            counteryl=0
def pressed(event):
    """
funcion que recive los eventos del teclado, exactamente de cuando una tecla es presionada y los compara con las teclas asignadas para realizar movimientos en mario,
en esta misma funcion tambien se determinan las caracteristicas para obtener o simular un mapa continuo y  se especifica la secuencia de animacion que tiene mario
    """
    global canvas,lemario,posxm,posym,limite,counterym,counterxm,estadom,nivel,points,nombre1,estadov1,estadov2,estadov3,score,muestra1,leluigi,posxl,posyl,limite1,counteryl,counterxl,estadol,final
    tecla = repr(event.char)
    if final!=1:
        if(tecla == "'w'"):
            presionado[0] = True
            if(presionado[2] == True):
                limite = False
                counterxm=0
                counterym=0
                saltar2()
            elif(presionado[1]==True):
                limite = False
                counterxm=0
                counterym=0
                saltar3()
            else:
                limite = False
                counterym=0
                saltar()
        elif(tecla == "'a'"):
            presionado[1] = True
            canvas.delete(lemario)
            if (((posym<=440) and (posym>=240))or((posym>=460) and (posym<=530))or((posym<=230) and (posym>=80))) and (posxm<0):
                posxm=800
                if(posym>=460) and (posym<=530):
                    posym=210
                elif(posym<=230) and (posym>=80):
                    posym=520
                lemario = canvas.create_image(posxm,posym, image=mario11)
            else:
                if estadom==0:
                    posxm = posxm - 10
                    if ((posym==420)and(((posxm>=300)and(posxm<=500)))):
                        posym=520
                        lemario = canvas.create_image(posxm,posym, image=mario11)
                    elif ((posym==310)and(((posxm>=580)or(posxm<=220)))):
                        posym=420
                        lemario = canvas.create_image(posxm,posym, image=mario11)
                    elif ((posym==210)and(((posxm>=330)and(posxm<=480)))):
                        posym=310
                        lemario = canvas.create_image(posxm,posym, image=mario11)
                    else:
                        lemario = canvas.create_image(posxm,posym, image=mario11)
                    estadom=1
                elif estadom==1:
                    posxm = posxm - 10
                    if ((posym==420)and(((posxm>=300)and(posxm<=500)))):
                        posym=520
                        lemario = canvas.create_image(posxm,posym, image=mario12)
                    elif ((posym==310)and(((posxm>=580)or(posxm<=220)))):
                        posym=420
                        lemario = canvas.create_image(posxm,posym, image=mario12)
                    elif ((posym==210)and(((posxm>=330)and(posxm<=480)))):
                        posym=310
                        lemario = canvas.create_image(posxm,posym, image=mario12)
                    else:
                        lemario = canvas.create_image(posxm,posym, image=mario12)
                    estadom=2
                elif estadom==2:
                    posxm = posxm - 10
                    if ((posym==420)and(((posxm>=300)and(posxm<=500)))):
                        posym=520
                        lemario = canvas.create_image(posxm,posym, image=mario13)
                    elif ((posym==310)and(((posxm>=580)or(posxm<=220)))):
                        posym=420
                        lemario = canvas.create_image(posxm,posym, image=mario13)
                    elif ((posym==210)and(((posxm>=330)and(posxm<=480)))):
                        posym=310
                        lemario = canvas.create_image(posxm,posym, image=mario13)
                    else:
                        lemario = canvas.create_image(posxm,posym, image=mario13)
                    estadom=0
        elif(tecla == "'d'"):
            presionado[2] = True
            canvas.delete(lemario)
            if (((posym<=440) and (posym>=240))or((posym>=460) and (posym<=530))or((posym<=230) and (posym>=80))) and (posxm>800):
                posxm=0
                if(posym>=460) and (posym<=530):
                    posym=210
                elif(posym<=230) and (posym>=80):
                    posym=520
                lemario = canvas.create_image(posxm,posym, image=mario1)
            else:
                if estadom==0:
                    posxm = posxm + 10
                    if ((posym==420)and(((posxm>=300)and(posxm<=500)))):
                        posym=520
                        lemario = canvas.create_image(posxm,posym, image=mario1)
                    elif ((posym==310)and(((posxm>=580)or(posxm<=220)))):
                        posym=420
                        lemario = canvas.create_image(posxm,posym, image=mario1)
                    elif ((posym==210)and(((posxm>=330)and(posxm<=480)))):
                        posym=310
                        lemario = canvas.create_image(posxm,posym, image=mario1)
                    else:
                        lemario = canvas.create_image(posxm,posym, image=mario1)
                    estadom=1
                elif estadom==1:
                    posxm = posxm + 10
                    if ((posym==420)and(((posxm>=300)and(posxm<=500)))):
                        posym=520
                        lemario = canvas.create_image(posxm,posym, image=mario2)
                    elif ((posym==310)and(((posxm>=580)or(posxm<=220)))):
                        posym=420
                        lemario = canvas.create_image(posxm,posym, image=mario2)
                    elif ((posym==210)and(((posxm>=330)and(posxm<=480)))):
                        posym=310
                        lemario = canvas.create_image(posxm,posym, image=mario2)
                    else:
                        lemario = canvas.create_image(posxm,posym, image=mario2)
                    estadom=2
                elif estadom==2:
                    posxm = posxm + 10
                    if ((posym==420)and(((posxm>=300)and(posxm<=500)))):
                        posym=520
                        lemario = canvas.create_image(posxm,posym, image=mario3)
                    elif ((posym==310)and(((posxm>=580)or(posxm<=220)))):
                        posym=420
                        lemario = canvas.create_image(posxm,posym, image=mario3)
                    elif ((posym==210)and(((posxm>=330)and(posxm<=480)))):
                        posym=310
                        lemario = canvas.create_image(posxm,posym, image=mario3)
                    else:
                        lemario = canvas.create_image(posxm,posym, image=mario3)
                    estadom=0
        elif(tecla == "'g'"):
            presionado[3] = True
            if parejas==False:
                archivo=open('unjugadorg.txt','r')
                nombre1=archivo.readlines(1)
                archivo.close()
                datos=[str(nombre1[0]),"\n",str(points),"\n",str(nivel),"\n",str(estadov1),"\n",str(estadov2),"\n",str(estadov3)]
                archivo=open('unjugadorg.txt','w')
                archivo.writelines(datos)     
                archivo.close()
            if parejas==True:
                archivo=open('dosjugadorg.txt','r')
                nombres=archivo.readlines()
                nombre1=nombres[0]
                nombre2=nombres[1]
                archivo.close()
                datos1=[str(nombre1),"\n",str(points),"\n",str(nivel),"\n",str(estadov1),"\n",str(estadov2),"\n",str(estadov3),"\n",str(nombre2),"\n",str(pointsl),"\n",str(estadov11),"\n",str(estadov21),"\n",str(estadov31)]
                print(datos1)
                archivo=open('dosjugadorg.txt','w')
                archivo.writelines(datos1)     
                archivo.close()
                archivo=open('dosjugadorg.txt','r')
                print(archivo.readlines())
                archivo.close()
    if parejas==True:
        if finall!=1:
            if(tecla == "'i'"):
                presionado[4] = True
                if(presionado[5] == True):
                    limite1 = False
                    counterxl=0
                    counteryl=0
                    saltar31()
                elif(presionado[6]==True):
                    limite1 = False
                    counterxl=0
                    counteryl=0
                    saltar21()
                else:
                    limite1 = False
                    counteryl=0
                    saltar11()
            elif(tecla == "'j'"):
                presionado[5] = True
                canvas.delete(leluigi)
                if (((posyl<=440) and (posyl>=240))or((posyl>=460) and (posyl<=530))or((posyl<=230) and (posyl>=80))) and (posxl<0):
                    posxl=800
                    if(posyl>=460) and (posyl<=530):
                        posyl=210
                    elif(posyl<=230) and (posyl>=80):
                        posyl=520
                    leluigi = canvas.create_image(posxl,posyl, image=luigi11)
                else:
                    if estadol==0:
                        posxl = posxl - 10
                        if ((posyl==420)and(((posxl>=300)and(posxl<=500)))):
                            posyl=520
                            leluigi = canvas.create_image(posxl,posyl, image=luigi11)
                        elif ((posyl==310)and(((posxl>=580)or(posxl<=220)))):
                            posyl=420
                            leluigi = canvas.create_image(posxl,posyl, image=luigi11)
                        elif ((posyl==210)and(((posxl>=330)and(posxl<=480)))):
                            posyl=310
                            leluigi = canvas.create_image(posxl,posyl, image=luigi11)
                        else:
                            leluigi = canvas.create_image(posxl,posyl, image=luigi11)
                        estadol=1
                    elif estadol==1:
                        posxl = posxl - 10
                        if ((posyl==420)and(((posxl>=300)and(posxl<=500)))):
                            posyl=520
                            leluigi = canvas.create_image(posxl,posyl, image=luigi12)
                        elif ((posyl==310)and(((posxl>=580)or(posxl<=220)))):
                            posyl=420
                            leluigi = canvas.create_image(posxl,posyl, image=luigi12)
                        elif ((posyl==210)and(((posxl>=330)and(posxl<=480)))):
                            posyl=310
                            leluigi = canvas.create_image(posxl,posyl, image=luigi12)
                        else:
                            leluigi = canvas.create_image(posxl,posyl, image=luigi12)
                        estadol=2
                    elif estadol==2:
                        posxl = posxl - 10
                        if ((posyl==420)and(((posxl>=300)and(posxl<=500)))):
                            posyl=520
                            leluigi = canvas.create_image(posxl,posyl, image=luigi13)
                        elif ((posyl==310)and(((posxl>=580)or(posxl<=220)))):
                            posyl=420
                            leluigi = canvas.create_image(posxl,posyl, image=luigi13)
                        elif ((posyl==210)and(((posxl>=330)and(posxl<=480)))):
                            posyl=310
                            leluigi = canvas.create_image(posxl,posyl, image=luigi13)
                        else:
                            leluigi = canvas.create_image(posxl,posyl, image=luigi13)
                        estadol=0
            elif(tecla == "'l'"):
                presionado[6] = True
                canvas.delete(leluigi)
                if (((posyl<=440) and (posyl>=240))or((posyl>=460) and (posyl<=530))or((posyl<=230) and (posyl>=80))) and (posxl>800):
                    posxl=0
                    if(posyl>=460) and (posyl<=530):
                        posyl=210
                    elif(posyl<=230) and (posyl>=80):
                        posyl=520
                    leluigi = canvas.create_image(posxl,posyl, image=luigi1)
                else:
                    if estadol==0:
                        posxl = posxl + 10
                        if ((posyl==420)and(((posxl>=300)and(posxl<=500)))):
                            posyl=520
                            leluigi = canvas.create_image(posxl,posyl, image=luigi1)
                        elif ((posyl==310)and(((posxl>=580)or(posxl<=220)))):
                            posyl=420
                            leluigi = canvas.create_image(posxl,posyl, image=luigi1)
                        elif ((posyl==210)and(((posxl>=330)and(posxl<=480)))):
                            posyl=310
                            leluigi = canvas.create_image(posxl,posyl, image=luigi1)
                        else:
                            leluigi = canvas.create_image(posxl,posyl, image=luigi1)
                        estadol=1
                    elif estadol==1:
                        posxl = posxl + 10
                        if ((posyl==420)and(((posxl>=300)and(posxl<=500)))):
                            posyl=520
                            leluigi = canvas.create_image(posxl,posyl, image=luigi2)
                        elif ((posyl==310)and(((posxl>=580)or(posxl<=220)))):
                            posyl=420
                            leluigi = canvas.create_image(posxl,posyl, image=luigi2)
                        elif ((posyl==210)and(((posxl>=330)and(posxl<=480)))):
                            posyl=310
                            leluigi = canvas.create_image(posxl,posyl, image=luigi2)
                        else:
                            leluigi = canvas.create_image(posxl,posyl, image=luigi2)
                        estadol=2
                    elif estadol==2:
                        posxl = posxl + 10
                        if ((posyl==420)and(((posxl>=300)and(posxl<=500)))):
                            posyl=520
                            leluigi = canvas.create_image(posxl,posyl, image=luigi3)
                        elif ((posyl==310)and(((posxl>=580)or(posxl<=220)))):
                            posyl=420
                            leluigi = canvas.create_image(posxl,posyl, image=luigi3)
                        elif ((posyl==210)and(((posxl>=330)and(posxl<=480)))):
                            posyl=310
                            leluigi = canvas.create_image(posxl,posyl, image=luigi3)
                        else:
                            leluigi = canvas.create_image(posxl,posyl, image=luigi3)
                        estadol=0
def released(event):
    """
esta funcion recive eventos de teclado exactamente cuando se ha dejado de presionar una tecla, asignando valores booleanos para su interpretacion en una lista
    """
    global canvas,lemario,posxm,posym,limite,estadom,estadoizdem
    tecla = repr(event.char)
    if(tecla == "'w'"):
        presionado[0] = False
    elif(tecla == "'a'"):
        estadoizdem=0
        presionado[1] = False
    elif(tecla == "'d'"):
        estadoizdem=1
        presionado[2] = False
    elif(tecla == "'g'"):
        presionado[3] = False
    elif(tecla == "'i'"):
        presionado[4] = False
    elif(tecla == "'j'"):
        estadoizdel=0
        presionado[5] = False
    elif(tecla == "'l'"):
        estadoizdel=1
        presionado[6] = False
canvas = tkinter.Canvas(v,bg="black",width=800,height=630)
for char in ["w","a","d","g","i","j","l"]:
    canvas.bind("<KeyPress-%s>" % char, pressed)
    canvas.bind("<KeyRelease-%s>" % char, released)
canvas.focus_set()
canvas.pack()
#definicion de las diferentes variables de imagenes que contienen desde enemigos hasta mario y sus animaciones
imagen = tkinter.PhotoImage(file='Mario_Bros(1).gif')
mario1=tkinter.PhotoImage(file='mario1.png')
mario2=tkinter.PhotoImage(file='mario2.png')
mario3=tkinter.PhotoImage(file='mario3.png')
mario4=tkinter.PhotoImage(file='mario4.png')
mario11=tkinter.PhotoImage(file='mario11.png')
mario12=tkinter.PhotoImage(file='mario12.png')
mario13=tkinter.PhotoImage(file='mario13.png')
mario14=tkinter.PhotoImage(file='mario14.png')
luigi1=tkinter.PhotoImage(file='luigi2.png')
luigi2=tkinter.PhotoImage(file='luigi1.png')
luigi3=tkinter.PhotoImage(file='luigi3.png')
luigi4=tkinter.PhotoImage(file='luigi4.png')
luigi11=tkinter.PhotoImage(file='luigi11.png')
luigi12=tkinter.PhotoImage(file='luigi12.png')
luigi13=tkinter.PhotoImage(file='luigi13.png')
luigi14=tkinter.PhotoImage(file='luigi14.png')
enemy1=tkinter.PhotoImage(file='enemigo1.png')
enemy2=tkinter.PhotoImage(file='enemigo2.png')
nube2=tkinter.PhotoImage(file='nube.png')
nube1=tkinter.PhotoImage(file='nube1.png')
goback=tkinter.PhotoImage(file='back.png')
life=tkinter.PhotoImage(file='vida.png')
muestra1=tkinter.Label(v,font=("Arial"),text=nombre1,width=20,bg=("black"),fg=("white"))
score=tkinter.Label(v,font=("Arial"),text=str(points),width=20,bg=("black"),fg=("white"))
scorel=tkinter.Label(v,font=("Arial"),text=str(pointsl),width=20,bg=("black"),fg=("white"))
#creacion de canvas
canvas.create_image(400,315, image=imagen)
#creacion de enemigos como imagenes y de las labels que se utilizaran para representar las vidas
lemario = canvas.create_image(posxm,posym, image=mario1)
leluigi = canvas.create_image(posxl,posyl, image=luigi1)
if parejas!=True:
    canvas.delete(leluigi)
enemy=canvas.create_image(posxe,posye, image=enemy1)
enemy11=canvas.create_image(posxe1,posye1, image=enemy1)
enemy12=canvas.create_image(posxe1,posye1, image=enemy1)
enemy13=canvas.create_image(posxe1,posye1, image=enemy1)
nube=canvas.create_image(posxe4,posye4, image=nube1)
nube11=canvas.create_image(posxe5,posye5, image=nube1)
nube12=canvas.create_image(posxe6,posye6, image=nube2)
nube13=canvas.create_image(posxe7,posye7, image=nube2)
enemy14=canvas.create_image(posxe8,posye8, image=enemy1)
enemy15=canvas.create_image(posxe9,posye9, image=enemy1)
enemy16=canvas.create_image(posxe10,posye10, image=enemy1)
enemy17=canvas.create_image(posxe11,posye11, image=enemy1)
nube14=canvas.create_image(posxe12,posye12, image=nube1)
nube15=canvas.create_image(posxe13,posye13, image=nube1)
nube16=canvas.create_image(posxe14,posye14, image=nube2)
nube17=canvas.create_image(posxe15,posye15, image=nube2)
vida3=tkinter.Label(v,image=life,width=50,bg=("black"),fg=("white"))
vida1=tkinter.Label(v,image=life,width=50,bg=("black"),fg=("white"))
vida2=tkinter.Label(v,image=life,width=50,bg=("black"),fg=("white"))
vida31=tkinter.Label(v,image=life,width=50,bg=("black"),fg=("white"))
vida11=tkinter.Label(v,image=life,width=50,bg=("black"),fg=("white"))
vida21=tkinter.Label(v,image=life,width=50,bg=("black"),fg=("white"))
def mover():
    """
esta funcion realiza el movimiento de un enemigo, haciendo tambien la simulacion de mapa continuo en este y los diferentes tipos de colisiones que puede tener desde matar
a mario y morir a manos de este
    """
    global posxe,enemy,posye,posym,posxm,estadoe,vida3,vida1,vida2,counterym,posxl,posyl,counteryl,vida31,vida11,vida21,parejas,parejas
    canvas.delete(enemy)
    posxe=posxe-1
    if (((posxm<=(posxe+30))and(posxm>=(posxe-30)))and((posym==(posye+50))or(posym==(posye-45)))):
        estadoe=0
        puntaje(100)
        empezar()
    if (((posxm<=(posxe+30))and(posxm>=(posxe-30)))and(posym==posye))and (counterym==0):
        posxm = 400
        posym = 520
        quitarvida()
    if (((posxl<=(posxe+30))and(posxl>=(posxe-30)))and((posyl==(posye+50))or(posyl==(posye-45)))):
        estadoe=0
        puntajel(100)
        empezar()
    if (((posxl<=(posxe+30))and(posxl>=(posxe-30)))and(posyl==posye))and (counteryl==0):
        posxl = 400
        posyl = 520
        quitarvidal()
    if estadoe!=0:    
        if (((posye<=440) and (posye>=240))or((posye>=460) and (posye<=530))or((posye<=230) and (posye>=80))) and (posxe<0):
            posxe=800
            if(posye>=460) and (posye<=530):
                puntaje(-100)
                if parejas==True:
                    puntajel(-100)
                posye=210
            elif(posye<=230) and (posye>=80):
                posye=520
        if ((posye==420)and(((posxe>=300)and(posxe<=500)))):
            posye=520
            enemy=canvas.create_image(posxe,posye, image=enemy1)
        elif ((posye==310)and(((posxe>=580)or(posxe<=220)))):
            posye=420
            enemy=canvas.create_image(posxe,posye, image=enemy1)
        elif ((posye==210)and(((posxe>=330)and(posxe<=480)))):
            posye=310
            enemy=canvas.create_image(posxe,posye, image=enemy1)
        else:
            enemy=canvas.create_image(posxe,posye, image=enemy1)
        v.after(10,mover)
def mover1():
    """
esta funcion realiza el movimiento de un enemigo, haciendo tambien la simulacion de mapa continuo en este y los diferentes tipos de colisiones que puede tener desde matar
a mario y morir a manos de este
    """
    global posxe1,enemy11,posye1,posym,posxm,estadoe1,vida3,vida1,vida2,counterym,posxl,posyl,counteryl,vida31,vida11,vida21,parejas
    canvas.delete(enemy11)
    posxe1=posxe1-1
    if ((posxm<=(posxe1+30))and(posxm>=(posxe1-30)))and((posym==(posye1+50))or(posym==(posye1-45))):
        estadoe1=0
        puntaje(100)
        empezar()
    if (((posxm<=(posxe1+30))and(posxm>=(posxe1-30)))and(posym==posye1))and (counterym==0):
        posxm = 400
        posym = 520
        quitarvida()
    if ((posxl<=(posxe1+30))and(posxl>=(posxe1-30)))and((posyl==(posye1+50))or(posyl==(posye1-45))):
        estadoe1=0
        puntajel(100)
        empezar()
    if (((posxl<=(posxe1+30))and(posxl>=(posxe1-30)))and(posyl==posye1))and (counteryl==0):
        posxl = 400
        posyl = 520
        quitarvidal()
    if estadoe1!=0:    
        if (((posye1<=440) and (posye1>=240))or((posye1>=460) and (posye1<=530))or((posye1<=230) and (posye1>=80))) and (posxe1<0):
            posxe1=800
            if(posye1>=460) and (posye1<=530):
                puntaje(-100)
                if parejas==True:
                    puntajel(-100)
                posye1=210
            elif(posye1<=230) and (posye1>=80):
                posye1=520
        if ((posye1==420)and(((posxe1>=300)and(posxe1<=500)))):
            posye1=520
            enemy11=canvas.create_image(posxe1,posye1, image=enemy1)
        elif ((posye1==310)and(((posxe1>=580)or(posxe1<=220)))):
            posye1=420
            enemy11=canvas.create_image(posxe1,posye1, image=enemy1)
        elif ((posye1==210)and(((posxe1>=330)and(posxe1<=480)))):
            posye1=310
            enemy11=canvas.create_image(posxe1,posye1, image=enemy1)
        else:
            enemy11=canvas.create_image(posxe1,posye1, image=enemy1)
        v.after(10,mover1)
def mover2():
    """
esta funcion realiza el movimiento de un enemigo, haciendo tambien la simulacion de mapa continuo en este y los diferentes tipos de colisiones que puede tener desde matar
a mario y morir a manos de este
    """
    global posxe2,enemy12,posye2,posym,posxm,estadoe2,vida3,vida1,vida2,counterym,posxl,posyl,counteryl,vida31,vida11,vida21,parejas
    canvas.delete(enemy12)
    posxe2=posxe2+1
    if ((posxm<=(posxe2+30))and(posxm>=(posxe2-30)))and((posym==(posye2+50))or(posym==(posye2-45))):
        estadoe2=0
        puntaje(100)
        empezar()
    if (((posxm<=(posxe2+30))and(posxm>=(posxe2-30)))and(posym==posye2))and (counterym==0):
        posxm = 400
        posym = 520
        quitarvida()
    if ((posxl<=(posxe2+30))and(posxl>=(posxe2-30)))and((posyl==(posye2+50))or(posyl==(posye2-45))):
        estadoe2=0
        puntajel(100)
        empezar()
    if (((posxl<=(posxe2+30))and(posxl>=(posxe2-30)))and(posyl==posye2))and (counteryl==0):
        posxl = 400
        posyl = 520
        quitarvidal()
    if estadoe2!=0:    
        if (((posye2<=440) and (posye2>=240))or((posye2>=460) and (posye2<=530))or((posye2<=230) and (posye2>=80))) and (posxe2>800):
            posxe2=0
            if(posye2>=460) and (posye2<=530):
                puntaje(-100)
                if parejas==True:
                    puntajel(-100)
                posye2=210
            elif(posye2<=230) and (posye2>=80):
                posye2=520
        if ((posye2==420)and(((posxe2>=300)and(posxe2<=500)))):
            posye2=520
            enemy12=canvas.create_image(posxe2,posye2, image=enemy2)
        elif ((posye2==310)and(((posxe2>=580)or(posxe2<=220)))):
            posye2=420
            enemy12=canvas.create_image(posxe2,posye2, image=enemy2)
        elif ((posye2==210)and(((posxe2>=330)and(posxe2<=480)))):
            posye2=310
            enemy12=canvas.create_image(posxe2,posye2, image=enemy2)
        else:
            enemy12=canvas.create_image(posxe2,posye2, image=enemy2)
        v.after(10,mover2)
def mover3():
    """
esta funcion realiza el movimiento de un enemigo, haciendo tambien la simulacion de mapa continuo en este y los diferentes tipos de colisiones que puede tener desde matar
a mario y morir a manos de este
    """
    global posxe3,enemy13,posye3,posym,posxm,estadoe3,vida3,vida1,vida2,counterym,posxl,posyl,counteryl,vida31,vida11,vida21,parejas
    canvas.delete(enemy13)
    posxe3=posxe3+1
    if ((posxm<=(posxe3+30))and(posxm>=(posxe3-30)))and((posym==(posye3+50))or(posym==(posye3-45))):
        estadoe3=0
        puntaje(100)
        empezar()
    if (((posxm<=(posxe3+30))and(posxm>=(posxe3-30)))and(posym==posye3))and (counterym==0):
        posxm = 400
        posym = 520
        quitarvida()
    if ((posxl<=(posxe3+30))and(posxl>=(posxe3-30)))and((posyl==(posye3+50))or(posyl==(posye3-45))):
        estadoe3=0
        puntajel(100)
        empezar()
    if (((posxl<=(posxe3+30))and(posxl>=(posxe3-30)))and(posyl==posye3))and (counteryl==0):
        posxl = 400
        posyl = 520
        quitarvidal()
    if estadoe3!=0:    
        if (((posye3<=440) and (posye3>=240))or((posye3>=460) and (posye3<=530))or((posye3<=230) and (posye3>=80))) and (posxe3>800):
            posxe3=0
            if(posye3>=460) and (posye3<=530):
                puntaje(-100)
                if parejas==True:
                    puntajel(-100)
                posye3=210
            elif(posye3<=230) and (posye3>=80):
                posye3=520
        if ((posye3==420)and(((posxe3>=300)and(posxe3<=500)))):
            posye3=520
            enemy13=canvas.create_image(posxe3,posye3, image=enemy2)
        elif ((posye3==310)and(((posxe3>=580)or(posxe3<=220)))):
            posye3=420
            enemy13=canvas.create_image(posxe3,posye3, image=enemy2)
        elif ((posye3==210)and(((posxe3>=330)and(posxe3<=480)))):
            posye3=310
            enemy13=canvas.create_image(posxe3,posye3, image=enemy2)
        else:
            enemy13=canvas.create_image(posxe3,posye3, image=enemy2)
        v.after(10,mover3)
def mover4():
    """
esta funcion realiza el movimiento de un enemigo, haciendo tambien la simulacion de mapa continuo en este y los diferentes tipos de colisiones que puede tener desde matar
a mario y morir a manos de este
    """
    global posxe4,nube,posye4,posym,posxm,estadoe4,vida3,vida1,vida2,counterym,posxl,posyl,counteryl,vida31,vida11,vida21,parejas
    canvas.delete(nube)
    posxe4=posxe4-1
    if ((posxm<=(posxe4+30))and(posxm>=(posxe4-30)))and((posym==(posye4+50))or(posym==(posye4-45))):
        estadoe4=0
        puntaje(150)
        empezar()
    if (((posxm<=(posxe4+30))and(posxm>=(posxe4-30)))and(posym==posye4))and (counterym==0):
        posxm = 400
        posym = 520
        quitarvida()
    if ((posxl<=(posxe4+30))and(posxl>=(posxe4-30)))and((posyl==(posye4+50))or(posyl==(posye4-45))):
        estadoe4=0
        puntajel(150)
        empezar()
    if (((posxl<=(posxe4+30))and(posxl>=(posxe4-30)))and(posyl==posye4))and (counteryl==0):
        posxl = 400
        posyl = 520
        quitarvidal()
    if estadoe4!=0:
        if (((posye4<=440) and (posye4>=240))or((posye4>=460) and (posye4<=530))or((posye4<=230) and (posye4>=80))) and (posxe4<0):
            posxe4=800
            if(posye4>=460) and (posye4<=530):
                puntaje(-100)
                if parejas==True:
                    puntajel(-100)
                posye4=210
            elif(posye4<=230) and (posye4>=80):
                posye4=520
        if ((posye4==420)and(((posxe4>=300)and(posxe4<=500)))):
            posye4=520
            nube=canvas.create_image(posxe4,posye4, image=nube1)
        elif ((posye4==310)and(((posxe4>=580)or(posxe4<=220)))):
            posye4=420
            nube=canvas.create_image(posxe4,posye4, image=nube1)
        elif ((posye4==210)and(((posxe4>=330)and(posxe4<=480)))):
            posye4=310
            nube=canvas.create_image(posxe4,posye4, image=nube1)
        else:
            nube=canvas.create_image(posxe4,posye4, image=nube1)
        v.after(10,mover4)
def mover5():
    """
esta funcion realiza el movimiento de un enemigo, haciendo tambien la simulacion de mapa continuo en este y los diferentes tipos de colisiones que puede tener desde matar
a mario y morir a manos de este
    """
    global posxe5,nube11,posye5,posym,posxm,estadoe5,vida3,vida1,vida2,counterym,posxl,posyl,counteryl,vida31,vida11,vida21,parejas
    canvas.delete(nube11)
    posxe5=posxe5-1
    if ((posxm<=(posxe5+30))and(posxm>=(posxe5-30)))and((posym==(posye5+50))or(posym==(posye5-45))):
        estadoe5=0
        puntaje(150)
        empezar()
    if (((posxm<=(posxe5+30))and(posxm>=(posxe5-30)))and(posym==posye5))and (counterym==0):
        posxm = 400
        posym = 520
        quitarvida()
    if ((posxl<=(posxe5+30))and(posxl>=(posxe5-30)))and((posyl==(posye5+50))or(posyl==(posye5-45))):
        estadoe5=0
        puntajel(150)
        empezar()
    if (((posxl<=(posxe5+30))and(posxl>=(posxe5-30)))and(posyl==posye5))and (counteryl==0):
        posxl = 400
        posyl = 520
        quitarvidal()
    if estadoe5!=0:    
        if (((posye5<=440) and (posye5>=240))or((posye5>=460) and (posye5<=530))or((posye5<=230) and (posye5>=80))) and (posxe5<0):
            posxe5=800
            if(posye5>=460) and (posye5<=530):
                puntaje(-100)
                if parejas==True:
                    puntajel(-100)
                posye5=210
            elif(posye5<=230) and (posye5>=80):
                posye5=520
        if ((posye5==420)and(((posxe5>=300)and(posxe5<=500)))):
            posye5=520
            nube11=canvas.create_image(posxe5,posye5, image=nube1)
        elif ((posye5==310)and(((posxe5>=580)or(posxe5<=220)))):
            posye5=420
            nube11=canvas.create_image(posxe5,posye5, image=nube1)
        elif ((posye5==210)and(((posxe5>=330)and(posxe5<=480)))):
            posye5=310
            nube11=canvas.create_image(posxe5,posye5, image=nube1)
        else:
            nube11=canvas.create_image(posxe5,posye5, image=nube1)
        v.after(10,mover5)
def mover6():
    """
esta funcion realiza el movimiento de un enemigo, haciendo tambien la simulacion de mapa continuo en este y los diferentes tipos de colisiones que puede tener desde matar
a mario y morir a manos de este
    """
    global posxe6,nube12,posye6,posym,posxm,estadoe6,vida3,vida1,vida2,counterym,posxl,posyl,counteryl,vida31,vida11,vida21,parejas
    canvas.delete(nube12)
    posxe6=posxe6+1
    if ((posxm<=(posxe6+30))and(posxm>=(posxe6-30)))and((posym==(posye6+50))or(posym==(posye6-45))):
        estadoe6=0
        puntaje(150)
        empezar()
    if (((posxm<=(posxe6+30))and(posxm>=(posxe6-30)))and(posym==posye6))and (counterym==0):
        posxm = 400
        posym = 520
        quitarvida()
    if ((posxl<=(posxe6+30))and(posxl>=(posxe6-30)))and((posyl==(posye6+50))or(posyl==(posye6-45))):
        estadoe6=0
        puntajel(150)
        empezar()
    if (((posxl<=(posxe6+30))and(posxl>=(posxe6-30)))and(posyl==posye6))and (counteryl==0):
        posxl = 400
        posyl = 520
        quitarvidal()
    if estadoe6!=0:    
        if (((posye6<=440) and (posye6>=240))or((posye6>=460) and (posye6<=530))or((posye6<=230) and (posye6>=80))) and (posxe6>800):
            posxe6=0
            if(posye6>=460) and (posye6<=530):
                puntaje(-100)
                if parejas==True:
                    puntajel(-100)
                posye6=210
            elif(posye6<=230) and (posye6>=80):
                posye6=520
        if ((posye6==420)and(((posxe6>=300)and(posxe6<=500)))):
            posye6=520
            nube12=canvas.create_image(posxe6,posye6, image=nube2)
        elif ((posye6==310)and(((posxe6>=580)or(posxe6<=220)))):
            posye6=420
            nube12=canvas.create_image(posxe6,posye6, image=nube2)
        elif ((posye6==210)and(((posxe6>=330)and(posxe6<=480)))):
            posye6=310
            nube12=canvas.create_image(posxe6,posye6, image=nube2)
        else:
            nube12=canvas.create_image(posxe6,posye6, image=nube2)
        v.after(10,mover6)
def mover7():
    """
esta funcion realiza el movimiento de un enemigo, haciendo tambien la simulacion de mapa continuo en este y los diferentes tipos de colisiones que puede tener desde matar
a mario y morir a manos de este
    """
    global posxe7,nube13,posye7,posym,posxm,estadoe7,vida3,vida1,vida2,counterym,posxl,posyl,counteryl,vida31,vida11,vida21,parejas
    canvas.delete(nube13)
    posxe7=posxe7+1
    if ((posxm<=(posxe7+30))and(posxm>=(posxe7-30)))and((posym==(posye7+50))or(posym==(posye7-45))):
        estadoe7=0
        puntaje(150)
        empezar()
    if (((posxm<=(posxe7+30))and(posxm>=(posxe7-30)))and(posym==posye7))and (counterym==0):
        posxm = 400
        posym = 520
        quitarvida()
    if ((posxl<=(posxe7+30))and(posxl>=(posxe7-30)))and((posyl==(posye7+50))or(posyl==(posye7-45))):
        estadoe7=0
        puntajel(150)
        empezar()
    if (((posxl<=(posxe7+30))and(posxl>=(posxe7-30)))and(posyl==posye7))and (counteryl==0):
        posxl = 400
        posyl = 520
        quitarvidal()
    if estadoe7!=0:    
        if (((posye7<=440) and (posye7>=240))or((posye7>=460) and (posye7<=530))or((posye7<=230) and (posye7>=80))) and (posxe7>800):
            posxe7=0
            if(posye7>=460) and (posye7<=530):
                posye7=210
                puntaje(-100)
                if parejas==True:
                    puntajel(-100)
            elif(posye7<=230) and (posye7>=80):
                posye7=520
        if ((posye7==420)and(((posxe7>=300)and(posxe7<=500)))):
            posye7=520
            nube13=canvas.create_image(posxe7,posye7, image=nube2)
        elif ((posye7==310)and(((posxe7>=580)or(posxe7<=220)))):
            posye7=420
            nube13=canvas.create_image(posxe7,posye7, image=nube2)
        elif ((posye7==210)and(((posxe7>=330)and(posxe7<=480)))):
            posye7=310
            nube13=canvas.create_image(posxe7,posye7, image=nube2)
        else:
            nube13=canvas.create_image(posxe7,posye7, image=nube2)
        v.after(10,mover7)
def mover8():
    """
esta funcion realiza el movimiento de un enemigo, haciendo tambien la simulacion de mapa continuo en este y los diferentes tipos de colisiones que puede tener desde matar
a mario y morir a manos de este
    """
    global posxe8,enemy15,posye8,posym,posxm,estadoe8,vida3,vida1,vida2,counterym,posxl,posyl,counteryl,vida31,vida11,vida21,parejas
    canvas.delete(enemy15)
    posxe8=posxe8-1
    if ((posxm<=(posxe8+30))and(posxm>=(posxe8-30)))and((posym==(posye8+50))or(posym==(posye8-45))):
        estadoe8=0
        puntaje(100)
        empezar()
    if (((posxm<=(posxe8+30))and(posxm>=(posxe8-30)))and(posym==posye8))and (counterym==0):
        posxm = 400
        posym = 520
        quitarvida()
    if ((posxl<=(posxe8+30))and(posxl>=(posxe8-30)))and((posyl==(posye8+50))or(posyl==(posye8-45))):
        estadoe8=0
        puntajel(100)
        empezar()
    if (((posxl<=(posxe8+30))and(posxl>=(posxe8-30)))and(posyl==posye8))and (counteryl==0):
        posxl = 400
        posyl = 520
        quitarvidal()
    if estadoe8!=0:    
        if (((posye8<=440) and (posye8>=240))or((posye8>=460) and (posye8<=530))or((posye8<=230) and (posye8>=80))) and (posxe8<0):
            posxe8=800
            if(posye8>=460) and (posye8<=530):
                posye8=210
                puntaje(-100)
                if parejas==True:
                    puntajel(-100)
            elif(posye8<=230) and (posye8>=80):
                posye8=520
        if ((posye8==420)and(((posxe8>=300)and(posxe8<=500)))):
            posye8=520
            enemy15=canvas.create_image(posxe8,posye8, image=enemy1)
        elif ((posye8==310)and(((posxe8>=580)or(posxe8<=220)))):
            posye8=420
            enemy15=canvas.create_image(posxe8,posye8, image=enemy1)
        elif ((posye8==210)and(((posxe8>=330)and(posxe8<=480)))):
            posye8=310
            enemy15=canvas.create_image(posxe8,posye8, image=enemy1)
        else:
            enemy15=canvas.create_image(posxe8,posye8, image=enemy1)
        v.after(10,mover8)
def mover9():
    """
esta funcion realiza el movimiento de un enemigo, haciendo tambien la simulacion de mapa continuo en este y los diferentes tipos de colisiones que puede tener desde matar
a mario y morir a manos de este
    """
    global posxe9,enemy14,posye9,posym,posxm,estadoe9,vida3,vida1,vida2,counterym,posxl,posyl,counteryl,vida31,vida11,vida21,parejas
    canvas.delete(enemy14)
    posxe9=posxe9-1
    if ((posxm<=(posxe9+30))and(posxm>=(posxe9-30)))and((posym==(posye9+50))or(posym==(posye9-45))):
        estadoe9=0
        puntaje(100)
        empezar()
    if (((posxm<=(posxe9+30))and(posxm>=(posxe9-30)))and(posym==posye9))and (counterym==0):
        posxm = 400
        posym = 520
        quitarvida()
    if ((posxl<=(posxe9+30))and(posxl>=(posxe9-30)))and((posyl==(posye9+50))or(posyl==(posye9-45))):
        estadoe9=0
        puntajel(100)
        empezar()
    if (((posxl<=(posxe9+30))and(posxl>=(posxe9-30)))and(posyl==posye9))and (counteryl==0):
        posxl = 400
        posyl = 520
        quitarvidal()
    if estadoe9!=0:    
        if (((posye9<=440) and (posye9>=240))or((posye9>=460) and (posye9<=530))or((posye9<=230) and (posye9>=80))) and (posxe9<0):
            posxe9=800
            if(posye9>=460) and (posye9<=530):
                posye9=210
                puntaje(-100)
                if parejas==True:
                    puntajel(-100)
            elif(posye9<=230) and (posye9>=80):
                posye9=520
        if ((posye9==420)and(((posxe9>=300)and(posxe9<=500)))):
            posye9=520
            enemy14=canvas.create_image(posxe9,posye9, image=enemy1)
        elif ((posye9==310)and(((posxe9>=580)or(posxe9<=220)))):
            posye9=420
            enemy14=canvas.create_image(posxe9,posye9, image=enemy1)
        elif ((posye9==210)and(((posxe9>=330)and(posxe9<=480)))):
            posye9=310
            enemy14=canvas.create_image(posxe9,posye9, image=enemy1)
        else:
            enemy14=canvas.create_image(posxe9,posye9, image=enemy1)
        v.after(10,mover9)
def mover10():
    """
esta funcion realiza el movimiento de un enemigo, haciendo tambien la simulacion de mapa continuo en este y los diferentes tipos de colisiones que puede tener desde matar
a mario y morir a manos de este
    """
    global posxe10,enemy16,posye10,posym,posxm,estadoe10,vida3,vida1,vida2,counterym,posxl,posyl,counteryl,vida31,vida11,vida21,parejas
    canvas.delete(enemy16)
    posxe10=posxe10+1
    if ((posxm<=(posxe10+30))and(posxm>=(posxe10-30)))and((posym==(posye10+50))or(posym==(posye10-45))):
        estadoe10=0
        puntaje(100)
        empezar()
    if (((posxm<=(posxe10+30))and(posxm>=(posxe10-30)))and(posym==posye10))and (counterym==0):
        posxm = 400
        posym = 520
        quitarvida()
    if ((posxl<=(posxe10+30))and(posxl>=(posxe10-30)))and((posyl==(posye10+50))or(posyl==(posye10-45))):
        estadoe10=0
        puntajel(100)
        empezar()
    if (((posxl<=(posxe10+30))and(posxl>=(posxe10-30)))and(posyl==posye10))and (counteryl==0):
        posxl = 400
        posyl = 520
        quitarvidal()
    if estadoe10!=0:    
        if (((posye10<=440) and (posye10>=240))or((posye10>=460) and (posye10<=530))or((posye10<=230) and (posye10>=80))) and (posxe10>800):
            posxe10=0
            if(posye10>=460) and (posye10<=530):
                posye10=210
                puntaje(-100)
                if parejas==True:
                    puntajel(-100)
            elif(posye10<=230) and (posye10>=80):
                posye10=520
        if ((posye10==420)and(((posxe10>=300)and(posxe10<=500)))):
            posye10=520
            enemy16=canvas.create_image(posxe10,posye10, image=enemy2)
        elif ((posye10==310)and(((posxe10>=580)or(posxe10<=220)))):
            posye10=420
            enemy16=canvas.create_image(posxe10,posye10, image=enemy2)
        elif ((posye10==210)and(((posxe10>=330)and(posxe10<=480)))):
            posye10=310
            enemy16=canvas.create_image(posxe10,posye10, image=enemy2)
        else:
            enemy16=canvas.create_image(posxe10,posye10, image=enemy2)
        v.after(10,mover10)
def mover11():
    """
esta funcion realiza el movimiento de un enemigo, haciendo tambien la simulacion de mapa continuo en este y los diferentes tipos de colisiones que puede tener desde matar
a mario y morir a manos de este
    """
    global posxe11,enemy17,posye11,posym,posxm,estadoe11,vida3,vida1,vida2,counterym,posxl,posyl,counteryl,vida31,vida11,vida21,parejas
    canvas.delete(enemy17)
    posxe11=posxe11+1
    if ((posxm<=(posxe11+30))and(posxm>=(posxe11-30)))and((posym==(posye11+50))or(posym==(posye11-45))):
        estadoe11=0
        puntaje(100)
        empezar()
    if (((posxm<=(posxe11+30))and(posxm>=(posxe11-30)))and(posym==posye11))and (counterym==0):
        posxm = 400
        posym = 520
        quitarvida()
    if ((posxl<=(posxe11+30))and(posxl>=(posxe11-30)))and((posyl==(posye11+50))or(posyl==(posye11-45))):
        estadoe11=0
        puntajel(100)
        empezar()
    if (((posxl<=(posxe11+30))and(posxl>=(posxe11-30)))and(posyl==posye11))and (counteryl==0):
        posxl = 400
        posyl = 520
        quitarvidal()
    if estadoe11!=0:    
        if (((posye11<=440) and (posye11>=240))or((posye11>=460) and (posye11<=530))or((posye11<=230) and (posye11>=80))) and (posxe11>800):
            posxe11=0
            if(posye11>=460) and (posye11<=530):
                posye11=210
                puntaje(-100)
                if parejas==True:
                    puntajel(-100)
            elif(posye11<=230) and (posye11>=80):
                posye11=520
        if ((posye11==420)and(((posxe11>=300)and(posxe11<=500)))):
            posye11=520
            enemy17=canvas.create_image(posxe11,posye11, image=enemy2)
        elif ((posye11==310)and(((posxe11>=580)or(posxe11<=220)))):
            posye11=420
            enemy17=canvas.create_image(posxe11,posye11, image=enemy2)
        elif ((posye11==210)and(((posxe11>=330)and(posxe11<=480)))):
            posye11=310
            enemy17=canvas.create_image(posxe11,posye11, image=enemy2)
        else:
            enemy17=canvas.create_image(posxe11,posye11, image=enemy2)
        v.after(10,mover11)
def mover12():
    """
esta funcion realiza el movimiento de un enemigo, haciendo tambien la simulacion de mapa continuo en este y los diferentes tipos de colisiones que puede tener desde matar
a mario y morir a manos de este
    """
    global posxe12,nube14,posye12,posym,posxm,estadoe12,vida3,vida1,vida2,counterym,posxl,posyl,counteryl,vida31,vida11,vida21,parejas
    canvas.delete(nube14)
    posxe12=posxe12-1
    if ((posxm<=(posxe12+30))and(posxm>=(posxe12-30)))and((posym==(posye12+50))or(posym==(posye12-45))):
        estadoe12=0
        puntaje(150)
        empezar()
    if (((posxm<=(posxe12+30))and(posxm>=(posxe12-30)))and(posym==posye12))and (counterym==0):
        posxm = 400
        posym = 520
        quitarvida()
    if ((posxl<=(posxe12+30))and(posxl>=(posxe12-30)))and((posyl==(posye12+50))or(posyl==(posye12-45))):
        estadoe12=0
        puntajel(150)
        empezar()
    if (((posxl<=(posxe12+30))and(posxl>=(posxe12-30)))and(posyl==posye12))and (counteryl==0):
        posxl = 400
        posyl = 520
        quitarvidal()
    if estadoe12!=0:
        if (((posye12<=440) and (posye12>=240))or((posye12>=460) and (posye12<=530))or((posye12<=230) and (posye12>=80))) and (posxe12<0):
            posxe12=800
            if(posye12>=460) and (posye12<=530):
                posye12=210
                puntaje(-100)
                if parejas==True:
                    puntajel(-100)
            elif(posye12<=230) and (posye12>=80):
                posye12=520
        if ((posye12==420)and(((posxe12>=300)and(posxe12<=500)))):
            posye12=520
            nube14=canvas.create_image(posxe12,posye12, image=nube1)
        elif ((posye12==310)and(((posxe12>=580)or(posxe12<=220)))):
            posye12=420
            nube14=canvas.create_image(posxe12,posye12, image=nube1)
        elif ((posye12==210)and(((posxe12>=330)and(posxe12<=480)))):
            posye12=310
            nube14=canvas.create_image(posxe12,posye12, image=nube1)
        else:
            nube14=canvas.create_image(posxe12,posye12, image=nube1)
        v.after(10,mover12)
def mover13():
    """
esta funcion realiza el movimiento de un enemigo, haciendo tambien la simulacion de mapa continuo en este y los diferentes tipos de colisiones que puede tener desde matar
a mario y morir a manos de este
    """
    global posxe13,nube15,posye13,posym,posxm,estadoe13,vida3,vida1,vida2,counterym,posxl,posyl,counteryl,vida31,vida11,vida21,parejas
    canvas.delete(nube15)
    posxe13=posxe13-1
    if ((posxm<=(posxe13+30))and(posxm>=(posxe13-30)))and((posym==(posye13+50))or(posym==(posye13-45))):
        estadoe13=0
        puntaje(150)
        empezar()
    if (((posxm<=(posxe13+30))and(posxm>=(posxe13-30)))and(posym==posye13))and (counterym==0):
        posxm = 400
        posym = 520
        quitarvida()
    if ((posxl<=(posxe13+30))and(posxl>=(posxe13-30)))and((posyl==(posye13+50))or(posyl==(posye13-45))):
        estadoe13=0
        puntajel(150)
        empezar()
    if (((posxl<=(posxe13+30))and(posxl>=(posxe13-30)))and(posyl==posye13))and (counteryl==0):
        posxl = 400
        posyl = 520
        quitarvidal()
    if estadoe13!=0:    
        if (((posye13<=440) and (posye13>=240))or((posye13>=460) and (posye13<=530))or((posye13<=230) and (posye13>=80))) and (posxe13<0):
            posxe13=800
            if(posye13>=460) and (posye13<=530):
                puntaje(-100)
                if parejas==True:
                    puntajel(-100)
                posye13=210
            elif(posye13<=230) and (posye13>=80):
                posye13=520
        if ((posye13==420)and(((posxe13>=300)and(posxe13<=500)))):
            posye13=520
            nube15=canvas.create_image(posxe13,posye13, image=nube1)
        elif ((posye13==310)and(((posxe13>=580)or(posxe13<=220)))):
            posye13=420
            nube15=canvas.create_image(posxe13,posye13, image=nube1)
        elif ((posye13==210)and(((posxe13>=330)and(posxe13<=480)))):
            posye13=310
            nube15=canvas.create_image(posxe13,posye13, image=nube1)
        else:
            nube15=canvas.create_image(posxe13,posye13, image=nube1)
        v.after(10,mover13)
def mover14():
    """
esta funcion realiza el movimiento de un enemigo, haciendo tambien la simulacion de mapa continuo en este y los diferentes tipos de colisiones que puede tener desde matar
a mario y morir a manos de este
    """
    global posxe14,nube16,posye14,posym,posxm,estadoe14,vida3,vida1,vida2,counterym,posxl,posyl,counteryl,vida31,vida11,vida21,parejas
    canvas.delete(nube16)
    posxe14=posxe14+1
    if ((posxm<=(posxe14+30))and(posxm>=(posxe14-30)))and((posym==(posye14+50))or(posym==(posye14-45))):
        estadoe14=0
        puntaje(150)
        empezar()
    if (((posxm<=(posxe14+30))and(posxm>=(posxe14-30)))and(posym==posye14))and (counterym==0):
        posxm = 400
        posym = 520
        quitarvida()
    if ((posxl<=(posxe14+30))and(posxl>=(posxe14-30)))and((posyl==(posye14+50))or(posyl==(posye14-45))):
        estadoe14=0
        puntajel(150)
        empezar()
    if (((posxl<=(posxe14+30))and(posxl>=(posxe14-30)))and(posyl==posye14))and (counteryl==0):
        posxl = 400
        posyl = 520
        quitarvidal()
    if estadoe14!=0:    
        if (((posye14<=440) and (posye14>=240))or((posye14>=460) and (posye14<=530))or((posye14<=230) and (posye14>=80))) and (posxe14>800):
            posxe14=0
            if(posye14>=460) and (posye14<=530):
                puntaje(-100)
                if parejas==True:
                    puntajel(-100)
                posye14=210
            elif(posye14<=230) and (posye14>=80):
                posye14=520
        if ((posye14==420)and(((posxe14>=300)and(posxe14<=500)))):
            posye14=520
            nube16=canvas.create_image(posxe14,posye14, image=nube2)
        elif ((posye14==310)and(((posxe14>=580)or(posxe14<=220)))):
            posye14=420
            nube16=canvas.create_image(posxe14,posye14, image=nube2)
        elif ((posye14==210)and(((posxe14>=330)and(posxe14<=480)))):
            posye14=310
            nube16=canvas.create_image(posxe14,posye14, image=nube2)
        else:
            nube16=canvas.create_image(posxe14,posye14, image=nube2)
        v.after(10,mover14)
def mover15():
    """
esta funcion realiza el movimiento de un enemigo, haciendo tambien la simulacion de mapa continuo en este y los diferentes tipos de colisiones que puede tener desde matar
a mario y morir a manos de este
    """
    global posxe15,nube17,posye15,posym,posxm,estadoe15,vida3,vida1,vida2,counterym,posxl,posyl,counteryl,vida31,vida11,vida21,parejas
    canvas.delete(nube17)
    posxe15=posxe15+1
    if ((posxm<=(posxe15+30))and(posxm>=(posxe15-30)))and((posym==(posye15+50))or(posym==(posye15-45))):
        estadoe15=0
        puntaje(150)
        empezar()
    if (((posxm<=(posxe15+30))and(posxm>=(posxe15-30)))and(posym==posye15))and (counterym==0):
        posxm = 400
        posym = 520
        quitarvida()
    if ((posxl<=(posxe15+30))and(posxl>=(posxe15-30)))and((posyl==(posye15+50))or(posyl==(posye15-45))):
        estadoe15=0
        puntajel(150)
        empezar()
    if (((posxl<=(posxe15+30))and(posxl>=(posxe15-30)))and(posyl==posye15))and (counteryl==0):
        posxl = 400
        posyl = 520
        quitarvidal()
    if estadoe15!=0:    
        if (((posye15<=440) and (posye15>=240))or((posye15>=460) and (posye15<=530))or((posye15<=230) and (posye15>=80))) and (posxe15>800):
            posxe15=0
            if(posye15>=460) and (posye15<=530):
                puntaje(-100)
                if parejas==True:
                    puntajel(-100)
                posye15=210
            elif(posye15<=230) and (posye15>=80):
                posye15=520
        if ((posye15==420)and(((posxe15>=300)and(posxe15<=500)))):
            posye15=520
            nube17=canvas.create_image(posxe15,posye15, image=nube2)
        elif ((posye15==310)and(((posxe15>=580)or(posxe15<=220)))):
            posye15=420
            nube17=canvas.create_image(posxe15,posye15, image=nube2)
        elif ((posye15==210)and(((posxe15>=330)and(posxe15<=480)))):
            posye15=310
            nube17=canvas.create_image(posxe15,posye15, image=nube2)
        else:
            nube17=canvas.create_image(posxe15,posye15, image=nube2)
        v.after(10,mover15)
def ganar():
    """
funcion que da por terminado el juego al haber ganado y dando como ultima opcion el salir de este
    """
    global v,final,finall
    final=0
    finall=0
    v.withdraw
    h=tkinter.Toplevel(v)
    canvas3 = tkinter.Canvas(h,width=600,height=450)
    gb=tkinter.PhotoImage(file='won.png')
    canvas3.create_image(300,225, image=gb)
    canvas3.focus_set()
    canvas3.pack()
    salir=tkinter.Button(h,text="Salir",font=("Agency FB",30),command=v.destroy,width=10,height=(1),bg=("blue"),fg=("white"))
    salir.place(x=325,y=225)
    h.resizable(0,0)
    h.mainloop()
def empezar():
    """
esta funcion es la superior a todas las que realizan el movimiento de los enemigos, ya que esta da las direcctrices basadas en el nivel en el que se encuentra siendo estos ultimos
son reglamentados por el puntaje actual del jugador
    """
    global nivel,posxe,posye,estadoe,posxe1,posye1,estadoe1,posxe2,posye2,estadoe2,posxe3,posye3,estadoe3,posxe4,posye4,estadoe4,posxe5,posye5,estadoe5,posxe6,posye6,estadoe6,posxe7,posye7,estadoe7,posxe8,posye8,estadoe8,posxe9,posye9,estadoe9,posxe10,posye10,estadoe10,posxe11,posye11,estadoe11,posxe12,posye12,estadoe12,posxe13,posye13,estadoe13,posxe14,posye14,estadoe14,posxe15,posye15,estadoe15,posxe16,posye16,estadoe16
    if nivel==0:
        v.after(10,mover)
        v.after(1000,mover1)
        v.after(10,mover2)
        v.after(1000,mover3)
        nivel=1
    if nivel>=1:
        if estadoe==0:
            posxe=790
            posye=210
            estadoe=1
        if estadoe1==0:
            posxe1=790
            posye1=210
            estadoe1=1
        if estadoe2==0:
            posxe2=20
            posye2=210
            estadoe2=1
        if estadoe3==0:
            posxe3=20
            posye3=210
            estadoe3=1
        if points>=2000 and nivel==1:
            v.after(20,mover4)
            v.after(1000,mover5)
            v.after(20,mover6)
            v.after(1000,mover7)
            nivel=2
    if nivel>=2:
        if estadoe4==0:
            posxe4=790
            posye4=210
            estadoe=1
        if estadoe5==0:
            posxe5=790
            posye5=210
            estadoe5=1
        if estadoe6==0:
            posxe6=20
            posye6=210
            estadoe6=1
        if estadoe7==0:
            posxe7=20
            posye7=210
            estadoe7=1
        if points>=4000 and nivel==2:
            v.after(20,mover8)
            v.after(1000,mover9)
            v.after(20,mover10)
            v.after(1000,mover11)
            nivel=3
    if nivel>=3:
        if estadoe8==0:
            posxe8=790
            posye8=210
            estadoe8=1
        if estadoe9==0:
            posxe9=790
            posye9=210
            estadoe9=1
        if estadoe10==0:
            posxe10=20
            posye10=210
            estadoe10=1
        if estadoe11==0:
            posxe11=20
            posye11=210
            estadoe11=1
        if points>=6000 and nivel==3:
            v.after(20,mover12)
            v.after(1000,mover13)
            v.after(20,mover14)
            v.after(1000,mover15)
            nivel=4
    if nivel>=4:
        if estadoe12==0:
            posxe12=790
            posye12=210
            estadoe12=1
        if estadoe13==0:
            posxe13=790
            posye13=210
            estadoe13=1
        if estadoe14==0:
            posxe14=20
            posye14=210
            estadoe14=1
        if estadoe15==0:
            posxe15=20
            posye15=210
            estadoe15=1
    if points>=8000 and nivel==4:
        nivel=5
    if points>=10000 and nivel==5:
        nivel=6
    if points>=12000 and nivel==6:
        ganar()
    muestran=tkinter.Label(v,font=("Arial"),text=nivel,width=10,bd=5,bg=("black"),fg=("white"))
    muestran.place(x=350,y=30)
            
            
def puntaje(b):
    """
funcion que con base en la muerte de un enemigo suma el puntaje que puede dar ese enemigo a el puntaje actual del jugador representandolo en un label en pantalla y que en caso
de que este puntaje sea u multiplo de cierto numero llamara a la funcion que da una vida
    """
    global points,estadov1,estadov2,estadov3,nivel
    points=points+b
    score=tkinter.Label(v,font=("Arial"),text=str(points),width=20,bg=("black"),fg=("white"))
    score.place(x=0,y=50)
    muestran=tkinter.Label(v,font=("Arial"),text=nivel,width=10,bd=5,bg=("black"),fg=("white"))
    muestran.place(x=350,y=30)
    if points%2000==0:
        darvida()
def puntajel(b):
    """
funcion que con base en la muerte de un enemigo suma el puntaje que puede dar ese enemigo a el puntaje actual del jugador representandolo en un label en pantalla y que en caso
de que este puntaje sea u multiplo de cierto numero llamara a la funcion que da una vida
    """
    global pointsl,estadov11,estadov21,estadov31,nivel
    pointsl=pointsl+b
    scorel=tkinter.Label(v,font=("Arial"),text=str(pointsl),width=20,bg=("black"),fg=("white"))
    scorel.place(x=600,y=50)
    muestran1=tkinter.Label(v,font=("Arial"),text=nivel,width=10,bd=5,bg=("black"),fg=("white"))
    muestran1.place(x=350,y=30)
    if pointsl%2000==0:
        darvidal()
def darvida():
    """
funcion que interactua con los labels que representan las vidas, entregando una en tal caso de que le falte, en caso de tener las vidas completas, la vida que se iba a
entregar se pierde
    """
    global vida1,vida3,vida2,estadov1,estadov2,estadov3
    if (estadov3==0)and((estadov2==1)and(estadov3==1)):
        vida3=tkinter.Label(v,image=life,width=50,bg=("black"),fg=("white"))
        vida3.place(x=300,y=0)
        estadov3=1
    elif (estadov1==1)and((estadov3==0)and(estadov2==0)):
        vida2=tkinter.Label(v,image=life,width=50,bg=("black"),fg=("white"))
        vida2.place(x=250,y=0)
        estadov2=1
    elif ((estadov1==0)and(estadov3==0)and(estadov2==0)):
        vida1=tkinter.Label(v,image=life,width=50,bg=("black"),fg=("white"))
        vida1.place(x=200,y=0)
        estadov1=1
def darvidal():
    """
funcion que interactua con los labels que representan las vidas, entregando una en tal caso de que le falte, en caso de tener las vidas completas, la vida que se iba a
entregar se pierde
    """
    global vida11,vida31,vida21,estadov11,estadov21,estadov31
    if (estadov31==0)and((estadov21==1)and(estadov31==1)):
        vida31=tkinter.Label(v,image=life,width=50,bg=("black"),fg=("white"))
        vida31.place(x=500,y=0)
        estadov31=1
    elif (estadov11==1)and((estadov31==0)and(estadov2==0)):
        vida21=tkinter.Label(v,image=life,width=50,bg=("black"),fg=("white"))
        vida21.place(x=550,y=0)
        estadov21=1
    elif ((estadov11==0)and(estadov31==0)and(estadov21==0)):
        vida11=tkinter.Label(v,image=life,width=50,bg=("black"),fg=("white"))
        vida11.place(x=600,y=0)
        estadov11=1
def gameover():
    """
funcion que da por terminado el juego al haber perdido y dando como ultima opcion el salir de este
    """
    global v
    v.withdraw
    h=tkinter.Toplevel(v)
    canvas3 = tkinter.Canvas(h,width=800,height=450)
    gb=tkinter.PhotoImage(file='gameover.png')
    canvas3.create_image(400,225, image=gb)
    canvas3.focus_set()
    canvas3.pack()
    salir=tkinter.Button(h,text="Salir",font=("Agency FB",30),command=v.destroy,width=15,height=(1),bg=("black"),fg=("white"))
    salir.place(x=285,y=300)
    h.resizable(0,0)
    h.mainloop()
def quitarvida():
    """
funcion que interactua con los labels que representan las vidas, quitando una en tal caso de que haya muerto algun personaje, al ya no tener mas vidas que quitar se determina
que ha perdido el juego
    """
    global estadov3,estadov2,estadov1,vida3,vida1,vida2,lemario,canvas,estadov31,estadov21,estadov11,vida31,vida11,vida21,lemario,leluigi,final,finall,both
    canvas.delete(lemario)
    if ((estadov1==1)and(estadov3==1)and(estadov2==1)):
        vida3.destroy()
        estadov3=0
        lemario=canvas.create_image(posxm,posym, image=mario1)
    elif (estadov3==0)and(estadov2==1):
        vida2.destroy()
        estadov2=0
        lemario=canvas.create_image(posxm,posym, image=mario1)
    elif (estadov3==0)and(estadov2==0)and(estadov1==1):
        vida1.destroy()
        estadov1=0
        lemario=canvas.create_image(posxm,posym, image=mario1)
    elif ((estadov3==0)and(estadov2==0)and(estadov1==0))and(final==0):
        if parejas==False:
            final=1
            gameover()
        else:
            final=1
    if (final==1 and finall==1)and (parejas==True)and(both==0):
        both=1
        gameover()
def quitarvidal():
    """
funcion que interactua con los labels que representan las vidas, quitando una en tal caso de que haya muerto algun personaje, al ya no tener mas vidas que quitar se determina
que ha perdido el juego
    """
    global estadov31,estadov21,estadov11,vida31,vida11,vida21,lemario,canvas,leluigi,estadov3,estadov2,estadov1,vida3,vida1,vida2,final,finall,both
    canvas.delete(leluigi)
    if parejas==True:
        if ((estadov11==1)and(estadov31==1)and(estadov21==1)):
            vida31.destroy()
            estadov31=0
            leluigi=canvas.create_image(posxl,posyl, image=luigi1)
        elif (estadov31==0)and(estadov21==1):
            vida21.destroy()
            estadov21=0
            leluigi=canvas.create_image(posxl,posyl, image=luigi1)
        elif (estadov31==0)and(estadov21==0)and(estadov11==1):
            vida11.destroy()
            estadov11=0
            leluigi=canvas.create_image(posxl,posyl, image=luigi1)
        elif ((estadov31==0)and(estadov21==0)and(estadov11==0))and(finall==0):
            finall=1
        if (final==1 and finall==1)and (parejas==True)and(both==0):
            both=1
            gameover()
v.withdraw()
def menu():
    """
    esta funcion despliega el menu como toplevel del juego
    """
    global v,nombre1,nombre2,vida1,vida3,vida2,vida11,vida31,vida21,estadov3,estadov2,estadov1,estadov31,estadov21,estadov11
    m=tkinter.Toplevel(v)
    canvas1 = tkinter.Canvas(m,width=800,height=630)
    menu=tkinter.PhotoImage(file='menu.png')
    canvas1.create_image(400,315, image=menu)
    canvas1.focus_set()
    canvas1.pack()
    def nombres1():
        """
    esta funcion despliega la pantalla para el ingreso de el nombre de un jugador como toplevel del juego
        """
        global v
        m.withdraw()
        n=tkinter.Toplevel(v)
        canvas2 = tkinter.Canvas(n,width=800,height=630)
        nombres=tkinter.PhotoImage(file='N1.png')
        canvas2.create_image(400,315, image=nombres)
        canvas2.focus_set()
        canvas2.pack()
        def juego2():
            """
    esta funcion inicia el juego en el modo un jugador
            """
            nombre1=str(jugador1.get())
            muestra1=tkinter.Label(v,font=("Arial"),text=nombre1,width=20,bg=("black"),fg=("white"))
            muestra1.place(x=0,y=0)
            vida1.place(x=200,y=0)
            estadov1=1
            vida2.place(x=250,y=0)
            estadov2=1
            vida3.place(x=300,y=0)
            estadov3=1
            v.iconify()
            n.withdraw()
            muestran1=tkinter.Label(v,font=("Arial"),text="NIVEL:",width=10,bd=5,bg=("black"),fg=("white"))
            muestran1.place(x=350,y=0)
            muestran=tkinter.Label(v,font=("Arial"),text=nivel,width=10,bd=5,bg=("black"),fg=("white"))
            muestran.place(x=350,y=30)
            nombres=[nombre1]
            archivo=open('unjugadorg.txt','w')
            archivo.writelines(nombres)     
            archivo.close()
            empezar()
        def atras():
            """
    esta funcion nos devuelve al menu desde cualquier pantalla donde se ingresan los nombres
            """
            n.withdraw()
            m.iconify()
        jugar=tkinter.Button(n,text="jugar",font=("Agency FB",30),command=juego2,width=10,height=(1),bg=("black"),fg=("white"))
        jugar.place(x=315,y=500)
        jugador1=tkinter.Entry(n,font=("Arial"),width=50,bd=5,bg=("black"),fg=("white"))
        jugador1.place(x=230,y=185)
        atras=tkinter.Button(n,image=goback,command=atras,width=20,height=(20),bg=("black"),fg=("white"))
        atras.place(x=0,y=0)
        n.resizable(0,0)
        n.mainloop()
    def nombres2():
        """
    esta funcion despliega la pantalla para el ingreso de el nombre de dos jugadores como toplevel del juego
        """
        global v,parejas
        parejas=True
        m.withdraw()
        n=tkinter.Toplevel(v)
        canvas2 = tkinter.Canvas(n,width=800,height=630)
        nombres=tkinter.PhotoImage(file='N.png')
        canvas2.create_image(400,315, image=nombres)
        canvas2.focus_set()
        canvas2.pack()
        def juego2():
            """
    esta funcion inicia el juego en el modo dos jugadores
            """
            nombre1=str(jugador1.get())
            nombre2=str(jugador2.get())
            muestra1=tkinter.Label(v,font=("Arial"),text=nombre1,width=20,bg=("black"),fg=("white"))
            muestra1.place(x=0,y=0)
            muestra2=tkinter.Label(v,font=("Arial"),text=nombre2,width=20,bd=5,bg=("black"),fg=("white"))
            muestra2.place(x=610,y=0)
            vida1=tkinter.Label(v,image=life,width=50,bg=("black"),fg=("white"))
            vida1.place(x=150,y=0)
            estadov1=1
            vida2=tkinter.Label(v,image=life,width=50,bg=("black"),fg=("white"))
            vida2.place(x=200,y=0)
            estadov2=1
            vida3=tkinter.Label(v,image=life,width=50,bg=("black"),fg=("white"))
            vida3.place(x=250,y=0)
            estadov3=1
            vida11=tkinter.Label(v,image=life,width=50,bg=("black"),fg=("white"))
            vida11.place(x=600,y=0)
            estadov11=1
            vida21=tkinter.Label(v,image=life,width=50,bg=("black"),fg=("white"))
            vida21.place(x=550,y=0)
            estadov21=1
            vida31=tkinter.Label(v,image=life,width=50,bg=("black"),fg=("white"))
            vida31.place(x=500,y=0)
            estadov31=1
            muestran1=tkinter.Label(v,font=("Arial"),text="NIVEL:",width=10,bd=5,bg=("black"),fg=("white"))
            muestran1.place(x=350,y=0)
            muestran=tkinter.Label(v,font=("Arial"),text=nivel,width=10,bd=5,bg=("black"),fg=("white"))
            muestran.place(x=350,y=30)
            nombres=[nombre1,"\n",nombre2]
            archivo=open('dosjugadorg.txt','w')
            archivo.writelines(nombres)     
            archivo.close()
            empezar()
            v.iconify()
            n.withdraw()
            empezar()
        def atras():
            """
    esta funcion nos devuelve al menu desde cualquier pantalla donde se ingresan los nombres
            """
            n.withdraw()
            m.iconify()
        jugador1=tkinter.Entry(n,font=("Arial"),width=50,bd=5,bg=("black"),fg=("white"))
        jugador1.place(x=230,y=185)
        jugador2=tkinter.Entry(n,font=("Arial"),width=50,bd=5,bg=("black"),fg=("white"))
        jugador2.place(x=230,y=300)
        jugar=tkinter.Button(n,text="jugar",font=("Agency FB",30),command=juego2,width=10,height=(1),bg=("black"),fg=("white"))
        jugar.place(x=315,y=500)
        atras=tkinter.Button(n,image=goback,command=atras,width=20,height=(20),bg=("black"),fg=("white"))
        atras.place(x=0,y=0)
        n.resizable(0,0)
        n.mainloop()
    def juego1():
        """
    esta funcion carga una partida existente de un jugador
        """
        archivo=open("unjugadorg.txt","r")
        datos=archivo.readlines()
        nombre1=datos[0]
        muestra1=tkinter.Label(v,font=("Arial"),text=nombre1,width=20,bg=("black"),fg=("white"))
        muestra1.place(x=0,y=0)
        estadov2=datos[4]
        estadov1=datos[3]
        estadov3=datos[5]
        if estadov1==1:
            vida1.place(x=200,y=0)
        if estadov2==1:
            vida2.place(x=250,y=0)
        if estadov3==1:
            vida3.place(x=300,y=0)
        muestran1=tkinter.Label(v,font=("Arial"),text="NIVEL:",width=10,bd=5,bg=("black"),fg=("white"))
        muestran1.place(x=350,y=0)
        puntaje(int(datos[1]))
        nivel=(datos[2])
        muestran=tkinter.Label(v,font=("Arial"),text=nivel,width=10,bd=5,bg=("black"),fg=("white"))
        muestran.place(x=350,y=30)
        v.iconify()
        m.withdraw()
        empezar()
        archivo.close()
    def juego3():
        """
    esta funcion carga una partida existente de dos jugadores
        """
        global v,parejas
        parejas=True
        archivo=open("dosjugadorg.txt","r")
        datos=archivo.readlines()
        nombre1=datos[0]
        muestra1=tkinter.Label(v,font=("Arial"),text=nombre1,width=20,bg=("black"),fg=("white"))
        muestra1.place(x=0,y=0)
        estadov2=datos[5]
        estadov1=datos[4]
        estadov3=datos[6]
        estadov21=datos[10]
        estadov11=datos[9]
        estadov31=datos[11]
        if estadov1==1:
            vida1.place(x=200,y=0)
        if estadov2==1:
            vida2.place(x=250,y=0)
        if estadov3==1:
            vida3.place(x=300,y=0)
        if estadov11==1:
            vida11.place(x=600,y=0)
        if estadov21==1:
            vida21.place(x=550,y=0)
        if estadov31==1:
            vida31.place(x=500,y=0)
        v.iconify()
        m.withdraw()
        muestran1=tkinter.Label(v,font=("Arial"),text="NIVEL:",width=10,bd=5,bg=("black"),fg=("white"))
        muestran1.place(x=350,y=0)
        puntaje(int(datos[2]))
        puntajel(int(datos[8]))
        nivel=(datos[3])
        muestran=tkinter.Label(v,font=("Arial"),text=nivel,width=10,bd=5,bg=("black"),fg=("white"))
        muestran.place(x=350,y=30)
        empezar()
        archivo.close()
    def control():
        """
    esta funcion despliega la pantalla para el ingreso de el nombre de dos jugadores como toplevel del juego
        """
        global v
        m.withdraw()
        n=tkinter.Toplevel(v)
        canvas2 = tkinter.Canvas(n,width=800,height=450)
        contro=tkinter.PhotoImage(file='controles.png')
        canvas2.create_image(400,225, image=contro)
        canvas2.focus_set()
        canvas2.pack()
        def atras():
            """
    esta funcion nos devuelve al menu desde cualquier desde donde se muestran 
            """
            n.withdraw()
            m.iconify()
        atras=tkinter.Button(n,image=goback,command=atras,width=20,height=(20),bg=("black"),fg=("white"))
        atras.place(x=0,y=0)
        n.resizable(0,0)
        n.mainloop()
    unjugador=tkinter.Button(m,text="Un Jugador",font=("Agency FB",30),command=nombres1,width=15,bg=("black"),fg=("white"))
    unjugador.place(x=0,y=315)
    COOP=tkinter.Button(m,text="Dos Jugadores",font=("Agency FB",30),command=nombres2,width=15,height=(1),bg=("black"),fg=("white"))
    COOP.place(x=280,y=315)
    cargar=tkinter.Button(m,text="Cargar Partida",font=("Agency FB",30),command=juego1,width=15,bg=("black"),fg=("white"))
    cargar.place(x=0,y=405)
    cargar2=tkinter.Button(m,text="Cargar Partida",font=("Agency FB",30),command=juego3,width=15,bg=("black"),fg=("white"))
    cargar2.place(x=280,y=405)
    controles=tkinter.Button(m,text="Controles",font=("Agency FB",30),command=control,width=15,height=(1),bg=("black"),fg=("white"))
    controles.place(x=565,y=315)
    salir=tkinter.Button(m,text="Salir",font=("Agency FB",30),command=v.destroy,width=15,height=(1),bg=("black"),fg=("white"))
    salir.place(x=565,y=405)
    m.resizable(0,0)
    m.mainloop()
menu()
v.resizable(0,0)
v.mainloop()
