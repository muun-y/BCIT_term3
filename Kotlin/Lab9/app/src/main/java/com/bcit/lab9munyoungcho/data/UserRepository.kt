package com.bcit.lab9munyoungcho.data

class UserRepository(private val userDao: UserDao) {

    //any business logic would go here
    fun insertEntity(user: LocalUser){
        userDao.add(user)
    }

    fun getAll(): List<LocalUser>{
        return userDao.getAll()
    }

    fun deleteUser(user:LocalUser){
        userDao.delete(user)
    }
}