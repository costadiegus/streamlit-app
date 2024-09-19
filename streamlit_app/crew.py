from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from llm import llama_3


@CrewBase
class PersonagemCrew:
    """Personagem crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    def __init__(self, personagem: str):
        """Construtor que recebe o alias do personagem"""
        self.personagem = personagem

    @agent
    def personagem_agent(self) -> Agent:
        return Agent(
            config=self.agents_config[self.personagem],
            # tools=[scrape_tool, search_tool,],
            llm=llama_3,
            # tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
            verbose=True,
        )

    @task
    def assistencia_task(self) -> Task:
        agente = self.personagem_agent()
        agent_params = vars(agente)
        print(agent_params)
        return Task(config=self.tasks_config["assistencia_task"], agent=agente)

    @crew
    def crew(self) -> Crew:
        """Creates the Personagem crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            max_rpm=30,
        )
