"""
Este arquivo contém os root types Query e Mutation.
Todos os futuros submódulos GraphQL implementados devem ser adicionados aqui como herança dos respectivos root types.
"""
import graphene

from .roman_numeral import RomanNumeralMutations


class Query(graphene.ObjectType):
    """Query root type: agrupa todas as queries do schema."""

    # Obs: Pelo menos uma Query é obrigatória para criar o schema.
    # O exemplo abaixo poderá ser apagado quando queries forem implementadas.
    hello = graphene.String()

    def resolve_hello(self, *args):
        """Query de exemplo."""
        return "hello"


class Mutation(RomanNumeralMutations):
    """Mutation root type: agrupa todas as mutations do schema."""


schema = graphene.Schema(query=Query, mutation=Mutation)
