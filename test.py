import vk
from my_data import MyData
import time

session = vk.Session(access_token='ad723d00ad723d00ad723d00f8ad1d829baad72ad723d00f33bb9646349238f3528633d')
vk_api = vk.API(session)

friends = vk_api.friends.get(user_id=MyData.my_id, fields='nickname, domain, sex, bdate, '
                                                          'city, country, last_seen',  v=5.103)
print(friends)
print(vk_api.database.getCities(country_id=1, v=5.0))

# информация о друзьях пользователя

print("\n Друзья пользователя")
for friend in friends["items"]:
    print("Name: ", friend["first_name"], " ", friend["last_name"])
    if (friend["sex"] == 1):
        current_sex = "female"
    else:
        current_sex = "male"
    print("\tsex: ", current_sex)
    try:
        print("\tbdate: ", friend["bdate"])
    except:
        print("\tbdate: No info")
    print("\tdomain: ",friend["domain"])
    try:
        if (friend["city"] != 0):
            print("\tcountry code: ", friend["country"])
            print("\tcity code: ", friend["city"])
    except:
        print("\tNo info about country and city")
    if friend['last_seen']:
        print("\tLast online time: ", time.ctime(friend['last_seen']['time']))

        
# информация о записях на стене пользователя(500 запросов в сутки(ограничение))
print("\n Записи пользователя")
wall_info = vk_api.wall.get(owner_id = MyData.my_id, v=5.1)
counter = 1
for i in wall_info['items']:
    print(counter, ". ", i)
    # информация о лайкнувших пользователях
    like_list = vk_api.likes.getList(type='post', owner_id=MyData.my_id, item_id=i["id"], filter='likes', extended=1,
                                     v=5.103)
    print("Список лайкнувших запись:")
    for i in like_list['items']:
        print("\t", i)
    counter += 1
    print("\n")

# топ 5 подписок пользователя
print("\n Топ 5 подписок пользователя")
groups_info = vk_api.users.getSubscriptions(user_id=MyData.my_id, extended=1, count=5, v=5.103)
for i in groups_info['items']:
    print(i)
# Выводит id, имя, домин, приватность, тип, а так же ссылки на аватар в разных размерностях


# информация о подписчиках пользователя
print("\nСписок подписчиков")
followers_info = vk_api.users.getFollowers(user_id=MyData.my_id, fields='first_name', v=5.1)
for follower in followers_info['items']:
    print(follower)


# С помощью метода get можно получить множество различной информации(но зависит так же от типа запроса, users.get,
# friends.get и т.п) о пользователе добавив в список fields нужные поля, которые нужно извлечь.
# Список всех возможных полей:
# Basic: 1. id 2. first_name 3. last_name 4.deactivated(возвращается, если страница в бане или удалена) 5. is_closed
# (скрытый профиль)
# Optional fields: 1. about(О себе) 2. activities(содержимое деятельность) 3. bdate(если скрыта, то нет)
# 4. books(любимые книги) 5. city(id и title) 6. common_count(количество общих друзей с текущем пользователем)
# 7. counters(количество различных объектов у пользователя: albums, videos, audios, photos, notes, friends, groups,
# online_friends, mutual_friends(общие друзья), user_videos(количество видео с пользователем), followers, pages
# (количество объектов в Интересных страницах) 8. country(id, title) 9. domain 10. education(university,
# university_name, faculty, faculty_name, graduation) 11. followers_count 12. games(содержимое любимые игры) 13. movies
# 14. music(Содержимое Любимая музыка) 15. online(информация о том, находится ли сейчас онлайн) 16. personal(информация
# из раздела Жизненная позиция) 17. relation(семейное положение) 18. sex 19. status 20. last_seen(время последнего
# посещения)



# Список новостей по запросу в параметре q, это может быть ответ на сообщение под записью
# текст записи и тд.
print('\nВывод новостей по поиску "Python programming"')
news_list = vk_api.newsfeed.search(q='Python programming', count=3, v=5.103)
for i in news_list['items']:
    print(i)
print("\t Total count: ", news_list['total_count'])


print('\nСписок фото пользователя')
wall_photos_list = vk_api.photos.get(owner_id=MyData.my_id, album_id='wall', extended=1, v=5.103)
print('Со стены:')
for i in wall_photos_list['items']:
    print(i)
profile_photos_list = vk_api.photos.get(owner_id=MyData.my_id, album_id='profile', extended=1, v=5.103)
print('Со страницы:')
for i in profile_photos_list['items']:
    print(i)
