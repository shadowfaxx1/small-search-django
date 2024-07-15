class trieNode:
    def __init__(self, text=" "):
        self.text = text
        self.children = dict()
        self.isword = False
class prefixTree:
    def __init__(self) -> None:
        self.root = trieNode()
    
    def insert(self, word):
        current = self.root 
        for i, char in enumerate(word.lower()):
            if char not in current.children:
                prefix = word[0:i+1]
                current.children[char] = trieNode(prefix)
            current = current.children[char]
        current.isword = True
        
    def ispresent(self, word):
        current = self.root
        for i, char in enumerate(word.lower()):
            if char not in current.children:
                return None
            current = current.children[char]
        if current.isword:
            return current.text
        return None
        
    def __child_words(self, node, words):
        if node.isword:
            words.append(node.text)
        for letter in node.children:
            self.__child_words(node.children[letter], words)
            
    def start_with(self, prefix):
        words = []
        current = self.root
        for char in prefix.lower():
            if char not in current.children:
                return list()
            current = current.children[char]
        self.__child_words(current, words)
        return words
