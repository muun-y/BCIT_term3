package com.bcit.lecture11

import android.app.Application
import com.bcit.lecture11.data.CharacterRepository
import io.ktor.client.HttpClient
import io.ktor.client.plugins.contentnegotiation.ContentNegotiation
import io.ktor.serialization.gson.gson

//put the settings about security
class MyApp: Application() {

    val client = HttpClient{

        install(ContentNegotiation){
            gson()
        }
    }

    val characterRepository = CharacterRepository(client)

}