"""
Serializers for recipe APIs
"""
import os
from email.mime import image
from rest_framework import serializers
from django.core.mail import send_mail

from core.models import Recipe





# class TagSerializer(serializers.ModelSerializer):
#     """Serializer  tags."""

#     class Meta:
#         model = Tag
#         fields = ['id', 'name']
#         read_only_fields = ['id']

# class IngredientSerializer(serializers.ModelSerializer):
#     """Serializer  ingredients."""

#     class Meta:
#         model = Ingredient
#         fields = ['id', 'name']
#         read_only_fields = ['id']


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer  recipes."""
    # tags = TagSerializer(many=True, required=False)
    # ingredients = IngredientSerializer(many=True, required=False)


    class Meta:
        model = Recipe
        fields = ['firstName', 'email', 'Phone', 'Company', 'Comment']
        # read_only_fields = ['id']

    # def _get_or_create_tags(self, tags, recipe):
    #     """tomar y crear los tags necesarios."""
    #     auth_user = self.context['request'].user
    #     for tag in tags:
    #         tag_obj, created = Tag.objects.get_or_create( # tomar o crear
    #             user=auth_user,
    #             **tag,
    #         )
    #         recipe.tags.add(tag_obj)

    # def _get_or_create_ingredients(self, ingredients, recipe):
    #     """Tomar y crear los ingredientes necesarios."""
    #     auth_user = self.context['request'].user
    #     for ingredient in ingredients:
    #         ingredient_obj, created = Ingredient.objects.get_or_create(
    #             user=auth_user,
    #             **ingredient,
    #         )
    #         recipe.ingredients.add(ingredient_obj)

    def create(self, validated_data):

        # tags = validated_data.pop('tags', [])
        # ingredients = validated_data.pop('ingredients', [])
        recipe = Recipe.objects.create(**validated_data)
        # self._get_or_create_tags(tags, recipe)
        # self._get_or_create_ingredients(ingredients, recipe)
        subject = f"Tienes un nuevo mensaje de contacto de {recipe.firstName}  "

        message = f"Tienes un mensaje de  {recipe.firstName} su email es  {recipe.email}\n\n" \
                      f" su telefono es {recipe.Phone}\'s de la compañia {recipe.Company} comments: {recipe.Comment}"
        response = send_mail(subject, message,'nahuel.perugi@gmail.com',
                      ['nahuel.perugi@gmail.com'],fail_silently=False)

        print(response)
        

        return recipe

#     def update(self, instance, validated_data):

#         tags = validated_data.pop('tags', None)
#         ingredients = validated_data.pop('ingredients', None)

#         if tags is not None:
#             instance.tags.clear()
#             self._get_or_create_tags(tags, instance)

#         if ingredients is not None:
#             instance.ingredients.clear()
#             self._get_or_create_ingredients(ingredients, instance)

#         for attr, value in validated_data.items():
#             setattr(instance, attr, value)

#         instance.save()
#         return instance


# class RecipeDetailSerializer(RecipeSerializer):


#     class Meta(RecipeSerializer.Meta):
#         fields = RecipeSerializer.Meta.fields + ['description', 'image']

# class RecipeImageSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Recipe
#         fields = ['id', 'image']
#         read_only_fields = ['id']
#         extra_kwargs = {'image': {'required': 'True'}}


