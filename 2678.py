def countSeniors(details: list[str]) -> int:
    cnt = 0
    for d in details:
        if int(d[11:13]) > 60:
            cnt += 1
    return cnt


if __name__ == "__main__":
    print(countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"]))
    print(countSeniors(["1313579440F2036","2921522980M5644"]))
