package com.bcit.lab8munyoungcho

import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Home
import androidx.compose.material.icons.filled.Star
import androidx.compose.material3.CenterAlignedTopAppBar
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.MutableState
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.navigation.NavController
import com.bcit.lab8munyoungcho.Screen

data class NavItem(val icon: ImageVector, val route:String)

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun MyTopBar(navController: NavController, selectedStar: Long){
    val navItems = listOf(
        NavItem(Icons.Filled.Home, Screen.HOME.route)
    )

    CenterAlignedTopAppBar(
        title = {
            Text(text = "Colors", fontSize = 40.sp)
        },
        navigationIcon = {
            IconButton(
                onClick = {
                    navController.navigate(navItems[0].route)
                }) {
                Icon(
                    navItems[0].icon,
                    contentDescription = null
                )
            }
        },
        actions = {
            selectedStar.let {
                Icon(
                    modifier = Modifier
                        .padding(10.dp)
                        .size(50.dp),
                    imageVector = Icons.Filled.Star
                    , contentDescription = null
                    , tint = Color(it)
                )
            }
        }
    )
}
