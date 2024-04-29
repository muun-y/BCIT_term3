package com.bcit.lab9munyoungcho.ui.main


import androidx.compose.runtime.toMutableStateList
import com.bcit.lab9munyoungcho.data.LocalUser
import com.bcit.lab9munyoungcho.data.UserRepository

class UserState(private val repository: UserRepository) {

    //UI state
    var users = repository.getAll().toMutableStateList()

    fun add(localUser: LocalUser){
        repository.insertEntity(localUser)
    }

    fun refresh(){
        users.apply {
            clear()
            addAll(repository.getAll())
        }
    }

    fun delete(localUser: LocalUser){
        // remove the user in mutableStateList
        users.remove(localUser)
        // Then delete the user in the database
        repository.deleteUser(localUser)
    }
}