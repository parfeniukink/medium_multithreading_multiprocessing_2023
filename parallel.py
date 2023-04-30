from multiprocessing import Process
from time import perf_counter

from kitchen import Dish, DishSize, cook


def main():
    lunch_for_john = Dish(
        name="John's lunch",
        size=DishSize.M,
        ingredients=["potato", "chicken"],
    )

    lunch_for_marry = Dish(
        name="Marry's lunch",
        size=DishSize.S,
        ingredients=["potato", "chicken"],
    )

    # The list includes the concrete dish with the time
    dishes: list[tuple[Dish, int]] = [
        (lunch_for_john, 3),
        (lunch_for_marry, 2),
    ]

    processes = [Process(target=cook, args=[dish, time]) for dish, time in dishes]

    # Start each proecss
    for process in processes:
        process.start()

    # Wait for each process complete
    for process in processes:
        process.join()


if __name__ == "__main__":
    start = perf_counter()
    main()
    end = perf_counter()
    print(f"\n🕓Total execution time: {end-start} seconds")
