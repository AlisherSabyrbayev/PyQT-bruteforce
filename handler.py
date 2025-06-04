import msoffcrypto
from PyQt5 import QtCore
from itertools import product, count
from string import ascii_letters, digits, punctuation

class ThreadHandler(QtCore.QThread):
    filepath: str = None
    config: list = None # [Цифры, спец.символы, латиница]
    signal = QtCore.pyqtSignal(list)

    template = {
        0: digits,
        1: punctuation,
        2: ascii_letters,
    }

    def run(self):
        sequence = ""

        for num, item in enumerate(self.config):
            if item: sequence += self.template[num]

        # Перебираем пароли в бесконечном цикле если в конфиге было что-то
        if sequence:
            file = msoffcrypto.OfficeFile(open(self.filepath, "rb")) # Открываем зашифрованный Excel-файл в режиме чтения в байтах.
            for length in count(0, 1):
                for passw in product(sequence, repeat=length):
                    password = "".join(passw)
                    try:
                        file.load_key(password=password)
                        file.decrypt(open("decrypted.xlsx", "wb"))
                        self.signal.emit(["result", password])
                        return
                    except Exception as err:
                        with open("data\\log.txt", "a+") as f:
                            f.seek(0)
                            if str(err) not in f.read():
                                f.write(f"{err}\n")
                        self.signal.emit(["fail", password])