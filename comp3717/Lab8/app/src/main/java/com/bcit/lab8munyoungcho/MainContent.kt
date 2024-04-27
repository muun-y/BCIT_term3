package com.bcit.lab8munyoungcho

import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Scaffold
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableLongStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.navigation.NavType
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import androidx.navigation.navArgument
import com.bcit.lab8munyoungcho.MyTopBar

enum class Screen(val route:String){
    HOME("home")
}

@Composable
fun MainContent() {

    val navController = rememberNavController()
    val starColor = remember {
        mutableLongStateOf(0xFFFFFFFF)
    }

    Scaffold(
        topBar = {
            MyTopBar(
                navController = navController,
                selectedStar = starColor.longValue
            )
        }
    ) {it ->
        NavHost(
            navController = navController,
            startDestination = Screen.HOME.route,
            modifier = Modifier.padding(it)
        ){
            composable(Screen.HOME.route){
                Home(navController, starColor)
            }
            composable("info/{name}", arguments = listOf(navArgument("name"){
                type = NavType.LongType
            })){
                val name = it.arguments?.getLong("name")
                Info(name!!)
            }
        }
    }
}

