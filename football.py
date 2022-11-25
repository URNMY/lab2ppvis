import random
import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Футбольчик")

main_theme = pygame_menu.Theme(
    background_color=(2, 149, 219),
    selection_color=(11, 14, 27),
    title_background_color=(2, 149, 219),
    widget_font_color=(11, 14, 27),
    widget_font_size=30,
    title_font_color=(11, 14, 27)
)


class Window:
    def __init__(self):
        pass


class PlayerController:
    def __init__(self):
        pass

    def start(self):
        pass

    def run_player_window(self):
        pass

    def show_statistics(self):
        pass

    def recovery(self):
        pass

    def change_team(self, teamWindow, teamList):
        pass

    def match(self):
        pass

    def display_def (self):
        display = Display()
        display.show_window()


class ManagerController:
    def __init__(self):
        pass

    def team_info(self):
        pass

    def transfers(self):
        pass

    def check_transfer(self):
        pass

    def change_roster(self):
        pass

    def start(self):
        pass

    def run_manager_window(self):
        pass

    def match(self):
        pass


class Player:
    def __init__(self):
        pass


class KindOfTraining:
    def __init__(self):
        pass


class KindOfRecovery:
    def __init__(self):
        pass


class FootballTeam:
    def __init__(self):
        pass


class Display:
    def __init__(self):
        self.window_view = WindowView()
        # self.controller = Controller()

    def show_window(self):
        self.window_view.input_selection()


class WindowView:
    def __init__(self):
        pass

    def input_selection(self):
        menu = pygame_menu.Menu("Football Manager", 800, 600, theme = main_theme)

        menu.add.button('Регистрация менеджера', self.registration_manager)
        menu.add.button('Регистрация игрока', self.registration_player)
        menu.add.button('Авторизация', self.login)
        #menu.add.button('Гость', self.all_doctors)
        #menu.add.button('Завершение', pygame_menu.events.EXIT)

        menu.mainloop(surface)

    def registration_player(self):
        menu = pygame_menu.Menu('Регистрация игрока', 800, 600, theme=main_theme)

        menu.add.text_input('Имя пользователя: ')
        menu.add.text_input('Пароль: ')
        menu.add.button('Регистрация', self.player_menu)

        menu.mainloop(surface)

    def registration_manager(self):
        menu = pygame_menu.Menu('Регистрация менеджера', 800, 600, theme=main_theme)

        menu.add.text_input('Имя пользователя: ')
        menu.add.text_input('Пароль: ')
        menu.add.button('Регистрация', self.manager_menu)

        menu.mainloop(surface)

    def login(self):
        menu = pygame_menu.Menu('Авторизация', 800, 600, theme=main_theme)

        menu.add.text_input('Имя пользователя: ')
        menu.add.text_input('Пароль: ')
        menu.add.button('Войти', self.player_menu)

        menu.mainloop(surface)

    def player_menu(self):
        menu = pygame_menu.Menu('Окно игрока', 800, 600, theme=main_theme)

        menu.add.button('Личная статистика', self.statistics)
        menu.add.button('Тренировка', self.training)
        menu.add.button('Восстановление', self.recovery)
        menu.add.button('Смена команды', self.change_team)
        menu.add.button('Матч', self.p_match)
        menu.add.button('Выйти', self.input_selection)

        menu.mainloop(surface)

    def error_login(self):
        menu = pygame_menu.Menu('Ошибка входа', 800, 600, theme=main_theme)

        menu.add.label('Неправильное')
        menu.add.label('имя пользователя')
        menu.add.label('или')
        menu.add.label('пароль')
        menu.add.button('Ввести ещё раз', )

        menu.mainloop(surface)

    def change_team(self):
        menu = pygame_menu.Menu('Смена команды', 800, 600, theme=main_theme)
        menu.add.button('Команда 1', self.player_menu)
        menu.add.button('Команда 2', self.player_menu)
        menu.mainloop(surface)

    def statistics(self):
        menu = pygame_menu.Menu('Личная статистика', 800, 600, theme=main_theme)
        menu.add.label('Статистика')
        menu.add.button('Назад', self.player_menu)
        menu.mainloop(surface)

    def recovery(self):
        menu = pygame_menu.Menu('Восстановление', 800, 600, theme=main_theme)
        menu.add.text_input('Восстановить: ')
        menu.add.button('Восстановить', self.player_menu)
        menu.mainloop(surface)

    def p_match(self):
        menu = pygame_menu.Menu('Матч', 800, 600, theme=main_theme)
        menu.add.label('Выиграла команда: ')
        menu.add.label(random.randint(1, 2))
        menu.add.button('Ок', self.manager_menu)
        menu.mainloop(surface)

    def m_match(self):
        menu = pygame_menu.Menu('Матч', 800, 600, theme=main_theme)
        menu.add.label('Выиграла команда: ')
        menu.add.label(random.randint(1, 2))
        menu.add.button('Ок', self.manager_menu)
        menu.mainloop(surface)

    def training(self):
        menu = pygame_menu.Menu('Тренировка', 800, 600, theme=main_theme)
        menu.add.text_input('Количество повышения навыка: ')
        menu.add.button('Повысить', self.player_menu)
        menu.mainloop(surface)

    def manager_menu(self):
        menu = pygame_menu.Menu('Окно менеджера', 800, 600, theme=main_theme)

        menu.add.button('Трансферы', self.transfers)
        menu.add.button('Смена состава', self.change_roster)
        menu.add.button('Информация о команде', self.info_team)
        menu.add.button('Матч', self.m_match)
        menu.add.button('Выйти', self.input_selection)

        menu.mainloop(surface)

    def transfers(self):
        menu = pygame_menu.Menu('Трансферы', 800, 600, theme=main_theme)
        menu.add.button('Купить игрока', self.buy_player)
        menu.add.button('Продать игрока', self.sell_player)
        menu.mainloop(surface)

    def buy_player(self):
        menu = pygame_menu.Menu('Покупка игрока', 800, 600, theme=main_theme)
        menu.add.label('Имя\n'
                        'Фамилия\n'
                        'Позиция\n'
                        'Характеристика\n'
                        'Состав')
        menu.add.button('Купить', self.manager_menu)
        menu.mainloop(surface)

    def sell_player(self):
        menu = pygame_menu.Menu('Продажа игрока', 800, 600, theme=main_theme)
        menu.add.label('Имя\n'
                       'Фамилия\n'
                       'Позиция\n'
                       'Характеристика\n'
                       'Состав')
        menu.add.button('Продать', self.manager_menu)
        menu.mainloop(surface)

    def change_roster(self):
        menu = pygame_menu.Menu('Смена состава', 800, 600, theme=main_theme)
        menu.add.button('Поменять состав', self.manager_menu)
        menu.mainloop(surface)

    def info_team(self):
        menu = pygame_menu.Menu('Информация о команде', 800, 600, theme=main_theme)
        menu.add.label('Инфо о команде')
        menu.add.button('Назад', self.manager_menu)
        menu.mainloop(surface)

class Application:
    def __init__(self):
        self.window = Window()
        self.controller = PlayerController()


if __name__ == '__main__':
    application = Application()
    application.controller.display_def()

