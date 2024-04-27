package com.bcit.lab8munyoungcho

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.sp

@Composable
fun Info(name:Long){
    Column(
        modifier = Modifier
            .fillMaxSize()
            .background(Color(name)),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center
    ) {
        Text(text = (name and 0xFFFFFFFFL).toHexString(), fontSize = 45.sp)
    }
}

fun Long.toHexString(): String {
    return java.lang.Long.toHexString(this)
}