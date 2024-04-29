package com.bcit.lab8munyoungcho

import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.outlined.Info
import androidx.compose.material3.Icon
import androidx.compose.runtime.Composable
import androidx.compose.runtime.MutableLongState
import androidx.compose.runtime.remember
import androidx.compose.runtime.toMutableStateList
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.toArgb
import androidx.compose.ui.unit.dp
import androidx.navigation.NavController


@Composable
fun Home(navController: NavController, selectedStar: MutableLongState){
    val list = listOf(
        Color(0xFFF44336),
        Color(0xFFE91E63),
        Color(0xFF9C27B0),
        Color(0xFF3F51B5),
        Color(0xFF2196F3),
        Color(0xFF009688),
        Color(0xFF4CAF50),
        Color(0xFFFFEB3B)
    )

    val stateList = remember{
        list.toMutableStateList()
    }

    LazyColumn{
        items(stateList.size){
            ColorItem(stateList[it], navController, selectedStar)
        }
    }
}

@Composable
fun ColorItem(color: Color, navController: NavController? = null, selectedStar: MutableLongState) {
    Row(
        horizontalArrangement = Arrangement.End,
        verticalAlignment = Alignment.Top,
        modifier = Modifier
            .padding(10.dp)
            .fillMaxWidth()
            .height(100.dp)
            .background(color)
            .clickable {
                selectedStar.longValue = color.toArgb().toLong()
            }
            .padding(10.dp)
    ) {
        Icon(
            imageVector = Icons.Outlined.Info,
            contentDescription = null,
            modifier = Modifier
                .size(30.dp)
                .clickable {
                    navController?.navigate("info/${color.toArgb()}")
                }
        )
    }
}