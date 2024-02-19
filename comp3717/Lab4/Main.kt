package com.bcit.lab4munyoungcho

/*
    Mun Young Cho
    A01330048
 */

fun main() {

    //create instance for each minion
    val dwarf = Dwarf()
    val elf = Elf()
    val human = Human()

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
    Gather(dwarf).start(missionListenerGather)
    Gather(dwarf).repeat(3, missionListenerGather)

    Hunt(elf).start(missionListenerHunt)
    Hunt(elf).repeat(3, missionListenerHunt)
}