class CustomerChatbot:
    
    def __init__(self):
        self.responses={
            
            "store hours":"hdjkbdjkf",
            "store location":"jdjfjewhfe",
            "return policy":"bhfdfhdj",
            "products":"ghddjsg",
            "support":"dbdbdaj",
            "payment":"hshbdjs",
            "bye":"byeeeee"
        }
    def get_response(self,user_input):
        
        user_input=user_input.lower()
        
        for key in self.responses:
            if key in user_input:
                return self.responses[key]
                
        return "sorry tey again .didnt understand"
        
    def start_response(self):
        print("welcome")
        
        while True:
            user_input=input("You:")
            if "bye" in user_input.lower():
                print("chatbot:"+self.responses["bye"])
                break
            else:
                print("cahtbot:"+self.responses[user_input])
                
chatbot=CustomerChatbot()
chatbot.start_response()
            