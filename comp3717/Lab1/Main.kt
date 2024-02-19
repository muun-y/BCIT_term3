package com.bcit.lab1munyoungcho

/*
    Mun Young Cho
    A01330048
 */

const val VERSION_NUM: Double = 0.2
const val SLOGAN: String = "deliver with a smile"

fun main(){
    val streetNum: Int = 123
    val streetName: String = "loch ness road"
    val fullAddress: String? = if(VERSION_NUM >= 1){
        "%s %s, Glasgow, Scotland".format(streetNum, streetName)
    }else{
        println(
            """Starting beta version...
... 
...
...
            
            """.trimIndent()
        )
        null
    }
    val message: String = """
        
            Food Delivery Service v$VERSION_NUM

Welcome to Glasgow's finest food delivery service, where we provide
you with swift instructions on where to deliver your food. 

            Please deliver the food to: 
        
            ${fullAddress?.uppercase()}
        
Your hard work and commitment to delivering food are
always appreciated, and never forget..${SLOGAN.uppercase()}
        
...Thank you.         
    """.trimIndent()

    println(message)
}