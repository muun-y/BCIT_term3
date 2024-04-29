package com.bcit.lab3munyoungcho

/*
    Mun Young Cho
    A01330048
 */

//red box using mutableMapOf
val map1 = mutableMapOf(
    1492 to "Christopher Columbus discovers America",
    1601 to "William Shakespeare writes Hamlet",
    1632 to "Galileo discovered the acceleration of gravity on Earth to be 9.8m/s",
    1838 to "Roughly 9.46 trillion km, the light-year is first used as a measurement in astronomy",
    2020 to "Covid 19 Pandemic"
)

//line1: use anonymous function in line1
//arg: int -> return: string
val line1 = fun(key: Int) : String{
    return "${map1[key]}"
}

//line2: use lambda function
//arg: int -> return: string?
val line2: (Int) -> String? = { key -> "${map1[key]}" }

//line3: use function as parameter and use function reference
//arg: int -> return: unit
fun line3(arg1: (Int) -> Unit, key: Int): Unit {
    arg1(key)
}

fun line(key: Int): Unit {
    val result = map1[key] ?: "Key not found"
    println(result)
}

//line4: use argument map
//arg: map -> return: unit
fun line4(map1: Map<Int, String>, key: Int): Unit {
    println("${map1[key]}")
}

//line5: use argument Pair
//arg: pair -> return: string
fun line5(pair: Pair<Int, String>): String{
    val(key, value) = pair
    return "${map1[key]}"
}


fun main(){
    //display red box
    map1.forEach{println(it)}

    println("""
        
        
    """.trimIndent())

    //display purple box
    //display line1
    val result1: String = line1(1492)
    println(result1)

    //display line2
    println(line2(1601))

    //display line3
    line3(::line, 1632)

    //display line4
    line4(map1, 1838)

    //display line5
    val result5 = line5(2020 to "")
    println(result5)
}



