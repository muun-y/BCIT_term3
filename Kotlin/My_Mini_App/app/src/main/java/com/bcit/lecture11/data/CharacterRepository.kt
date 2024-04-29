package com.bcit.lecture11.data

import com.google.gson.Gson
import com.google.gson.JsonObject
import io.ktor.client.HttpClient
import io.ktor.client.call.body
import io.ktor.client.request.get

class CharacterRepository(private val client: HttpClient) {

    suspend fun getCharacter():Character{
        val response = client.get(ApiEndpoints.CHARACTERS.url)

        val json = response.body<JsonObject>().toString()

        return deserializeJson(json)
    }

    private fun deserializeJson(json:String):Character{
        return Gson().fromJson(json, Character::class.java)
    }

}