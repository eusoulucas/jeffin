from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import itertools
from explicit import waiter, XPATH
import time
import random
from datetime import datetime
from tkinter import messagebox
import threading

hora_inicio = str(datetime.now())


class InstagramBot:
    def __init__(self, username, password, site, num_de_igs, n_seguidores, endereco, init):
        self.username = username
        self.password = password
        self.site = site
        self.n_igs = num_de_igs
        self.n_seguidores = n_seguidores
        self.endereco = endereco
        self.init = init
        self.driver = webdriver.Firefox(executable_path=r"D:\geckodriver-v0.26.0-win64\geckodriver.exe")

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com')
        time.sleep(5)

        campo_user = driver.find_element_by_xpath(
            "//input[@name = 'username']")
        campo_user.click()
        campo_user.clear()
        campo_user.send_keys(self.username)
        campo_password = driver.find_element_by_xpath(
            "//input[@name='password']")
        campo_password.click()
        campo_password.clear()
        campo_password.send_keys(self.password)
        campo_password.send_keys(Keys.RETURN)
        time.sleep(8)

    def listar_seguidores(self):
        seguidores = []
        account = str(self.username)

        print('Followers of the "{}" account'.format(account))
        for count, follower in enumerate(self.scrape_followers(self.driver, account = account), 1):
            seguidores.append(follower)
            if count >= self.n_seguidores:
                break
        lista_seguidores = open(self.endereco, "w")
        for seguidor in seguidores:
            lista_seguidores.write("@" + seguidor+"\n")

        lista_seguidores.close()
        self.driver.close()

    def scrape_followers(self, driver, account):
        # Load account page
        driver.get("https://www.instagram.com/" + self.username)

        # Click the 'Follower(s)' link
        # driver.find_element_by_partial_link_text("follower").click()
        waiter.find_element(driver, "//a[@href='/" + self.username + "/followers/']", by=XPATH).click()

        # Wait for the followers modal to load
        waiter.find_element(driver, "//div[@role='dialog']", by=XPATH)

        # At this point a Followers modal pops open. If you immediately scroll to the bottom,
        # you hit a stopping point and a "See All Suggestions" link. If you fiddle with the
        # model by scrolling up and down, you can force it to load additional followers for
        # that person.

        # Now the modal will begin loading followers every time you scroll to the bottom.
        # Keep scrolling in a loop until you've hit the desired number of followers.
        # In this instance, I'm using a generator to return followers one-by-one
        follower_css = "ul div li:nth-child({}) a.notranslate"  # Taking advange of CSS's nth-child functionality
        for group in itertools.count(start=1, step=12):
            for follower_index in range(group, group + 12):
                yield waiter.find_element(driver, follower_css.format(follower_index)).text

            # Instagram loads followers 12 at a time. Find the last follower element
            # and scroll it into view, forcing instagram to load another 12
            # Even though we just found this elem in the previous for loop, there can
            # potentially be large amount of time between that call and this one,
            # and the element might have gone stale. Lets just re-acquire it to avoid
            # that
            last_follower = waiter.find_element(driver, follower_css.format(follower_index))
            driver.execute_script("arguments[0].scrollIntoView();", last_follower)

    @staticmethod
    def human_typing(frase, onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(3, 10) / 40)

    def comment_pics(self):
        def mostra_erro(erro, in_coment):
            messagebox.showinfo("Jeffin", "O processo deu o erro '"+ str(erro) +"' no comentario "+ str(in_coment))

        driver = self.driver
        driver.get(self.site)
        time.sleep(random.randint(7, 10))

        arq_seguidores = open(self.endereco, 'r', encoding="utf8")
        arrobas = []
        arrobas_aux = []

        for seguidor in arq_seguidores:
            arrobas.append(seguidor)

        for arroba in arrobas[0:self.n_seguidores]:
            arrobas_aux.append(arroba)

        while (len(arrobas_aux) % 2) != 0 and (self.n_seguidores % 2) == 0:
            arrobas_aux.append(random.choice(arrobas))

        p = self.init
        k = 0
        verify = False
        for i in range(0, int(len(arrobas_aux) / self.n_igs)):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(random.randint(8, 11))
            k = k + 1

            if (i % 10) == 0:
                time.sleep(random.randint(20,30))

            if (i % 15) == 0:
                time.sleep(random.randint(20,30))

            try:
                driver.find_element_by_class_name('Ypffh').click()
                campo_comment = driver.find_element_by_class_name('Ypffh')
                time.sleep(random.randint(7, 10))

                for j in range(p, p + self.n_igs):
                    self.human_typing(arrobas_aux[j] + " ", campo_comment)
                    if j == p + self.n_igs and verify:
                        self.human_typing("#equipeAmotocenter", campo_comment)
                    relatorio = open("relatorios\controle_ig " + str(self.username) + hora_inicio[8:11] + ".txt", "a", encoding="utf8")
                    relatorio.write("[" + str(p) + "]" + arrobas_aux[j])
                    relatorio.close()
                p = p + 3
                time.sleep(random.randint(7, 10))
                driver.find_element_by_xpath('//button[contains(text(), "Publicar")]').click()
                time.sleep(random.randint(55, 60))

            except Exception as e:
                time.sleep(random.randint(14, 30))
                relatorio_erro = open("relatorios\controle_ig " + str(self.username) + hora_inicio[6:11] + ".txt", "a", encoding="utf8")
                relatorio_erro.write("Erro " + str(e) + " no comentário: " + str(k) + ", " + str(datetime.now()))
                relatorio_erro.close()
                tr_erro = threading.Thread(target = mostra_erro, args=[e, p])
                tr_erro.start()

                driver.get(self.site)
                time.sleep(random.randint(6, 9))

        relatorio_fim = open("relatorios\controle_ig " +str(self.username)+ hora_inicio[8:11] + ".txt", "a", encoding="utf8")
        relatorio_fim.write("\nO processo se iniciou " + hora_inicio + " e se encerrou " + str(datetime.now())
                        + " totalizando " + str(p) + " comentários")
        relatorio_fim.close()
        messagebox.showinfo("Jeffin", "O processo terminou")

