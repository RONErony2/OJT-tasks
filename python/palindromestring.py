# 22. Find the palindrome words with the count value from the given string.Output should be in
# form of dict. key will be palidrome word and value will be number of occurence.
# i/p given a string - Nittin & his mom went to a park last friday. His Mom observed that the weather
# was too cool. Nittin also met his sis. If we reverse the number 1331 then we also get 1331.
# o/p - {'nittin': 2, 'mom': 2, 'sis': 1, '1331': 2}


from collections import defaultdict

def find_palindrome_word(string):
    result = defaultdict(int)

    string = string.lower()
    sentences = string.split('.')
    for sentence in sentences:
        words = [w for w in sentence.split() if len(w)>1]
        for word in words:
            if word[::-1] == word:
                result[word] += 1
    return dict(result)

string = input("Enter the string : ")
print(find_palindrome_word(string))