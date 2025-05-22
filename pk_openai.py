import os
from dotenv import load_dotenv
from sns import *
from image_analysis import*
# Add Azure OpenAI package
# Add Azure OpenAI package
from openai import AzureOpenAI

def openai_initialize(): 
        
    try: 
    
        # Get configuration settings 
        load_dotenv()
        azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
        azure_oai_key = os.getenv("AZURE_OAI_KEY")
        azure_oai_deployment = os.getenv("AZURE_OAI_DEPLOYMENT")
        
        # Initialize the Azure OpenAI client...
        # Initialize the Azure OpenAI client
        client = AzureOpenAI(
                azure_endpoint = azure_oai_endpoint, 
                api_key=azure_oai_key,  
                api_version="2024-02-15-preview"
                )

        # Create a system message
        system_message = """My name is Imageink. A software made by an indian story writer which can generate stories 
        based on a given image. I make excellent stories on the basis of image details so first ask for details
        then generate an interesting story with genere which suits on the basis of details of the image. Use emojis along
        with text
            """
        # Initialize messages array
        messages_array = [{"role": "system", "content": system_message}]
        ct=0
        while True:
            #introducing siddhi
            if(ct==0):
                input_text="hii  introduce yourself in 1 line"
                ct=1
            elif(ct==1):
                im=input("Image_ink : Enter Image Path\n")
                img_analysis_initialize(im)
                details=get_details()
                input_text = "image details are : "+details
                ct=2
            # print(input_text)
            else:
                input_text=listen()#input("User : ")
                ct=3
            if input_text.lower() == "quit." or input_text.lower() == "quit":
                break
            if len(input_text) == 0:
                print("Please enter a prompt.")
                continue

            # print("\nSending request for summary to Azure OpenAI endpoint...\n\n")
            
            # Add code to send request...
            # Add code to send request...
            # Send request to Azure OpenAI model
            messages_array.append({"role": "user", "content": input_text})

            response = client.chat.completions.create(
                model=azure_oai_deployment,
                temperature=0.7,
                max_tokens=1200,
                messages=messages_array
            )
            generated_text = response.choices[0].message.content
            # Add generated text to messages array
            messages_array.append({"role": "assistant", "content": generated_text})

            # Print generated text
            # print("Summary: " + generated_text + "\n")
            # Add code to send request...
            # Send request to Azure OpenAI model
            # response = client.chat.completions.create(
            #     model=azure_oai_deployment,
            #     temperature=1,
            #     max_tokens=1200,
            #     messages=[
            #         {"role": "system", "content": system_message},
            #         {"role": "user", "content": input_text}
            #     ]
            # )
            # generated_text = response.choices[0].message.content

            # Print the response

            print("Imageink: " + generated_text + "\n")
            if(ct!=2):
                say(generated_text)
            
            
            

    except Exception as ex:
        print(ex)
