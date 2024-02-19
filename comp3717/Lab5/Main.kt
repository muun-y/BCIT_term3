package com.bcit.lab5munyoungcho

/*
    Mun Young Cho
    A01330048
 */

fun main() {

    //create instance for each minion
    val dwarf = Dwarf()
    val elf = Elf()
    val human = Human()
    val orc = Orc(elf)

    //missionListener for Gather
    val missionListenerGather = object : MissionListener {
        override fun missionStart(minion: Minion) {
            when(minion){
                is Elf -> {
                    println(
                        """
            ${minion.catchphrase}
            
            An ${minion.race} was sent off to gather some resources! 
        """.trimIndent()
                    )

                }
                else ->{
                    println(
                        """
            ${minion.catchphrase}
            
            A ${minion.race} was sent off to gather some resources! 
        """.trimIndent()
                    )
                }
            }

        }

        override fun missionProgress() {
            println(
                """
            ...
            ...
            ...
        """.trimIndent()
            )
        }

        override fun missionComplete(minion: Minion, result: String) {
            when (minion) {
                is Elf -> {
                    println("An ${minion.race} has returned from gathering, and found $result!\n")
                }

                else -> {
                    println("A ${minion.race} has returned from gathering, and found $result!\n")
                }

            }
        }
    }

    //missionListener for Hunt
    val missionListenerHunt = object : MissionListener {
        override fun missionStart(minion: Minion) {
            when(minion){
                is Elf ->{
                    println(
                        """
            ${minion.catchphrase}
            An ${minion.race} started a new hunt!
        """.trimIndent()
                    )

                }
                else -> {
                    println(
                        """
            ${minion.catchphrase}
            A ${minion.race} started a new hunt!
        """.trimIndent()
                    )
                }
            }

        }

        override fun missionProgress() {
            println(
                """
            ...
            ...
            ...
        """.trimIndent()
            )
        }


        override fun missionComplete(minion: Minion, result: String) {
            when (minion) {
                is Elf -> {
                    println("An ${minion.race} has returned from gathering, and found a $result!\n")
                }

                else -> {
                    println("A ${minion.race} has returned from gathering, and found a $result!\n")
                }
            }
        }
    }

    // Run the gather mission once
    Hunt(elf ,item = Item.MAP, companion = elf).repeat(5, missionListenerHunt)
    Hunt(orc,item = Item.MAP, companion = elf).repeat(2, missionListenerHunt)

}