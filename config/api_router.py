import abnormal.views
import inspection.views
import notices.views
import reptile.views
import users.views
import vaccinate.views
from rest_framework_extensions.routers import ExtendedDefaultRouter

router = ExtendedDefaultRouter()

router.register("auth", users.views.AuthViewSet, basename="auth")
router.register("reptile", reptile.views.ReptileViewSet, basename="reptile")
router.register("inspection", inspection.views.InspectionViewSet, basename="inspection")
router.register("vaccinate", vaccinate.views.VaccinateViewSet, basename="vaccinate")
router.register("abnormal", abnormal.views.AbnormalViewSet, basename="abnormal")
router.register("notices", notices.views.NoticesViewSet, basename="notices")

app_name = "api"
urlpatterns = router.urls + []
