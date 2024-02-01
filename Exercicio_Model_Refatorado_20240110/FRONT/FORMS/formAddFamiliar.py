import tkinter as tk
from tkinter import messagebox
from BLL.familiaresBLL import FamiliaresBLL
from MODELS.familiaresVO import FamiliaresVO
from FRONT.builders import BuilderEntry, BuilderCombobox


class FormAddFamiliar(tk.Tk):
    def __init__(self, frmFront, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.frmFront = frmFront

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
                FamiliaresBLL().adicionarFamiliar(objFamiliaresVO)
            except Exception as e:
                messagebox.showinfo("Erro", str(e))
            else:
                messagebox.showinfo("Sucesso", "Familiar adicionado com sucesso")
                self.frmFront.importarFamiliares()
                self.destroy()