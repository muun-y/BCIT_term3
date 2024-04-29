package com.bcit.lab5munyoungcho

import kotlin.properties.Delegates
import kotlin.random.Random

class Hunt(minion: Minion, item:Item, companion: Companion):Mission(minion, item, companion), Repeatable {
    override fun determineMissionTime(): Int {
        val missionTime = (minion.baseHealth + minion.baseSpeed + (item?.timeModifier ?:0)) * Random.nextInt(0, 5)
        return missionTime
    }

    override fun reward(value: Int): String {
        return  if(companion != null ){
            companion.huntReward(value)
        }else {
            when (value) {
                in 11..20 -> "mouse"
                in 21..30 -> "fox"
                in 31..40 -> "buffalo"
                in 41..60 -> "dinosaur"
                else -> "Nothing"
            }
        }
    }


    override var repeatNum: Int by Delegates.vetoable(3) { _, _, newRepeatNum ->
        newRepeatNum <= 3
    }

    override fun repeat(count: Int, listener: MissionListener) {

        if (count > 3) {
            println("A minion cannot repeat a hunt more than 3 times! Repeating a hunt 3 times...\n")

        } else {
            println("Repeating a hunt $count times\n")
            }
        repeatNum = count
        repeat(repeatNum) {
            start(listener)
        }
        }


    }

