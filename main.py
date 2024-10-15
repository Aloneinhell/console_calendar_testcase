class CalendarTaskManager:
    event_id = 0
    def init_calendar(self):
        answer = input('\nНапишите что вы хотите сделать.\n/new_event - Чтобы создать новую запись\n'
                       '/events - Чтобы посмотреть список всех событий\n'
                       '/get_event - Чтобы увидеть конкретное событие\n'
                       '/get_by_date - Посмотреть события на конкретную дату\n'
                       '/get_by_cat - Посмотреть события из определенной категории\n'
                       '/update - Чтобы изменить событие\n'
                       '/delete - чтобы удалить событие\n/stop - Завершить работу\n')
        if answer.strip() == '/new_event':
            self.write_ivent()
        elif answer.strip() == '/events':
            self.read_events()
        elif answer.strip() == '/get_event':
            self.read_certain_event()
        elif answer.strip() == '/get_by_date':
            self.read_events_by_date()
        elif answer.strip() == '/get_by_cat':
            self.read_events_by_cat()
        elif answer.strip() == '/update':
            self.update_event()
        elif answer.strip() == '/delete':
            self.delete_event()
        elif answer.strip() == '/stop':
            self.stop()


    def write_ivent(self):
        self.event_id += 1
        f = open('calendar.txt', 'a')

        event_date = input('Введите дату мероприятия в формате YYYY-MM-DD: ')

        f.write(f"\nid: {self.event_id}\n")
        f.write(f"Дата: {event_date}\n")
        event_time = input('Введите время мероприятия, например 14:30 : ')
        f.write(f"Время: {event_time}\n")

        event_cat = input('Введите категорию мероприятия, например "личное": ')
        f.write(f"Категория: {event_cat}\n")

        event_name = input('Введите заголовок мероприятия: ')
        f.write(f"Заголовок: {event_name}\n")

        event_description = input('Введите описание мероприятия(детали): ')
        f.write(f"Описание: {event_description}\n")
        f.flush()
        f.close()


        self.event_date = event_date
        self.event_time = event_time
        self.event_cat = event_cat
        self.event_name = event_name
        self.event_description = event_description

        self.init_calendar()

    def read_events(self):
        f = open('calendar.txt', 'r')
        print(f"\n{f.read()}\n")
        f.flush()
        f.close()
        self.init_calendar()

    def read_certain_event(self):
        f = open('calendar.txt', 'r')
        event_id = input('Введите ID мероприятия : ')
        content = f.read()
        next_id = int(event_id) + 1
        start_of_post = content.find(f"id: {event_id}")
        if start_of_post == -1:
            print('\nНет события с таким id!')
            self.init_calendar()
        end_of_post = content.find(f"id: {str(next_id)}")
        print(f"\n{content[start_of_post: end_of_post].strip()}")
        f.close()
        self.init_calendar()

    def read_events_by_date(self):
        f = open('calendar.txt', 'r')
        content = f.read()
        event_date = input('Введите дату, чтобы посмотреть запланированные события(YYYY-MM-DD): ')
        new_content = '\n'
        iii = 0
        ids = content.count('id:')
        while iii < ids:
            razor = content.find(f"Дата: {event_date}") - 5

            content = content[razor:]
            razor_end = content.find('id:')
            if new_content == '\n' and razor > -6:
                new_content += 'i' + content[:razor_end]
                content = content[razor_end:]
                iii += 1
            elif razor > -6 and razor_end != -1 and content[razor:] not in new_content:
                new_content += 'i' + content[:razor_end]
                content = content[razor_end:]
                iii += 1
            elif razor > -6 and razor_end == -1 and content[razor:] not in new_content:
                new_content += 'i' + content
                iii += 1

            else:
                iii += 1

        if new_content == '\n':
            print('\nСобытий на эту дату нет в календаре!')
        else:
            print(f"\n{new_content}")
        f.close()
        self.init_calendar()

    def read_events_by_cat(self):
        f = open('calendar.txt', 'r')
        content = f.read()
        event_cat = input('Введите категорию, чтобы посмотреть события из этой категории: ')
        new_content = '\n'
        iii = 0
        ids = content.count('id:')
        while iii < ids:
            razor = content.find(f"Категория: {event_cat}") - 35
            if razor <= -1 and new_content == '\n':
                print("\nНет такой категории!")
                self.init_calendar()
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

        if new_content == '\n':
            print('\nСобытий этой категории нет в календаре!')
        else:
            print(new_content)
        f.close()
        self.init_calendar()

    def update_event(self):
        event_id = input('Введите id события, чтобы изменить его: ')
        with open('calendar.txt', 'r') as old_f:
            old_data = old_f.read()
            razor = old_data.find(f"id: {event_id}")
            if razor == -1:
                print('Нет такого id')
                self.init_calendar()
            razor_end = old_data[razor + 1:].find('id:') + razor
            data_to_change = old_data[razor + 6: razor_end]
            print(f"Событие с id {event_id} содержит следующую информацию:\n{data_to_change}\n"
                  f"\nОно подлежит изменению.\n")
            event_date = input('Введите новую дату в формате YYYY-MM-DD: ')
            event_time = input('Введите новое время, напимер 14:30 : ')
            event_cat = input('Введите новую категорию события: ')
            event_name = input('Введите новый заголовок события: ')
            event_description = input('Введите новое описания события: ')

            changes =f"Дата: {event_date}\nВремя: {event_time}\nКатегория: {event_cat}\n" \
                        f"Заголовок: {event_name}\nОписание: {event_description}\n"
        new_data = old_data.replace(data_to_change, changes)
        with open('calendar.txt', 'w') as new_f:
            new_f.write(new_data)
        with open('calendar.txt', 'r') as f:
            updated_content = f.read()
            razor = updated_content.find(f"id: {event_id}")
            razor_end = updated_content[razor + 1:].find('id:') + razor
            updated_post = updated_content[razor + 6: razor_end]
            print(f"Событие с id {event_id} изменено:\n{updated_post}\n")
            self.init_calendar()

    def delete_event(self):
        event_id = input('Введите id события, чтобы удалить его: ')
        with open('calendar.txt', 'r') as old_f:
            old_data = old_f.read()
            razor = old_data.find(f"id: {event_id}")
            if razor == -1:
                print('Нет такого id')
                self.init_calendar()
            razor_end = old_data[razor + 1:].find('id:') + razor
            if razor_end == - 1 + razor:
                data_to_change = old_data[razor:]
            else:
                data_to_change = old_data[razor: razor_end]
            print(f"Событие с id {event_id} содержит следующую информацию:\n{data_to_change}\n"
                  f"\nОно подлежит УДАЛЕНИЮ.\n")
            changes =""
        new_data = old_data.replace(data_to_change, changes)
        with open('calendar.txt', 'w') as new_f:
            new_f.write(new_data)

        print(f"Событие с id {event_id} УДАЛЕНО!\n")
        self.init_calendar()

    def stop(self):
        pass



cal = CalendarTaskManager()
cal.init_calendar()
