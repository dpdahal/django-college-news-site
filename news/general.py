from .models import Setting, Category


def send_global_data(request):
    content = {
        'settingData': Setting.objects.last(),
        'categoryData': Category.objects.all()

    }
    return content
