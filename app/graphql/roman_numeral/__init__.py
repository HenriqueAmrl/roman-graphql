import graphene

from .mutations import Search


class RomanNumeralMutations(graphene.ObjectType):
    search = Search.Field()
