package com.bcit.lab5munyoungcho

interface MissionListener {
    fun missionStart(minion: Minion)
    fun missionProgress()
    fun missionComplete(minion: Minion, result: String){
    }
}