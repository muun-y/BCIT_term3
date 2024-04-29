package com.bcit.lecture11

import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.AccountCircle
import androidx.compose.material.icons.outlined.Info
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Icon
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.MutableLongState
import androidx.compose.runtime.remember
import androidx.compose.runtime.toMutableStateList
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.toArgb
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.unit.dp
import androidx.navigation.NavController
import androidx.navigation.compose.rememberNavController
import coil.compose.AsyncImage

@Composable
fun HomeComposable(savedImageUrl: String?) {
    val navController = rememberNavController()
    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp)
            .size(150.dp),
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally
    ) {

        if (savedImageUrl != null && savedImageUrl.isNotEmpty()) {
            Column(modifier = Modifier
                .fillMaxSize()
                .padding(16.dp)
                .size(150.dp),
                verticalArrangement = Arrangement.Center,
                horizontalAlignment = Alignment.CenterHorizontally) {
                AsyncImage(
                    model = savedImageUrl,
                    contentDescription = null,
                    modifier = Modifier
                        .padding(10.dp)
                        .size(150.dp),
                    contentScale = ContentScale.Fit
                )
                Button(
                    onClick = {
                        navController.navigate(Screen.INFO.route)
                    },
                    colors = ButtonDefaults.buttonColors(
                        contentColor = Color.White,
                        containerColor = Color(0xFF5991BD),
                    ),
                    modifier = Modifier.padding(16.dp)
                ) {
                    Text("Chang!!")
                }
                Text(
                    "Change your Favorite Disney Character!!",
                    color = Color(0xFF5991BD)
                )
            }
        } else {
            Column(modifier = Modifier
                .fillMaxSize()
                .padding(16.dp)
                .size(150.dp),
                verticalArrangement = Arrangement.Center,
                horizontalAlignment = Alignment.CenterHorizontally) {
                Icon(
                    modifier = Modifier
                        .padding(10.dp)
                        .size(150.dp),
                    imageVector = Icons.Filled.AccountCircle,
                    contentDescription = null,
                    tint = Color(0xFFB5D3EB)
                )

                Button(
                    onClick = {
                        navController.navigate(Screen.INFO.route)
                    },
                    colors = ButtonDefaults.buttonColors(
                        contentColor = Color.White,
                        containerColor = Color(0xFF5991BD),
                    ),
                    modifier = Modifier.padding(16.dp)
                ) {
                    Text("Click!")
                }
                Text(
                    "Find your Favorite Disney Character!!",
                    color = Color(0xFF5991BD)
                )

            }
        }
    }
}