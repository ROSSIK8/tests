#1
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
geo_logs = [visit for visit in geo_logs if list(visit.values())[0][1] == 'Россия']


#2
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
list_id = []
for user in ids.values():
    list_id.extend(user)
set_id = set(list_id)
unique_list_id = list(set_id)
print(unique_list_id)


#4
stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
val_key_stats = {val: key for key, val in stats.items()}
max_ = val_key_stats[max(val_key_stats)]
print(max(stats.values()))
print(max_)