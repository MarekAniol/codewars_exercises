# This time no story, no theory. The examples below show you how to write function accum:
# Examples:
#
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"

def accum(s):
    new_s = ''
    i = 1
    for el in s:
        new_s = new_s + (el * i).title() + "-"
        i += 1

    return new_s[0:-1]

def accum2(s):
    new_str = ''
    for i in range(len(s)):
        if i == len(s)-1:
            new_str += (s[i] * (i + 1)).title()
        else:
            new_str += (s[i]*(i+1)).title() + "-"

    return new_str

def accum3(s):
    return "-".join([(s[i] * (i+1)).capitalize() for i in range(len(s))])  # faster than title

print(accum3("ZpglnRxqenU"))