import os
import dspy
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure DSPy with Gemini and tracking enabled
dspy.settings.configure(
    lm=dspy.LM(
        f"gemini/{os.getenv('GEMINI_MODEL')}",
        api_key=os.getenv("GEMINI_API_KEY"),
        cache=False,
    ),
    track_usage=True,
)


# Define a simple program that makes multiple LM calls
class MyProgram(dspy.Module):
    def __init__(self):
        self.predict1 = dspy.ChainOfThought("question -> answer")
        self.predict2 = dspy.ChainOfThought("question, answer -> score")

    def __call__(self, question: str) -> str:
        answer = self.predict1(question=question)
        score = self.predict2(question=question, answer=answer)
        return score


def main():
    # Run the program and check usage
    program = MyProgram()
    output = program(question="hi what is your model?")
    print("Output:", output)
    print("Token Usage:", output.get_lm_usage())


if __name__ == "__main__":
    main()
