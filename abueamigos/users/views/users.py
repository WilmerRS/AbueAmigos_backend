# Django Restframework
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

# Models
from abueamigos.users.models.profiles import Profile

# Serializers
from abueamigos.users.serializers.profile import ProfileSerializer
from abueamigos.users.serializers.users import UserLoginSerializer


class Users(mixins.CreateModelMixin,
            mixins.RetrieveModelMixin,
            mixins.UpdateModelMixin,
            mixins.ListModelMixin,
            viewsets.GenericViewSet):
    lookup_field = 'user__username'
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    @action(detail=False, methods=['post'])
    def login(self, request):
        """User sign in."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': ProfileSerializer(Profile.objects.get(user=user)).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)

    # @action(detail=True, methods=['get'])
    # def reservations(self, request, *args, **kwargs):
    #     reservations = Reservation.objects.filter(vehicle__owner__user=self.get_object())
    #     serializer = ReservationSerializer(reservations, many=True)
    #     return Response(serializer.data)


