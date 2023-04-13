from tkinter import *
from bot import *
import threading


def void_loop():
    def iniciar_bot():
        usuario_bot = usuario.get()
        senha_bot = senha.get()
        site_bot = site.get()
        nr_pessoas_bot = int(nr_pessoas.get())
        n_seguidores_bot = int(n_seguidores.get())
        endereco_bot = "listas_de_seguidores\\" + endereco.get()
        init_bot = int(init.get())
        bot = InstagramBot(usuario_bot, senha_bot, site_bot, nr_pessoas_bot, n_seguidores_bot, endereco_bot, init_bot)
        bot.login()
        bot.comment_pics()

    def cr_listaseg():
        usuario_bot = usuario.get()
        senha_bot = senha.get()
        site_bot = site.get()
        nr_pessoas_bot = int(nr_pessoas.get())
        n_seguidores_bot = int(n_seguidores.get())
        init_bot = int(init.get())
        endereco_bot = "listas_de_seguidores\\" + endereco.get()
        temp = open(endereco_bot, "w")
        temp.close()
        bot = InstagramBot(usuario_bot, senha_bot, site_bot, nr_pessoas_bot, n_seguidores_bot, endereco_bot, init_bot)
        bot.login()
        bot.listar_seguidores()

    janela = Tk()
    janela.geometry("650x370")
    janela.attributes('-alpha', 0.95)
    janela.title("Jeffin - Sr. Robô")

    img_fundo = PhotoImage(file = "img/logo.png")

    fundo = Label(janela, bg = "#000000", image = img_fundo)
    fundo.place(relwidth = "0.4", relheight = "1")
    frame_pr = Frame(janela, bg = "#000000")
    frame_pr.place(relwidth = "0.6", relheight = "1", relx = "0.4")

    lb_titulo = Label(frame_pr, text = "INFO",
                    bg  = "#800000", fg = "#000000", font = "Impact 22")
    lb_titulo.place(relwidth = "1", rely = "0.05" )
    lb_site = Label(frame_pr, text = "Imagem oficial (URL):",
                    bg  = "#000000", fg = "#800000", font = "Bahnschrift 12")
    lb_site.place(relx = "0.06", rely = "0.2" )
    lb_usuario = Label(frame_pr, text = "Usuário:",
                    bg  = "#000000", fg = "#800000", font = "Bahnschrift 12")
    lb_usuario.place(relx = "0.3", rely = "0.3" )
    lb_senha = Label(frame_pr, text = "Senha:",
                    bg  = "#000000", fg = "#800000", font = "Bahnschrift 12")
    lb_senha.place(relx = "0.32", rely = "0.4" )
    lb_nsegu = Label(frame_pr, text = "Número de seguidores:",
                    bg  = "#000000", fg = "#800000", font = "Bahnschrift 12")
    lb_nsegu.place(relx = "0.015", rely = "0.5" )
    lb_nrp = Label(frame_pr, text = "Nº de pessoas:",
                    bg  = "#000000", fg = "#800000", font = "Bahnschrift 12")
    lb_nrp.place(relx = "0.02", rely = "0.6" )
    lb_init = Label(frame_pr, text = "Iníciar do arroba:",
                    bg  = "#000000", fg = "#800000", font = "Bahnschrift 12")
    lb_init.place(relx = "0.5", rely = "0.6" )
    lb_end = Label(frame_pr, text = "Lista de seguidores:",
                    bg  = "#000000", fg = "#800000", font = "Bahnschrift 12")
    lb_end.place(relx = "0.06", rely = "0.7" )

    site = Entry(frame_pr, bg = "#800000", fg = "#000000", font = "Bahnschrift 12", bd = 0)
    site.place(relx = "0.50", rely = "0.21", relwidth = "0.47")
    usuario = Entry(frame_pr, bg = "#800000", fg = "#000000", font = "Bahnschrift 12", bd = 0)
    usuario.place(relx = "0.50", rely = "0.31", relwidth = "0.47")
    senha = Entry(frame_pr, bg = "#800000", fg = "#000000", show='*', font = "Bahnschrift 12", bd = 0)
    senha.place(relx = "0.50", rely = "0.41", relwidth = "0.47")
    n_seguidores = Entry(frame_pr, bg = "#800000", fg = "#000000", font = "Bahnschrift 12", bd = 0)
    n_seguidores.place(relx = "0.50", rely = "0.51", relwidth = "0.47")
    nr_pessoas = Spinbox(frame_pr, from_= 1, to=10000, bg = "#800000", fg = "#000000", font = "Bahnschrift 12", bd = 0)
    nr_pessoas.place(relx = "0.32", rely = "0.61", relwidth = "0.13")
    init = Spinbox(frame_pr, from_= 1, to=100000, bg = "#800000", fg = "#000000", font = "Bahnschrift 12", bd = 0)
    init.place(relx = "0.85", rely = "0.61", relwidth = "0.13")
    endereco = Entry(frame_pr, bg = "#800000", fg = "#000000", font = "Bahnschrift 12", bd = 0)
    endereco.place(relx = "0.50", rely = "0.71", relwidth = "0.47")

    #criando nossa threads secundarias
    t2 = threading.Thread(target = iniciar_bot)
    t3 = threading.Thread(target = cr_listaseg)

    bt_start = Button(frame_pr, text = "START", command = t2.start,
                      bg = "#800000", fg = "#000000", font = "Bahnschrift 12", bd = 0)
    bt_start.place(relwidth = "1", relheight = "0.08", rely = "0.80")

    bt_seg = Button(frame_pr, text = "Criar lista de seguidores", command = t3.start,
                      bg = "#800000", fg = "#000000", font = "Bahnschrift 12", bd = 0)
    bt_seg.place(relwidth = "0.7", relheight = "0.08", rely = "0.90", relx = "0.15")

    bt_seg = Button(frame_pr, text = "Criar lista de seguidores", command = t3.start,
                      bg = "#800000", fg = "#000000", font = "Bahnschrift 12", bd = 0)
    bt_seg.place(relwidth = "0.7", relheight = "0.08", rely = "0.90", relx = "0.15")

    janela.mainloop()

#criando nossa thread principal
t1 = threading.Thread(target = void_loop)

#iniciando a primeira thread
t1.start()
