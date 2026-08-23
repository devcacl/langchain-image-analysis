from detalles_imagen import DetallesImagen
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_cohere import ChatCohere
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from langchain.globals import set_debug

from my_models import GEMINI_FLASH
from my_keys import GEMINI_API_KEY, COHERE_API_KEY
from my_helper import encode_image


set_debug(True)


# =========================
# 1. MODELO GEMINI
# =========================

llm = ChatGoogleGenerativeAI(
    api_key=GEMINI_API_KEY,
    model=GEMINI_FLASH
)


# =========================
# 2. CODIFICAR IMAGEN
# =========================

imagen = encode_image("datos/example_image.jpg")


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
            """
        ),
        (
            "user",
            [
                {
                    "type": "text",
                    "text": "Describe la imagen:"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{imagen}"
                    }
                }
            ]
        )
    ]
)


# =========================
# 4. CADENA DE ANÁLISIS
# =========================

cadena_analisis = (
    template_analisis
    | llm
    | StrOutputParser()
)

parser_json = JsonOutputParser(
    pydantic_object=DetallesImagen
)


# =========================
# 5. ANALIZAR IMAGEN
# =========================

respuesta_analisis = cadena_analisis.invoke({})

print("\n========== ANÁLISIS DE GEMINI ==========\n")
print(respuesta_analisis)


# =========================
# 6. MODELO COHERE
# =========================

#llm_cohere = ChatCohere(cohere_api_key=COHERE_API_KEY)


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

    #FORMATO DE SALIDA
    {formato_salida}
    """,
    input_variables=["respuesta_analisis_imagen"],
    partial_variables={
        "formato_salida":parser_json.get_format_instructions()
        }
)

# =========================
# 8. CADENA DE RESUMEN
# =========================

cadena_resumen = (
    template_respuesta
    | llm
    | parser_json
)


# =========================
# 9. GENERAR RESUMEN
# =========================

respuesta = cadena_resumen.invoke(
    {
        "respuesta_analisis_imagen": respuesta_analisis
    }
)


print("\n========== RESUMEN DE COHERE ==========\n")
print(respuesta)







