import os
import pandas as pd
import ast
from django.core.management.base import BaseCommand
from searchapp.models import TrieModel
from searchapp.trie import prefixTree  

class Command(BaseCommand):
    help = 'Load data from CSV and build Trie'

    def handle(self, *args, **kwargs):
        p = r"C:\Users\mail2\Documents\lpth\.vscode\DataSciencePrac\projects\BackendProjects\project4\app\searchapp\static\searchapp\restaurants_small.csv"
        path = os.path.join(os.path.dirname(__file__),p )
        df = pd.read_csv(path)
         # cleaning of the csv data from the local dir
        df['items'] = df['items'].apply(ast.literal_eval)
        df['item_keys'] = df['items'].apply(lambda x: [key.lower() for key in x.keys()])
        all_keys = [key for sublist in df['item_keys'] for key in sublist]
        items_set = set(all_keys)
        
        tree = prefixTree()
        for item in items_set:
            tree.insert(item)
        
        trie_model = TrieModel()
        trie_model.save_trie(tree)
        trie_model.save()

        self.stdout.write(self.style.SUCCESS('Successfully built and saved the Trie from CSV data'))
