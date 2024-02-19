package com.bcit.lab2munyoungcho

/*
    Mun Young Cho
    A01330048
 */

fun main(){
    val words = arrayOf("The", "Quick", "Brown", "Fox", "Went", "Over", "The", "Lazy", "Dog")
    val wordLength = mutableListOf<Int>()

    //line #1
    println("Words: ${words.contentToString()}")

    //line #2
    for(word in words){
        wordLength.add(word.length)
        continue
    }
    println("Word lengths: $wordLength")

    //line #3
    val longest = mutableListOf("")
    var longestWord =""
    var maxLength = 0
    for(i in 0..8){
        if(words[i].length > maxLength){
            maxLength = words[i].length
            longestWord = words[i]
        }else if(words[i].length == maxLength){
            longest.add(words[i])
        }else{
            break
        }

    }
    longest.add(longestWord)
    longest.removeFirst()
    println("Longest word(s): ${longest.reversed()}")

    //line #4
    var minLength = Int.MAX_VALUE
    words.forEach { word ->
        if (word.length < minLength) {
            minLength = word.length
        }
    }

    val shortestWords = mutableListOf<String>()
    var i = words.size - 1
    while (i >= 0) {
        if (words[i].length == minLength && !shortestWords.contains(words[i])) {
            shortestWords.add(words[i])
        }
        i--
    }

    println("Shortest word(s): $shortestWords")
}