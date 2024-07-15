from django.db import models
import pickle

class TrieModel(models.Model):
    trie_data = models.BinaryField()

    def save_trie(self, trie):
        self.trie_data = pickle.dumps(trie)

    def load_trie(self):
        return pickle.loads(self.trie_data)
