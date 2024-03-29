from  rest_framework  import serializers
from watchlist_app.models import Movie

class MovieSerializers(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    descriptive=serializers.CharField()
    active=serializers.BooleanField()

    '''
    class Meta:
        model=Movie
        fields="__all__"
    '''
    def create(self,validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.descriptive = validated_data.get('descriptive', instance.descriptive)
        instance. active = validated_data.get('active', instance.active)

        instance.save()
        return instance
        