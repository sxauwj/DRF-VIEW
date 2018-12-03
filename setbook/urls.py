from rest_framework.routers import DefaultRouter, SimpleRouter
from . import views
from django.conf.urls import url

urlpatterns = [
    # url(r'^heros/$', views.Heros2View.as_view()),
    # url(r'^heros/(?P<pk>\d+)/$', views.Hero2View.as_view()),
    url(r'^heros/latest/$', views.HeromodelView.as_view({'get': 'latest'}))
]
# 定义路由对象
# 输入127.0.0.1:8000时会提示路由路径，建议使用该方法定义路由对象
router = DefaultRouter()
# 输入127.0.0.1:8000时会提示找不到页面
# router = SimpleRouter()
# 注册路由
router.register('heros', views.HeromodelView, base_name='heros')
urlpatterns += router.urls
