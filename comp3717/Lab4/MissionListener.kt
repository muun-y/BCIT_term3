package com.bcit.lab4munyoungcho

interface MissionListener {
    fun missionStart(minion: Minion)
    fun missionProgress()
    fun missionComplete(minion: Minion, result: String){
    }
}