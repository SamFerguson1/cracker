def worderizer(listOWords):
    low1 = listOWords[0]
    nlow1 = low1[:3]
    low2 = listOWords[1]
    nlow2 = low2[5:]
    worderizedWord = nlow1 + nlow2 + "s"
    return worderizedWord

def main():

    words = ["Queen", "congestion"]
    print(worderizer(words))

main()
