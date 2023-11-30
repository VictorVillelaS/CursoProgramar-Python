from front import *

app = tk.Tk()
frmPreferencias = FrmPreferencias(app)
frmPreferencias.pack()

app.mainloop()

"""
TODO:
-Nomear os parâmetros do edit
"""

"""
Model referencia uma tabela do banco de dados
Recebe o nome f"{tabela}Vo" -> View Objects
1 atributo para cada coluna da tabela
"""