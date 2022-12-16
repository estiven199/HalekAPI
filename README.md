# HALEK API

## Descripción

La API de HALEK te permite realizar todas las operaciones que haces con nuestro cliente web.
La API de HALEK se creó sobre principios RESTful que garantizan direcciones URL predecibles que facilitan la creación de aplicaciones. Esta API sigue las reglas de HTTP, lo que permite utilizar una amplia gama de clientes HTTP para interactuar con la API.
Cada recurso se expone como una URL. La URL de cada recurso se puede obtener accediendo al Punto final raíz de la API.


## Índice 

- [Preparacion](#preparacion)
- [Instalación](#instalación)
- [Uso](#uso)

## Preparacion

- Instalar Docker y Docker Compose en su sistema local siguiendo las instrucciones proporcionadas en la   [documentación oficial de Docker ](https://docs.docker.com/)
- Asegúrese de que exista un archivo llamado `.env`donde deberá estar una variable con el siguiente formato y valor: ``` export SECRET='ZQeOwY6pNusL_xnUV_2i2g5F6BhYFaoL4mt9pB5ANw8='```

## Instalación

-Clonar el proyecto en la maquina localmente. [Clonar un repositorio ](https://docs.github.com/es/repositories/creating-and-managing-repositories/cloning-a-repository)

Ejecute los siguiente comandos:

```sh
docker compose build "Construye las imágenes de Docker que se especifican en el archivo docker-compose.yml"
docker compose up  "Crea y ejecuta los contenedores de un proyecto a partir de las imágenes de Docker"
```
El archivo docker-compose.yml especifica dos contenedores: un contenedor api y un contenedor mongo.

El contenedor api se construye a partir del directorio actual (.) y se le da el nombre de Fastapi. Está configurado para reiniciar siempre y expone el puerto 8000 en la máquina anfitriona, mapeándolo al puerto 8000 en el contenedor. El contenedor api también está vinculado al contenedor mongo y tiene un volumen que mapea el directorio actual en la máquina anfitriona a /usr/src/app en el contenedor.

El contenedor mongo se basa en la imagen mongo y se le da el nombre de mongodatabsae. Expone el puerto 27017 en la máquina anfitriona, mapeándolo al puerto 27017 en el contenedor.


## Uso



El api esta basado en el modelo de autenticación JWT
El token se genera haciendo un llamadao `POST` utilizando los siguientes headers:

`
x-token:"gAAAAABjm11ka8Kh5AgxWxB12Awwh31fe83qGs1TLG5atIHFBBZmabjFufJ3-J1SIRkv2n2i3VwNXgqk3tbfzUznlQOF0xKErA==",
x-api-key:"gAAAAABjm4YLsCwWHqZXSNZr6PCEuBSIGChznJjWGWJSBJcwkCBENNM5gi0u791D773Rynov4T10LwwfAfM2cECzOJlkSK8bgehtmmdUAlSBy5a8N3HIl0w=",
x-secret-id: "gAAAAABjm120N7cjeEbPm48tI1kcfaxW9fuK2K1O56ylLBiXFyMQkKESnXgsKCmEs2qg3t2ACtmjtnavmg8K_t58PlsKfHZ2azWt5lrpqd0mlKkR-oFLBV4="
`

En este enpoint se va ha generar un token del tipo bearer token: **Estos token tiene tiempo de expiración de 10 dias.

`eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ4X3Rva2VuIjoiZ0FBQUFBQmptMTFrYThLaDVBZ3hXeEIxMkF3d2gzMWZlODNxR3MxVExHNWF0SUhGQkJabWFiakZ1ZkozLUoxU0lSa3YybjJpM1Z3TlhncWszdGJmelV6bmxRT0YweEtFckE9PSIsInhfYXBpX2tleSI6ImdBQUFBQUJqbTRZTHNDd1dIcVpYU05acjZQQ0V1QlNJR0Noem5KaldHV0pTQkpjd2tDQkVOTk01Z2kwdTc5MUQ3NzNSeW5vdjRUMTBMd3dmQWZNMmNFQ3pPSmxrU0s4YmdlaHRtbWRVQWxTQnk1YThOM0hJbDB3PSIsInhfc2VjcmV0X2lkIjoiZ0FBQUFBQmptMTIwTjdjamVFYlBtNDh0STFrY2ZheFc5ZnVLMksxTzU2eWxMQmlYRnlNUWtLRVNuWGdzS0NtRXMycWczdDJBQ3RtanRuYXZtZzhLX3Q1OFBsc0tmSFoyYXpXdDVscnBxZDBtbEtrUi1vRkxCVjQ9IiwiZXhwIjoxNjcyMDYyMDE1fQ.6DuI0K4YSRho6KFSHFt7zXYerS-7hM1OcMhqaaXrY7c`
***

`POST https://fastapimongo-43tleytuxq-uc.a.run.app/api/generate_token`

***

## Endpoints

Para utilizar los diferentes endpoints de la API, exceptuando `/api/generate_token`,  es `requerido` utilizar para cada una de ellas el `headers authorization` y pasarle un token.


 [documentación oficial de la API ](https://fastapimongo-43tleytuxq-uc.a.run.app)

Dado un user, para conocer las vacantes que podrían ajustarse a su perfil, se debe utilizar el endpoint GET /api/searches_vacancies/{user_id}, solo basta con pasarle el user_id y este genera las vancantes compatibles.


