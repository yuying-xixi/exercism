def recite(start_verse, end_verse):
    # 定义每一段的核心元素（动作 + 对象），按出现顺序排列
    elements = [
        ("house that Jack built", ""),  # 第1段没有前置动作
        ("malt", "lay in"),
        ("rat", "ate"),
        ("cat", "killed"),
        ("dog", "worried"),
        ("cow with the crumpled horn", "tossed"),
        ("maiden all forlorn", "milked"),
        ("man all tattered and torn", "kissed"),
        ("priest all shaven and shorn", "married"),
        ("rooster that crowed in the morn", "woke"),
        ("farmer sowing his corn", "kept"),
        ("horse and the hound and the horn", "belonged to")
    ]
    
    verses = []
    # 生成从start_verse到end_verse的每一段
    for verse in range(start_verse, end_verse + 1):
        # 确定当前段用到的元素（从0到verse-1索引）
        parts = elements[:verse]
        # 第一段的特殊处理（没有动作，直接结尾）
        if verse == 1:
            line = f"This is the {parts[0][0]}."
        else:
            # 构建嵌入的短语部分
            embedded = []
            # 从当前段的最后一个元素倒序遍历到第二个元素（索引1到verse-1）
            for i in range(verse - 1, 0, -1):
                obj, action = parts[i]
                prev_obj = parts[i - 1][0]
                embedded.append(f"that {action} the {prev_obj}")
            # 拼接完整段落
            first_obj = parts[-1][0]
            embedded_str = ' '.join(embedded)
            line = f"This is the {first_obj} {embedded_str}."
        verses.append(line)
    return verses
