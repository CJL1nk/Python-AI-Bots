import openai


openai.api_key = "ENTER YOUR KEY HERE"

if openai.api_key == "ENTER YOUR KEY HERE":
    
    input("Please enter your key on line 6 in this file, variable openai.api_key")
    
model_engine = "gpt-3.5-turbo"

def main():
    
    print("Enter prompt below:\n")
    
    message = {"role": "user", "content": input(">> ")}
    
    conversation = [{"role": "system", "content": "DIRECTIVE_FOR_gpt-3.5-turbo"}]
    
    while True:
        
        conversation.append(message)
        
        response = generateResponse(conversation)
        print("\n", response.choices[0].message.content, "\n")
        
        message['content'] = input(">> ")
        conversation.append(response.choices[0].message)
        
        
def generateResponse(conversation):
    
    completion = openai.ChatCompletion.create ( 
    model = model_engine,
    messages = conversation
    )
    
    return completion


if __name__ == "__main__":
    
    main()