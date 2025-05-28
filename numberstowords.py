def words(n):
    ones=["zero","one","two","three","four","five","six","seven","eight","nine"]
    two=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    hundred=["","","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
    if n<10:
        return ones[n]
    elif n<20:
        return two[n-10]
    elif n<100:  #99
        return hundred[n//10]+(ones[n%10] if n%10!=0 else " ")
    elif n<1000:   #311  three hunderd and eleven
        return ones[n//100]+"hunderd and"+(words(n%100) if n%100!=0 else " ")
    return n

print(words(8129))