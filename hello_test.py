import hello;
import io;

def test_hello(capsys):
    hello.main() 
    captured = capsys.readouterr()

    expected_output = "Hello World!"
    expected_output = expected_output.replace('\r\n', '\n').strip()
    actual_output = captured.out
    actual_output = '\n'.join(line.strip() for line in actual_output.splitlines())
    actual_output = actual_output.replace('\r\n', '\n').strip()

    assert actual_output == expected_output
 
