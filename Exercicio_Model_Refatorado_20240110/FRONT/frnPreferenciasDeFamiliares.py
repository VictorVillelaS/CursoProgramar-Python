import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter.simpledialog import askstring
from MODELS.preferenciasVO import PreferenciasVO
from MODELS.familiaresVO import FamiliaresVO
from BLL.preferenciasDeFamiliaresBLL import PreferenciasDeFamiliares


class FrmPreferenciasDeFamiliares(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.btnWidth = 20
        self.btnPadY = 5
        self.btnPadX = 10

        self.frmBotoes = tk.Frame(self)
        self.frmBotoes.pack(side='left')

        self.btnConsultarFamiliar = tk.Button(self.frmBotoes, width=self.btnWidth, bg='grey', text="Consultar",
                                              command=self.importarPreferenciasFamiliares)
        self.btnConsultarFamiliar.pack(side='top', padx=self.btnPadX, pady=self.btnPadY)

        self.btnAdicionarFamiliar = tk.Button(self.frmBotoes, width=self.btnWidth, bg='grey', text="Adicionar",
                                              command=self.addPreferenciaFamiliar)
        self.btnAdicionarFamiliar.pack(side='top', padx=self.btnPadX, pady=self.btnPadY)

        self.btnEditarFamiliar = tk.Button(self.frmBotoes, width=self.btnWidth, bg='grey', text="Editar",
                                           command=self.editarPreferenciaFamiliar)
        self.btnEditarFamiliar.pack(side='top', padx=self.btnPadX, pady=self.btnPadY)

        self.btnRemoverFamiliar = tk.Button(self.frmBotoes, width=self.btnWidth, bg='grey', text="Remover",
                                            command=self.removerPreferenciaFamiliar)
        self.btnRemoverFamiliar.pack(side='top', padx=self.btnPadX, pady=self.btnPadY)

        # Configurações da tabela para visualizar os dados
        self.cols = ["ID Familiar", "ID Preferencia", "Intensidade", "Observacao"]
        self.colsSize = [100, 100, 100, 100]
        self.colsAnchor = [tk.CENTER, tk.CENTER, tk.CENTER, tk.W]

        # Declaração da tabela e atribuição das propriedades de cada coluna
        self.treeview = ttk.Treeview(self, columns=self.cols, height=6, show='headings')
        self.treeview.pack(side='left')

        for i in range(len(self.cols)):
            self.treeview.heading(self.cols[i], text=self.cols[i])
            self.treeview.column(self.cols[i], width=self.colsSize[i], anchor=self.colsAnchor[i])

        self.importarPreferenciasFamiliares()

    def importarPreferenciasFamiliares(self):
        try:
            linhas = PreferenciasDeFamiliares().importPreferenciasFamiliares()
            self.treeview.delete(*self.treeview.get_children())
            for linha in linhas:
                values = [linha.objFamiliar.id, linha.objPreferencia.id, linha.intensidade, linha.observacao]
                self.treeview.insert('', 'end', values=values)
        except Exception as e:
            raise e

    def addPreferenciaFamiliar(self):
        pass

    def editarPreferenciaFamiliar(self):
        pass

    def removerPreferenciaFamiliar(self):
        pass