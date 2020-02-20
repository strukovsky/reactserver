from django.http import HttpResponse
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization, Authorization
from tastypie.resources import ModelResource
from tastypie.utils.mime import build_content_type

from shop.models import Product, Order


class ProductResource(ModelResource):
    class Meta:
        queryset = Product.objects.all()
        allowed_methods = ['get']

    """
    def create_response(self, request, data, response_class=HttpResponse, **response_kwargs):
        desired_format = self.determine_format(request)
        serialized = self.serialize(request, data, desired_format)
        response = response_class(content=serialized, content_type=build_content_type(desired_format),
                                  **response_kwargs)
        response['Access-Control-Allow-Origin'] = 'http://localhost:3000'
        response['Access-Control-Allow-Credentials'] = 'true'
        response['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Origin, Content-Type, Accept'
        return response
    """

class OrderResource(ModelResource):
    class Meta:
        queryset = Order.objects.all()
        allowed_methods = ['post']
        authorization = Authorization()
    """
      def create_response(self, request, data, response_class=HttpResponse, **response_kwargs):
        desired_format = self.determine_format(request)
        serialized = self.serialize(request, data, desired_format)
        response = response_class(content=serialized, content_type=build_content_type(desired_format),
                                  **response_kwargs)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Credentials'] = 'true'
        response['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With'
        return response
    """
