import A1_1_ms18_bil_elektrik
import pytest

def test_luas_dan_lilitan_bulatan(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]):
    # Define a function to simulate multiple user inputs
    user_inputs = ["300"]

    def mock_input(_):
        return user_inputs.pop(0)

    # Use the function to simulate user input
    monkeypatch.setattr('builtins.input', mock_input)

    # Call the main function, which uses input() and prints the result
    A1_1_ms18_bil_elektrik.main()

    # Capture the printed output
    captured = capsys.readouterr()
    
    assert captured.out.strip() == "bil elektrik = RM92.80"