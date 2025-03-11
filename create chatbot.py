import random

class AIAgentChatBot:
    def __init__(self):
        self.goal = 'Provide assistance and help with questions.'
        self.responses = {
            'hello': 'Hi there ! How can i assist you today ?',
            'how are you': 'i am just a chatbot, but iam doing great ! how can i help?',
            'bye': 'Goodbye! have a nice day',
            'what is your goal': 'My goal is to provide assistance, answer questions and help with tasks',
            'default': 'i am sorry, i did not quite understand that . Can you rephrase'
        }

    def get_percept(self, user_input):
        tokens = user_input.lower().strip().split()
        return ' '.join(tokens)
    
    def update_goal(self, new_goal):
        self.goal = new_goal
        return f"Goal updated to: {self.goal}"
    
    def learn_response(self, key, response):
        self.responses[key] = response
        return f"Learned response for '{key}'"
    
    def process_action(self, user_input):
        if user_input.startswith("goal:"):
            new_goal = user_input[len("goal:"):].strip()
            return self.update_goal(new_goal)
        if user_input.startswith("learn:"):
            try:
                _, pair = user_input.split("learn:", 1)
                key, response = pair.split("=>")
                return self.learn_response(key.strip(), response.strip())
            except Exception:
                return "Learning command format error. Use: learn: key => response"
        response = self.responses.get(user_input, self.responses['default'])
        return response
    
    def process_nlp(self, user_input):
        return user_input

    def environment(self):
        print('Your are in a chat with an AI Agent')
    
    def communicate(self):
         self.environment()
         while True:
            user_input = input('You: ')
            percept = self.get_percept(user_input)
            percept = self.process_nlp(percept)
            if percept == 'bye':
                    print('AI Agent: Goodbye! Take care')  
                    break
            response = self.process_action(percept)
            print('AI Agent:', response)
    
if __name__ == '__main__':
    agent = AIAgentChatBot()
    agent.communicate()