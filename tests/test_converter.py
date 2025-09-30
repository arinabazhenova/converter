from app.converter import convert

def test_convert():
    result = convert("bitcoin", "ethereum", 0.01)
    assert isinstance(result, float)
    assert result > 0
