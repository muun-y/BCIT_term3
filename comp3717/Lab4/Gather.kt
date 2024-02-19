package com.bcit.lab4munyoungcho

import kotlin.random.Random

class Gather(override val minion: Minion):Mission(){

    override fun start(listener: MissionListener) {
        super.start(listener)
    }

    override fun determineMissionTime(): Int {
        val missionTime = (minion.backpackSize + minion.baseSpeed) * Random.nextInt(0, 5)
        return missionTime
    }

    override fun reward(value: Int): String {
        val result =  when (value) {
            in 10..21 -> "bronze"
            in 22..33 -> "silver"
            in 34..50 -> "gold"
            else -> "Nothing"
        }
        return result

    }
}
