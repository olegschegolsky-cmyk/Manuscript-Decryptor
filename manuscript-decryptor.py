from typing import List, Set, Dict, Optional

class TrieNode:
    def __init__(self):
        self.children: Dict[str, 'TrieNode'] = {}
        self.is_word: bool = False
        self.word: str = ""

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
        node.word = word

class ManuscriptDecryptor:
    def find_words(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        rows, cols = len(board), len(board[0])
        found_words: List[str] = []

        def dfs(r: int, c: int, parent_node: TrieNode) -> None:
            char = board[r][c]
            curr_node = parent_node.children.get(char)

            if not curr_node:
                return

            if curr_node.is_word:
                found_words.append(curr_node.word)
                curr_node.is_word = False

            board[r][c] = '#'

            directions = [
                (-1, 0), (1, 0), (0, -1), (0, 1),
                (-1, -1), (-1, 1), (1, -1), (1, 1)
            ]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(nr, nc, curr_node)

            board[r][c] = char

            if not curr_node.children and not curr_node.is_word:
                del parent_node.children[char]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie.root)

        return found_words

def run_tests():
    decryptor = ManuscriptDecryptor()

    print("Running tests...")

    board1 = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    words1 = ["oath", "pea", "eat", "rain", "hath", "after", "tea", "tank", "ear"]
    expected1 = {"oath", "eat", "tea", "ear"}
    result1 = set(decryptor.find_words(board1, words1))
    assert result1 == expected1, f"Test 1 failed: Expected {expected1}, got {result1}"
    print("Test 1 passed!")

    board2 = [
        ['a', 'b'],
        ['c', 'd']
    ]
    words2 = ["ab", "cb", "ad", "bd", "ac", "ca", "d", "a", "abdc", "xyz"]
    expected2 = {"ab", "cb", "ad", "bd", "ac", "ca", "d", "a", "abdc"}
    result2 = set(decryptor.find_words(board2, words2))
    assert result2 == expected2, f"Test 2 failed: Expected {expected2}, got {result2}"
    print("Test 2 passed!")
    
    board3 = [
        ['a', 'a']
    ]
    words3 = ["aaa"]
    expected3 = set()
    result3 = set(decryptor.find_words(board3, words3))
    assert result3 == expected3, f"Test 3 failed (visited cells check): Expected empty set, got {result3}"
    print("Test 3 passed!")

    print("All tests passed successfully!")

if __name__ == "__main__":
    run_tests()