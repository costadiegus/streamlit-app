from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from llm import llama_3

# Uncomment the following line to use an example of a custom tool
# from agencia_noticias.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import ScrapeWebsiteTool

# from langchain_community.tools import DuckDuckGoSearchRun
# scrape_tool = DuckDuckGoSearchRun()

from crewai_tools import ScrapeWebsiteTool
from crewai_tools import SerperDevTool

scrape_tool = ScrapeWebsiteTool()
search_tool = SerperDevTool()


@CrewBase
class StreamlitAppCrew:
    """StreamlitApp crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def assistente(self) -> Agent:
        return Agent(
            config=self.agents_config["assistente"],
            # tools=[scrape_tool, search_tool,],
            llm=llama_3,
            # tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
            verbose=True,
        )

    @task
    def assistencia_task(self) -> Task:
        return Task(
            config=self.tasks_config["assistencia_task"], agent=self.assistente()
        )

    @crew
    def crew(self) -> Crew:
        """Creates the StreamlitApp crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            max_rpm=30,
        )
