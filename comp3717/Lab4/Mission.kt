package com.bcit.lab4munyoungcho

abstract class Mission() {
    protected abstract val minion: Minion
    fun start(listener: MissionListener){
        val missionTime = determineMissionTime()
        val missionResult = reward(missionTime)
        listener.missionStart(minion)
        listener.missionProgress()
        listener.missionComplete(minion, missionResult)
    }
    protected abstract fun determineMissionTime(): Int
    protected abstract fun reward(value: Int): String
}