from django.core.exceptions import ValidationError

# Create your models here.

def valiadte_content(value):
	content = value
	if content == "":
		raise ValidationError("Content cannot be blank")
	return value