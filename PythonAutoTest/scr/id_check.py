def is_valid_tw_id(id_number):
    try:
        if not isinstance(id_number, str):
            return False
        if len(id_number) != 10:
            return False
        first = id_number[0].upper()
        if not first.isalpha():
            return False
        if id_number[1] not in ['1', '2']:
            return False
        if not id_number[2:].isdigit():
            return False
        return True
    except Exception as e:
        print("錯誤內容：", e)
        return False