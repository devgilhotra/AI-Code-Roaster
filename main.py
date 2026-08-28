# AI Code Roaster

from google import genai 
from dotenv import load_dotenv
import os 

# .env file load karege

load_dotenv()

# step 1 --> ccreate gemini function
def setup_gemini():
    """
    gemini client bnayege
    """
    # API key lo laayenge enviroment se

    api_key = os.getenv("GEMINI_API")

    # Check akro api mili yah nhi 
    if not api_key:
        print("Error:Gemini API Key not available") 
        exit()

    # client bnayege and return karenge
    client = genai.Client(api_key=api_key)
    return client


# step 2
def get_code_from_user():
    """
    hum yah par user se uska code lenge
    """
    print("\n" + "=" * 40)
    print("Apna code paste karo")
    print("Code finish hone ke baad END likho")
    print("=" * 40)

    # code lines store karne ke liye

    code_lines = []

    # baar baar lines lo end aaney tak 

    # while loop is infinte loop
    # user code dega, humey nhi pta user ke code mei kitne line hai 
    while True:
        # ek line lo user se 
        line = input("> ")

        # end aya band karo
        # strip is used to remove extra spaces from start and end of line 
        # user kuch bhi likhe usko upper case mei convert krdo
        # break means while loop ko end krdo
        if line.strip().upper() == "END":
            break 

        # line store laro

        code_lines.append(line)

        # sab lines ek string mei jodo

        # list ke jo bhi lines mil rhe hai usko join krdo ek hi string mei 
        complete_code = "\n".join(code_lines)
    return complete_code 

    
# step 3
# gemini se roast kar veyege

def roast_code(client, code):
    """
    gemeini se roast karvayege
    """
    prompt = f"""

    tu ek expert python developer hai
    jo funny style mei code review karta hai 

    neeche diya gya python code dekh

    '''python
    {code}
'''

ab yeh karo:
1. Roast funny style code main
iski kamiya btao hindi aur english mix karke. Emoji bhi use kr skte ho 
aur genuine mistakes ko point out kro

2. Better code - sahi tarik dikhao
explain karo kyu better haai yeeh

3. Level - btao yeh code hau
Beginner / Intermediate / Advannced

4. Score - 1 to 10 mein score do

Format exactly yeh rakho
🔥 Roast:
[roast yaha par]

Better code
(better code yahan par)

level : [level]

[motivational line]
"""

    # gemini ko prompt do
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents = prompt
    )

    return response.text

# step 4 result print karo 
def print_result(roast):
    """
    roast result nichey print karo
    """

    print("\n" + "=" *40)
    print("gemini ka roast")
    print("="*40)
    print(roast)
    print("\n"+"="*40)

# step 5
def ask_again():
    """
    user se dobara puchege
    """

    choice = input("\n Ek aur code roast karna hai kya (yes/no)")
    return choice.strip().lower() == "yes"

def main():
    """
    pura program run karege
    gemini setup karo
    """

    # gemini setup karo ek baar
    client = setup_gemini()

    # pheli baar sidha chlao

    # phir user ke marzi pr

    while True:
        # user se code lo
        code = get_code_from_user()

        # check karo - code empty toh nhi 

        # agar user nah kuch nhi likha enter dbaya tooh yel line print ho jayege
        if not code.strip():
            print("bhai kuch to likho")
            continue

        # roast karvao
        print("\n Gemini se poch rha hoon...")
        roast = roast_code(client,code)

        #result dikhao 
        print_result(roast)

        # dobara
        if not ask_again():
            print("\n Bye code likhte raho")
            break


main()