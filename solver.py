class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True

def findWords(board, words):
    root = TrieNode()
    for w in words:
        root.addWord(w)
    row, col = len(board), len(board[0])
    res, visit = set(), set()
        
    def dfs(r, c, node, word):
        if r < 0 or c < 0 or r == row or c == col or (r,c) in visit or board[r][c] not in node.children:
            return
        visit.add((r,c))
        node = node.children[board[r][c]]
        word += board[r][c]
        if node.isEnd:
            res.add(word)
            
        dfs(r + 1, c, node, word)
        dfs(r - 1, c, node, word)
        dfs(r, c + 1, node, word)
        dfs(r, c - 1, node, word)
        dfs(r + 1, c + 1, node, word)
        dfs(r + 1, c - 1, node, word)
        dfs(r - 1, c + 1, node, word)
        dfs(r - 1, c - 1, node, word)
        visit.remove((r,c))
    for i in range(row):
        for j in range(col):
            dfs(i,j,root,'')
    return res
board = []
for i in range(1,5):
    row = []
    rowlet = input(f'please enter letters in row {i} in the form abcd where abcd are the letters in the row\n')
    while len(row) > 4:
        rowlet = input(f'please enter letters in row {i} in the form abcd\n')
    rowlet = rowlet.lower()
    for c in rowlet:
        row.append(c)
    print(row)
    board.append(row)
textFile = open('50kdict.txt')
words = textFile.readlines()
for i in range(len(words)):
    words[i] = words[i][:len(words[i])-1]
ans = findWords(board,words)
words = textFile.readlines()
print(ans, len(ans))

