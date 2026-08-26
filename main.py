from langchain.agents import AgentExecutor

from orquestador import AgenteOrquestador


def main():
    agente = AgenteOrquestador()
    ejecutor = AgentExecutor(
        agent=agente.agente,
        tools=agente.tools,
        verbose=True,
        handle_parsing_errors=True,
    )

    pregunta = "Realiza el análisis de la imagen ejemplo_grafico.jpg"
    respuesta = ejecutor.invoke({"input": pregunta})

    print(respuesta["output"])


if __name__ == "__main__":
    main()
