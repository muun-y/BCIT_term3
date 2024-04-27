package com.bcit.lecture11

import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.AccountCircle
import androidx.compose.material.icons.filled.Home
import androidx.compose.material.icons.filled.Star
import androidx.compose.material3.CenterAlignedTopAppBar
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBarDefaults
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.unit.sp
import androidx.navigation.NavController


enum class Screen(val route: String){
    HOME("home"),
    INFO("info")
}

data class NavItem(val icon: ImageVector, val route:String)

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun MyTopBar(navController: NavController){
    val navItems = listOf(
        NavItem(Icons.Filled.Home, com.bcit.lecture11.Screen.HOME.route)
    )

    CenterAlignedTopAppBar(
        title = {
            Text(
                text = "Disney Character Profile",
                fontSize = 19.sp,
                color=Color.White)
        },
        colors = TopAppBarDefaults.centerAlignedTopAppBarColors(containerColor = Color(0xFFA6AFE4)),
        navigationIcon = {
            IconButton(
                onClick = {
                    navController.navigate(navItems[0].route)
                }) {
                Icon(
                    navItems[0].icon,
                    contentDescription = null,
                    tint = Color.White
                )
            }
        }
    )
}
