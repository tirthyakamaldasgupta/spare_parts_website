from rest_framework import serializers

#Car manufacturers serializer
class CarManufacturersSerializer(serializers.Serializer):
    cm_id = serializers.IntegerField()
    cm_name = serializers.CharField()

#Car series Serializer
class CarseriesSerializer(serializers.Serializer):
    cs_id = serializers.IntegerField()
    cs_name = serializers.CharField()

#Categories of parts serializer
class PartsCategoriesSerializer(serializers.Serializer):
    pc_id = serializers.IntegerField()
    pc_name = serializers.CharField()

#All items serializer irrespective of specific series(s) of a car manufacturer
class AllItemsSerializer(serializers.Serializer):
    i_id = serializers.IntegerField()
    i_name = serializers.CharField()