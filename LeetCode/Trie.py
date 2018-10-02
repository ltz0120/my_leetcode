import collections

class TrieNode:

    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_word = True

    def search(self, word):
        current = self.root
        print("current",current)
        for letter in word:
            print("letter", letter, current.children)
            current = current.children.get(letter)
            if current is None:
                return False
        return current.is_word

    def startsWith(self, prefix):
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if current is None:
                return False
        return True

if __name__ == "__main__":
    trie = Trie()
    trie.insert("hello")
    trie.insert("hi")
    print(trie.search("hello"))

    # for i in trie.root.children:
    #     print(i)