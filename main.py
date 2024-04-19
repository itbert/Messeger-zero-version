"""
ГЛАВНОЕ ИСПОЛНЯЕМОЕ ПРИЛОЖЕНИЕ. ЗДЕСЬ ПРОИСХОДИТ ЗАПУСК И СБОРКА ПРОЕКТА
"""

import flet as ft
from Registration.WelcomePage import welcome_reg
from MainScreen.Collector import collector_main_screen


def main(page: ft.Page):
    welcome_reg(page)
    collector_main_screen(page)


ft.app(target=main)
