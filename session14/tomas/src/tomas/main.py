#!/usr/bin/env python
import warnings
from datetime import datetime
from pydantic import BaseModel
from crewai.flow import Flow, listen, start
from tomas.crew import TomasCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


class ResearchFlowState(BaseModel):
    """State model for the research flow"""
    topic: str = "AI LLMs"
    current_year: str = str(datetime.now().year)
    report: str = ""


class TomasFlow(Flow[ResearchFlowState]):
    """Main research flow orchestrating the crew execution"""

    @start()
    def prepare_topic(self, crewai_trigger_payload: dict | None = None):
        """Prepare the research topic from payload or use defaults"""
        if crewai_trigger_payload:
            self.state.topic = crewai_trigger_payload.get("topic", "AI LLMs")
        else:
            self.state.topic = "AI LLMs"
        
        self.state.current_year = str(datetime.now().year)
        print(f"🎯 Topic: {self.state.topic}")
        print(f"📅 Year: {self.state.current_year}")

    @listen(prepare_topic)
    def run_research(self):
        """Execute the research crew"""
        print(f"\n🔍 Starting research on: {self.state.topic}")
        result = TomasCrew().crew().kickoff(
            inputs={
                "topic": self.state.topic,
                "current_year": self.state.current_year
            }
        )
        self.state.report = result.raw
        print("✅ Research crew finished.")

    @listen(run_research)
    def save_report(self):
        """Confirm report saved"""
        print("\n📄 Report path: output/report.md")
        print("✨ Flow completed successfully!")


def kickoff():
    """Run the complete flow"""
    flow = TomasFlow()
    flow.kickoff()


def plot():
    """Plot the flow diagram"""
    flow = TomasFlow()
    flow.plot()


if __name__ == "__main__":
    kickoff()
