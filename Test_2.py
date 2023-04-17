import logging

logging.basicConfig(filename='defenders.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')

def defenders():
    try:
        plants = list(map(int, input("Enter plants, separated: ").split()))
        zombies = list(map(int, input("Enter zombies, separated: ").split()))
    except ValueError:
        logging.error("Invalid input: separated by spaces")
        return None

    if len(plants) != len(zombies):
        logging.warning("Attention different numbers")
        return len(plants) > len(zombies)

    zombie_power = sum(zombies)
    plant_power = sum(plants)

    plant_survivors = sum(p > z for z, p in zip(zombies, plants))
    zombie_survivors = sum(z > p for z, p in zip(zombies, plants))

    if plant_survivors > zombie_survivors:
        logging.info("Plants win!")
        return True
    elif zombie_survivors > plant_survivors:
        logging.info("Zombies win!")
        return False
    else:
        logging.info("Equal powers")
        return zombie_power >= plant_power


result = defenders()
if result is not None:
    print(result)
else:
    print("check logs")