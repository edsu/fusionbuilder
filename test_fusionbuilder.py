from fusion import parse

def test_text():
    root, text = parse('no fusion here, thank the gods')
    assert root == None
    assert text == 'no fusion here, thank the gods'

def test_self_closing():
    t = 'hi [fusion_text foo="bar"/] there'
    root, text = parse(t)
    print(root)
    assert text == 'hi there'
    assert root.name == "root"
    assert len(root.children) == 1
    assert root.children[0].name == 'fusion_text'
    assert root.children[0].attrs['foo'] == 'bar'

def test_text_element():
    t = 'hi [fusion_text foo="bar"]hello world![/fusion_text]'
    root, text = parse(t)
    assert text == 'hi hello world!'
    assert root.name == 'root'
    assert len(root.children) == 1
    assert root.children[0].name == 'fusion_text'
    assert root.children[0].attrs['foo'] == 'bar'
    assert root.children[0].text == "hello world!"

def test_empty_element():
    t = 'hi [fusion_text foo="bar"][/fusion_text]'
    root, text = parse(t)
    assert text == 'hi '
    assert root.name == 'root'
    assert len(root.children) == 1
    assert root.children[0].name == 'fusion_text'
    assert root.children[0].attrs['foo'] == 'bar'

def test_containment():
    t = 'hi [fusion_text a="1"][fusion_code b="2"]abc123[/fusion_code][/fusion_text]'
    root, text = parse(t)
    assert text == 'hi '
    assert root.name == 'root'
    assert len(root.children) == 1
    assert root.children[0].name == 'fusion_text'
    assert root.children[0].attrs['a'] == "1"
    assert len(root.children[0].children) == 1
    assert root.children[0].children[0].name == 'fusion_code'
    assert root.children[0].children[0].attrs['b'] == '2'
    assert root.children[0].children[0].text == 'abc123'


