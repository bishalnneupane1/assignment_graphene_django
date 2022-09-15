import graphene
from graphene_django.types import DjangoObjectType
from graphene_django import  DjangoListField
from .models import Users

class UsersType(DjangoObjectType):
    class Meta:
        model = Users
        fields = ("id", "name" "email", "password", "is_Active", "created_On", "updated_On")


class Query(graphene.ObjectType):

     all_users = graphene.Field(UsersType, id=graphene.Int())

     def resolve_all_users(root, info, id, name):
         return Users.objects.get(pk=id)


# Mutation query to add users

class UserMutation(graphene.Mutation):

    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    @classmethod
    def mutate(root, info, name, id):
       name = Users.objects.get(pk=id)
       password = Users(password=password)
       email = Users(email=email)
       return UserMutation(name=name)

       Users.save()


class Mutation(graphene.ObjectType):

    update_users = UserMutation.Field()




schema = graphene.Schema(query=Query, mutation=Mutation)

