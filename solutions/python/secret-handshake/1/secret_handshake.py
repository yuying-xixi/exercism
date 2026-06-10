"""
To output specified list
"""
def commands(binary_str):
    """
    :param binary_str:str -命令字符串
    :return :list -对应的动作列表
    """
    handshake_list = ['jump', 'close your eyes', 'double blink', 'wink']
    actions = []

    sliced_binary_str = binary_str[1:]

    for index, item in enumerate(sliced_binary_str):
        if item == '1':
            actions.append(handshake_list[index])

    if binary_str[0] != '1':
        actions.reverse()
    return actions
    
