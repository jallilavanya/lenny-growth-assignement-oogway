from app.schemas.chat import AskRequest
import pytest
def test_validation():
 with pytest.raises(Exception): AskRequest(content='')
