import yaml

with open('new_data.yaml') as file:
    data = yaml.full_load(file)
    keywords = []
    
    for details in data.values():
        for _item in details:
            _words = _item.get('keywords', [])
            for _word in _words:
                keywords.append(_word)
    print(keywords)
                    
        
