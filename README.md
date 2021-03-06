# 馃 Bots node
En este proyecto proponemos 2 bots en distintas plataformas: telegram y twitter.

## Bot Telegram 鉁夛笍 

El bot de telegram para el Nodo tiene las siguientes caracter铆sticas:
- Desplegar r谩pidamente informaci贸n del nodo: temperatura, memoria, estado de procesos, ip, etc a solicitud de una (o varias) cuentas maestras. El nodo #bitcoin bitbol esta montado sobre la red TOR por default pues usa un cliente UMBREL (internamente funciona en un container Docker) y este no puede ser desactivado. Se puede tener acceso remoto al nodo por medio de esta red. En un caso de emergencia puede ser una alternativa para tener a mano esta direcci贸n (se debe tener extremo cuidado en la manipulaci贸n de estas por seguridad, este es solo un experimento.)
- Interactuar con otros usuarios brindando informaci贸n que puede ser 煤til para potenciales usuarios de Bolivia:
	- Informaci贸n del clima. 
	  Usando un API que entrega datos meteorol贸gicos podemos recopilar y facilitar esta informaci贸n para todo el territorio. De ser posible brindar info como la radiaci贸n solar, atardecer, etc.
	- Verificaci贸n de exposici贸n de filtraci贸n de datos.
	  En 2021 se filtraron mas de 3 millones de cuentas Bolivianas de facebook con nombres, n煤mero celular, perfil, etc. Diversas estafas pueden usar esta informaci贸n que es p煤blica con prop贸sitos maliciosos. Puedes verificar si tu n煤mero de celular (solo de Bolivia) esta asociada a alguna cuenta de facebook filtrada.
	- Gr谩ficas y series de tiempo Bitcoin.
	  El nodo BitBol puede comunicarse y extraer informaci贸n de la red Bitcoin de manera directa. Se puede brindar algunas gr谩ficas como la mempool el como varia el precio. A futuro an谩lisis onchain.
	- Paga por aprender.
	  Este punto es por ahora una idea. Trata de construir un sistema de pagos en satoshis que por cada pdf que pueda ser entregado y superado un breve test libera una factura en la red lightning 鈿?. Existen ejemplos de servicios como Fountain que lo hacen con podcasts. 
- Interactuar con otros usuarios brindando informaci贸n que puede ser 煤til para potenciales usuarios de todo Hispano Am茅rica:
	- Verificador de transacci贸n. 
	  Una transacci贸n bitcoin no se considera irreversible cuando llega a la mempool sino cuando es confirmada al menos 6 veces (confirmaci贸n en el contexto de nuevos bloques adelante). Algunos exchanges y servicios crypto consideran suficiente la verificaci贸n de 2 bloques. Se busca que el nodo pueda notificar cuando tenga 2 verificaciones de una transacci贸n dada (o se pueda configurar cuantas se quiera). Telegram tiene la ventaja de mantener un poco mas el anonimato para realizar esta consulta, el nodo realiza la verificaci贸n directa sin recurrir a ning煤n otro servicio protegiendo los datos de los interesados. 
	- Verificaci贸n de direcciones.
	  Se verifica la direcci贸n en una Blacklist para asegurar un historial limpio de los bitcoins.
	  (Se abandon贸 esta idea luego de entender los argumentos vertidos por andreas en el video):
	  https://www.youtube.com/watch?v=FFLLx-iufM4
	- Blockclock, mempool stats, price.

## Bot Twitter 馃惁

Crear un Bot Twitter es un proceso (en mi experiencia) que demora algunos d铆as en habilitarse desde el portal https://developer.twitter.com/en y realizar las habilitaciones para publicar tuits y modificar el perfil.


La idea central de este bot es brindar un servicio automatizado que recopile informaci贸n directamente del blockchain como:
  - Blockclock -  Muestra el 煤ltimo bloque verificado.
  - Precio - Muestra el precio de bitcoin.
  - Un reporte hecho cada 12 hrs. (n煤mero de transacciones, hashrate, fee promedio).
  - **Ideas** (a eval煤ar):
    - Movimiento de ballenas.
    - Reporte an谩lisis onchain.
    - Estado de la red (n煤mero de nodos)
    - Jugar con facturas lightning.

- Twitter profile Responsive:
  - Cambia el nombre cuando se verifica un nuevo bloque.
  - Cambia un banner con la foto de los 煤ltimos 5 seguidores
  - autom谩tico cada 10min. 

## Instalaci贸n 

Crea un entorno virtual (venv), lo activas, clonas el repositorio e instalas (con pip) los requerimientos.

``` sh
$python -m venv bots
$cd bots/
$source bin/activate
(bots)$git clone https://github.com/jpcrespo/bitbolnode.git
(bots)$cd bitbolnode
(bots)$pip install requerimientos.txt
```
> **Note**
> 
> Para crear los bots e interactuar con los distintos APIs (telegram/twitter) necesitamos almacenar los tokens (llaves) de acceso:
> 
> - En el caso de Telegram es una sola clave. Adem谩s que tambi茅n guardamos el id 芦master禄 para verificar accesos privilegiados. 
> 
> - En el caso de Twitter son 4 claves (Bearer es opcional).
> Estas se guardan en un archivo de texto plano en la carpeta app. Finalmente se explicita en el '.gitignore' (es prudente no compartirlas).

![ejemplo](env.png)

