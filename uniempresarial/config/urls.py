from rest_framework.routers import DefaultRouter

from config.api_views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'users', UserViewSet, 'user')
router.register(r'facultys', FacultyViewSet, 'faculty')
router.register(r'programs', ProgramViewSet, 'program')
router.register(r'schedule-models', ScheduleModelViewSet, 'schedule-model')
router.register(r'promotion-models', PromotionModelViewSet, 'promotion-model')
router.register(r'account-models', AccountModelViewSet, 'account-model')
router.register(r'module-configs', ModuleConfigViewSet, 'module-config')
router.register(r'rol-configs', RolConfigViewSet, 'rol-config')
router.register(r'rol-users', RolUserViewSet, 'rol-user')
