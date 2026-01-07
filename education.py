class EducationAgent:

    def identify_subject(self, question):
        q = question.lower()

        if "derivative" in q or "integral" in q:
            return "Mathematics"
        elif "force" in q or "newton" in q:
            return "Physics"
        elif "acid" in q or "base" in q:
            return "Chemistry"
        else:
            return "General"

    def generate_answer(self, question):
        subject = self.identify_subject(question)

        if subject == "Mathematics":
            return "This is a Maths question. I will solve it step by step."
        elif subject == "Physics":
            return "This is a Physics question. I will explain using laws and formulas."
        elif subject == "Chemistry":
            return "This is a Chemistry question. I will explain reactions and concepts."
        else:
            return "I am analyzing your question."