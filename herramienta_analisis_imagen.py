import ast

from langchain.tools import BaseTool
from langchain_google_genai import ChatGoogleGenerativeAI
from my_models import GEMINI_FLASH
from my_keys import GEMINI_API_KEY
from my_helper import encode_image
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from detalles_imagen import DetallesImagen


class HerramientaAnalisisImagen(BaseTool):
    name: str = "HerramientaAnalisisImagen"
    description: str = """
        Utiliza esta herramienta siempre que te sea solicitado realizar un análisis de una imagen.

        # ENTRADAS REQUERIDAS
        - 'nombre_imagen' (str): Nombre de la imagen a ser analizada con extensión JPG.
        Ejemplo: test.jpg o test.jpeg
    """
    return_direct: bool = False

    def _run(self, accion):
        try:
            accion = ast.literal_eval(accion)
        except (SyntaxError, ValueError):
            accion = {"nombre_imagen": accion}

        if not isinstance(accion, dict):
            raise ValueError("La entrada debe incluir el nombre de la imagen.")

        camino_imagen = accion.get("nombre_imagen", "")
        if not camino_imagen:
            raise ValueError("No se indicó el nombre de la imagen.")

        llm = ChatGoogleGenerativeAI(
            api_key=GEMINI_API_KEY,
            model=GEMINI_FLASH,
        )

        # =========================
        # 2. CODIFICAR IMAGEN
        # =========================
        imagen = encode_image(f"datos/{camino_imagen}")

        # =========================
        # 3. PROMPT PARA ANALIZAR IMAGEN
        # =========================
        template_analisis = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """
                    Asume que eres un analista de imágenes.
                    Tu principal tarea consiste en analizar una imagen
                    para extraer las informaciones más relevantes de manera objetiva.

                    # FORMATO DE SALIDA
                    Descripción de la imagen: Tu descripción de la imagen aquí.
                    Etiquetas: Una lista con 3 palabras clave separadas por comas.
                    """,
                ),
                (
                    "user",
                    [
                        {"type": "text", "text": "Describe la imagen:"},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{imagen}"
                            },
                        },
                    ],
                ),
            ]
        )

        # =========================
        # 4. CADENA DE ANÁLISIS
        # =========================
        cadena_analisis = template_analisis | llm | StrOutputParser()
        parser_json = JsonOutputParser(pydantic_object=DetallesImagen)

        # =========================
        # 5. ANALIZAR IMAGEN
        # =========================
        respuesta_analisis = cadena_analisis.invoke({})

        # =========================
        # 7. PROMPT PARA RESUMEN
        # =========================
        template_respuesta = PromptTemplate(
            template="""
            Genera un resumen utilizando un lenguaje claro y objetivo,
            enfocado en el público colombiano.

            La idea es que la comunicación del resultado sea lo más
            sencilla posible, priorizando los registros para consultas posteriores.

            # RESULTADO DEL ANÁLISIS DE LA IMAGEN
            {respuesta_analisis_imagen}

            # FORMATO DE SALIDA
            {formato_salida}
            """,
            input_variables=["respuesta_analisis_imagen"],
            partial_variables={
                "formato_salida": parser_json.get_format_instructions()
            },
        )

        # =========================
        # 8. CADENA DE RESUMEN
        # =========================
        cadena_resumen = template_respuesta | llm | parser_json

        # =========================
        # 9. GENERAR RESUMEN
        # =========================
        respuesta = cadena_resumen.invoke(
            {"respuesta_analisis_imagen": respuesta_analisis}
        )

        return str(respuesta)
