from pokeretriever.pokedex_api_retriever import PokeAPIRetriever
import asyncio

async def main():
    """
    Main function to run the PokeAPIRetriever.

    :author: Mun Young Cho(A01330048), Youngeun Kwon(A01263922)
    """
    poke = PokeAPIRetriever()
    print(await poke.execute_request())

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())