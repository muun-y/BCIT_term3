package com.bcit.lab5munyoungcho

class Orc(minion: Minion) : Minion by minion {
    override var race: String = "Orc"
    override var catchphrase: String = "ARRGH!"
}