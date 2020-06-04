from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for taking input string of maximum length 10 in APIView"""

    name = serializers.CharField(max_length=100)
