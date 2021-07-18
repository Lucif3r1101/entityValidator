# EntityValidator
A Django App which has 2 REST APIs.
POST API for validation of an entity.
POST API for validation of a numeric constraints.
Docker to run Django app.


# Requirements
The following are the requirements for the project, which will be installed in the docker automatically while creating docker file -

* django(open-source web framework that follows the model–template–views architectural pattern)
* marshmallow(Validator of incoming data)
* djangorestframework(a powerful and flexible toolkit for building Web APIs)
* danjo-rest-swagger(OpenAPI Documentation Generator for Django REST Framework)



# Docker
Size of the image =  931 MB
## Steps to deploy
Port exposed = 8000

To build the image: `docker build -t <image_name> <path_to_dockerfile>`
To run the image: `docker run -p 8000:8000 <image_name>`
`image_name` : `vernacular`


