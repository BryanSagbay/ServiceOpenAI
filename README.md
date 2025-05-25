
<div align="center" id="top"> 
	
<img src="https://i0.wp.com/imgs.hipertextual.com/wp-content/uploads/2022/07/openai.png?fit=1200%2C675&quality=50&strip=all&ssl=1"  height="300" width="600" alt="ServiceOpenAI" />
</div>

# Service OpenAI: 🚀 

Este código es un script de Python que utiliza el modelo GPT-4 de OpenAI para clasificar problemas en un sistema universitario. El script recibe el texto extraido del correo, que luego se concatena con una lista de tipos de problemas obtenidos de un archivo JSON. Luego, el mensaje resultante se envía al modelo GPT-4, que genera una respuesta.

[![](https://img.shields.io/badge/python-purple?logo=python)](https://img.shields.io/badge/python-purple?logo=python) [![](https://img.shields.io/badge/HTML5-brown?logo=html5)](https://img.shields.io/badge/html5-purple?logo=html5) [![Langua](https://img.shields.io/github/languages/count/BryanSagbay/ServiceOpenAI?color=c90e21 "Langua")](https://img.shields.io/github/languages/count/BryanSagbay/ServiceOpenAI?color=c90e21 "Langua") [![Git](https://img.shields.io/github/repo-size/bryansagbay/serviceopenai?color=56BEB8 "Gut")](https://img.shields.io/github/repo-size/bryansagbay/serviceopenai?color=56BEB8 "Gut") [![Start](https://img.shields.io/github/stars/bryansagbay/serviceopenaI?color=blue "Start")](https://img.shields.io/github/stars/bryansagbay/serviceopenaI?color=blue "Start") 

</p>

<h4 align="center"> 
	🚧  ServiceOpenAI - Under construction...  🚧
</h4> 

<hr> 
<br>
> ### 1. How to use?

1. Clone el repositorio en tu máquina local.
```bash
$ git clone https://github.com/BryanSagbay/ServiceOpenAI.git
```

2. Instale las dependencias requeridas ejecutando:
```bash
$ npm install
```

3. En el archivo config.py agregue su clave API de OpenAI dentro de la variable api_Key.
```bash
$ api_Key='{You_apiKey}'
```

4. Ejecute el script ejecutando python3 main.py en su terminal.
```bash
$ python3 main.py
``` 
<br>


> ### 2. Dependencias

- OpenAI
- Json
- Email
- Imaplib
- Email-Header
- Flask
<br>


> ###  3. Datos

El script utiliza un archivo JSON ubicado en ./data/gpli.json para obtener una lista de tipos de problemas. El archivo contiene una serie de objetos, cada uno de los cuales tiene una propiedad de tipo que describe un tipo de problema en el sistema universitario.

```bash
  {
        "type": "Tipo de Problema",
        "engineer": "Ingeniero a cargo",
        "email": "Correo del Ingeniero",
        "caso": "Tipo de caso",
        "description":"Descripción del Tipo de Problema"
    }
```

<br>


> ### License & Copy &copy;

Este proyecto está bajo licencia. Para mas detalles, consulte el archivo de licencias.


Hecho por: <a href="https://github.com/BryanSagbayt" target="_blank">Bryan Sagbay & Sebastián Carrión</a>


------------

<a href="#top">Back to top</a>
