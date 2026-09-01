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

    pregunta = "explicame que es la IA de forma breve"
    respuesta = ejecutor.invoke({"input": pregunta})

    print(respuesta["output"])


if __name__ == "__main__":
    main()
