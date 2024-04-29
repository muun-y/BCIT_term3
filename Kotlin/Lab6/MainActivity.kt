package com.bcit.lab6munyoungcho

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.bcit.lab6munyoungcho.ui.theme.Lab6MunYoungChoTheme

/**
 * Mun Young Cho, A01330048
 */

data class MyBoxData(val color: Color, val size:Int)
val boxDataList = listOf(
    MyBoxData(Color(0xFFF87FA9), 110),
    MyBoxData(Color(0xFF26CC2D), 80),
    MyBoxData(Color(0xFFF3B04C), 130)
)

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            Greeting()
        }
    }
}

@Composable
fun MyBox(data:MyBoxData){

    Row(
        modifier = Modifier,
        horizontalArrangement = Arrangement.Center
    ) {
        Box(
            modifier = Modifier
                .size(data.size.dp)
                .background(data.color)
        )
    }
}

@Composable
fun Greeting() {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .background(Color(0xFF426D91)),
        verticalArrangement = Arrangement.SpaceEvenly
    ) {
        Row(
            modifier = Modifier,
            verticalAlignment = Alignment.Bottom

        ) {
            Box(
                modifier= Modifier
                    .size(200.dp)
                    .background(Color(0xFF0326E9))

            )

            Box(
                modifier= Modifier
                    .size(50.dp)
                    .background(Color(0xFFEC0000))
            )
        }
        Row (
            modifier = Modifier
                .fillMaxWidth()
                .size(150.dp)
                .background(Color(0xFF7F42EB))
                .padding(end = 15.dp),
            horizontalArrangement = Arrangement.End,
            verticalAlignment = Alignment.CenterVertically
        ){
            LazyRow(
                modifier = Modifier,
                verticalAlignment = Alignment.CenterVertically
            ) {
                items(boxDataList.size) {
                    MyBox(boxDataList[it])
                }
            }
        }
        Row(
            modifier = Modifier
                .fillMaxWidth(),
            horizontalArrangement = Arrangement.Center

        ) {
            Box(
                modifier = Modifier
                    .size(160.dp)
                    .background(Color(0xFF864B02)),
                contentAlignment = Alignment.Center
            ) {
                Text(
                    text = "Lab 6",
                    color = Color.White,
                    fontSize = 50.sp
                )
            }
        }

    }
}


