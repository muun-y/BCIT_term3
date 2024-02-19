package com.bcit.lab5munyoungcho

import kotlin.random.Random

class Gather(minion: Minion, item:Item, companion: Companion):Mission(minion, item, companion){

    override fun determineMissionTime(): Int {
        val missionTime = (minion.backpackSize + Item.COMPASS.timeModifier + minion.baseSpeed) * Random.nextInt(0, 5)
        return missionTime
    }

    override fun reward(value: Int): String {
        val result = when (value) {
            in 10..21 -> "bronze"
            in 22..33 -> "silver"
            in 34..44 -> "gold"
            in 45..60 -> "diamond"
            else -> "Nothing"
        }
        return result

    }
}
