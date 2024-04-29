package com.bcit.lab9munyoungcho.data

import androidx.room.Database
import androidx.room.RoomDatabase


@Database(entities = [LocalUser::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun userDao(): UserDao
}