package com.bcit.lecture11.data

import com.google.gson.annotations.SerializedName

data class Character (
    @SerializedName("data")
    val character: List<CharacterInfo>
)

data class CharacterInfo(
    @SerializedName("_id")
    val id: Int,
    val name: String,
    val imageUrl: String

)