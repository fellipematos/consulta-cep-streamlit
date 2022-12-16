import customtkinter
import httpx

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("350x500")

textVariable = customtkinter.StringVar()

def getCep():
    if len(entryCep.get()) != 9:
        textVariable.set('Digite o um CEP válido!')
    else:
        entryCep.get().replace("-", "")
        request = httpx.get(f'https://brasilapi.com.br/api/cep/v2/{entryCep.get()}')
        adress_data = request.json()
        if 'code' not in adress_data:

            cep = adress_data["cep"]
            logradouro = adress_data["street"]
            bairro = adress_data["neighborhood"]
            localidade = adress_data["city"]
            uf = adress_data["state"]
            
            textVariable.set(f"{logradouro}\n{bairro}\n{localidade} - {uf}\n{cep}")     
        else:
            textVariable.set('CEP não encontrado')
            
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=12, padx=20, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="DIGITE O CEP", font=("Roboto", 24, "bold"))
label.pack(pady=30, padx=10)

entryCep = customtkinter.CTkEntry(master=frame, placeholder_text="00000-000", width=180)
entryCep.pack(pady=30, padx=10)

button = customtkinter.CTkButton(master=frame, text="BUSCAR", command=getCep, width=160)
button.pack(pady=30, padx=20)

labelResponse = customtkinter.CTkLabel(master=frame, textvariable=textVariable, font=("Roboto", 18))
labelResponse.pack(pady=25, padx=15)


root.mainloop()
