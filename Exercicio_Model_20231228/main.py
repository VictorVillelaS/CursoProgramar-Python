from front import *

app = tk.Tk()
tabControl = ttk.Notebook(app)

tab1 = FrmPreferencias(tabControl)
tabControl.add(tab1, text='Preferencias')

tab2 = FrmFamiliares(tabControl)
tabControl.add(tab2, text='Familiares')

tabControl.pack(expand=1, fill="both")
app.mainloop()

"""
TODO:
-abrir excel automatico
-mandar email
"""

"""
Model referencia uma tabela do banco de dados
Recebe o nome f"{tabela}Vo" -> View Objects
1 atributo para cada coluna da tabela
"""