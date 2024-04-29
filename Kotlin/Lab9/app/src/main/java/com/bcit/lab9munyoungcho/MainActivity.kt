package com.bcit.lab9munyoungcho

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.runtime.remember
import com.bcit.lab9munyoungcho.ui.main.MainContent
import com.bcit.lab9munyoungcho.ui.main.UserState

/**
 * Mun Young Cho, A01330048
 */

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val userRepository = (application as MyApp).userRepository
        setContent {
            val userState = remember{
                UserState(userRepository)
            }
            MainContent(userState)
        }
    }
}

