
s = 'bzyxabb' #This is what we're looking at
longestRun = s[0] #This is what we want to print.
#started with first index in the event that there is no substring larger than len() = 1

for i in range(len(s)): #iterate through all letters except the last one
    checkLongestRun = s[i] #tries new substrings
#loop that checks alphabetical order and concatenates
    while (i < (len(s)-1)) and (s[i] <= s[i+1]):#checks if either the next letter is the same or greater
        checkLongestRun += s[i+1]#concatenates substring
        if len(checkLongestRun) > len(longestRun):#checks current substring against existing substring
            longestRun = checkLongestRun #replaces existing with current if current is larger
        i += 1 #moves to the next index
            
#here's our goal... to print this string
print('Longest substring in alphabetical order is: ' + str(longestRun))
