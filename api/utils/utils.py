


def advert_picture_directory_path(instance, filename):
    return 'advert_picture_{0}/{1}'.format(instance.id, filename)


def profile_photo_directory_path(instance, filename):
    """Формируем путь медиа файла"""
    return 'profile_photo_{0}/{1}'.format(instance.user.username, filename)