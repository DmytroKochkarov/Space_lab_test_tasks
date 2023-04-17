import logging
logging.basicConfig(level=logging.INFO, filename="log_text.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")
def Triangle(kot):
        kot.sort()
        for a in range(len(kot) - 2):
            for b in range(a + 1, len(kot) - 1):
                for c in range(b + 1, len(kot)):
                    if kot[a] ** 2 + kot[b] ** 2 == kot[c] ** 2:
                        logging.info(f"Good job u found: {kot[a]}, {kot[b]}, {kot[c]}")
                        return True
        logging.info(f"What a shame, try again")
        return False

kot = []
for i in range(3):
    while True:
        g = input(f"Введіть три числа для визначення Піфагоровської трійки: ")
        try:
            g = int(g)
            if g > 0:
                kot.append(g)
                break
            else:
                logging.warning(f"Введіть число !")
        except ValueError or NameError:
            logging.warning(f"Введіть додатнє число, не букви !!!")

print(Triangle(kot))