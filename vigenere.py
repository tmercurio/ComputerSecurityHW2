def findRepeats(cipher):

    repeats = []
    back_to_back = {}

    cur_repeat = False
    repeat_start = 0
    repeat_index = 0

    for i, letter in enumerate(cipher):
        print(i, letter)
        if cur_repeat:
            #print(i, letter, repeat_start)
            if letter == cipher[repeat_start + repeat_index + 1]:
                repeat_index += 1
            else:
                if (repeat_index >= 2):
                    print(repeat_start, repeat_index, i, cipher[repeat_start + repeat_index], letter)
                repeats.append((cipher[repeat_start:repeat_start + repeat_index + 1], repeat_start, i - repeat_index - 1))
                cur_repeat = False

        elif i > 0 and cipher[i - 1] in back_to_back:
            for next in back_to_back[cipher[i - 1]]:
                if letter == next[0]:
                    cur_repeat = True
                    repeat_start = next[1]
                    repeat_index = 1
                    break

        back_to_back[cipher[i - 1]] = back_to_back.get(cipher[i - 1], []) + [(letter, i - 1)]
        #print(back_to_back)
        #print()
        #print()

    #print(back_to_back)
    return repeats


def make_alphabets(cipher, period):
    alphabets = []
    for i, letter in enumerate(cipher):
        if (len(alphabets) >= period):
            alphabets[i % period].append(letter)
        else:
            alphabets.append([letter])

    frequencies = []

    for i, alphabet in enumerate(alphabets):
        frequencies.append({})
        for letter in alphabet:
            frequencies[i][letter] = frequencies[i].get(letter, 0) + 1


    for i, alpha in enumerate(frequencies, 1):
        print("Alphabet ", i)
        for letter in sorted(alpha):
            print(f"{letter}: {alpha[letter]};", end = " ")

        print("\n")

    average_frequencies = [0.08, 0.015, 0.03, 0.04, 0.13, 0.02, 0.015, 0.06, 0.065, 0.005, 0.005, 0.035, 0.03, 0.07, 0.08, 0.02, 0.002, 0.065, 0.06, 0.09, 0.03, 0.01, 0.015, 0.005, 0.02, 0.002]
    probabilities = []
'''
    for i, alpha in enumerate(frequencies):
        print(alpha)
        probabilities.append([])
        for j in range(26):
            probabilities[i].append([chr(65 + j), 0])
            for k in range(26):
                probabilities[i][j][1] += round((alpha.get(chr(k + 65), 0) * average_frequencies[j]), 2)
        print(probabilities)

    for alpha in probabilities:
        print(alpha)
        print()

'''

def decode(cipher):
    cipher_list = list(cipher)

    for i in range(len(cipher)):
        if (i % 5) == 1:
            cipher_list[i] = chr(((ord(cipher[i]) - 51) % 26) + 65)
        if (i % 5) == 3:
            cipher_list[i] = chr(((ord(cipher[i]) - 64) % 26) + 65)
        if (i % 5) == 4:
            cipher_list[i] = chr(((ord(cipher[i]) - 69) % 26) + 65)

    for i, letter in enumerate(cipher_list):
        if i % 5 == 4:
            print(letter, end = " ")
        else:
            print(letter, end = "")


def main():
    #cipher = "SQRHISAFHRTQRVSVQN"
    cipher = "TTEUMGQNDVEOIOLEDIREMQTGSDAFDRCDYOXIZGZPPTAAITUCSIXFBXYSUNFESQRHISAFHRTQRVSVQNBEEEAQGIBHDVSNARIDANSLEXESXEDSNJAWEXAODDHXEYPKSYEAESRYOETOXYZPPTAAITUCRYBETHXUFINR"

    #for repeat in findRepeats(cipher):
    #    print(repeat)
    #make_alphabets(cipher, 5)
    decode(cipher)

if __name__ == "__main__":
    main()
