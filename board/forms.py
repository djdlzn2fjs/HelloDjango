class BoardForm (ModelForm):
    class meta:
        model = Board
        fields = ['title', 'userid', 'contents']

