class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions = [
    Question("What is the capital of France?\n(a) Paris\n(b) Rome\n(c) Berlin\n", "a"),
    Question("Who wrote 'Romeo and Juliet'?\n(a) William Shakespeare\n(b) Jane Austen\n(c) Charles Dickens\n", "a"),
    Question("What is 2 + 2?\n(a) 3\n(b) 4\n(c) 5\n", "b")
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt).lower()
        if answer == question.answer:
            score += 1
    print(f"You got {score}/{len(questions)} correct.")

def main():
    run_quiz(questions)

if __name__ == "__main__":
    main()
