from django.http import JsonResponse
from rest_framework.decorators import api_view 
from django.views.decorators.csrf import ensure_csrf_cookie
from .serializers import UsuarioSerializer
from .models import Usuario



@api_view(["GET"])
@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({"message": "CSRF cookie enviado correctaeamente"}, status=200)

@api_view(['POST'])
@ensure_csrf_cookie  #envio el token por kokies , tienen que devolver el token para que le permita la solicitud
def registro(request):
    if request.method == 'POST':
        try:
            data = request.data
            serializer = UsuarioSerializer(data=data)

            # Validar el formato de los datos
            if not serializer.is_valid():
                return JsonResponse({
                    'error': 'Datos inválidos',
                    'details': serializer.errors
                }, status=400)

            # Validar que las contraseñas coincidan
            if data['password1'] != data['password2']:
                return JsonResponse({
                    'error': 'Las contraseñas no coinciden'
                }, status=400)

            # Crear el usuario manualmente
            user = Usuario.objects.create_user(
                nombre=data['nombre'],
                celular=data['celular'],
                correo_electronico=data['correo_electronico'],
                password=data['password1'],
                estado='Activo'  # Se establece automáticamente
            )

            return JsonResponse({
                'mensaje': 'Usuario registrado correctamente',
                'usuario_id': user.id
            }, status=201)

        except Exception as e:
            return JsonResponse({
                'error': str(e)
            }, status=400)

    return JsonResponse({
        'error': 'Método no permitido'
    }, status=405)