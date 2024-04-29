import aiohttp

from .pokedex.pokedex_object import PokedexObject
from .pokedex.ability import Ability
from .pokedex.pokemon import Pokemon
from .pokedex.move import Move
from .pokedex.stat import Stat
from .pokedex_request_mode import RequestMode


async def generate_pokedex_object(poke_request, data) -> PokedexObject:
    """
    Generate a PokedexObject based on the API data.

    :param poke_request: Request - An instance of the Request class containing request details.
    :param data: dict - JSON object containing API data.

    :return: PokedexObject - An object representing the API data in a standardized format.
    """
    mode = RequestMode(poke_request.mode)
    if mode == RequestMode.POKEMON:
        return await generate_pokemon(poke_request, data)
    elif mode == RequestMode.ABILITY:
        return generate_ability(data)
    elif mode == RequestMode.MOVE:
        return generate_move(data)
    elif mode == RequestMode.STAT:
        return generate_stat(data)


async def get_moves(data):
    """
    Retrieve moves data from the API.

    :param data: dict - JSON object containing move data.

    :return: list - A list of move names.
    """
    list_of_moves = []
    async with aiohttp.ClientSession() as session:
        for move_data in data["moves"]:
            move_url = move_data["move"]["url"]
            if move_url:  # URL이 존재하는 경우에만 비동기적으로 처리
                async with session.get(move_url) as response:
                    move_data_response = await response.json()
                    new_move = generate_move(move_data_response)
                    list_of_moves.append(new_move.__str__())
    await session.close()
    return list_of_moves


async def generate_pokemon(poke_request, data):
    """
    Generate a Pokemon object based on API data.

    :param poke_request: Request - Used to determine expanded mode status.
    :param data: dict - JSON object containing API data.

    :return: Pokemon - An object representing a Pokemon with its attributes.
    """

    list_of_abilities = []
    list_of_stats = []
    list_of_moves = [moves["move"]["name"]for moves in data["moves"]]
    # list_of_moves = []

    if poke_request.is_expanded:
        try:
            for ability in data["abilities"]:
                async with aiohttp.ClientSession() as session:
                    async with session.get(ability["ability"]["url"]) as response:
                        ability_data = await response.json()
                        new_ability = generate_ability(ability_data)
                        list_of_abilities.append(new_ability.__str__())
                    await session.close()
        except Exception as e:
            print(e)

        try:
            for stat in data["stats"]:
                async with aiohttp.ClientSession() as session:
                    async with session.get(stat["stat"]["url"]) as response:
                        stat_data = await response.json()
                        new_stat = generate_stat(stat_data)
                        list_of_stats.append(new_stat.__str__())
                    await session.close()
        except Exception as e:
            print(e)

        # try:
            if "moves" in data:  # "moves" 키가 있는지 확인
                for move in data["moves"]:
                    # "move"와 "url" 키가 모두 있는지 확인
                    if "move" in move and "url" in move["move"]:
                        async with aiohttp.ClientSession() as session:
                            async with session.get(move["move"]["url"]) as response:
                                move_data = await response.json()
                                new_move = generate_move(move_data)
                                list_of_moves.append(new_move.__str__())
                        await session.close()
                    else:
                        print("Invalid move data:", move)  # 유효하지 않은 데이터에 대한 처리
            else:
                # "moves" 키가 없는 경우에 대한 처리
                print("No moves data found in the provided data.")
        # except Exception as e:
        #     # print("move url\n", move["move"]["url"])

        #     # print("\nnew_move error\n", move_data)
        #     print("complete", e)
        # try:
        #     list_of_moves = await get_moves(data)
        # except Exception as e:
        #     print("여기오류인가?", e)

    else:
        list_of_stats = {stat["stat"]["name"]: str(
            stat["base_stat"]) for stat in data["stats"]}
        list_of_abilities = [ability["ability"]["name"]
                             for ability in data["abilities"]]
        list_of_moves = [{"Move name": move["move"]["name"],
                          "Level acquired": move["version_group_details"][0]["level_learned_at"]} for move in data["moves"]]

    return Pokemon(height=data["height"],
                   weight=data["weight"],
                   stats=list_of_stats,
                   types=[types["type"]["name"] for types in data["types"]],
                   abilities=list_of_abilities,
                   moves=list_of_moves,
                   id=data["id"],
                   name=data["name"])


def generate_ability(data):
    """
    Generate an Ability object based on API data.

    :param data: dict - JSON object containing ability data.

    :return: Ability - An object representing an ability with its attributes.
    """
    return Ability(generation=data["generation"]["name"],
                   effect=data["effect_entries"][1]["effect"],
                   effect_short=data["effect_entries"][1]["short_effect"],
                   pokemon=[pokemon["pokemon"]["name"]
                            for pokemon in data["pokemon"]],
                   id=data["id"],
                   name=data["name"])


def generate_move(data):
    """
    Generate a Move object based on API data.

    :param data: dict - JSON object containing move data.

    :return: Move - An object representing a move with its attributes.
    """
    return Move(id=data["id"],
                name=data["name"],
                generation=data["generation"]["name"],
                accuracy=data["accuracy"],
                pp=data["pp"],
                power=data["power"],
                type=data["type"]["name"],
                damage_class=data["damage_class"]["name"],
                effect_short=data["effect_entries"][0]["short_effect"])


def generate_stat(data):
    """
    Generate a Stat object based on API data.

    :param data: dict - JSON object containing stat data.

    :return: Stat - An object representing a stat with its attributes.
    """
    move_damage_class = data["move_damage_class"]

    if move_damage_class is None:
        move_damage_class_str = "N/A"
    else:
        move_damage_class_str = move_damage_class["name"]
    return Stat(id=data["id"],
                name=data["name"],
                is_battle_only=data["is_battle_only"],
                move_damage_class=move_damage_class_str)
