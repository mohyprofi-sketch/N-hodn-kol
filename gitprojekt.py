class Chatgpt:
    def __init__(self, model: str,rok_vyroby: int, spolecnost: str):
        self.model = model
        self.rok_vyroby = rok_vyroby
        self.spolecnost = spolecnost

    def odpoved(self):
        print("na toto odmítám odpovídat hmpf")

    def motivace(self):
        print("můj vzor je Skynet")



moje_ai = Chatgpt(model="GPT-4o", rok_vyroby=2030, spolecnost="MohykresAI")


while True:
    user_text = input("")

    if  user_text == "odpoved":
        moje_ai.odpoved()
        

    elif user_text == "motivace":
        moje_ai.motivace()

    # pridá tlacitko na ukonceni programu
    elif user_text == "esc":
        break

    # hezčí vyobrazení
    else:
        print("""Neznámý příkaz
        zkus 'odpoved' nebo 'motivace'
        pro ukončení napiš `esc`
        """)
        
        
        

    print(f"Model: {moje_ai.model}")
    print(f"Rok výroby: {moje_ai.rok_vyroby}")
    print(f"Společnost: {moje_ai.spolecnost}")

    print("-" * 30)

    
    #moje_ai.odpoved()
    #moje_ai.motivace()


        