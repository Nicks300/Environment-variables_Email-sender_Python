from src.doctor_5 import Doctor
from src.config_5 import Configuration


def main() -> str:
    configuration = Configuration()
    doc = Doctor(configuration)

    mode = input("Нужно ли будет сохранить рецепт в файле? ")
    path = None
    if mode != "":
        path = input("Введите имя файла, куда будет сохранен рецепт: ")
    return doc.write_recipe(path)


if __name__ == "__main__":
    main()
