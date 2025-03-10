import hello;
import io;

def test_hello():
    #monkeypatch.setattr('sys.stdin', io.StringIO('3 2 1 nn bb aa'))
    printText.main() 
    captured = capsys.readouterr()

    expected_output = "Hello\nWorld!"
    actual_output = captured.out

    # Schleife über alle Zeilen in actual_output; dabie werden in jeder Zeile führende und nachfolgende Leerzeichen entfernt
    actual_output = '\n'.join(line.strip() for line in actual_output.splitlines())
    
    # Normalize line endings and remove trailing spaces at line endings
    assert actual_output.replace('\r\n', '\n').strip() == expected_output.replace('\r\n', '\n').strip()
 