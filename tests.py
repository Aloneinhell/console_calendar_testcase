def test_create_event():
    with open('test_cal.txt', 'w') as f:
        test_id = '1'
        test_date = '2000-01-01'
        test_time = '11:00'
        test_cat = 'private'
        test_name = 'test1'
        test_description = 'some test description'
        f.write(f"id: {test_id}\nДата: {test_date}\nВремя: {test_time}\n"
                f"Категория: {test_cat}\nЗаголовок: {test_name}\nОписание: {test_description}\n")
    test_data = [test_id, test_date, test_time, test_cat, test_name, test_description]
    with open('test_cal.txt', 'r') as f:
        is_in_dots = []
        content = f.read()
        for data in test_data:
            is_in_file = content.find(data)
            is_in_dots.append(is_in_file)
        for data in is_in_dots:
            assert data > -1


def test_read_events_by_cat():
    with open('test_cal.txt', 'w') as f:
        #создаем несколько записей, чтоб нужная была между ними
        test_id = '1'
        test_date = '2000-01-01'
        test_time = '11:00'
        test_cat = 'somesthing'
        test_name = 'test1'
        test_description = 'some test description'
        f.write(f"id: {test_id}\nДата: {test_date}\nВремя: {test_time}\n"
                f"Категория: {test_cat}\nЗаголовок: {test_name}\nОписание: {test_description}\n\n")

        test_id_2 = '2'
        test_date_2 = '2022-02-02'
        test_time_2 = '12:00'
        test_cat_2 = 'private'
        test_name_2 = 'test2(needed)'
        test_description_2 = 'some test description 2!!!! That is the correct post'
        f.write(f"id: {test_id_2}\nДата: {test_date_2}\nВремя: {test_time_2}\n"
                f"Категория: {test_cat_2}\nЗаголовок: {test_name_2}\nОписание: {test_description_2}\n\n")

        test_id_3 = '3'
        test_date_3 = '2033-03-03'
        test_time_3 = '13:00'
        test_cat_3 = 'somesthing3'
        test_name_3 = 'test3333'
        test_description_3 = 'some test description33333'
        f.write(f"id: {test_id_3}\nДата: {test_date_3}\nВремя: {test_time_3}\n"
                f"Категория: {test_cat_3}\nЗаголовок: {test_name_3}\nОписание: {test_description_3}\n\n")

    with open('test_cal.txt', 'r') as f:
        content = f.read()
        test_cat = 'private'
        new_content = '\n'
        iii = 0
        ids = content.count('id:')
        while iii < ids:
            razor = content.find(f"Категория: {test_cat}") - 35
            if razor <= -1 and new_content == '\n':
                #это значение - не провал теста, а отлов неправильного ввода категории. Этот иф не случится.
                new_content += "Нет такой категории!"
            else:
                content = content[razor:]
                razor_end = content.find('id:')
                if new_content == '\n':
                    new_content += 'i' + content[:razor_end]
                    content = content[razor_end:]
                    iii += 1
                elif razor > -1 and razor_end != -1 and content[razor:] not in new_content:
                    new_content += 'i' + content[:razor_end]
                    content = content[razor_end:]
                    iii += 1
                elif razor > -1 and razor_end == -1 and content[razor:] not in new_content:
                    new_content += 'i' + content
                    iii += 1

                else:
                    iii += 1

    #ЕЩЕ РАЗ ОТКРЫВАЕМ ФАЙЛ, чтобы мы могли его прочитать и получить не обрезанный текст
    with open('test_cal.txt', 'r') as f:
        original_content = f.read()
        print(f"\nlol!\n{new_content}")

        print('\n\n', original_content)
    assert original_content.find(new_content) > -1


def test_update_event():
    with open('test_cal.txt', 'w') as f:
        #создаем несколько записей, чтоб нужная была между ними
        test_id = '1'
        test_date = '2000-01-01'
        test_time = '11:00'
        test_cat = 'somesthing'
        test_name = 'test1'
        test_description = 'some test description'
        f.write(f"id: {test_id}\nДата: {test_date}\nВремя: {test_time}\n"
                f"Категория: {test_cat}\nЗаголовок: {test_name}\nОписание: {test_description}\n\n")
    event_id = '1'
    with open('test_cal.txt', 'r') as old_f:
        old_data = old_f.read()
        razor = old_data.find(f"id: {event_id}")
        if razor <= -1:
            print('Нет такого id')
        razor_end = old_data[razor + 1:].find('id:') + razor
        data_to_change = old_data[razor + 6: razor_end]
        # print(f"Событие с id {event_id} содержит следующую информацию:\n{data_to_change}\n"
        #       f"\nОно подлежит изменению.\n")
        event_date = '1999-09-09'
        event_time = '19:00'
        event_cat = 'work'
        event_name = 'test_update'
        event_description = 'test description updated'

        changes = f"Дата: {event_date}\nВремя: {event_time}\nКатегория: {event_cat}\n" \
                  f"Заголовок: {event_name}\nОписание: {event_description}\n"
    new_data = old_data.replace(data_to_change, changes)
    with open('test_cal.txt', 'w') as new_f:
        new_f.write(new_data)
    with open('test_cal.txt', 'r') as f:
        updated_content = f.read()
        razor = updated_content.find(f"id: {event_id}")
        razor_end = updated_content[razor + 1:].find('id:') + razor
        updated_post = updated_content[razor + 6: razor_end]
        print(updated_post)
        assert updated_content.find(updated_post) > -1


def test_delete_event():
    test_id = '1'
    with open('test_cal.txt', 'r') as old_f:
        old_data = old_f.read()
        razor = old_data.find(f"id: {test_id}")
        if razor <= -1:
            print('Нет такого id')
        razor_end = old_data[razor + 1:].find('id:') + razor
        if razor_end <= - 1 + razor:
            data_to_change = old_data[razor:]
        else:
            data_to_change = old_data[razor: razor_end]
        changes =""
    new_data = old_data.replace(data_to_change, changes)
    with open('test_cal.txt', 'w') as new_f:
        new_f.write(new_data)
    with open('test_cal.txt', 'r') as updated_f:
        content = updated_f.read()
        assert content.find(test_id) == -1



