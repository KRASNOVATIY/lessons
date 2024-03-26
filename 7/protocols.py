from dataclasses import dataclass
from typing import Protocol, runtime_checkable


@runtime_checkable  # это добавит проверку соответствия во время выполнения программы
class EngineProtocol(Protocol):
    def run(self):
        ...


@dataclass
class PetrolEngine(EngineProtocol):
    def run(self):
        print('ж-ж-ж')

    def stall(self):
        print('заглох')


@dataclass
class JetEngine(EngineProtocol):
    def run(self):
        print('у-у-у')

    def fly(self):
        print('летим')


@dataclass
class Car:
    e: JetEngine  # обратите внимание! Явно указали реализацию

    def poehali(self):
        self.e.run()


def main():
    p = PetrolEngine()
    j = JetEngine()
    c = Car(p)  # обратите внимание! IDE подсвечивает ошибку, а mypy пропускает. Это связанно с тем что JetEngine соответсвует протоколу EngineProtocol
    c.poehali()
    c = Car(j)
    c.poehali()


if __name__ == '__main__':
    main()