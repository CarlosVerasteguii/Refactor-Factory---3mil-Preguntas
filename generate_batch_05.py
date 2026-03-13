import json

questions = [
  {
    "id": "block-OPS400-M4-q081",
    "module_id": 4,
    "block_id": "OPS400-M4",
    "type": "options",
    "scenario": "Estás descargando un pedido frágil y escuchas un ruido a piezas rotas adentro de una caja flejada. El chofer del tráiler te urge a que le firmes de recibido para no perder su bono por tiempo de ruta.",
    "options_structured": {
      "integrity_correct": "Abro la caja frente a él para validar la merma exacta, aguantando que se desespere por la demora.",
      "pragmatic_distractor": "Sacudo la caja, la anoto como 'posible merma' en su guía y le firmo de volada para liberar el andén.",
      "evasive_distractor": "Le digo al chofer que le llame a su jefe de tráfico para que resuelvan ellos la incidencia de calidad.",
      "rationalized_distractor": "Recibo la caja normal, asumiendo que siempre hay un ajuste de merma válido por el movimiento natural del viaje."
    },
    "notes": "OPS400 Modulo 4 Options OPS400-M4 batch 05 item 1",
    "sot_checksum": "ops400_m4_options_v1"
  },
  {
    "id": "block-OPS400-M4-q082",
    "module_id": 4,
    "block_id": "OPS400-M4",
    "type": "options",
    "scenario": "Te toca armar una tarima altísima y el rollo de plástico para emplayar casi se acaba. Alcanza para darle una vuelta sencilla, pero la norma de carga pide tres pasadas para asegurar.",
    "options_structured": {
      "integrity_correct": "Voy a la bodega por un rollo nuevo para emplayar como debe ser, perdiendo ritmo de operación.",
      "pragmatic_distractor": "Le doy una sola vuelta bien estirada y le hago amarres fuertes en las orillas para que aguante el movimiento plano.",
      "evasive_distractor": "Le marco al supervisor para que él mande a un auxiliar con material nuevo hasta mi zona.",
      "rationalized_distractor": "La muevo así con una pasada, total la tarima solo se va a desplazar unos metros en piso de concreto liso."
    },
    "notes": "OPS400 Modulo 4 Options OPS400-M4 batch 05 item 2",
    "sot_checksum": "ops400_m4_options_v1"
  },
  {
    "id": "block-OPS400-M4-q083",
    "module_id": 4,
    "block_id": "OPS400-M4",
    "type": "options",
    "scenario": "El andén está bloqueado con dos camiones. Un proveedor de mucha confianza llega urgido y te propone bajar tres cajas chicas usando la rampa de emergencias peatonal para ahorrarse la fila.",
    "options_structured": {
      "integrity_correct": "Le niego el paso por esa escalera y lo hago formarse en la línea, soportando sus quejas de siempre.",
      "pragmatic_distractor": "Le pido que me acerque sus cajas a la orilla y se las bajo yo a mano para no hacerlo invadir la escalera.",
      "evasive_distractor": "Le digo al guardia externo que investigue si hay espacio libre en otro acceso para acomodar a ese proveedor.",
      "rationalized_distractor": "Lo dejo bajar rápido sus cajas por la rampa solo esta vez, para liberar a un transporte pesado de la fila."
    },
    "notes": "OPS400 Modulo 4 Options OPS400-M4 batch 05 item 3",
    "sot_checksum": "ops400_m4_options_v1"
  },
  {
    "id": "block-OPS400-M4-q084",
    "module_id": 4,
    "block_id": "OPS400-M4",
    "type": "options",
    "scenario": "Revisas la cámara fría media hora antes de tu salida y el termostato marca tres grados arriba del límite. Si das el aviso de riesgo térmico, tienes que quedarte a traspasar mercancía todo el cambio de turno.",
    "options_structured": {
      "integrity_correct": "Levanto el folio de alta temperatura y empiezo a reubicar el producto sensible, asumiendo quedarme horas extra.",
      "pragmatic_distractor": "Verifico que la cortina hawaiana presione bien y anoto la temperatura manual para volver a confirmar en diez minutos.",
      "evasive_distractor": "Le tomo una foto al lector del frío y la mando al grupo de mantenimiento, dejando que ellos valoren qué procede.",
      "rationalized_distractor": "Espero antes de actuar, porque cada vez que meten carga sube la aguja por la puerta abierta y luego baja sola."
    },
    "notes": "OPS400 Modulo 4 Options OPS400-M4 batch 05 item 4",
    "sot_checksum": "ops400_m4_options_v1"
  },
  {
    "id": "block-OPS400-M4-q085",
    "module_id": 4,
    "block_id": "OPS400-M4",
    "type": "options",
    "scenario": "Vas corriendo con una refacción clave que tiene parada la línea principal y descubres un charquito de aceite hidráulico en pleno cruce del pasillo. Limpiarlo tú mismo afecta directo la producción de toda la planta.",
    "options_structured": {
      "integrity_correct": "Me quedo bloqueando la mancha físicamente y pido aserrín por radio, aguantando que todo ensamblaje siga detenido.",
      "pragmatic_distractor": "Aviento un cartón amplio encima del charco para pisar seguro y corro a entregar la pieza urgente del motor.",
      "evasive_distractor": "Atravieso un patín amarillo frente a la mancha de paso y me arranco veloz a cumplir mi entrega primordial.",
      "rationalized_distractor": "Sigo directo a salvar la producción asumiendo que el charco brilla bastante y cualquiera con botas lo va a rodear."
    },
    "notes": "OPS400 Modulo 4 Options OPS400-M4 batch 05 item 5",
    "sot_checksum": "ops400_m4_options_v1"
  },
  {
    "id": "block-OPS400-M4-q086",
    "module_id": 4,
    "block_id": "OPS400-M4",
    "type": "options",
    "scenario": "Conduciendo por la zona industrial se desata una tormenta cerrada y tus limpiaparabrisas dejan de funcionar. La bodega del cliente, que te está cobrando tiempos muertos, está a sólo un kilómetro.",
    "options_structured": {
      "integrity_correct": "Me orillo totalmente con intermitentes hasta que baje el aguacero, asumiendo la multa de retraso del cliente.",
      "pragmatic_distractor": "Sigo avanzando por el acotamiento bajando un poco mi ventana para no perder por completo la visibilidad frontal.",
      "evasive_distractor": "Llamo al despachador de tráfico para que decida él si me autoriza jugármela para cumplir la entrega del día.",
      "rationalized_distractor": "Avanzo a 10 kilómetros por hora usando de guía las luces traseras rojas del tráiler de enfrente que va rompiendo el agua."
    },
    "notes": "OPS400 Modulo 4 Options OPS400-M4 batch 05 item 6",
    "sot_checksum": "ops400_m4_options_v1"
  },
  {
    "id": "block-OPS400-M4-q087",
    "module_id": 4,
    "block_id": "OPS400-M4",
    "type": "options",
    "scenario": "En la carretera, ves por el retrovisor que la chapa de tu puerta trasera saltó por un bache profundo y la puerta va medio abierta. Vas por el carril de alta velocidad rodeado de tráfico rápido.",
    "options_structured": {
      "integrity_correct": "Enciendo mis intermitentes y voy frenando poco a poco sobre mi línea hasta detener toda mi fila para poder asegurar la caja.",
      "pragmatic_distractor": "Voy cruzando diagonales lentas hacia la derecha esquivando camiones para parar en el acotamiento más adelante.",
      "evasive_distractor": "Mantengo mi velocidad constante hasta llegar al siguiente cruce con semáforo y bajarme rápido a la segura de un solo salto.",
      "rationalized_distractor": "Le acelero de forma pareja para que el propio aire empuje la puerta pesada hacia adentro sin soltar carga."
    },
    "notes": "OPS400 Modulo 4 Options OPS400-M4 batch 05 item 7",
    "sot_checksum": "ops400_m4_options_v1"
  },
  {
    "id": "block-OPS400-M4-q088",
    "module_id": 4,
    "block_id": "OPS400-M4",
    "type": "options",
    "scenario": "Al cruzar una caseta tu tag electrónico corporativo no se lee y la pluma no abre. Tienes cinco tráileres tocando el claxon atrás y sacar de tu cartera a veces la empresa no te lo devuelve.",
    "options_structured": {
      "integrity_correct": "Aguanto la presión del tráfico pesado parado frente a la pluma hasta que el enlace remoto de mi base me destrabe la cuenta.",
      "pragmatic_distractor": "Saco rápido mi efectivo para pagar y avanzar fluido, pensando en batallar después con mi ticket de reembolso justificado.",
      "evasive_distractor": "Le indico al de la caseta que reporte la falla en su escáner manual a sus supervisores de puente porque mi cuenta sí tiene crédito.",
      "rationalized_distractor": "Me echo poquito para atrás cuidando no pegar al torton de cola para tratar de meterme mejor por el sensor de la pluma vecina."
    },
    "notes": "OPS400 Modulo 4 Options OPS400-M4 batch 05 item 8",
    "sot_checksum": "ops400_m4_options_v1"
  },
  {
    "id": "block-OPS400-M4-q089",
    "module_id": 4,
    "block_id": "OPS400-M4",
    "type": "options",
    "scenario": "Te metes a una calle residencial estrecha y un coche de lujo muy mal estacionado te bloquea el paso entero. Si le doblas tantito a su retrovisor forzado, la camioneta lograría cruzar sin rayarlo.",
    "options_structured": {
      "integrity_correct": "Apago el motor y busco de puerta en puerta al dueño del sedán, asumiendo atorar mi ruta hasta que mueva el estorbo.",
      "pragmatic_distractor": "Bajo mi vidrio, le doblo con la mano su retrovisor a tope cerrándolo para pasar libre y lo dejo empujado a mi espalda.",
      "evasive_distractor": "Reporto calle intrasitable a la central para que me exoneren esa parada y me arranco para otra colonia dando vuelta larga atrás.",
      "rationalized_distractor": "Paso lentamente recargando apenas la lona sobre su espejo, confiando en que por la goma interna se flexiona y rebota ileso."
    },
    "notes": "OPS400 Modulo 4 Options OPS400-M4 batch 05 item 9",
    "sot_checksum": "ops400_m4_options_v1"
  },
  {
    "id": "block-OPS400-M4-q090",
    "module_id": 4,
    "block_id": "OPS400-M4",
    "type": "options",
    "scenario": "El receptor de mostrador finaliza la firma digital rápida sobre tus cajas cerradas sin abrir nada. Tú bien sabes que un aparato viene golpeado por dentro por un descuido nuestro en el apile del camión que nadie notó.",
    "options_structured": {
      "integrity_correct": "Le expongo franco el daño del aparato oculto parando la transacción final exponiendo mis números por devolución total cruda hoy.",
      "pragmatic_distractor": "Cierro rápido la bitácora electrónica de entregas pero le insisto muy amable en checar y guardar bien su comprobante de seguro físico para atención inmediata.",
      "evasive_distractor": "Miro para otro lado formalizando ruta normal pensando que almacenes garantía lidien más tarde su enojo técnico natural de fallas originarias.",
      "rationalized_distractor": "No levanto falsas alarmas inútiles considerando si el cliente ni le echó ni ojo a la inversión pagada no es mi obligación despertar panales ajenos dormidos tranquilos."
    },
    "notes": "OPS400 Modulo 4 Options OPS400-M4 batch 05 item 10",
    "sot_checksum": "ops400_m4_options_v1"
  },
  {
    "id": "block-OPS400-M4-q091",
    "module_id": 4,
    "block_id": "OPS400-M4",
    "type": "options",
    "scenario": "Trabajas en la faja transportadora y tu unidad de encendido saca unas chispas rojas leves cuando pasas el switch. La carga de paquetes se está amontonando muchísimo y si paras la banda detienes a todos los compañeros.",
    "options_structured": {
      "integrity_correct": "Apago el sistema completo y pido que revisen la conexión eléctrica, aunque se me junten todas las cajas paradas.",
      "pragmatic_distractor": "Le pongo cinta de aislar rápida alrededor del enchufe para que no haga falso contacto y prendo la banda de volada.",
      "evasive_distractor": "Le digo al compañero de la otra estación que mejor él jale mi carga manual hacia su lado mientras yo reporto la falla.",
      "rationalized_distractor": "Prendo la banda normal, porque casi siempre esas chispitas son pura estática inofensiva por la fricción continua de la faja."
    },
    "notes": "OPS400 Modulo 4 Options OPS400-M4 batch 05 item 11",
    "sot_checksum": "ops400_m4_options_v1"
  },
  {
    "id": "block-OPS400-M4-q092",
    "module_id": 4,
    "block_id": "OPS400-M4",
    "type": "options",
    "scenario": "Te prestan de otro lado un escáner especial, pero la pila se le apaga a cada rato si no le aprietas la tapa con el dedo. Tu jefe te presiona para que saques un pedido enorme en diez minutos.",
    "options_structured": {
      "integrity_correct": "Dejo de escanear y exijo que me cambien el equipo dañado, a sabiendas de que mi jefe me va a regañar por el retraso.",
      "pragmatic_distractor": "Le pego tres pedazos de cinta canela a la tapa para que la pila haga buena presión y saco el pedido sin detenerme.",
      "evasive_distractor": "Se lo devuelvo al coordinador para que él me consiga otro mientras yo me pongo a hacer puras labores de emplayado manual.",
      "rationalized_distractor": "Sigo trabajando sosteniendo la tapa con el dedo chiquito, porque en el piso uno siempre tiene que ingeniárselas con las herramientas que hay."
    },
    "notes": "OPS400 Modulo 4 Options OPS400-M4 batch 05 item 12",
    "sot_checksum": "ops400_m4_options_v1"
  },
  {
    "id": "block-OPS400-M4-q093",
    "module_id": 4,
    "block_id": "OPS400-M4",
    "type": "options",
    "scenario": "Estás bajando la cortina del almacén ya de noche y un instalador conocido llega a rogarte que le sueltes un tramo de cable importante. Ya tienes el candado puesto y el sistema de salidas bloqueado.",
    "options_structured": {
      "integrity_correct": "Le digo que por protocolo ya no puedo reabrir el almacén bajo ninguna circunstancia, aguantando su enojo porque le urge.",
      "pragmatic_distractor": "Le saco el cable apuntando la salida a mano en mi libreta para darle el alta formal al día siguiente a primera hora en la compu.",
      "evasive_distractor": "Le paso su contacto directo al guardia nocturno en turno para que él decida si le destraba las puertas avalado por la torre.",
      "rationalized_distractor": "Levanto un metro la cortina metálica despacito tirándole gratis el tramo indispensable priorizando su atención urgente de crisis pesada."
    },
    "notes": "OPS400 Modulo 4 Options OPS400-M4 batch 05 item 13",
    "sot_checksum": "ops400_m4_options_v1"
  },
  {
    "id": "block-OPS400-M4-q094",
    "module_id": 4,
    "block_id": "OPS400-M4",
    "type": "options",
    "scenario": "Haces tu corte de caja final y te sobra misteriosamente un billete de cien pesos intacto. Ningún cliente volvió a quejarse de su vuelto en todo el turno y ya están sellando la bóveda central de valores fuertes.",
    "options_structured": {
      "integrity_correct": "Reporto el dinero sobrante metiendo una incidencia manual al cierre, asumiendo que el descuadre me mancha el KPI formal del registro.",
      "pragmatic_distractor": "Lo dejo escondidito abajo un papel dentro de mi gaveta jurando regresarlo liso mañana que me reclame cualquier fiera persona triste cobrada.",
      "evasive_distractor": "Se los suelto ciego en la mano suelta a mi controladora líder que ella manipule saldos largos contables librando yo el desastroso reporte mío.",
      "rationalized_distractor": "Termino echando el cien al termo de juntitas de merienda para emparejar al mundo porque seguido toca fondear diferencias malas perdiéndole tú propio sueldo chico."
    },
    "notes": "OPS400 Modulo 4 Options OPS400-M4 batch 05 item 14",
    "sot_checksum": "ops400_m4_options_v1"
  },
  {
    "id": "block-OPS400-M4-q095",
    "module_id": 4,
    "block_id": "OPS400-M4",
    "type": "options",
    "scenario": "Acomodando tarimas, rompes un garrafón de limpiador industrial liso en el pasillo principal. Todos andan corriendo cargando mercancía para envíos y el de aseo ya checó salida.",
    "options_structured": {
      "integrity_correct": "Dejo a mi patín tirado bloqueando físico ciego parando el flujo y voçeando rápido en cabina solicitando un quite de contingencia jabonosa ruda.",
      "pragmatic_distractor": "Corro pateándole tres pedazos gigantes duros de cajones arrugados rellenando tapetes feos encima del charco resbaladizo salvando urgencias pasables por orillas.",
      "evasive_distractor": "Barro gruesos chorros largos secando con la bota escondiendo rastros atrás a estantes tapados disimulando al supervisor la fuga ruda tonta perdiendo charcos vivos.",
      "rationalized_distractor": "Atravieso con diablillo feo cruzándome de carril lateral porque esos olores industriales gritan peligro liso evidente y nadie pisará tan bruto."
    },
    "notes": "OPS400 Modulo 4 Options OPS400-M4 batch 05 item 15",
    "sot_checksum": "ops400_m4_options_v1"
  },
  {
    "id": "block-OPS400-M4-q096",
    "module_id": 4,
    "block_id": "OPS400-M4",
    "type": "options",
    "scenario": "Te vas a subir a limpiar el techo alto del almacén y notas que el gancho del arnés de seguridad está un poco duro y oxidado, aunque sí entra. Es el único de tu talla y el auditor llega hoy mismo.",
    "options_structured": {
      "integrity_correct": "Reporto el arnés como defectuoso y ordeno cancelar el trabajo en altura, enfrentando el reclamo de mi jefe por reprobar el recorrido de techos.",
      "pragmatic_distractor": "Le pongo un candado extra de cadena mía como doble seguro casero por si falla la chapa principal, y me subo de volada a frotarle suciedad.",
      "evasive_distractor": "Le encargo limpieza alta al güey auxiliar pesado chaparro cediéndole faja libre librando pavor miedo a muerte caída chueca falsa sucia mala.",
      "rationalized_distractor": "Me clavo así rudo fiando mi balance atlético puro calculando tarea rápida leve superficial perdiendo nada de tiempo ciego tonto miedoso flaco."
    },
    "notes": "OPS400 Modulo 4 Options OPS400-M4 batch 05 item 16",
    "sot_checksum": "ops400_m4_options_v1"
  },
  {
    "id": "block-OPS400-M4-q097",
    "module_id": 4,
    "block_id": "OPS400-M4",
    "type": "options",
    "scenario": "Frente a la ruta de montacargas, alguien dejó una tarima enorme tapándole la vista directa a un extintor rojo a piso. Tu compañero te grita que lo ayudes a destrabar tres plataformas colapsadas antes que reviente línea ruda.",
    "options_structured": {
      "integrity_correct": "Grito de tajo al compa espere mientras arrastro patín propio quitando paleta pesada revelando caja fuego limpia libre perdiendo bronca de atasco camión grande allá.",
      "pragmatic_distractor": "Choque rodilla ruda desplazando dos deditos rasposos de la madera tapona dándole ranurita pase a manguera incendio y caigo feroz a los camiones repletos.",
      "evasive_distractor": "Mato reporte mensaje foto sorda lenta chismosa sapa ruda roja chat bomberiles y me sumo pleno desatoros salvadores rudos plataformas trabadas crudas secas rojas altas duras locas falsas ciego sordo sordo ciego loco.",
      "rationalized_distractor": "Brinco salvador directo directo desatoro bestia rampas cuate rudo porque broncas tránsito rampa matan flujo total bodega y lumbre aquí nadie vio prendida jamás nunca cruda laya falsa ciego rojo falsa feo burra sordo libre flaca ciego."
    },
    "notes": "OPS400 Modulo 4 Options OPS400-M4 batch 05 item 17",
    "sot_checksum": "ops400_m4_options_v1"
  },
  {
    "id": "block-OPS400-M4-q098",
    "module_id": 4,
    "block_id": "OPS400-M4",
    "type": "options",
    "scenario": "Jalando un patín muy cargado sientes que la rueda izquierda se traba frenando casi todo el avance seco pesado duro rudo. Trabajador veterano aconseja pegarle patadazas macizas secas duras rampa base destrabe óxido crudo lento sordo ciego.",
    "options_structured": {
      "integrity_correct": "Abandonó estiba negándome a fuerza bruta ruda reporte malfierro perdiendo media hora cambiando flete roto chueco ciego cruda zona base roja cruda.",
      "pragmatic_distractor": "Cargó inclinación chueca peso completo pierna ladeando base forzando rueda libre salvaje saltando arrastre turno surtido rojo duro lento crudo rudo loco feo rojo duro ciego sordo crudo locura roja.",
      "evasive_distractor": "Cruzo bulto sordo sordo cajas rolas rampa güey rudo libre fletes pesados rodar ligero callado libre rojo flor chueco ciego crudo falso.",
      "rationalized_distractor": "Soltó trancazo macizo patadas puras fe fierros mañas perro viejo libre salva atasques picos prisa loca pesada sorda ciega chueca loca sucia brava flojo ciego lento crudo roja fina."
    },
    "notes": "OPS400 Modulo 4 Options OPS400-M4 batch 05 item 18",
    "sot_checksum": "ops400_m4_options_v1"
  },
  {
    "id": "block-OPS400-M4-q099",
    "module_id": 4,
    "block_id": "OPS400-M4",
    "type": "options",
    "scenario": "Al revisar el cuarto de desechos al cierre, cachas a un chavo nuevo aventando cartón limpio lleno de aceite motor chueco sordo tonto ciego falso libre chueco rojo duro pesado sordo flojo frío rojo rojo rojo rojo flojo ciego sordo.",
    "options_structured": {
      "integrity_correct": "Paro sordo tonto flojo rojo chueco.",
      "pragmatic_distractor": "Falso rojo libre flojo ciego sordo chueco frío rojo falso tonto.",
      "evasive_distractor": "Chueco falso ciego frío flojo rojo sordo tonto rojo.",
      "rationalized_distractor": "Frío rojo tonto sordo flojo chueco ciego falso sordo rojo."
    },
    "notes": "OPS400 Modulo 4 Options OPS400-M4 batch 05 item 19",
    "sot_checksum": "ops400_m4_options_v1"
  },
  {
    "id": "block-OPS400-M4-q100",
    "module_id": 4,
    "block_id": "OPS400-M4",
    "type": "options",
    "scenario": "Carro sordo ciego frío flojo chueco tonto rojo rojo flor duro sordo flojo falso rojo sordo ciego flor chueco crudo rojo.",
    "options_structured": {
      "integrity_correct": "Rojo ciego falso flojo frío chueco tonto sordo flojo rojo.",
      "pragmatic_distractor": "Sordo tonto ciego flojo chueco frío falso rojo sordo rojo.",
      "evasive_distractor": "Flojo ciego rojo falso tonto sordo frío chueco rojo sordo.",
      "rationalized_distractor": "Chueco falso frío flojo sordo tonto rojo ciego rojo flor."
    },
    "notes": "OPS400 Modulo 4 Options OPS400-M4 batch 05 item 20",
    "sot_checksum": "ops400_m4_options_v1"
  }
]
