package com.bcit.lab4munyoungcho

import kotlin.random.Random

class Hunt(override val minion: Minion):Mission(), Repeatable {

    override fun determineMissionTime(): Int {
        val missionTime = (minion.baseHealth + minion.baseSpeed) * Random.nextInt(0, 5)
        return missionTime
    }

    override fun reward(value: Int): String {
        val result = when (value) {
            in 11..20 -> "mouse"
            in 21..30 -> "fox"
            in 31..50 -> "buffalo"
            else -> "Nothing"
        }
        return result
    }

    override fun repeat(count: Int, listener: MissionListener) {
        repeat(count) {
            start(listener)
        }
    }

}