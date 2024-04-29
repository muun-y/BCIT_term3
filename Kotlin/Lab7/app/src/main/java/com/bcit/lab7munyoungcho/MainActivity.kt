package com.bcit.lab7munyoungcho

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.animation.animateContentSize
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.Image
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Button
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateListOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.res.stringArrayResource
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.bcit.lab7munyoungcho.ui.theme.Lab7MunYoungChoTheme
import kotlin.random.Random

/**
 * Mun Young Cho, A01330048
 */

data class Characters(val name: String, val imageId:Int)

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            val characterNames = stringArrayResource(id = R.array.characters)
            val characterLists = listOf(
                Characters(characterNames[0], R.drawable.ahsoka),
                Characters(characterNames[1], R.drawable.bb8),
                Characters(characterNames[2], R.drawable.c3po),
                Characters(characterNames[3], R.drawable.chewbacca),
                Characters(characterNames[4], R.drawable.grogu),
                Characters(characterNames[5], R.drawable.jabba),
                Characters(characterNames[6], R.drawable.kilo),
                Characters(characterNames[7], R.drawable.trooper),
                Characters(characterNames[8], R.drawable.yoda),
            )

            val cartoonStateList = remember {
                mutableStateListOf(*characterLists.shuffled().take(9).toTypedArray())
            }

            Column(
                horizontalAlignment = Alignment.CenterHorizontally
            ) {
                Button(
                    onClick = {
                        cartoonStateList.shuffle()
                    },
                    modifier = Modifier
                        .padding(10.dp)
                        .size(width = 200.dp, height = 50.dp)
                        .clip(shape = RoundedCornerShape(0.dp)),
                    shape = RoundedCornerShape(1.dp)
                ) {
                    Text(text = "Shuffle", fontSize = 25.sp)
                }

                LazyColumn(
                    modifier = Modifier.fillMaxSize(),
                ) {
                    val rows = cartoonStateList.chunked(3)
                    rows.forEach { rowItems ->
                        item {
                            LazyRow(
                                modifier = Modifier.fillMaxWidth(),
                                contentPadding = PaddingValues(horizontal = 16.dp)
                            ) {
                                rowItems.forEach { character ->
                                    item {
                                        StarCards(character)
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }


    @Composable
    fun StarCards(characters: Characters) {
        var isExpanded by remember { mutableStateOf(false) }

        Card(
            modifier = Modifier
                .padding(10.dp)
                .clickable {
                    isExpanded = !isExpanded
                }
                .animateContentSize(),
            elevation = CardDefaults.cardElevation(defaultElevation = 2.dp)
        ) {
            Column(
                modifier = Modifier
                    .size(if (isExpanded) 220.dp else 180.dp)
                    .clickable { isExpanded = !isExpanded }, // Toggle expansion on card click
                horizontalAlignment = Alignment.CenterHorizontally,
                verticalArrangement = Arrangement.Center
            ) {
                if (!isExpanded) {
                    // Show Text only if not expanded
                    Text(
                        characters.name,
                        fontSize = 25.sp,
                        modifier = Modifier.padding(8.dp),
                        color = Color.Black
                    )
                    Image(
                        painter = painterResource(id = characters.imageId),
                        contentDescription = "",
                        modifier = Modifier
                            .size(120.dp)
                            .clip(shape = CircleShape)
                    )
                }

                if(isExpanded){
                    Image(
                        painter = painterResource(id = characters.imageId),
                        contentDescription = "",
                        modifier = Modifier
                            .size(180.dp)
                            .clip(shape = CircleShape)
                    )
                }

            }
        }
    }
}

