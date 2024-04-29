package com.bcit.lab5munyoungcho

abstract class Mission(protected val minion: Minion,
                       protected val item: Item? = null,
                       protected val companion: Companion? = null
) {
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