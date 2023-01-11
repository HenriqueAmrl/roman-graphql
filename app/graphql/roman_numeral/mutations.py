import graphene
from app.domain.roman_numeral import get_highest_value_from_string


class Search(graphene.Mutation):
    """Calcula o número romano com valor mais alto contido na string text"""

    class Arguments:
        text = graphene.NonNull(graphene.String)

    number = graphene.String()
    value = graphene.Int()

    @classmethod
    def mutate(cls, root, info, text):
        number = get_highest_value_from_string(text)
        response = cls(number=number.number, value=number.value)

        return response
