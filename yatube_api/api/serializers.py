from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.relations import StringRelatedField
from posts.models import Comment, Post, Follow, Group, User


class GroupSerializer(serializers.ModelSerializer):
    """Сериалайзер групп."""

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description',)


class PostSerializer(serializers.ModelSerializer):
    """Сериалайзер постов."""
    author = StringRelatedField(read_only=True)

    class Meta:
        fields = ('id', 'text', 'pub_date', 'author', 'image', 'group')
        model = Post
        read_only_fields = ('author',)


class CommentSerializer(serializers.ModelSerializer):
    """Сериалайзер комментариев к постам."""
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created',)
        model = Comment
        read_only_fields = ('post',)


class FollowSerializer(serializers.ModelSerializer):
    """Сериалайзер подписок."""
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        fields = ('user', 'following')
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following')
            )
        ]

    def validate(self, data):
        if data['following'] == self.context.get('request').user:
            raise serializers.ValidationError(
                'Нельзя подписаться на себя!')
        return data
