from threading import Thread

def getDuplexFor(index: int, sections: list[int], *digits) -> int:
    n: int = digits.__len__()
    sections[index] = (
        digits[0] * digits[0] if n == 1 else 
        2 * digits[0] * digits[1] if n == 2 else
        2 * digits[0] * digits[2] + (digits[1] * digits[1]) if n == 3 else
        (2 * digits[0] * digits[3]) + (2 * digits[1] * digits[2]) if n == 4 else 0
    )


def startAndJoinThreads(threads: list[Thread]) -> None:
    for thread in threads:
        thread.start()
        thread.join()


def calculateSquare(n: int, sections: list[int]) -> int:
    answer: int = 0
    for i in range(n, -1, -1):
        answer = (sections[i] % (10 if i > 0 else sections[i] + 1) * pow(10, (n - i)) + answer)
        sections[i] //= 10
        sections[i - 1] += sections[i]

    return answer


def handle2Digit(threads: list[Thread], digits: list[int]) -> int:
    n: int = 3
    sections: list[int] = [0] * n
    threads.append(Thread(target=getDuplexFor, args=[0, sections, digits[0]]))
    threads.append(Thread(target=getDuplexFor, args=[1, sections, digits[0], digits[1]]))
    threads.append(Thread(target=getDuplexFor, args=[2, sections, digits[1]]))
    startAndJoinThreads(threads)
    return calculateSquare(n - 1, sections)
    


def handle3Digit(threads: list[Thread], digits: list[int]) -> int:
    n: int = 5
    sections: list[int] = [0] * n
    threads.append(Thread(target=getDuplexFor, args=[0, sections, digits[0]]))
    threads.append(Thread(target=getDuplexFor, args=[1, sections, digits[0], digits[1]]))
    threads.append(Thread(target=getDuplexFor, args=[2, sections, digits[0], digits[1], digits[2]]))
    threads.append(Thread(target=getDuplexFor, args=[3, sections, digits[1], digits[2]]))
    threads.append(Thread(target=getDuplexFor, args=[4, sections, digits[2]]))
    startAndJoinThreads(threads)
    return calculateSquare(n - 1, sections)


def handle4Digit(threads: list[Thread], digits: list[int]) -> int:
    n: int = 7
    sections: list[int] = [0] * n
    threads.append(Thread(target=getDuplexFor, args=[0, sections, digits[0]]))
    threads.append(Thread(target=getDuplexFor, args=[1, sections, digits[0], digits[1]]))
    threads.append(Thread(target=getDuplexFor, args=[2, sections, digits[0], digits[1], digits[2]]))
    threads.append(Thread(target=getDuplexFor, args=[3, sections, digits[0], digits[1], digits[2], digits[3]]))
    threads.append(Thread(target=getDuplexFor, args=[4, sections, digits[1], digits[2], digits[3]]))
    threads.append(Thread(target=getDuplexFor, args=[5, sections, digits[2], digits[3]]))
    threads.append(Thread(target=getDuplexFor, args=[6, sections, digits[3]]))
    startAndJoinThreads(threads)
    return calculateSquare(n - 1, sections)
    


if __name__ == "__main__":
    n: int = int(input("Enter a number:\t"))
    digits: list[int] = [int(digit) for digit in str(n)]
    threads: list[Thread] = []

    if n < 10:
        print(n * n)
    elif n < 100:
        print(handle2Digit(threads, digits))
    elif n < 1000:
        print(handle3Digit(threads, digits))
    elif n < 10000:
        print(handle4Digit(threads, digits))

