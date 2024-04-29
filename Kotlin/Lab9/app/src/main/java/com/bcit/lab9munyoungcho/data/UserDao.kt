package com.bcit.lab9munyoungcho.data

import androidx.room.Dao
import androidx.room.Delete
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query

@Dao
interface UserDao {
    @Query("SELECT * FROM user_table")
    fun getAll():List<LocalUser>

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    fun add(user: LocalUser)

    @Delete
    fun delete(user: LocalUser)
}