from rest_framework.permissions import BasePermission


class IsActiveStaff(BasePermission):
    """
    Разрешает доступ только активным сотрудникам.
    """

    def has_permission(self, request, view):
        # Проверяем, что пользователь аутентифицирован,
        # является сотрудником и активен.
        return (
            request.user
            and request.user.is_authenticated
            and request.user.is_staff
            and request.user.is_active
        )
