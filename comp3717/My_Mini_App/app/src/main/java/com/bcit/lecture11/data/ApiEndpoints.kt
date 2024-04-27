package com.bcit.lecture11.data

enum class ApiEndpoints(val url: String) {
    BASE_URL("https://api.disneyapi.dev"),
    CHARACTERS("${BASE_URL.url}/character"),
}