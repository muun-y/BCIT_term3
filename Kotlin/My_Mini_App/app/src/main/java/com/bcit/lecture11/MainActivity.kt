package com.bcit.lecture11

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.navigation.NavController
import com.bcit.lecture11.ui.main.CharacterState
import com.bcit.lecture11.ui.main.MainContent
import com.bcit.lecture11.ui.theme.Lecture11Theme

/**
 * My mini app: This is an app that helps people who are Disney fans find their favorite Disney character
 * as their profile image. When they click the "search" button on the home page, it will link to the Disney
 * character list (info) page. Then, when they click on the character they want to use as a profile image,
 * the card will be expanded. Clicking the star button will change the star's color. After that, clicking
 * the home button on the top bar will apply the chosen profile image.
 *
 * Mun Young Cho(A01330048)
 */
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val characterRepository = (application as MyApp).characterRepository
        setContent {
            val characterState = CharacterState(characterRepository)

            LaunchedEffect(characterState){
                characterState.getCharacter()
            }

            MainContent(characterState)
        }
    }
}
