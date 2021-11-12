# Sistemas De Gestión Empresarial 2º DAM

## Tecnologías 🚀

* **Python**  

## Pogramas Utilizados 📌

* **Odoo 13**
* **Visual Studio**

## Control De Versiones 📌

* **Git y GitHub**

## Autor ✒️

* **Juan Sáez García** -  [Web Personal](https://juamber.com)

## Configuración 🛠️

❌ LA MÁQUINA VIRTUAL YA ESTÁ CONFIGURADA ❌

Esta configuración es por si quieres probar los módulos en tu propia máquina virtual.

Si ya tiene instalado Odoo 13.

Una vez instalado PyCharm, lo abriremos y crearemos un nuevo proyecto ( Recomiento cambiar la ruta a documentos "C:\Users\{USER-NAME}\{NOMBRE-DEL-PROYECTO}" )

Añadimos el intérprete a poder ser Python 3.7 (En mi caso estaba en la carpeta "server" de Odoo)
Creamos la carpeta "extra-addons" dónde alojaremos los nuevos módulos.

En la terminal de Pycharm ejecutamos la siguiente línea:
pip install -r "C:\Program Files (x86)\Odoo 13.0\server\requirements.txt"

Falta configurar el ejecutable del proyecto dónde pondremos el siguiente archivo de inicio: "C:\Program Files (x86)\Odoo 13.0\server\odoo-bin" con la siguiente configuración: --conf "C:\Users\user\Documents\2DAM-SistemasDeGestionEmpresarial\odoo.conf"

