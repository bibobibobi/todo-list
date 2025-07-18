import json
filepath = r'C:\Users\brian\Documents\Python\todo_list_project\todo.txt'

#顯示所有代辦事項
def show_all_event(todo_list):
    for index, event in enumerate(todo_list, 1):
                status = '完成' if event['done'] else '未完成'
                print(f'{index}. {event["task"]} {status}')

todo_list = []

#讀檔功能
try:
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            todo_list.append(json.loads(line.strip()))
except FileNotFoundError:
    pass

while True:
    print('========== To-Do list menu ==========')
    print('1. 查看代辦事項清單')
    print('2. 新增代辦事項')
    print('3. 刪除代辦事項')
    print('4. 標記代辦事項為已完成')
    print('5. 離開')

    while True:
        try:
            choice = int(input('請輸入功能選項(1~5) : '))
            break
        except ValueError:
            print('請輸入正確功能選項')
            continue

    if choice == 1: #查看
        if not todo_list:
            print('無代辦事項 請先新增代辦事項')
        else:
            show_all_event(todo_list)

    elif choice == 2: #新增
        event = input('輸入要新增的代辦事項 : ')
        todo_list.append({'task':event,'done':False})
        print(f'已新增代辦事項 : {event}')

    elif choice == 3: #刪除
        if not todo_list:
            print('無代辦事項 請先新增代辦事項')
        else:
            show_all_event(todo_list)

            while True: #輸入刪除編號並判斷是否有效
                try:
                    delete = int(input('請輸入要刪除的代辦事項編號'))
                    if 1 <= delete <= len(todo_list):
                        break
                    else:
                        print('請輸入正確範圍中的代辦事項編號')
                except ValueError:
                    print('請輸入有效編號')
                    continue

            remove = todo_list.pop(delete - 1)
            print(f'已刪除 : {remove["task"]}')
    elif choice == 4: #標記已完成
        if not todo_list:
            print('無代辦事項 請先新增代辦事項')
        else:
            show_all_event(todo_list)

            while True: #輸入要標記的編號並判斷是否有效
                try:
                    complete = int(input('請選擇要標記為已完成的選項 : '))
                    if 1 <= complete <= len(todo_list):
                        break
                except ValueError:
                    continue

            todo_list[complete - 1]['done'] = True


    elif choice == 5: #離開
        #存檔功能
        with open(filepath, 'w', encoding='utf-8') as file:
            for event in todo_list:
                file.write(json.dumps(event) + '\n')

        print('下次再見~')
        break
