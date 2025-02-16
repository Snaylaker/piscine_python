from tqdm import tqdm
from time import sleep
import sys


def ft_tqdm(lst: range) -> None:

    loadingChar = '\u2588'
    print("start ", lst.start)
    current = lst.start if lst.start else 0
    bar = ""


    while current <= lst.stop:
        bar += '\u2588'
        print(f'{0 if current == 0 else int((current / lst.stop) * 100)}%|{bar}| {current}/{lst.stop}', end="\r", flush=True)
        yield current
        current += lst.step if lst.step else 1
#