def solution(hp):
    val = 5
    count = 0
    while hp > 0:
        count += hp // val
        hp = hp % val
        val -= 2
    return count