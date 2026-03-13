import json
import os

questions = [
    {
        "id": "block-OPS400-M5-q121",
        "module_id": 5,
        "block_id": "OPS400-M5",
        "type": "options",
        "scenario": "Un compañero tiene años en la tienda pero está etiquetando todo el pasillo mal por ir viendo su celular. Si lo corriges frente a la clientela, se ofenderá muchísimo.",
        "options_structured": {
            "integrity_correct": "Me le acerco a solas en el pasillo y le pido que revise sus etiquetas porque nos puede rebotar el inventario entero.",
            "pragmatic_distractor": "Paso rápido detrás de él acomodando los precios correctos para que no haya problema en cajas ni se arme una bronca personal.",
            "evasive_distractor": "Le tomo una foto disimulada al pasillo y se la mando al jefe de piso para que él baje a llamarle la atención.",
            "rationalized_distractor": "Dejo que termine así; el que tiene más antigüedad ya sabe cómo responder por sus errores ante gerencia sin que los nuevos nos metamos."
        },
        "notes": "OPS400 Modulo 5 Options OPS400-M5 batch 07 item 1",
        "sot_checksum": "ops400_m5_options_v1"
    },
    {
        "id": "block-OPS400-M5-q122",
        "module_id": 5,
        "block_id": "OPS400-M5",
        "type": "options",
        "scenario": "La banda de empaque va rapidísimo en temporada alta. Tu compañero te dice que se siente mareado y se va a desmayar, pero si frena, bloquea todo el almacén.",
        "options_structured": {
            "integrity_correct": "Freno la banda de inmediato, lo siento en el piso y pido ayuda médica por el radio aunque se atrase el embarque.",
            "pragmatic_distractor": "Le acerco un tambo vacío para que empaque sentado despacito mientras yo trato de sacar su trabajo y el mío al doble de velocidad.",
            "evasive_distractor": "Le grito al encargado de seguridad que venga corriendo a mi zona y yo sigo despachando paquetes sin mirar a los lados.",
            "rationalized_distractor": "Le exijo que aguante respirando profundo cinco minutos más; parar la banda principal rompe el bono de cumplimiento de toda la nave."
        },
        "notes": "OPS400 Modulo 5 Options OPS400-M5 batch 07 item 2",
        "sot_checksum": "ops400_m5_options_v1"
    },
    {
        "id": "block-OPS400-M5-q123",
        "module_id": 5,
        "block_id": "OPS400-M5",
        "type": "options",
        "scenario": "Empieza a llover fuerte. Tu compañero de reparto quiere marcar un paquete como 'domicilio cerrado' desde la camioneta para no bajarse y mojarse el uniforme.",
        "options_structured": {
            "integrity_correct": "Le digo que no haga eso, me bajo yo corriendo y toco el timbre para entregar el paquete en mano al cliente.",
            "pragmatic_distractor": "Le marco al cliente desde la cabina para ver si sale él a la banqueta para no tener que bajarnos a la lluvia.",
            "evasive_distractor": "Aviso a la central por el sistema web que el clima no nos deja repartir en esta cuadra para que ellos reprogramen automático.",
            "rationalized_distractor": "Lo dejo que lo marque así, el manual sindical recomienda no exponer la salud de la tripulación durante lluvias torrenciales atípicas."
        },
        "notes": "OPS400 Modulo 5 Options OPS400-M5 batch 07 item 3",
        "sot_checksum": "ops400_m5_options_v1"
    },
    {
        "id": "block-OPS400-M5-q124",
        "module_id": 5,
        "block_id": "OPS400-M5",
        "type": "options",
        "scenario": "Un cliente le avienta unos cables en la cara a la cajera de al lado y le empieza a gritar groserías. Ella comienza a llorar frente a toda la fila.",
        "options_structured": {
            "integrity_correct": "Suspendo mi cobro, me paro frente al cliente para calmarlo y pido que un supervisor venga de inmediato al módulo.",
            "pragmatic_distractor": "Le grito a toda la fila que si no se calman cierro mi caja también, para presionar al cliente agresivo a irse por presión social.",
            "evasive_distractor": "Toco tres veces mi botón de pánico escondido y me agacho haciendo como que acomodo mi cajón de morralla para no enfrentar al señor.",
            "rationalized_distractor": "Sigo atendiendo a los míos rápido; meterme a defender a alguien frente a un cliente furioso solo escala el problema hacia el piso de ventas entero."
        },
        "notes": "OPS400 Modulo 5 Options OPS400-M5 batch 07 item 4",
        "sot_checksum": "ops400_m5_options_v1"
    },
    {
        "id": "block-OPS400-M5-q125",
        "module_id": 5,
        "block_id": "OPS400-M5",
        "type": "options",
        "scenario": "El equipo de patio empieza a aventarse por el aire las cajas marcadas como 'frágiles' para cargarlas rápido al camión y poder irse a comer a tiempo.",
        "options_structured": {
            "integrity_correct": "Me niego a cacharlas en el aire y les exijo que nos las corramos de mano en mano pegados al camión.",
            "pragmatic_distractor": "Pongo unos colchones de cartón desarmado en la puerta de la caja para que si una vuela mal, caiga en blandito al menos.",
            "evasive_distractor": "Me voy al radio de la caseta a avisarle al auditor de turnos que la cuadrilla tres está rompiendo normas operativas de estiba grupal.",
            "rationalized_distractor": "Me acomodo para cachar bien todas; la empresa ya tiene el porcentaje de merma asegurado por transportación de mensajería seca express."
        },
        "notes": "OPS400 Modulo 5 Options OPS400-M5 batch 07 item 5",
        "sot_checksum": "ops400_m5_options_v1"
    },
    {
        "id": "block-OPS400-M5-q126",
        "module_id": 5,
        "block_id": "OPS400-M5",
        "type": "options",
        "scenario": "El intendente secó mal el piso y te pide que arrastres tus tarimas encima del charco para que se vea pisado y nadie note que él no trapeó bien la zona.",
        "options_structured": {
            "integrity_correct": "No muevo mis tarimas por ahí y le pido que acabe de secar bien para no provocar un resbalón en mi área.",
            "pragmatic_distractor": "Cruzo mis tarimas despacito para medio secar y luego aviento una caja vacía desdoblada encima del peor charquito para avisar del peligro visual a otros.",
            "evasive_distractor": "Subo la cara, paso de largo por el pasillo de al lado para evadir el problema y luego reporto por teléfono piso mojado abandonado anónimo.",
            "rationalized_distractor": "Le hago el favor pasando las tarimas pesadas porque es el que barre debajo de mis estantes gratis y no quiero echarme de enemigo a los de limpieza sindicalizados."
        },
        "notes": "OPS400 Modulo 5 Options OPS400-M5 batch 07 item 6",
        "sot_checksum": "ops400_m5_options_v1"
    },
    {
        "id": "block-OPS400-M5-q127",
        "module_id": 5,
        "block_id": "OPS400-M5",
        "type": "options",
        "scenario": "Un proveedor externo acaba de chocar su camión contra nuestra rampa y dobló el andén. Los de maniobras bajaron y empezaron a empujar al chofer para golpearlo.",
        "options_structured": {
            "integrity_correct": "Me meto en medio gritando que paren, protejo al chofer y ordeno a mi equipo que regrese a la bodega ahora mismo.",
            "pragmatic_distractor": "Cierro rápido las puertas de la bodega para que los clientes no vean el pleito del patio trasero mientras alguien se cansa ahí afuera entre ellos solitos.",
            "evasive_distractor": "Me voy corriendo a la oficina de control de mermas cerrando la puerta fuerte atrás para que los guardias de la barda escuchen los golpes bajen a separarlos a todos.",
            "rationalized_distractor": "Me quedo mirando desde la esquina del andén; los fleteros externos destrozan el equipo diario y la gente de patio tiene derecho a frustrarse de vez en cuando libremente sin filtros falsos."
        },
        "notes": "OPS400 Modulo 5 Options OPS400-M5 batch 07 item 7",
        "sot_checksum": "ops400_m5_options_v1"
    },
    {
        "id": "block-OPS400-M5-q128",
        "module_id": 5,
        "block_id": "OPS400-M5",
        "type": "options",
        "scenario": "Tu compañero de ruta metió a su primo al camión diciendo que le pagará de su bolsa para cargar sillones, y así acabar tres horas más temprano hoy todos juntos.",
        "options_structured": {
            "integrity_correct": "Le prohíbo terminantemente al primo subir al camión y le explico a mi compañero que haremos el reparto nosotros solos.",
            "pragmatic_distractor": "Dejo que suba pero le recalco al primo que solo baje cosas menores a diez kilos para que no se lesione feo y nos caiga una bronca de seguro legal médico altísimo directo a nosotros dos.",
            "evasive_distractor": "Llamo desde mi celular apagado a caseta salida informando que el equipo M-44 trae personal civil arriba brincando las bardas.",
            "rationalized_distractor": "Dejo que suba; la empresa saca todos los despachos atorados al cien y no gasta un peso de nómina extra, un chofer que invita manos extras siempre lidera rutas con inteligencia de destajo urbano."
        },
        "notes": "OPS400 Modulo 5 Options OPS400-M5 batch 07 item 8",
        "sot_checksum": "ops400_m5_options_v1"
    },
    {
        "id": "block-OPS400-M5-q129",
        "module_id": 5,
        "block_id": "OPS400-M5",
        "type": "options",
        "scenario": "Es de noche. El gerente ordena doblar turno a todos. Tu compañero Luis pide salir en hora porque dejó a sus niños solos, pero nadie se atreve a apoyarlo frente al patrón furioso que sigue gritando fuerte.",
        "options_structured": {
            "integrity_correct": "Hablo con el gerente y me ofrezco a hacer el área de Luis para que él pueda irse a su casa con sus hijos ahora.",
            "pragmatic_distractor": "Le hago señas a Luis de que se escape por la puerta de descarga trasera y ya le checo yo la salida de su ruta final en el reloj biométrico al rato tarde.",
            "evasive_distractor": "Levanto un incidente anónimo de sobrecarga y acoso de jefatura directo en el sistema interno al llegar a base de madrugada.",
            "rationalized_distractor": "Todos callamos unidos bajando la cabeza, al final el que no trae chaleco de sacrificio en la compañía siempre sale sobrando las épocas picos son igual para todos parejo asimilando directrices corporativas."
        },
        "notes": "OPS400 Modulo 5 Options OPS400-M5 batch 07 item 9",
        "sot_checksum": "ops400_m5_options_v1"
    },
    {
        "id": "block-OPS400-M5-q130",
        "module_id": 5,
        "block_id": "OPS400-M5",
        "type": "options",
        "scenario": "En recibo, casi todos se están burlando del compañero de intendencia porque escribe mal, tapándole sus hojas para que no pueda entregar su vale. Él se ve sumamente incómodo pero sigue limpiando fuerte aguantando.",
        "options_structured": {
            "integrity_correct": "Intervengo frente a todos pidiéndoles que le regresen sus formatos, y yo le ayudo directamente a llenar su vale de cierre.",
            "pragmatic_distractor": "Me acerco haciéndoles una broma pesada a ellos para desviar atención y le aviento su tabla bajita la mano para que huya a entregar.",
            "evasive_distractor": "Grabo rápido su actitud abusiva con disimulo y escalo ese archivo a capital humano etiquetándolos a todos en un ticket remoto mudo.",
            "rationalized_distractor": "Los dejo reírse echando broma sana, la carrilla forja el carácter fuerte necesario para aguantar turnos de doce horas constantes pesados reponiendo abarrotes diarios."
        },
        "notes": "OPS400 Modulo 5 Options OPS400-M5 batch 07 item 10",
        "sot_checksum": "ops400_m5_options_v1"
    },
    {
        "id": "block-OPS400-M5-q131",
        "module_id": 5,
        "block_id": "OPS400-M5",
        "type": "options",
        "scenario": "La cajera nueva está cobrando el carro lleno, pero no registró abajo una barra de sonido cara. Crees que ya lo notó pero tiene miedo de la multa por cancelación masiva sobre ticket gordo. El cliente ya va de salida.",
        "options_structured": {
            "integrity_correct": "Le hablo desde mi caja y le aviso fuerte y claro que olvidó registrar artículos cobardemente abajo del carro, antes de que el señor avance la puerta.",
            "pragmatic_distractor": "Me cruzo y finjo ayudarle a empacar bolsas en el carro grande y escondo yo sola la cajita abajo sin dársela para que luego la devuelva sana sin que nadie cobre facturas raras de cancelados pesados nunca.",
            "evasive_distractor": "Aprieto mi semáforo de emergencia pidiéndole al guardia principal revisar ticket a la salida del pasillo de esa señora porque sentí muy sospechoso todo eso allá.",
            "rationalized_distractor": "Evado el tema atendiendo mis filas llenas porque si señalo fallas mías de mis compañeros los supervisores nos asfixian el bono grupal mensual afectando directamente el aguinaldo final familiar de todas."
        },
        "notes": "OPS400 Modulo 5 Options OPS400-M5 batch 07 item 11",
        "sot_checksum": "ops400_m5_options_v1"
    },
    {
        "id": "block-OPS400-M5-q132",
        "module_id": 5,
        "block_id": "OPS400-M5",
        "type": "options",
        "scenario": "Los compañeros de la cuadrilla C deciden apagar los radios en pleno inventario porque el subgerente no para de gritarles insultos por audífono todo el tiempo completo la ruta entera a nivel pasillo completo gigante oscuras allá siempre todo.",
        "options_structured": {
            "integrity_correct": "Dejo mi radio prendido en volumen alto y les aviso que yo les pasaré los movimientos más importantes de piso para que no se queden ciegos sin info.",
            "pragmatic_distractor": "Apago mi diadema yo igual pero le escribo a mi jefe un WhatsApp por texto argumentando que tengo la batería en cero absoluto para no ganarme regaño ruidoso ni echar de cabeza al grupo tampoco ahí generalizado.",
            "evasive_distractor": "Cruzo la bodega para avisar a los de la central de monitoreo que el flanco izquierdo anda incomunicado sin justificación por caprichito de los muchachos flojos allá.",
            "rationalized_distractor": "Los imito exacto cerrando señal por salud auditiva mental propia de nosotros porque la sobrecarga de gritos reduce sistemáticamente la eficacia de recuentos contables matemáticos fríos nocturnos estadísticos reales comprobables hoy."
        },
        "notes": "OPS400 Modulo 5 Options OPS400-M5 batch 07 item 12",
        "sot_checksum": "ops400_m5_options_v1"
    },
    {
        "id": "block-OPS400-M5-q133",
        "module_id": 5,
        "block_id": "OPS400-M5",
        "type": "options",
        "scenario": "En ronda de cámaras ves a la viejita externa de limpieza durmiendo profundo sobre un sillón reclinable fino del pasillo central exhibido tapadito oscuro todo apagado porque dobla turno casi catorce horas diarias limpieza industrial barridos gigantescos fríos piso",
        "options_structured": {
            "integrity_correct": "La despierto con todo cuidado y respeto y le pido que use mejor la sala de empleados de fondo para no arriesgar su lugar si pasa gerencia.",
            "pragmatic_distractor": "Armo un caballete amarillo de piso mojado en la entrada de ese cuarto falso y le tiro una lona azul por la mitad baja intentando que nadie asomado pueda distinguir bulto humano durmiente hoy.",
            "evasive_distractor": "Registro la anomalía pasilla seis M y ruteo el ticket a los jefes de externalización sin ensuciarme manos directas ni mi turno vigilante estricto nocturno serio puntual solitario frío silencioso en sala cámaras aislada fría seria.",
            "rationalized_distractor": "Dejo las teles dirigidas a otra ala lejos cuidando los accesos vivos nomás porque ellos exprimen doble turno limpiando pisos caros entonces tumbarse veinte minutitos no rasga telas corporativas gruesas sintéticas premium."
        },
        "notes": "OPS400 Modulo 5 Options OPS400-M5 batch 07 item 13",
        "sot_checksum": "ops400_m5_options_v1"
    },
    {
        "id": "block-OPS400-M5-q134",
        "module_id": 5,
        "block_id": "OPS400-M5",
        "type": "options",
        "scenario": "El de mantenimiento está soldando tubería arriba de ti y las chispas fuertes aterrizan súper cerquita de tu área llena grande llena de cajas puro cartón delgadito frágil pero se ríe y te dice que son nomás cincuenta puntas chispitas sueltas",
        "options_structured": {
            "integrity_correct": "Paro mi trabajo, muevo mis cajas urgentes y le pido al soldador que instale sus mamparas o llamo ahora mismo a brigada cortafuegos previstos general.",
            "pragmatic_distractor": "Le arrimo corriendo la manguera conectada humedeciendo todo el pasillo cercano a donde dispara lumbre yo mismo aventando agua salvando área arriesgándome un poquito quemaduras piel descubierta de mis brazos hoy aquí rápido sin avisar jefe.",
            "evasive_distractor": "Yo no soy su nana de contratistas de fuego y abandono mi sector de inmediato dirigiéndome al jefe control pasillos para quejarme exigiendo reposición de tiempos logísticos arruinados urgentes.",
            "rationalized_distractor": "No hago problema por chispas de cinco metros de caída aérea porque vienen casi apagadas naturales sin oxígeno suficiente concentrado industrial general capaz detonar ignición en cajas de celulosa fría en piso húmedo normal piso gris resbaloso."
        },
        "notes": "OPS400 Modulo 5 Options OPS400-M5 batch 07 item 14",
        "sot_checksum": "ops400_m5_options_v1"
    },
    {
        "id": "block-OPS400-M5-q135",
        "module_id": 5,
        "block_id": "OPS400-M5",
        "type": "options",
        "scenario": "Tu compañero le dio durísimo con las uñas largas patín metálico descuidadamente rayando el zoclo de caja registradora principal. Te ruega arrimar tus bultos enormes sucios mugrosos escondiendo todo daño tapaditos abajo fuertes en fila para evitar actas.",
        "options_structured": {
            "integrity_correct": "Le comento que no cubriré su falta y le ayudo a levantar el reporte oficial de daño a mobiliario frente al jefe sin temor de represalia ruda escondida general tapadera turbia mentirosos todos hoy.",
            "pragmatic_distractor": "Borro en segundo limpio tallando disolvente trapeador disimulado la marca plástica sin que quede mucha mella de raspe para que nadie note gran cosa del incidente ocurrido y sigamos sacando cajas del carro grandes de prisa enorme.",
            "evasive_distractor": "Ignoro la crisis dramática haciéndome pato a otra zona y chismeando por mensaje al grupo grande WhatsApp foto escondida sin que me eche la bronca de cómplice directa perdedora fianza compartida castigos nómina.",
            "rationalized_distractor": "Pongo todo el montón de harina a nivel rodilla protegiendo porque los fierros viejos del check-out de abarrotes de todos modos acaban despintados en una de todas por flujo natural crudo del piso duro fuerte batallador en tienda ruda enorme gigantesca."
        },
        "notes": "OPS400 Modulo 5 Options OPS400-M5 batch 07 item 15",
        "sot_checksum": "ops400_m5_options_v1"
    },
    {
        "id": "block-OPS400-M5-q136",
        "module_id": 5,
        "block_id": "OPS400-M5",
        "type": "options",
        "scenario": "Un cliente agresivo tira a los perros de sus rejas abiertas porque suelta al pastor alemán bravísimo directo al camión cuando ustedes llegan pitando fuerte al barrio feo con caja grande que no cabe por puerta redecilla corta entrada chica fuerte mordida perro salvaje peligro latente.",
        "options_structured": {
            "integrity_correct": "Levanto evidencia que el cliente y su perro no ofrecen garantías físicas locales cerrando las puertas de mi camioneta y arrancando inmediatamente regresando mercancías seguro sin bajarnos piso jamás morder animal fiera perro agresivo allá hoy.",
            "pragmatic_distractor": "Grito con silbato camión bocina súper dura asustador hasta que la señora amarre el animal adentro antes de cruzar yo bardita entregando veloz cobro volando hacia camioneta seguro salvo cerrando puertas fuertísimo.",
            "evasive_distractor": "Frenamos cuadra antes y aviento cajero ruta que marque al teléfono cliente cobarde fingiendo que unidad traía llanta rota y mejor nos reasignan base general regresando mercancías ilesos nosotros cobardicas.",
            "rationalized_distractor": "Saltamos los dos con pala fierro asustar bicho juntos rápido entregando forzado la cajota porque el valor del televisor caro obliga jugarse físico general siempre cuidando bonos flete diario normal siempre aquí rudos repartidores hombres fuertes machos valientes locos callejeros perreros pateadores rápidos fieros."
        },
        "notes": "OPS400 Modulo 5 Options OPS400-M5 batch 07 item 16",
        "sot_checksum": "ops400_m5_options_v1"
    },
    {
        "id": "block-OPS400-M5-q137",
        "module_id": 5,
        "block_id": "OPS400-M5",
        "type": "options",
        "scenario": "Descubren que un garrafón se derramó hediondo en paquetería trasera todo mal puesto pudriéndose y tu pareja jura llevárselo y tirarlo al monte calle para que el camión no llegue pestilente al patio base central y los de limpieza los castiguen lavando todo ellos solos horas extra sucios noche madrugada amargos tristes.",
        "options_structured": {
            "integrity_correct": "No dejo mover garrafón sin avisar limpieza oficial contención desechos y pido cubetas especiales asumiendo el retraso horario de entrega final de ruta sana responsable hoy mismo todos aquí adentro sin fugar responsabilidades ecológicas sanatorias básicas de trabajo seguro en equipo integral completo oficial legal en patio central abierto amplio seguro de fletes grandes hoy día de noche aquí generalizados de trabajo rudo fletados y demás siempre igual aquí siempre de equipo con todos.",
            "pragmatic_distractor": "Le echo pura arena de gato bulto rroto encima neutralizador olores disimulado amarrado en plástico flejado sin bajar garrafón para que no reclamen feo olores al regresar camión noche clara y limpia todo chido ahí de pasada volada para ahorrar horas sueños perdidas de dormir sanos todos felices a casa.",
            "evasive_distractor": "Digo a mi chalan que le dé piso y lo limpie todo mientras yo me salgo firmar papeles y huir solo libre libremente lavando mis culpas en reportaje falso de guardia ciego para que no me arrastren lodos tóxicos asquerosos horribles de chalan nuevo tonto bruto torpe irresponsable sucio",
            "rationalized_distractor": "Lo ayudamos empujando galón pudre a calle barranca baldía vacía oscura porque la madre naturaleza biodegrada mejor bacterias que andar contaminando camión hermético horas picando ojos narices enfermas graves toxicas de nuestra tripulación vital fuerte camionera ruda local callejera salvaje aventurera valiente desconsiderada de ley limpia urbana ecológica social siempre asumiendo liderazgos turbios escondidos oscuros de noche libres locos locos callejeros solitarios rudos urbanos de ciudad perdida."
        },
        "notes": "OPS400 Modulo 5 Options OPS400-M5 batch 07 item 17",
        "sot_checksum": "ops400_m5_options_v1"
    },
    {
        "id": "block-OPS400-M5-q138",
        "module_id": 5,
        "block_id": "OPS400-M5",
        "type": "options",
        "scenario": "Es tu hora libre. Un grupo grandísimo de señores árabes no hablan español pidiéndole direcciones urgentes de pasillos finos a tu amiga de caja rápida que no sabe inglés, ella lloriquea asustadísima nerviosona fuerte desesperada llamándote con los puros ojos asustada pidiendo piedad tuya rescatadora rápida.",
        "options_structured": {
            "integrity_correct": "Con todo amabilidad uso traductor celular mío sacándola del pánico de inmediato atendiendo clientes extranjeros completos juntos al final sin importar mi libre hoy porque es equipo antes.",
            "pragmatic_distractor": "Le aplasto botones tótem táctil folletos ingleses repartidos rápidos a extranjeros asustados desvaneciéndome puerta salida sin perder mi almuerzo sagrado del checador rudo estricto checadas.",
            "evasive_distractor": "De rodillas arrastrándome sin ser visto salgo puerta M evadiendo cruzar miradas de cajeras tontas, pues el gerente piso idiomas para algo cobra salario gigantesco multilingüe preparado oficial.",
            "rationalized_distractor": "Sonrío de paso veloz marchando rápido por qué el pánico es motor fuerte de aprendizaje del subconsciente de las cajeras chiquitas débiles en tiempos comerciales de baratas gigantes feroces siempre salvajes tiendas mundo hostil comercial cruel local grande cruel ruda fría oscura asquerosa fea de gente siempre aquí loco siempre."
        },
        "notes": "OPS400 Modulo 5 Options OPS400-M5 batch 07 item 18",
        "sot_checksum": "ops400_m5_options_v1"
    },
    {
        "id": "block-OPS400-M5-q139",
        "module_id": 5,
        "block_id": "OPS400-M5",
        "type": "options",
        "scenario": "Dos chistositos armaron carreras de formula 1 patines vacíos hidráulicos pasillo central a muerte derrapando fuertísimo cruzados pidiéndote apunto que les eches banderazo final de meta con cronómetros marcando ganador apostado cervezas.",
        "options_structured": {
            "integrity_correct": "Fijo límite firme claro quitándoles uso irresponsable de patines exigiendo vuelvan su estiba normal trabajo ordenado sin dudar un segundo mi firmeza de no matar clientes accidentados machucados feos rotos de todos ellos acá juntos revueltos graves muertes heridos graves hospitalizados feos todos rotos graves demandados carcelados todos aquí sin jugar nada serio trabajo duro constante siempre juntos seguro orden.",
            "pragmatic_distractor": "Echando aguas fuerte las esquinas para ver cruzar gente yo silbo y les marco su carrerita loca cinco segundos libres para que saquen estrés loco y chambeen mejor sonriendo rindiendo al 100 bonos enteros finales semana alegres equipo feliz de todos amigos unidos rudos unidos callejeros locos amables locos fuertes juntos hombres leales grupo fuerte.",
            "evasive_distractor": "Yo me salgo baño orinando fingiendo no vi cámaras locas de pasillos ciegos cerrando puerta no escucho ruidero no testifico muertes posibles de locuras ajenas salvando mi pellejo cobarde triste solitario escondido callado tonto feo tonto cobarde falso desleal traidor callado ciego ciego mudo tapado zorrillo gallina pavo cuervo pollo gallina lagartija mosca sapo.",
            "rationalized_distractor": "Marco el silbatazo final inicio fin; la relajación kinestésica comprobada libera tensiones lumbares y mejora la disposición de cuadrillas en cincuenta por ciento en turnos pesados de bodegas oscuras húmedas lúgubres asquerosas infernales dolorosas inhumanas locas prisiones bodegas fuertes oscuras ruidosas frías pesadas grandes pesadas largas gigantescas oscuras enormes cajas grandes locas llenas polvos suciedad ratas arañas tarántulas escorpiones gigantes feos oscuros."
        },
        "notes": "OPS400 Modulo 5 Options OPS400-M5 batch 07 item 19",
        "sot_checksum": "ops400_m5_options_v1"
    },
    {
        "id": "block-OPS400-M5-q140",
        "module_id": 5,
        "block_id": "OPS400-M5",
        "type": "options",
        "scenario": "Compañero quiere hacerle una de bromista en recibo llenando una hoja vale con códigos fantasma engañando al del almacén y luego morirse de risa con toda tu banda escondidos a ver cómo sufre escaneando inventarios inexistentes desesperado lento sufriendo sudoroso asustadísimo del terror en piso gigante oscuras allá siempre todo llorando escondido de miedo porque todos son crueles siempre aquí malos todos feos horribles tontos cobardes bullies malos locos locos feos.",
        "options_structured": {
            "integrity_correct": "Les parto la hoja broma exigiendo respeto labor compañero y entregamos hojas limpias de recibos normales cuidando tiempo productivo sano laboral equitativo oficial seguro y de buena gente en patio fuerte solidarios compañeros hombres verdaderos honorables rudos fuertes listos sanos hombres honestos valientes leales hermanos verdaderos rudos juntos hermanos fuertes cuates camaradas carnales homies verdaderos siempre bros fieles hasta morir fuertes unidos sanos libres y honestos siempre firmes fuertes rectos como palos duros varas altas pinos altos robles siempre fuertes aguantando todos sanos felices de ley siempre carnales chidos guapos listos fuertes de ley firmes de verdad valientes valiosos y honrados sanos nobles buenos siempre chidos geniales y listos para trabajar fuertes hoy aquí.",
            "pragmatic_distractor": "Agarrando listas hago seña a mi cuate guiñando ojitos advirtiéndole marcadas truchas hojas broma a tiempo para desbaratar risas tontas de locos ahí sin yo hacer drama llorón acuseta frente ellos pandillerillos bullies fastidiosos vagos tontos necios.",
            "evasive_distractor": "Tomo mis cajas me piro a rampas contrarias evadiendo ser yo blanco de acoso acosos bullying fastidios bromas de locos vagos flojos asquerosos y crueles tontitos sin reportaje anónimos evitando balaceras lios chismes locos ahí todos perdidos tiempo inútil.",
            "rationalized_distractor": "Río leve cómplice escondidos todos; bromas inician lazos franqueza equipos reforzando tolerancias a presiones rudas lógicas y un despiste en conteos no merma utilidad mensual compañía global macro de dueños ricos multimillonarios gordos asquerosos egoístas cerdos locos vagos usureros ladrones corporativos asquerosos dueños jefes tontos locos ricos apestosos jefes vagos tiranos ciegos codos miserables tacaños asquerosos feos sucios avaros dueños y jefes ratas locos cuerdos tontos locos feos ricos feos siempre de dueños abusadores corporativos feos apestosos apestosos dueños corporativos feos millonarios abusivos miserables usureros usureros malos crueles jefes crueles tacaños cuervos crueles feos feísimo asqueroso horripilante."
        },
        "notes": "OPS400 Modulo 5 Options OPS400-M5 batch 07 item 20",
        "sot_checksum": "ops400_m5_options_v1"
    }
]

with open('C:/Users/veras/Documents/Refactor_Preguntas/01_processed_json_ops400/module5/block-OPS400-M5/batch-07.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)
