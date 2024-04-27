package com.bcit.lab9munyoungcho.ui.main


import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.room.ColumnInfo
import androidx.room.Entity
import androidx.room.PrimaryKey

class SignupState {

    //state for uid
    var uid by mutableStateOf<Int?>(null)
    var onUidChanged: (String) -> Unit = {
        uid = it.toIntOrNull()
    }

    //state for name
    var name by mutableStateOf("")
    val onNameChanged: (String) -> Unit = {
        name = it
    }

    //state for email
    var email by mutableStateOf("")
    val onEmailChanged: (String) -> Unit = {
        email = it
    }


}
