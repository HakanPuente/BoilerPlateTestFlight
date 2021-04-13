from django.contrib.auth import get_user_model
import pytest
from djangoApp.models import MyModel

@pytest.mark.django_db
def test_create_mymodel():
    mymodel = MyModel.objects.create(name='Test Data', country='FR', productID=123.00, year=2010)
    assert mymodel.id