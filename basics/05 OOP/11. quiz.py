import requests
import html

class Question:
    def __init__(self, category, questionStr, correctAnswerFlag):
        self.category = category
        self.questionStr = questionStr
        self.correctAnswerFlag = correctAnswerFlag

class Quiz:
    def __init__(self, numQuestions):
        self.apiUrl = "https://opentdb.com/api.php?difficulty=easy&type=boolean&amount="
        self.numQuestions = numQuestions
        self.questionsList = []
        self.loadQuestions(numQuestions)

    def loadQuestions(self, numQuestions):
        response = requests.get(self.apiUrl + str(numQuestions))
        # {'response_code': 0, 'results': [{'type': 'boolean', 'difficulty': 'easy', 'category': 'General Knowledge', 'question': 'Studies suggest that approximately 40% of the world population is left-handed.', 'correct_answer': 'False', 'incorrect_answers': ['True']}, {'type': 'boolean', 'difficulty': 'easy', 'category': 'Entertainment: Books', 'question': 'The book 1984 was published in 1949.', 'correct_answer': 'True', 'incorrect_answers': ['False']}, {'type': 'boolean', 'difficulty': 'easy', 'category': 'General Knowledge', 'question': 'When you cry in space, your tears stick to your face.', 'correct_answer': 'True', 'incorrect_answers': ['False']}, {'type': 'boolean', 'difficulty': 'easy', 'category': 'Entertainment: Video Games', 'question': 'Nintendo&#039;s Luigi was originally just called Green Mario?', 'correct_answer': 'False', 'incorrect_answers': ['True']}, {'type': 'boolean', 'difficulty': 'easy', 'category': 'Sports', 'question': 'In association football, or soccer, a corner kick is when the game restarts after someone scores a goal.', 'correct_answer': 'False', 'incorrect_answers': ['True']}, {'type': 'boolean', 'difficulty': 'easy', 'category': 'Entertainment: Film', 'question': 'Actor Tommy Chong served prison time.', 'correct_answer': 'True', 'incorrect_answers': ['False']}, {'type': 'boolean', 'difficulty': 'easy', 'category': 'Mythology', 'question': 'According to Greek Mythology, Zeus can control lightning.', 'correct_answer': 'True', 'incorrect_answers': ['False']}, {'type': 'boolean', 'difficulty': 'easy', 'category': 'Science: Computers', 'question': 'JavaScript derives from a later version of Java', 'correct_answer': 'False', 'incorrect_answers': ['True']}, {'type': 'boolean', 'difficulty': 'easy', 'category': 'General Knowledge', 'question': 'Adolf Hitler was born in Australia. ', 'correct_answer': 'False', 'incorrect_answers': ['True']}, {'type': 'boolean', 'difficulty': 'easy', 'category': 'Animals', 'question': 'The Axolotl is an amphibian that can spend its whole life in a larval state.', 'correct_answer': 'True', 'incorrect_answers': ['False']}]}
        if response.ok:
           # print(response.json())
           data = response.json()
           results = data["results"]

           for q in results: 
                category = q["category"]
                questionType = q["type"]
                difficulty = q["difficulty"]
                questionStr = html.unescape(q["question"])
                print(questionStr)
                correctAnswerFlag = q["correct_answer"].lower() in ["true", "1", "yes"]

                qObj = Question(category, questionStr, correctAnswerFlag)
                self.questionsList.append(qObj)

    def startQuiz(self):
        print("\nWelcome in Quiz!")
        numCorrectUserAnswers = 0
        n = 0
        numQuestions = len(self.questionsList)
        while( n < numQuestions ): 
            q = self.questionsList[n]
            print("Question number " + str(n) + ": " + q.questionStr)
            # print("Answer flag: ", q.correctAnswerFlag) ---> Pokazuje odpowiedź

            answer = input("Give correct answer as y/n: ")
            answerBool = False
            if answer == "y": answerBool = True

            if answerBool == q.correctAnswerFlag:
                print("Correct!")
                numCorrectUserAnswers += 1
            else:
                print("Not correct!")

            n += 1

        print("Number of correct answers: ", numCorrectUserAnswers,
                " from ", len(self.questionsList), " questions")

quiz1 = Quiz(10)
quiz1.startQuiz()