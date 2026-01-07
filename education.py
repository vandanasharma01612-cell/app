class EducationAI:

    def get_subject(self, question):
        q = question.lower()

        if any(word in q for word in ["derivative", "integral", "limit"]):
            return "Mathematics"
        elif any(word in q for word in ["newton", "force", "motion"]):
            return "Physics"
        elif any(word in q for word in ["acid", "base", "reaction"]):
            return "Chemistry"
        else:
            return "General"

    def generate_answer(self, question):
        subject = self.get_subject(question)

        if subject == "Mathematics":
            return (
                "📘 Subject: Mathematics\n\n"
                "Let us solve this step by step:\n"
                "1. Understand the given problem\n"
                "2. Identify the correct formula\n"
                "3. Apply the formula carefully\n"
                "4. Simplify and write final answer\n\n"
                "✅ This is the standard method used in exams."
            )

        elif subject == "Physics":
            return (
                "📗 Subject: Physics\n\n"
                "Explanation:\n"
                "1. Identify physical quantities\n"
                "2. Write the relevant law\n"
                "3. Substitute values\n"
                "4. Get the result with unit\n\n"
                "✅ This approach is used in board & competitive exams."
            )

        elif subject == "Chemistry":
            return (
                "📙 Subject: Chemistry\n\n"
                "Explanation:\n"
                "1. Identify type of reaction\n"
                "2. Write balanced chemical equation\n"
                "3. Explain the process\n"
                "4. Conclude the result\n\n"
                "✅ This format is exam-oriented."
            )

        else:
            return (
                "📚 Education AI Response\n\n"
                "Please ask a question related to:\n"
                "- Mathematics\n"
                "- Physics\n"
                "- Chemistry\n\n"
                "I will explain it like a teacher 🙂"
            )