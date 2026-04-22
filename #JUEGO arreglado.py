
# ~~~ nivel 1 ~~~

print("\n" + "="*50)
print(" 🧟‍♂️ Resident evil: mansion spencer ☣️")
print("="*50 + "\n")
print(" eres chris redfiel, un miembro de s.t.a.r.s estas en el comedor de una mansion que parece abandonada🏰.")
print("tu objetivo es encontrar y salvar a jill valentine, quien desaparecio investigando la mansion🚶‍♀️.")
print("🔦 tienes contigo una ganzua para abrir puertas, tu pistola y tu cuchillo de combate. 🔪\n")

decision1 = input("¿que preparas primero? ¿la GANZUA 🗝️ la PISTOLA 🔫 o el CUCHILLO 🔪? > ").lower()

if decision1 == "ganzua":
        
        # ~~~ nivel 2 (ruta de la ganzua) ~~~

        print("\n🗝️ usas la ganzua para abrir la puerta. en el pasillo hay tres caminos.🚪\n")
        print("⬅️uno va hacia la izquierda, elpasillo es oscuro y huele a humedad.\n➡️el otro va hacia la derecha, es un pasillo ancho y con sangre en el piso.\n")
        print("➡️el tercero va hacia arriba, es un pasillo estrecho con escaleras.\n")
        decision2 = input("¿que camino tomas? ¿IZQUIERDA ⬅️ o DERECHA ➡️ o ARRIBA ⬆️ ? > ").lower()

        if decision2 == "izquierda":

            # ~~~ nivel 3 (ruta de la izquierda) ~~~

            print("\n🚶‍♂️ el pasillo de la izquierda es angosto, escuchas gotas callendo del techo. 💧\n")
            print("🦠🧪 llegas a una enfermeria con un frasco de suero verde sobre la mesa.\n")
            print("😓 estas herido pero no sabes si el quimico es seguro.\.n")
            decision3 = input("que vas a hacer? ¿BEBER el suero 🧪, SEGUIR por la puerta 🚶‍♂️o CRUZAR la ventana? >").lower()

            if decision3 == "beber":

                # ~~~ nivel 4 ~~~

                print("\n el suero es una mezcla de hierbas medicinales. tus heridas cierran rapido. 💪🏼\n")
                print("👀 notas un interruptor oculto 🌫️\n")
                decision4 = input("¿vas a ENTRAR por el pasaje secreto 🚪 o IGNORARLO 🚶🏻‍♂️ y seguir adelante? > ").lower()

                if decision4 == "entrar":

                    # ~~~ nivel 5 () ~~~

                    print("\n🚪 el pasaje te lleva a un laboratorio subterraneo. encontraste al tyrant!☣️💀\n")
                    print(" la criatura esta en reposo dentro de un tanque 😴. es tu oportunidad de eliminarla.\n")
                    decision5 = input("¿donde disparas? apuntas a la CABEZA 🧠, al CORAZON 🫀 o a la COMPUTADORA 💻 > ").lower()

                    if decision5 == "computadora":

                        # ~~~ nivel 6 (Final) ~~~

                        print("\n💻 se sobrecarga el sistema de autodestruccion, el laboratorio explota con el tyrant dentro.💥\n")
                        print("🏆🎉 ¡GANASTE! lograste rescatar a  jill y escapar antes de la explosion. 🚁🎉\n")
                    elif decision5 == "cabeza":
                        print("\n intentas disparar a la cabeza, pero el cristal del tanque es blindado, el tyrant se despierta y te atraviesa con su garra. 💀\n")
                        print("☠️💀 Fin del juego. wesker se quedacon jill 😭 \n")
                    elif decision5 == "corazon":
                        print("\n tu ataque al corazon 🫀 no le hace nada. el monstruo rompe el tanque y te aplasta. 🧱\n")
                        print("☠️💀 Fin de Juego. eres una victima mas del virus 🦠 💀☠️\n")
                    else:
                        print("😵 respuesta invalida. el tyrant rompe el cristal y te mata por tu indecision. 🧟‍♂️☠️\n")

                elif decision4 == "ignorar":
                    print("\n decides que es muy arriesgado. sigues caminando🚶🏻‍♂️ pero te quedas sin balas en un pasillo sin salida.\n")
                    print("☠️💀 Fin del juego. los zombies te alcanzaron. 🧟‍♂️ ☠️☠️\n")
                else:
                    print("respuesta invalida. mientras dudas, un zombie salta del techo y te ataca. 💀\n")

            elif decision3 == "seguir":
                print("\n🚶‍♂️sigues por la puerta y llegas a un helicoptero pero lo ves y esta rodeado de cuervos infectados. 🐦‍⬛\n")
                print("☠️💀 Fin del juego. los cuervos te rodean y te caes al vacio. ☠️\n")
            elif decision3 == "cruzar":
                print("\n🏃‍♂️intentas pasar por la ventana pero caes en una zona llena de perros infectados. 🐕🦠\n")
                print("☠️💀 Fin del juego. eres comido por los perros.\n")
            else:
                print("😵 respuesta invalida, mientras piensas un zombie te muerde por la espalda.🧟‍♂️\n")

        elif decision2 == "derecha":

            # ~~~ nivel 3 (ruta de la derecha) ~~~

            print("\n➡️ el pasillo derecho huele a mierda. al fondo ves una luz roja. 🚨\n")
            print("🚨 es la alarma de seguridad, hay camaras vigilando 📹.\n")
            decision3 = input("que vas a hacer? ¿DESTRUYES las camaras 🔫 para avanzar. las IGNORAS o las USAS como distraccion? > ").lower()

            if decision3 == "destruyes":
                print("🔫 disparas a las camaras. un equipo de seguridad llga en segundos.\n")
                print("☠️💀💀 Fin del juego. te superaron en numero y armamento 💀💀☠️ \n")
            elif decision3 == "usas":
                print("\n💻 hackeas la señal de la camara. usas el ruido para llevar a los zombies a otra habitacion. 🚪\n")
                print(" mientras avanzas, encuentras a jill encerrada dn una celda.\n")
                print("abres la puerta 🚪 y sacas a jill, ambos lograron escapar antes del amanecer.🚁\n")
                print("🎉🏆 ¡HAS GANADO! rescataste a jill. 🎉🏆\n")
            elif decision3 == "ignoras":
                print("\n🚶‍♂️ decides que las camaras no son un riesgo. pero al pasar por debajo de una camara, esta detecta tu movimiento y activa la alarma. 🚨\n")
                print("☠️💀 Fin del juego. el ruido de la alarma atrajo a los zombies, te rodean y te eliminan. 🧟‍♂️\n")
            else:
                print("😵 respuesta invalida . la alarma se prende y los zombies te rodean. ☠️\n")
        elif decision2 == "arriba":
        
            # ~~~ nivel 3 (ruta de arriba) ~~~

            print("\n⬆️ subes las escaleras y llegas a un pasillo con ventanas y poco iluminado. \n")
            print("👀 ves una sombra moviendose por una ventana. 🧟‍♂️\n")
            decision3 = input("que vas a hacer? ¿intentas VER por la ventana 🕵️‍♂️, SIGUES por el pasillo 🚶🏻‍♂️ o ESPERAR que la sombra se vaya 🤫 ? > ").lower()

            if decision3 == "ver":
                print("\n🕵️‍♂️ te acercas a la ventana para ver mejor, pero unos kipepeo te ven y te atacan. 🧟‍♂️\n")
                print("☠️💀 Fin del juego. te arrancaron la cabeza  por curioso. 🧟‍♂️\n")

            elif decision3 == "sigues":
                print("\n🚶‍♂️ sigues por el pasillo y llegas a una biblioteca. encuentras un libro con un mapa de la mansion. 🗺️\n")
                print("el mapa te muestra una ruta de la celda donde esta jill y la salida de la mansion. 🏰\n")
                print("🏆🎉 ¡HAS GANADO! usaste tu ingenio para escapar de la mansion. 🎉🏆\n")

            elif decision3 == "esperar":
                print("\n🤫 esperas en silencio a que la sombra se vaya. 🧟‍♂️\n")
                print("☠️💀 Fin del juego. te atacan por la espalda mientras esperas. 🧟‍♂️\n")
        else:
            print("😵💀💀 respuesta invalida. te quedaste en el pasillo y los zombies llegaron, Fin del juego 🧟‍♂️💀 \n")

