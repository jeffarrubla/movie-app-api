from rest_framework import serializers
from .models import Moviedata

class MovieSerializer(serializers.Model):
	class Meta:
		model = Moviedata
		fields = ['id','name','duration','rating']