import openai


openai.api_key = "ENTER YOUR KEY HERE"

if openai.api_key == "ENTER YOUR KEY HERE":
    
    input("Please enter your key on line 6 in this file, variable openai.api_key")
    
model_engine = "text-davinci-003"

def main():
    
    print("Enter prompt below:\n")
    
    while True:
        
        userInput = input(">> ")
        
        response = generateResponse(userInput)
        
        print(response, "\n")
        
        
def generateResponse(prompt):
    
    completion = openai.Completion.create (
        
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
    )
    
    response = completion.choices[0].text
    
    return response


if __name__ == "__main__":
    
    main()
