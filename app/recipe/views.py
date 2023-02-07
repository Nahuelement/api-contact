"""
Views for the recipe APIs
"""
from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiParameter,
    OpenApiTypes,
)
from rest_framework import viewsets, mixins, status
from rest_framework import generics, authentication, permissions

# Create your views here.
from core.models import Recipe
from recipe import serializers

@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                'tags',
                OpenApiTypes.STR,
                description='separacion por , para diferenciar los tags ',
            ),
            OpenApiParameter(
                'ingredients',
                OpenApiTypes.STR,
                description='separacion por , para diferenciar los filter',
            ),
        ]
    )
)
class RecipeViewSet(viewsets.ModelViewSet):


    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]






















### No hay mas que lo de arriba


    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    # def _params_to_ints(self, qs):

    #     return [int(str_id) for str_id in qs.split(',')]

    # def get_queryset(self):

    #     tags = self.request.query_params.get('tags')
    #     ingredients = self.request.query_params.get('ingredients')
    #     queryset = self.queryset
    #     if tags:
    #         tag_ids = self._params_to_ints(tags)
    #         queryset = queryset.filter(tags__id__in=tag_ids)
    #     if ingredients:
    #         ingredient_ids = self._params_to_ints(ingredients)
    #         queryset = queryset.filter(ingredients__id__in=ingredient_ids)

    #     return queryset.filter(
    #         user=self.request.user
    #     ).order_by('-id').distinct()

    # def get_serializer_class(self):

    #     if self.action == 'list':
    #         return serializers.RecipeSerializer
    #     elif self.action == 'upload_image':
    #         return serializers.RecipeImageSerializer

    #     return self.serializer_class

    # def perform_create(self, serializer):

    #     serializer.save(user=self.request.user)

    # @action(methods=['POST'], detail=True, url_path='upload-image')
    # def upload_image(self, request, pk=None):

    #     recipe = self.get_object()
    #     serializer = self.get_serializer(recipe, data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @extend_schema_view(
#     list=extend_schema(
#         parameters=[
#             OpenApiParameter(
#                 'assigned_only',
#                 OpenApiTypes.INT, enum=[0, 1],
#                 description='filtro por item asignado a recipe.',
#             ),
#         ]
#     )
# )
# class BaseRecipeAttrViewSet(mixins.DestroyModelMixin,
#                             mixins.UpdateModelMixin,
#                             mixins.ListModelMixin,
#                             viewsets.GenericViewSet):

#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):

#         assigned_only = bool(
#             int(self.request.query_params.get('assigned_only', 0))
#         )
#         queryset = self.queryset
#         if assigned_only:
#             queryset = queryset.filter(recipe__isnull=False)

#         return queryset.filter(
#             user=self.request.user
#         ).order_by('-name').distinct()

# class TagViewSet(BaseRecipeAttrViewSet):

#     serializer_class = serializers.TagSerializer
#     queryset = Tag.objects.all()



# class IngredientViewSet(BaseRecipeAttrViewSet):

#     serializer_class = serializers.IngredientSerializer
#     queryset = Ingredient.objects.all()


