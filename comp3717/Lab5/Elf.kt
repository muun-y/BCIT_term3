package com.bcit.lab5munyoungcho
    open class Elf : Minion, Companion {
        override var race: String = "Elf"
        override var baseHealth: Int = 2
        override var baseSpeed: Int = 8
        override var backpackSize: Int = 3
        override var catchphrase: String = "My arrows never miss!"
        override fun huntReward(value: Int): String {
            return when (value) {
                in 11..20 -> "fish"
                in 21..30 -> "forest bear"
                in 31..40 -> "orc"
                in 41..60 -> "troll"
                else -> "Nothing"
            }
        }
    }
