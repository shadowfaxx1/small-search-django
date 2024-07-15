from django.shortcuts import render,redirect
from .forms import SearchForm
from .models import TrieModel

def search(request):
    form = SearchForm()
    results = []

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            trie_model = TrieModel.objects.first()
            trie = trie_model.load_trie()
            results = trie.start_with(query.lower())

    return render(request, 'searchapp/search.html', {'form': form, 'results': results})
