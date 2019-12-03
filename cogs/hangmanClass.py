

class Hangman():
    def __init__(self,word: str):
        self.word=list(word)
        self.output=['_' for i in self.word]
        self.usedletters=[]
        self.tries=10

    def seek(self,letter: str):
        assert len(letter) == 1
        occurrences = [ i for (i,j) in enumerate(self.word) if j == letter]
        self.usedletters.append(letter)
        if len(occurrences)!=0:
            for i in occurrences:
                self.output[i]=self.word[i]
        else:
            self.tries=self.tries-1
        return

    def getOutput(self):
        return(' '.join(self.usedletters)+f'. {self.tries} attempts left.\n'+' '.join(self.output))