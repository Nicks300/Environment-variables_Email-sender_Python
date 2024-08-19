import json
import os
from typing import Tuple, Optional
from src.config_5 import Configuration


class Doctor:
    name: str
    speciality: str

    def __init__(self, configuration: Configuration) -> None:
        self.config = configuration
        self.name = self.__doctor_find()[0]
        self.speciality = self.__doctor_find()[1]

    def __doctor_find(self) -> Tuple[str, str]:
        DOCTORS_DIR = 'doctors'
        with open(f"{self.config.base_folder}/{DOCTORS_DIR}/{self.config.login}.json", 'r', encoding="Utf-8") as f:
            dictionary = json.load(f)
        return f"{dictionary['Фамилия']} {dictionary['Имя']} {dictionary['Отчество']}", dictionary['Специальность']

    def __write_receipt_to_file(self, recipe: str, filename: str) -> None:
        RECEIPTS_DIR = 'receipts'
        if os.path.exists(
                f"{self.config.base_folder}/{RECEIPTS_DIR}"):  # создание папки, если она не сущестует.
            # Не знаю, нужно ли это: по ТЗ не понятно
            pass
        else:
            os.mkdir(f"{self.config.base_folder}/{RECEIPTS_DIR}")

        with open(f"{self.config.base_folder}/{RECEIPTS_DIR}/{filename}.txt", 'w', encoding="Utf-8") as new_f:
            new_f.write(recipe)

    def write_recipe(self, filename: Optional[str]) -> str:
        recipe = ""
        print(
            "Введите записи (чтобы закончить нажмите два раза Enter):")  # в тексте задания и в самом примере этот текст разный
        line_check = 0
        while True:
            line = input()
            if line == '':
                line_check += 1
            else:
                line_check = 0
            if line_check == 2:
                break
            else:
                recipe += (line + '\n')

        recipe += self.name
        recipe += f"\nВрач-{self.speciality}"

        print(recipe)  # не понятно, надо ли выводить на экран результат

        if filename != None:
            self.__write_receipt_to_file(recipe, filename)

        return recipe
