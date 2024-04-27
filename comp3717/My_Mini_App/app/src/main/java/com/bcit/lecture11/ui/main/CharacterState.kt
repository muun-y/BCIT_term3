package com.bcit.lecture11.ui.main

import androidx.compose.runtime.mutableStateListOf
import com.bcit.lecture11.data.CharacterInfo
import com.bcit.lecture11.data.CharacterRepository

class CharacterState(private val characterRepository: CharacterRepository) {

    var character = mutableStateListOf<CharacterInfo>()

    suspend fun getCharacter() {
        character.also {
            it.clear()
            it.addAll(characterRepository.getCharacter().character)
        }


    }

    fun getImageUrl(index: Int): String {
        if (index < 0 || index >= character.size) {
            return ""
        }

        return character[index]?.imageUrl ?: ""
    }

}