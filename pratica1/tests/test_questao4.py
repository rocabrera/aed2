import pytest
from pratica1.estruturas import MyArray


@pytest.mark.parametrize(
    "lista,element,expected",
    [
     ([1,2,3,4], 2, 1), 
     ([1,2,3,4], 1, 0), 
     ([1,2,3,4], 4, 3), 
     ([1,2,3,4,5], 3, 2), 
     ([1,2,3,4,5], 1, 0), 
     ([1,2,3,4,5], 5, 4), 
    ],
)
def test_questao4(lista, element, expected):
    """
    Funciona somente para listas ordenadas
    """

    array = MyArray(lista)

    assert array.binary_search(element) == expected
