import requests
from easygui import *
import json
from rich import print_json
from rich.console import Console



def display_data(data):
    x=json.loads(data)["result"]
    console = Console()
   
    console.print("Top Result",style="bold magenta",justify="center")
    print_json(json.dumps(x[0]),indent=4)
    print("\n")
    
    console.print("Other Results",style="bold magenta",justify="center")
    for i in range(1,len(x)):
        
        print_json(json.dumps(x[i]),indent=4)
        print("\n")

def main():

    text = "Welcome to ani-search"

    title = "ani-search"

    button_list = []

    button_list.append("Upload a file")
    button_list.append("Url")
    output = buttonbox(text, title, button_list)


    #print(output)

    if output == "Upload a file":
        f= fileopenbox()



        files = {"files":open(f,'rb')}

        url = "https://api.trace.moe/search?cutBorders&"

        r=requests.post(url,files=files)
        
        display_data(r.text)
        
    else:
        #create an url ennter box in easygui
        text = "Enter the url"
        title = "ani-search"
        
        url = enterbox(text, title)
        
        r=requests.get(
            'https://trace.moe/image-proxy?url='+url,
            headers={
                'referer': 'https://trace.moe/'+url,
            }
            )
        x=requests.post("https://api.trace.moe/search?cutBorders&",files={"files":r.content})
        display_data(x.text)
        

if __name__ == "__main__":
    main()