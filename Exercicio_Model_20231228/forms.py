import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from preferenciasBLL import Familiares
from FamiliaresVO import FamiliaresVO


class BuilderEntry(tk.Frame):
    def __init__(self, master, labelText, entryWidth=20, varType=str, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.entryVar = tk.StringVar()
        self.varType = varType
        
        self.label = tk.Label(self, text=labelText, anchor='w')
        self.label.pack(side='top', fill='x')
        
        self.entry = tk.Entry(self, textvariable=self.entryVar, width=entryWidth)
        self.entry.pack(side='bottom', anchor='w')
    
    def get(self):
        value = self.entry.get()
        try:
            return(self.varType(value))
        except(ValueError, TypeError):
            return None
    
    def set(self, value):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, value)


class BuilderCombobox(tk.Frame):
    def __init__(self, master, labelText, comboboxValues, comboboxWidth=20,*args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.comboboxVar = tk.StringVar()

        self.label = tk.Label(self, text=labelText, anchor='w')
        self.label.pack(side='top', fill='x')

        self.combobox = ttk.Combobox(self, textvariable=self.comboboxVar, values=comboboxValues, width=comboboxWidth)
        self.combobox.pack(side='bottom')
    
    def get(self):
        return self.combobox.get()
    
    def set(self, valor):
        self.combobox.set(valor)


class FormAddFamiliar(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.padx = 5
        self.pady = 5
        self.title("Adicionar Cliente")

        self.entryNome = BuilderEntry(self, "Nome")
        self.entryNome.pack(side='top', padx=self.padx, pady=self.pady)
        
        self.comboboxSexo = BuilderCombobox(self, "Sexo", ["Homem", "Mulher", "Outro"])
        self.comboboxSexo.pack(side='top', padx=self.padx, pady=self.pady, fill='x')

        self.entryIdade = BuilderEntry(self, "Idade", varType=int)
        self.entryIdade.pack(side='top', padx=self.padx, pady=self.pady)

        self.entrySalario = BuilderEntry(self, "Salario", varType=int)
        self.entrySalario.pack(side='top', padx=self.padx, pady=self.pady)

        self.entryFavorito = BuilderEntry(self, "Favorito")
        self.entryFavorito.pack(side='top', padx=self.padx, pady=self.pady)

        self.btnSave = tk.Button(self, text="Salvar", width=10, command=self.addFamiliar)
        self.btnSave.pack(side='top', padx=self.padx, pady=self.pady)

        self.mainloop()

    def addFamiliar(self):
        if messagebox.askokcancel("Confirmar mudança", "Tem certeza que quer adicionar esse familiar?") is True:
            try:
                nome = self.entryNome.get()
                sexo = self.comboboxSexo.get()
                idade = self.entryIdade.get()
                salario = self.entrySalario.get()
                favorito = self.entryFavorito.get()

                objFamiliaresVO = FamiliaresVO(nome=nome, sexo=sexo, idade=idade, salario=salario, favorito=favorito)
                Familiares().adicionarFamiliar(objFamiliaresVO)
            except Exception as e:
                messagebox.showinfo("Erro", str(e))
            else:
                messagebox.showinfo("Sucesso", "Familiar adicionado com sucesso")
                self.destroy()


class FormEditFamiliar(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.padx = 10
        self.pady = 5
        self.title = "Editar Cliente"

        self.id = BuilderEntry(self, "ID")
        self.id.pack(side='top', padx=self.padx, pady=self.pady)
        self.id.entry.bind("<KeyRelease>", self.atualizarInformacoes)

        self.entryNome = BuilderEntry(self, "Nome")
        self.entryNome.pack(side='top', padx=self.padx, pady=self.pady)
        
        self.comboboxSexo = BuilderCombobox(self, "Sexo", ["Homem", "Mulher", "Outro"])
        self.comboboxSexo.pack(side='top', padx=self.padx, pady=self.pady)

        self.entryIdade = BuilderEntry(self, "Idade", varType=int)
        self.entryIdade.pack(side='top', padx=self.padx, pady=self.pady)

        self.entrySalario = BuilderEntry(self, "Salario", varType=int)
        self.entrySalario.pack(side='top', padx=self.padx, pady=self.pady)

        self.entryFavorito = BuilderEntry(self, "Favorito")
        self.entryFavorito.pack(side='top', padx=self.padx, pady=self.pady)

        self.btnSave = tk.Button(self, text="Editar", width=10, command=self.editFamiliar)
        self.btnSave.pack(side='top', padx=self.padx, pady=self.pady)

        self.mainloop()

    def atualizarInformacoes(self, event):
        print("update:")
        id = self.id.get()
        print(f"id = {id}")
        infocliente = Familiares().consultarBDFamiliares(id)

        if infocliente is not None:
            print(f"linha encontrada!:{infocliente}")
            self.entryNome.set(infocliente.nome)
            self.comboboxSexo.set(infocliente.sexo)
            self.entryIdade.set(infocliente.idade)
            self.entrySalario.set(infocliente.salario)
            self.entryFavorito.set(infocliente.favorito)
        else:
            print("nada encontrado.")
            print("")
            self.entryNome.set("")
            self.comboboxSexo.set("")
            self.entryIdade.set("")
            self.entrySalario.set("")
            self.entryFavorito.set("")            

    def editFamiliar(self):
        ID = self.id.get()
        nome = self.entryNome.get()
        sexo = self.comboboxSexo.get()
        idade = self.entryIdade.get()
        salario = self.entrySalario.get()
        favorito = self.entryFavorito.get()

        if messagebox.askokcancel("Confirmar edição", "Tem certeza que deseja editar esse familiar") is True:
            try:
                objFamiliaresVO = FamiliaresVO(ID, nome, sexo, idade, salario, favorito)
                Familiares().editarFamiliar(objFamiliaresVO)
                self.destroy()
            except Exception as e:
                raise e
