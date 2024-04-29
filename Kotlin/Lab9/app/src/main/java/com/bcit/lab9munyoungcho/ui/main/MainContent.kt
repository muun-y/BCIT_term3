package com.bcit.lab9munyoungcho.ui.main

import android.graphics.drawable.Icon
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Clear
import androidx.compose.material3.Button
import androidx.compose.material3.Icon
import androidx.compose.material3.Text
import androidx.compose.material3.TextField
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.bcit.lab9munyoungcho.data.LocalUser

@Composable
fun MainContent(userState: UserState) {
    val signupState = remember {
        SignupState()
    }

    Column(
        modifier = Modifier
            .fillMaxSize(),
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Spacer(modifier = Modifier.height(20.dp))
        CustomTextField(
            "uid::",
            signupState.uid.toString(),
            signupState.onUidChanged,
        )
        CustomTextField(
            "name::",
            signupState.name,
            signupState.onNameChanged
        )
        CustomTextField(
            "email::",
            signupState.email,
            signupState.onEmailChanged,
        )
        Spacer(modifier = Modifier.height(50.dp))
        Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.SpaceEvenly
        ) {
            Button(
                onClick = {
                    userState.add(LocalUser(
                        uid = signupState.uid,
                        name = signupState.name,
                        email = signupState.email
                    ))
                },
            ) {
                Text("Add",
                    fontSize = 30.sp)
            }
            Button(
                onClick = { userState.refresh() },
            ) {
                Text("Refresh",
                    fontSize = 30.sp)
            }
        }
        Spacer(modifier = Modifier.height(30.dp))
        LazyColumn{
            items(userState.users.size) {
                UserItem(
                    uid = userState.users[it].uid!!,
                    name = userState.users[it].name!!,
                    email = userState.users[it].email!!,
                    userState = userState,
                    signupState = signupState
                )
            }
        }
    }
}

@Composable
fun UserItem(uid: Int?, name: String, email: String, userState: UserState, signupState: SignupState) {
    Row(
        modifier = Modifier
            .fillMaxWidth()
            .height(100.dp)
            .padding(10.dp)
            .clickable {
                signupState.uid = uid
                signupState.name = name
                signupState.email = email
            }
            .background(
                color = Color(0xFFEAE4EF),
                shape = RoundedCornerShape(10.dp))
            .padding(20.dp),
        horizontalArrangement = Arrangement.SpaceBetween,
        verticalAlignment = Alignment.CenterVertically
    ) {
        Text(text = name, fontSize = 25.sp)
        Text(text = email, fontSize = 25.sp)
        Icon(
            imageVector = Icons.Default.Clear,
            contentDescription = "Delete Icon",
            modifier = Modifier
                .clickable {
                    userState.users.remove(LocalUser(uid, name, email))
                    userState.delete(LocalUser(uid, name, email))
                }
                .size(20.dp)
        )
    }
}

@Composable
fun CustomTextField(label: String, value: String?, onValueChanged: (String) -> Unit) {
    var displayValue = ""
    if (value != "null") {
        displayValue = value!!
    }
    Column() {
        Text(text = label)
        TextField(
            value = displayValue,
            onValueChange = onValueChanged,
            textStyle = TextStyle(fontSize = 20.sp),
            modifier = Modifier.width(350.dp)
        )
    }
}