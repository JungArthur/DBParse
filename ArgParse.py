

def find_end_bracket(source, start_index):
    print(f'find_bracket : {source}    start : {start_index}')
    cursor = 0
    find_left_list = []
    find_right_list = []
    find_comma_list = []

    # find_left_list.append( slice_source.find('(') )

    for index in range(len(source)):

        if source[index] == ',':
            # print(f', : find index = {index}')
            find_comma_list.append(index)

        if source[index] == '(':
            # print(f'( : find index = {index}')
            find_left_list.append(index)

        if source[index] == ')':
            # print(f') : find index = {index}')
            find_right_list.append(index)

        # finish Flag len( find_left_list ) == len( find_right_list ) :
        if len(find_left_list) + len(find_right_list) > 1 and len(find_left_list) == len(find_right_list):
            # print('Scuccess')

            first_args_start = find_left_list[0]
            first_args_end = find_comma_list[0]
            last_args_start = find_comma_list[len(find_comma_list) - 1]
            last_args_end = find_right_list[len(find_right_list) - 1]

            # 재귀적이였으면 허용안됨.

            first_args = source[first_args_start + 1: first_args_end]
            # 세번째 인자가 없는 케이스
            if first_args_end == last_args_start:
                second_args = source[last_args_start + 1: last_args_end]
                last_args = ''
            else:
                second_args = source[first_args_end: last_args_start + 1]
                last_args = source[last_args_start + 1: last_args_end]

            # 여기 포함되면 Pass
            mssql_third_args = ['1', '8', '10', '21', '24', '12', '23', '23', '20', '120', '126', '111', '108', '114',
                                '121', '112', '126']
            date_seconds_args = ["STATUS", 'TYPE', "ID", "QTY", "QUANTITY", "NO", "SUM", "COUNT", "DECIMAL", "CNT",
                                 "KEY"]

            return {
                'source': source.strip()[0:index],
                'first_args': first_args.strip(),
                'second_args': second_args.strip(),
                'last_args': last_args.strip(),
                'first_args_result': -1 != first_args.strip().upper().find('CHAR'),
                'secound_args_result': len([n for n in date_seconds_args if n in second_args.strip().upper()]) > 0,
                'last_args_result': last_args.strip() in mssql_third_args
            }

        # End for

        # Error if slice_source's legnth over !
        # Error if find_left == -1 ! && if find_right == -1 !
        # left > right && both != -1
        # right < left && both != -1
        # left == -1 right != -1
        # left != -1 right == -1

    # End function


def conver_args(input_string):
    if len(input_string) == 0:
        return

    find_index = 0

    # 대문자로 변경
    convert_string = input_string.upper()

    return_value_list = []

    # 대소문자구분안하는로직추가
    print(convert_string.upper().find('CONVERT', find_index + 1))
    while convert_string.find('CONVERT(', find_index + 1) != -1:

        find_index = convert_string.find('CONVERT(', find_index + 1)

        slice_source = convert_string[find_index:len(convert_string)]

        return_value = find_end_bracket(slice_source, find_index)

        # print(f'result : {return_value}')
        if return_value is not None:
            return_value_list.append(return_value)

    return return_value_list