elif decision1 == "pistola":
        
        # ~~~ nivel 2 (ruta de la pistola) ~~~

        print("\n🔫 agarras tu pistola, pero te das cuenta que solo tienes 6 balas. 💀\n")
        print("👀 ves a un zombie acercandose por el pasillo. 🧟‍♂️\n")
        decision2 = input("decides DISPARAR al zombie 🔫, HUIR del zombie 🏃🏻‍♂️ o ESCONDERTE en una habitacion 🚪? > ").lower()

        if decision2 == "disparar":
            print("\n🔫 disparas al zombie, pero solo le das en el brazo. el zombie te alcanza y te ataca. 🧟‍♂️\n")
            print("☠️💀 Fin del juego. te quedaste sin balas y el zombie te mato. 🧟‍♂️\n")
        elif decision2 == "huir":
            print("\n🏃‍♂️ sales corriendo por el pasillo y llegas a una habitacion con un armario. 🚪\n")
            print("👀 ves a otro zombie entrando a la habitacion por la puerta de atras. 🧟‍♂️\n")
            decision3 = input("decides ESCONDERTE en el armario 🚪 o ENFRENTAR al zombie con tu cuchillo 🔪? > ").lower()

            if decision3 == "esconderte":
                print("\n🚪 te metes al armario y cierras la puerta. el zombie entra a la habitacion y no te ve 👀.\n")
                print("esperas unos minutos hasta que el zombie se va. 🧟‍♂️\n")
                print("🏆🎉 ¡HAS GANADO! lograste escapar del zombie sin usar tus balas, encontraste a jill y escapaste de la mansion. 🎉🏆\n")
            elif decision3 == "enfrentar":
                print("\n🔪 sales del armario para enfrentar al zombie, pero no viste que habia otro detras de ti. 💀\n")
                print("☠️💀 Fin del juego. los zombies te rodean y te eliminan. 🧟‍♂️\n")
            else:
                print("😵 respuesta invalida, mientras dudas los zombies te atacan por la espalda. 🧟‍♂️\n")

