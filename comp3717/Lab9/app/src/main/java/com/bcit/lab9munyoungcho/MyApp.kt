package com.bcit.lab9munyoungcho

import android.app.Application
import androidx.room.Room
import com.bcit.lab9munyoungcho.data.AppDatabase
import com.bcit.lab9munyoungcho.data.UserRepository

class MyApp: Application() {

    private val db by lazy{
        Room.databaseBuilder(
            applicationContext,
            AppDatabase::class.java, "my-cool-database")
            .allowMainThreadQueries()
            .build()
    }

    val userRepository by lazy{
        UserRepository(db.userDao())
    }
}