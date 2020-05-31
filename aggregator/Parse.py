import requests as req
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets
import design
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtCore import QUrl
import sys



class AppParser(QtWidgets.QMainWindow, design.Ui_MainWindow):
    """App for parsing rss feeds"""
    def __init__(self):
        super().__init__()
        self.Web = QtWebEngineWidgets.QWebEngineView()
        self.sel_cat = []
        self.res_list = []
        self.setupUi(self)
        self.links = ['https://news.tut.by/rss/all.rss',
                      'https://www.onliner.by/feed',
                      'https://www.belta.by/rss',]
        self.Parse_btn_start.clicked.connect(self.parse_only_checked)
        self.pushButton.clicked.connect(self.open_article)
        self.pushButton_2.clicked.connect(self.reset_ch)
        self.progressBar.setValue(0)

    def parser(self, url: str) -> list:
        """
        Parsing your rss web-resource
        :param url: href of rss
        :return: list with next trips (title, category, link) + change obj self.res_list
        """
        result = req.get(url)
        soup = BeautifulSoup(result.text, 'html.parser')
        for i in soup.find_all('item'):
            for title, cat, link in zip(i.find_all('title')[0],
                                        i.find_all('category')[0],
                                        i.find_all('guid'),):
                try:
                    self.res_list.append([title.strip(), cat.strip(), link.text.strip()])
                except:
                    pass
        return self.res_list

    def create_db_category(self):
        for i in self.res_list:
            if i[1] in "Технологии,В Беларуси,Наука,Интернет и связь,Гаджеты,Игры,Оружие".split(','):
                i[1] = "Технологии и Наука"

            elif i[1] in "В мире,Попкорн,Люди,Мнения,Комментарии,Интервью,Колумнисты,Кругозор,Калейдоскоп,Общество,Регионы,Люди,Культура".split(','):
                i[1] = "Общество"

            elif i[1] in "Единоборства,Спорт,Чемпионат Беларуси по футболу,Биатлон,Хоккей,Футбол,Теннис,Баскетбол,Гандбол,Околоспорт".split(','):
                i[1]="Спорт"

            elif i[1] in "Видео,Авто,Дорога,Тест-драйвы,Автобизнес,Автоновости".split(','):
                i[1]="Авто"

            elif i[1] in "Деньги и власть,Президент,Политика,Экономика,Личный счет,Публичный счет,Банки".split(','):
                i[1]="Экономика и финансы"

            elif i[1] in "Недвижимость,Экспертиза,От застройщика,Строительство,Аренда,Деньги,Интерьер,дизайн,ремонт".split(','):
                i[1]="Недвижимость"

            elif i[1] in "Лекарства,ЗОЖ,Правильное питание,Врачи,Болезни,Тренировки,Красота,Медицинские новости".split(','):
                i[1]="Здоровье"

            elif i[1] in "Тело,Вкус жизни,Отношения,Стиль,Карьера,Звезды,Вдохновение,Еда,Анонсы".split(','):
                i[1]="Леди"
            
            elif i[1] in "эксклюзив,Эксклюзив".split(','):
                i[1]="Эксклюзив"

            elif i[1] in "Происшествия,происшествия".split(','):
                i[1]="Происшествия"

            elif i[1] in "Афиша,Места,Обзоры,Премьера TUT,Звезды,Новости".split(','):
                i[1]="Афиша"

            else: 
                i[1]="Разное"

    def open_article(self):
        try:
            for i in self.res_list:
                if i[0] == self.listWidget.item(self.listWidget.currentRow()).text():
                    self.Web.load(QUrl(i[2]))
                    self.Web.show()

        except:
            pass
        pass



    def parse_only_checked(self):
        """Call parser according to chosen web-resources"""
        self.listWidget.clear()
        self.res_list = []
        self.progressBar.setValue(0)
        if self.Tutby_chk_box.isChecked():
            self.parser(self.links[0])

        self.progressBar.setValue(10)
        if self.Onliner_chk_box.isChecked():
            self.parser(self.links[1])

        self.progressBar.setValue(20)
        if self.Belta_chk_box.isChecked():
            self.parser(self.links[2])

        self.progressBar.setValue(30)
        self.create_db_category()
        self.sel_cat = [i.text() for i in map(self.listWidget_2.item, range(12)) if i.isSelected()]
        for i in self.res_list:
            if i[1] in self.sel_cat:
                self.listWidget.addItem(i[0])
        self.listWidget_2.item(1).setSelected(0)
        # with open('RES.txt', 'w+') as f:
        #     for i in self.res_list:
        #         try:
        #             f.write(f'TITLE -->> {i[0]}\n'
        #                     f'CATEGORY -->> {i[1]}\n'
        #                     f'LINK -->> {i[2]}\n\n')
        #         except:
        #             print(f'{i[0]}\n{i[1]}\n{i[2]}')
        self.progressBar.setValue(100)
    
    def print_all_info(self) -> None:
        """
        Show all parsed info
        Do Print
        :return: All parsed info  >>>  TITLE:: CATEGORY::  LINK::
        """
        if not self.res_list:
            print('Choose web-resource, use method check_box_value_return to chose')
        for title, category, link in self.res_list:
            print(f'{"<<< NEW BLOCK >>>":^100}\n'
                  f'{title:^100}\n'
                  f'{category:^100}\n'
                  f'{link}\n')

    def reset_ch(self):
        [i.setSelected(0) for i in map(self.listWidget_2.item, range(12))]

if __name__ == '__main__':
    Main = QtWidgets.QApplication(sys.argv)
    window = AppParser()
    window.show()
    Main.exec_()
