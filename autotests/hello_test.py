import hello;

def test_hello():
    #monkeypatch.setattr('sys.stdin', io.StringIO('3 2 1 nn bb aa'))
    printText.main() 
    captured = capsys.readouterr()

    expected_output = "Hello World!"
    actual_output = captured.out
    
    # Normalize line endings and remove trailing spaces at line endings
    assert actual_output.replace('\r\n', '\n').strip() == expected_output.replace('\r\n', '\n').strip()
    