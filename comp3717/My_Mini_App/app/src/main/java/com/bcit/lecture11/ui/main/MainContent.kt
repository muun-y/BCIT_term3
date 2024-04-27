package com.bcit.lecture11.ui.main


import androidx.compose.animation.animateContentSize
import androidx.compose.foundation.Image
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.AccountCircle
import androidx.compose.material.icons.filled.Star
import androidx.compose.material.icons.outlined.Star
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableLongStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import coil.compose.AsyncImage
import coil.compose.rememberImagePainter
import com.bcit.lecture11.MyTopBar
import com.bcit.lecture11.Screen


@Composable
fun MainContent(characterState: CharacterState) {
    val navController = rememberNavController()
    var savedImageUrl by remember { mutableStateOf<String?>(null) }

    Scaffold(
        topBar = {
            MyTopBar(
                navController = navController,

                )
        }
    ) { it ->
        NavHost(
            navController = navController,
            startDestination = Screen.HOME.route,
            modifier = Modifier.padding(it)
        ) {
            composable(Screen.HOME.route) {
                Column(
                    modifier = Modifier
                        .fillMaxSize()
                        .padding(16.dp),
                    verticalArrangement = Arrangement.Center,
                    horizontalAlignment = Alignment.CenterHorizontally
                ) {

                    Box {
                        //when there is no selected image just icon showed up
                        if (savedImageUrl.isNullOrEmpty()) {
                            Icon(
                                imageVector = Icons.Filled.AccountCircle,
                                contentDescription = null,
                                modifier = Modifier.size(120.dp),
                                tint = Color(0xFFA6AFE4),
                            )
                        } else {
                            Column(
                                verticalArrangement = Arrangement.Center,
                                horizontalAlignment = Alignment.CenterHorizontally) {
                                Text(
                                    "New profile image is applied!",
                                    color = Color(0xFF8E9AE6),
                                    fontSize = 20.sp,
                                    modifier = Modifier
                                        .padding(16.dp)
                                )

                                Box(
                                    modifier = Modifier
                                        .size(120.dp)
                                        .clip(CircleShape)
                                        .border(
                                            width = 2.dp,
                                            color = Color(0xFF8E9AE6),
                                            shape = CircleShape
                                        )
                                ) {
                                    AsyncImage(
                                        model = savedImageUrl,
                                        contentDescription = null,
                                        modifier = Modifier.fillMaxSize()

                                    )
                                }
                            }
                        }
                    }

                    Button(
                        onClick = {
                            navController.navigate(Screen.INFO.route)
                        },
                        colors = ButtonDefaults.buttonColors(
                            contentColor = Color(0xFF8E9AE6),
                            containerColor = Color(0xFFD2D6EC),
                        ),
                        modifier = Modifier.padding(16.dp)
                    ) {
                        Text("Search")
                    }
                    Text(
                        "Find your Favorite Disney Character!!",
                        color = Color(0xFF8E9AE6),
                        fontSize = 20.sp
                    )
                }
            }

            composable(Screen.INFO.route) {
                LazyColumn() {
                    items(characterState.character.size) { index ->
                        var isExpanded by remember { mutableStateOf(false) }
                        val character = characterState.character[index]
                        var isStarred by remember { mutableStateOf(false) }
                        Card(modifier = Modifier
                            .padding(8.dp)
                            .fillMaxWidth()
                            .clickable { isExpanded = !isExpanded }
                            .animateContentSize(),
                            elevation = CardDefaults.cardElevation(defaultElevation = 2.dp),
                            colors = CardDefaults.cardColors(containerColor = Color(0xFFD2D6EC))) {
                            Row {
                                Column(
                                    horizontalAlignment = Alignment.CenterHorizontally,
                                    verticalArrangement = Arrangement.Center,
                                    modifier = Modifier
                                        .padding(16.dp)
                                        .clickable {
                                            isExpanded = !isExpanded
                                        }, // Toggle expansion on card click

                                ) {
                                    if (!isExpanded) {
                                        Text(character.name, color = Color(0xFF8E9AE6))
                                    }

                                    if (isExpanded) {
                                        Row {
                                            Text(character.name, color = Color(0xFF8E9AE6))

                                            IconButton(
                                                onClick = {
                                                    savedImageUrl =
                                                        characterState.getImageUrl(index)
                                                    isStarred = !isStarred
                                                }
                                            ) {
                                                Icon(
                                                    imageVector = if (isStarred) Icons.Filled.Star else Icons.Outlined.Star,
                                                    contentDescription = null,
                                                    tint = if (isStarred) Color(0xFF8E9AE6) else Color.White,
                                                    modifier = Modifier.size(25.dp)
                                                )
                                            }

                                            AsyncImage(
                                                model = characterState.getImageUrl(index),
                                                contentDescription = null,
                                                modifier = Modifier.size(120.dp)
                                            )
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}