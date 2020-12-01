import pytest


@pytest.fixture(scope="function")
def day_1_input(tmp_path):
    p = tmp_path / "input.txt"
    content = [
        "1721",
        "979",
        "366",
        "299",
        "675",
        "1456",
    ]
    p.write_text("\n".join(content))

    return p
