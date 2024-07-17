import asyncio


async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования")
    for ball in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f"Силач {name} поднял {ball} шар")
    print(f"Силач {name} закончил соревнования")


async def main():
    strongman_1 = asyncio.create_task(start_strongman('Pasha', 3))
    strongman_2 = asyncio.create_task(start_strongman('Denis', 4))
    strongman_3 = asyncio.create_task(start_strongman('Apollon', 5))
    await strongman_1
    await strongman_2
    await strongman_3


if __name__ == "__main__":
    asyncio.run(main())
