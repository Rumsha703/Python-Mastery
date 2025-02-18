import re

def sentimentalTool(text:str):

    positive_pattrens=re.compile(r"(good|great|amazing|awosome)", flags=re.I)
    negative_patterns=re.compile(r"(bad|terrible|awful)", flags=re.I)


    positive_matches=re.findall(positive_pattrens,text)
    negative_matches=re.findall(negative_patterns,text)


    if len(positive_matches) > len(negative_matches):

        return "Positive sentiment"
    elif len(positive_matches) < len(negative_matches):
        return "Negative snetiment"
    else:
        return "Neutral"
    

print(sentimentalTool("This movie is really good!"))
print(sentimentalTool("I had a terrible experience."))
print(sentimentalTool("The weather is okay."))