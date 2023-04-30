from dataclasses import dataclass
from enum import Enum, auto
from time import sleep


class StrEnum(str, Enum):
    pass


class DishSize(StrEnum):
    """Includes all available dish sizes."""

    S = auto()
    M = auto()
    L = auto()


@dataclass
class Dish:
    """Represents the final dish data model."""

    name: str
    size: DishSize
    ingredients: list[str]

    def __str__(self) -> str:
        return self.name


def heat(dish: Dish, time: int) -> None:
    """
    Pass the dish into this function for heating.
    The time passed in seconds.

    P.S. This function is IO-bound task since
         chef is waiting until the meal is warm.
    """

    print(f"🍲 Heating {dish}")
    sleep(time)
    print(f"🥘 The {dish} is warm")


def cook(dish: Dish, time: int) -> None:
    """
    Pass the dish into this function for telling chef to cook.
    The time passed in seconds.

    P.S. This function is CPU-bound task since
         chef is cooking by himself.
    """

    print(f"👨‍🍳 Started cook the {dish.name}")

    # Simulate the CPU-bound task
    # The interation over 63.000.000 takes about the 1 second
    N = 63_000_000 * time
    for _ in range(N):
        pass

    print(f"🍳 The {dish} is ready")
