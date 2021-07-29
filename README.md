# EntityValidator
A Django App which has 2 REST APIs.
POST API for validation of an entity.
POST API for validation of a numeric constraints.
Docker to run Django app.


# Requirements
The following are the requirements for the project, which will be installed in the docker automatically while creating docker file -

* django : 3.2.5(open-source web framework that follows the model–template–views architectural pattern)
* marshmallow : 3.12.2(Validator of incoming data)
* django-rest-marshmallow : 4.0.2(provides an alternative serializer implementation to the built-in serializers)
* djangorestframework : 3.12.4(a powerful and flexible toolkit for building Web APIs)
* django-rest-swagger : 2.2.0(OpenAPI Documentation Generator for Django REST Framework)



# Docker
Size of the image =  96 MB
## Steps to deploy
Port exposed = 8000

To build the image: 
```docker build -t <image_name> <path_to_dockerfile>```

To run the image: 
```docker run -p 8000:8000 <image_name>```

`image_name` : **vernacular**