elif decision1 == "cuchillo":
        
        # ~~~ nivel 2 (ruta del cuchillo) ~~~
        
        print("\n🔪 agarras el cuchillo. avanzas en silencio🚶‍♂️.\n")
        print("🧟‍♂️ sientes una presencia detras de tu y escuchas un chasqueo de dientes 💀\n")
        decision2 = input("decides AVANZAR hacia el ruido 🏃🏻‍♂️, HUIR del ruido o ESPERAR en silencio 🤫 ? > ").lower()

        if decision2 == "avanzar":
            print("\n🏃‍♂️ corrs hacia el origen del sonido. te encuentras de frente con el primer zombie de la mansion 🧟‍♂️.\n")
            print("el zombie te ve 👀 y sale corriendo hacia ti 💀🧟‍♂️\n")
            decision3 = input(" que vas a hacer ? ATACAS de frente 🔪, intentes HABLAR 🗣️ con el o te RETIRAS lentamente 🚶🏻‍♂️? > ").lower()

            if decision3 == "atacas":
                print("\n🔪 vas con el cuchillo, pero no viste que el suelo estana podrido. 💀\n")
                print("☠️💀 Fin del juego. caes en una trsmpa de puas.💀☠️\n")
            elif decision3 == "hablar":
                print("\n🗣️ intentas hable pero zombie no te para bola. 🧟‍♂️\n")
                print("casualmente aparece jill y le vuela la cabeza con su pistola 🔫\n")
                print("🏆🎉 ¡HAS GANADO! con la ayuda jill saliste de la mansion rapido. 🎉🏆\n")
            elif decision3 == "retiras":
                print("\n🚶🏻‍♂️ intentas retroceder, pero el zombie es mas raoido y te mata. 🧟‍♂️☠️ \n")
                print("☠️💀 Fin del juego. ¡webon! nunca le des la espalda a un zombie 🧟‍♂️.\n")
            else:
                print("😵 respuesta invslida. por tu indecision te rodean y te eliminan. 🧟‍♂️☠️\n")

        elif decision2 == "huir":
            print("\n🏃‍♂️ sales corriendo por el pasillo y llegas al comedor. otros zombies te escucharon y van tras de ti. !!! 🧟‍♂️\n")
            print("☠️💀 Fin del juego. te rodean y aceptas tu destino.🧟‍♂️.\n")
        
        elif decision2 == "esperar":
            print("\n🤫 esperas es las oscuridad, el zombie pasa de largo y no te ve 👀.\n")
            print("es tu oportunidad de revisar la oficina de wesker. 💻 🏰.\n")
            print("encuentras un disco con datos con evidencia en contra de umbrella  y una llave para salir. 🔑\n")
            print("🏆🎉 ¡HAS GANADO! tienes pruebas para hundir a la corporacion. 🎉🏆\n")
        else:
            print("😵 respuesta invalida, el miedo te vence y abandonas la mision. 💀\n")        
else:          
        print("😵 respuesta invalida, el miedo te vence y abandonas la mision. 💀\n")


