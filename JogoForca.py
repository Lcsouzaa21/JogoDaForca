import tkinter as tk
import random

def escolher_palavra():
    palavras = ['python', 'programacao', 'desenvolvimento', 'algoritmo', 'inteligencia']
    return random.choice(palavras)

def iniciar_jogo():
    global palavra, palavra_descoberta, letras_tentadas, tentativas_restantes, erros
    palavra = escolher_palavra()
    palavra_descoberta = ['_'] * len(palavra)
    letras_tentadas = []
    tentativas_restantes = 6
    erros = 0
    atualizar_tela()

def atualizar_tela():
    palavra_label.config(text=' '.join(palavra_descoberta))
    letras_label.config(text='Letras tentadas: ' + ', '.join(letras_tentadas))
    tentativas_label.config(text=f"Tentativas restantes: {tentativas_restantes}")
    exibir_forca()

def exibir_forca():
    estagios = [
        """
           -----
           |   |
           |
           |
           |
           |
        --------
        """,
        """
           -----
           |   |
           |   O
           |
           |
           |
        --------
        """,
        """
           -----
           |   |
           |   O
           |   |
           |
           |
        --------
        """,
        """
           -----
           |   |
           |   O
           |  /|
           |
           |
        --------
        """,
        """
           -----
           |   |
           |   O
           |  /|\
           |
           |
        --------
        """,
        """
           -----
           |   |
           |   O
           |  /|\
           |  /
           |
        --------
        """,
        """
           -----
           |   |
           |   O
           |  /|\
           |  / \
           |
        --------
        """
    ]
    forca_label.config(text=estagios[erros])

def tentar_letra():
    global erros, tentativas_restantes
    letra = letra_entry.get().lower()
    letra_entry.delete(0, tk.END)
    
    if letra in letras_tentadas:
        resultado_label.config(text="Você já tentou essa letra. Tente outra.")
        return
    
    letras_tentadas.append(letra)
    
    if letra in palavra:
        for i, l in enumerate(palavra):
            if l == letra:
                palavra_descoberta[i] = letra
        resultado_label.config(text="Boa! Você acertou uma letra.")
    else:
        erros += 1
        tentativas_restantes -= 1
        resultado_label.config(text="Ops! Letra errada.")
    
    atualizar_tela()
    verificar_fim_jogo()

def verificar_fim_jogo():
    if '_' not in palavra_descoberta:
        resultado_label.config(text="Parabéns! Você descobriu a palavra!")
        letra_entry.config(state=tk.DISABLED)
    elif erros == 6:
        resultado_label.config(text=f"Puxa, você foi enforcado! A palavra era: {palavra}")
        letra_entry.config(state=tk.DISABLED)

def reiniciar_jogo():
    letra_entry.config(state=tk.NORMAL)
    iniciar_jogo()

root = tk.Tk()
root.title("Jogo da Forca")

palavra_label = tk.Label(root, font=("Helvetica", 18))
palavra_label.pack(pady=10)

letras_label = tk.Label(root, text="Letras tentadas:", font=("Helvetica", 14))
letras_label.pack(pady=10)

tentativas_label = tk.Label(root, text="Tentativas restantes: 6", font=("Helvetica", 14))
tentativas_label.pack(pady=10)

forca_label = tk.Label(root, font=("Courier", 14))
forca_label.pack(pady=10)

letra_entry = tk.Entry(root, font=("Helvetica", 14))
letra_entry.pack(pady=10)

tentar_button = tk.Button(root, text="Tentar letra", command=tentar_letra, font=("Helvetica", 14))
tentar_button.pack(pady=10)

resultado_label = tk.Label(root, text="", font=("Helvetica", 14))
resultado_label.pack(pady=10)

reiniciar_button = tk.Button(root, text="Reiniciar Jogo", command=reiniciar_jogo, font=("Helvetica", 14))
reiniciar_button.pack(pady=10)

iniciar_jogo()

root.mainloop()