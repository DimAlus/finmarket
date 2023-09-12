"""Testing creating """
import os
from .lib import reverted, callr, revert


def recreate(name: str):
    os.system(f'echo "{name} revert\\n" >> ./tests/log')


@reverted(recreate)
def create_user(name: str) -> None:
    """aaa"""
    os.system(f'echo "{name} deploy\\n" >> ./tests/log')
    assert "h" in name


def test_one():
    revs = []
    try:
        callr(revs, create_user, "abh")
        callr(revs, create_user, "ahg")
        callr(revs, create_user, "abc")
        callr(revs, create_user, "ahg")
    except Exception as ex:
        raise ex
    finally:
        revert(revs)
