# Member D(ingmar): Valid Segmentation

def word_break(s, word_dict):
    #DP array to store the list of sentences that can be formed for each prefix
    dp = [[] for _ in range(len(s) + 1)]
    dp[0] = ['']  #Base case: empty string has one way to be "segmented" (empty string)
    
    #Iterate through the string
    for i in range(1, len(s) + 1):
        for j in range(i):
            #Check if the substring s[j:i] is in the word dictionary
            if s[j:i] in word_dict:
                #If dp[j] is not empty, it means we found a valid segmentation up to index j
                for sentence in dp[j]:
                    #Add current word to all valid sentences from dp[j]
                    dp[i].append((sentence + ' ' + s[j:i]).strip())
    for item in reversed(dp):
        if item:  #This checks not '', not [], not None, etc.
            return item
    return ["No valid segmentation found using the given dictionary."]  #If no non-empty item is found


#Example usage
#word_dict = {"this", "is", "a", "pen", "apple"}
#string = "thisisapen"
#word_dict = {"cats", "cat", "and", "dog", "dogs"}
#string = "catsanddogssdfsdf"
#valid_segmentations = word_break(string, word_dict)
#print(valid_segmentations[0])
        