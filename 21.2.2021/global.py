def fun():
    global i
    i=0
    print(i)
    i=i+1
    fun()

fun()
