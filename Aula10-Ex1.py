import tkinter as tk
from tkinter import messagebox

def realizar_login():
    email = entry_email.get()
    senha = entry_senha.get()

    if len(senha) < 6:
        messagebox.showerror("Erro de senha", "A senha deve ter pelo menos 6 caracteres.")
    elif "@" not in email:
        messagebox.showerror("Erro de e-mail", "O e-mail deve conter o caractere '@'.")
    else:
        messagebox.showinfo("Login bem-sucedido", "Login realizado com sucesso para o e-mail: " + email)

# Criar a janela
janela = tk.Tk()
janela.title("Login")

# Criar os widgets
label_email = tk.Label(janela, text="E-mail:")
label_email.grid(row=0, column=0, padx=5, pady=5)

entry_email = tk.Entry(janela)
entry_email.grid(row=0, column=1, padx=5, pady=5)

label_senha = tk.Label(janela, text="Senha:")
label_senha.grid(row=1, column=0, padx=5, pady=5)

entry_senha = tk.Entry(janela, show="*")
entry_senha.grid(row=1, column=1, padx=5, pady=5)

botao_login = tk.Button(janela, text="Login", command=realizar_login)
botao_login.grid(row=2, columnspan=2, padx=5, pady=5)

# Executar a janela
janela.mainloop()