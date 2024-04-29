package com.bcit.lab5munyoungcho

interface Repeatable {
    var repeatNum: Int
    fun repeat(count: Int, listener: MissionListener)
}