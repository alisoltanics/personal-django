import graphene

from graphene_django.types import DjangoObjectType

from .models import Post


class PostType(DjangoObjectType):
    image = graphene.String(source='image_absolute_path')

    class Meta:
        model = Post


class Query(graphene.AbstractType):
    published_posts = graphene.List(PostType)

    def resolve_published_posts(self, args):
        """
        Query example:
            query {
                publishedPosts {
                    id
                    title
                    description
                    image
                    createDate
                }
            }
        """
        return Post.objects.filter(published=True)
