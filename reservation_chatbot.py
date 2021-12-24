# class Reserve():
#     def __init__(self):
            
#         self.specializations = ['internal' , 'cardiology'  , 'physical therapy']
#         self.doctors = ['Ahmed Ali' , 'Nada Nader' , 'Ramy Medhat' , 'Sara Magdy' , 'Tamer Hassan' , 'Ola Adel'] 

#         self.doc = {
#             'Ahmed Ali' : ['Sat 6.00:9.00 pm' , 'Mon 5.00:7.00 pm'] ,
#             'Nada Nader' : ['Sun 5.30:8.00 pm' , 'Wed 6.00:8.00 pm'] ,
#             'Ramy Medhat' : ['Tues 7.00:9.00 pm' , 'Thur 3.30:6.00 pm'] ,
#             'Sara Magdy' : ['Sat 6.00:9.00 pm' , 'Mon 5.00:7.00 pm'],
#             'Tamer Hassan' : ['Tues 7.00:9.00 pm' , 'Thur 3.30:6.00 pm'] ,
#             'Ola Adel' : ['Sun 5.30:8.00 pm' , 'Wed 6.00:8.00 pm'] 
#         }

#         self.spec = {
#             'internal' : ['Ahmed Ali' , 'Nada Nader'] ,
#             'cardiology' : ['Ramy Medhat' , 'Sara Magdy']  , 
#             'physical therapy' : ['Tamer Hassan' , 'Ola Adel']
#         }

#     def reply(self,msg):
        
#         if msg == 'start':
#             return (f' Please choose one specialization from {self.specializations} ')
        
#         for i in len(self.specializations):
#             if msg ==  self.specializations[i] :
#                 self.specialization = self.spec[msg]
#                 return (f' Please choose one doctors from {self.spec[msg]} ')
            
            
#         for i in len(self.doctors):
#             if  msg ==  self.doctors[i] :
#                 self.doctor = self.doc[msg]
#                 return (f' Please choose a suitable day from {self.doc[msg]} ')
        
#         if msg == 'sat' | 'sun' | 'mon' | 'tues' | 'wed' | 'thur' :
#             return (f'your reservation is with Dr.{self.doctor} in {self.specialization} specialization, on {msg}day ')
               
            
        
import nltk
from nltk.chat.util import Chat, reflections

reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}



pairs = [
    # [
    #     r"my name is (.*)",
    #     ["Hello %1, How are you today ?",]
    # ],
    [
        r"hi|hey|hello",
        ["Hello, please enter one of the following specializations\n 'internal' \n 'cardiology' \n 'physical therapy' \n  ",]
    ], 
    [
        r"internal",
        ["Available doctors: \n'Ahmed Ali' \n'Nada Nader'",]
    ],
    [
        r"cardiology",
        ["Available doctors: \n'Ramy Medhat'\n'Sara Magdy'",]
    ],
    [
        r"physical therapy",
        ["Available doctors: \n'Tamer Hassan' \n'Ola Adel'",]
    ],
    [
        r"'Ahmed Ali' |  ",
        ["at 6.00:9.00 pm \n Mon 5.00:7.00 pm \n",]
    ],
    [
        r"Nada Nader",
        ["Tues 7.00:9.00 pm\n Thur 3.30:6.00 pm \n",]
    ],
    [
        r"Ramy Medhat",
        ["Sun 5.30:8.00 pm \nWed 6.00:8.00 pm \n",]
    ],
    [
        r"Sara Magdy",
        ["Sat 6.00:9.00 pm \n Mon 5.00:7.00 pm \n",]
    ],
    [
        r"Tamer Hassan",
        ["Tues 7.00:9.00 pm\n Thur 3.30:6.00 pm \n",]
    ],
    [
        r"Ola Adel",
        ['Sun 5.30:8.00 pm\n Wed 6.00:8.00 pm \n',]
    ],
    [
        r"Sat|sat|saturday|Saturday",
        ["Sat 6.00:9.00 pm\nplease enter <ok> or <confirm> \n "]
    ],
    [
        r"Sun|sun|sunday|Sunday",
        ['Sun 5.30:8.00 pm\nplease enter <ok> or <confirm> \n ',]
    ],
    [
        r"Mon|mon|Monday|monday",
       ['Mon 5.00:7.00 pm\nplease enter <ok> or <confirm> \n ',]
    ],
    [
        r"Tues|tues|Tuesday|tuesday",
        ['Tues 7.00:9.00 pm\nplease enter <ok> or <confirm> \n ',]
    ],
    [
        r"Wednesday|wednesday|Wed|wed",
        ['Wed 6.00:8.00 pm\nplease enter <ok> or <confirm> \n ',]
    ],
    [
        r"Thur|thur|Thuresday|thuresday",
        ['Thur 3.30:6.00 pm \nplease enter <ok> or <confirm> or <quit> \n ',]
    ],
    [
        r"quit|exit",
        ["Bye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"ok|confirm",
        ["your reservation is done"]
    ],
]

def chat(msg):
    # print("Hi! I am a chatbot created by Biomedical engineers for your service")
    chat = Chat(pairs, reflections)
    # chat.converse()
    response  = chat.respond(msg)
    # print(str(response))
    return str(response)
#initiate the conversation
if __name__ == "__main__":
    print("Hi! I am a chatbot created by Biomedical engineers for your service")
    chat("hi")
            