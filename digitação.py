import random
import time
import tkinter as tk

class TreinadorDigitacao:
    def __init__(self):
        self.janela = tk.Tk()  # (link unavailable)()
        self.janela.title("Treinador de Digitação")
        self.janela.geometry("800x600")

        self.texto_label = tk.Label(self.janela, text="Digite o seguinte texto:", font=("Arial", 18))
        self.texto_label.pack()

        self.texto_a_digitar = tk.Label(self.janela, text="", font=("Arial", 18))
        self.texto_a_digitar.pack()

        self.texto_entry = tk.Text(self.janela, height=10, font=("Arial", 18))
        self.texto_entry.pack()

        self.texto_resultado_label = tk.Label(self.janela, text="", font=("Arial", 18))
        self.texto_resultado_label.pack()

        self.botao_iniciar = tk.Button(self.janela, text="Iniciar", command=self.iniciar_treinamento, font=("Arial", 18))
        self.botao_iniciar.pack()

        self.botao_finalizar = tk.Button(self.janela, text="Finalizar", command=self.finalizar_treinamento, font=("Arial", 18))
        self.botao_finalizar.pack_forget()

        self.start_time = 0
        self.texto = ""

        self.janela.bind('<Return>', self.finalizar_treinamento_enter)

        self.janela.mainloop()

    def gerar_texto(self):  # Aqui você modifica as frases 
        textos = [
            "O rato roeu a roupa do rei de Roma.",
            "A vaca malhada foi molhada pela chuva.",
            "O gato gordo comeu o rato.",
            "A casa azul é muito grande.",
            "O carro vermelho é muito rápido."
        ]
        self.texto = random.choice(textos)
        self.texto_a_digitar['text'] = self.texto

    def iniciar_treinamento(self):
        self.gerar_texto()
        self.start_time = time.time()
        self.texto_entry.delete(1.0, tk.END)
        self.texto_entry.focus()
        self.botao_iniciar.pack_forget()
        self.botao_finalizar.pack()

    def finalizar_treinamento(self):
        self.end_time = time.time()
        self.tempo = self.end_time - self.start_time
        self.digitado = self.texto_entry.get(1.0, tk.END)
        self.erros = 0
        for i in range(min(len(self.texto), len(self.digitado))):
            if self.texto[i] != self.digitado[i]:
                self.erros += 1
        if len(self.texto) != len(self.digitado):
            self.erros += abs(len(self.texto) - len(self.digitado))
        self.velocidade = len(self.texto) / self.tempo * 60
        self.precisao = (len(self.texto) - self.erros) / len(self.texto) * 100
        self.texto_resultado_label['text'] = f"Tempo: {self.tempo:.2f} segundos\nVelocidade: {self.velocidade:.2f} caracteres por minuto\nPrecisão: {self.precisao:.2f}%\nErros: {self.erros}"
        self.botao_iniciar.pack()
        self.botao_finalizar.pack_forget()

    def finalizar_treinamento_enter(self, event):
        self.botao_finalizar.invoke()

TreinadorDigitacao()
