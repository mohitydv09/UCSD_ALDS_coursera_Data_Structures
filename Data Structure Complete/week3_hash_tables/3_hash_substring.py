# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    multiplier=263
    prime=1000000007
    size_of_pattern=len(pattern)

    multiplier_exp=1
    for i in range(size_of_pattern-1):
        multiplier_exp=(multiplier_exp*multiplier)%prime

    pattern_hash=hash_func(pattern,prime,multiplier)
    last_index=len(text) - size_of_pattern + 1

    similar_hash=[]
    subtext_hash=hash_func(text[last_index-1:],prime,multiplier)
    if subtext_hash==pattern_hash:
            if pattern==text[last_index-1:]:
                similar_hash.append(last_index-1)

    for i in range(last_index-2,-1,-1):
        subtext_hash=ord(text[i])+(multiplier*(subtext_hash - (ord(text[i+size_of_pattern])*multiplier_exp)%prime))%prime
        if subtext_hash==pattern_hash:
            if pattern==text[i:i+size_of_pattern]:
                # print("text:",text[i:i+size])
                similar_hash.append(i)

    return reversed(similar_hash)

def hash_func(s,prime,multiplier):
    ans=0
    for c in reversed(s):
        ans=(ans*multiplier+ord(c))%prime
    return ans

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

