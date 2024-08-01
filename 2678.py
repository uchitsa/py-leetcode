def countSeniors(details: list[str]) -> int:
    cnt = 0
    for d in details:
        tens = int(d[11])*10
        if tens<6:
            continue
        if tens + int(d[12]) > 60:
            cnt += 1
    return cnt


if __name__ == "__main__":
    print(countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"]))
    print(countSeniors(["1313579440F2036","2921522980M5644"]))
