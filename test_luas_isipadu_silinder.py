import A1_3_ms24_luas_isipadu_silinder
import pytest

def test_luas_dan_lilitan_bulatan(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]):
    # Define a function to simulate multiple user inputs
    user_inputs = ["4", "5"]

    def mock_input(_):
        return user_inputs.pop(0)

    # Use the function to simulate user input
    monkeypatch.setattr('builtins.input', mock_input)

    # Call the main function, which uses input() and prints the result
    A1_3_ms24_luas_isipadu_silinder.main()

    # Capture the printed output
    captured = capsys.readouterr()
    
    assert captured.out.strip() == "Luas tangki air = 226.22 dan isipadu tangki air = 251.36"