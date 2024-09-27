# 密码本
code = [
    "ZWAXJGDLUBVIQHKYPNTCRMOSFE",
    "KPBELNACZDTRXMJQOYHGVSFUWI",
    "BDMAIZVRNSJUWFHTEQGYXPLOCK",
    "RPLNDVHGFCUKTEBSXQYIZMJWAO",
    "IHFRLABEUOTSGJVDKCPMNZQWXY",
    "AMKGHIWPNYCJBFZDRUSLOQXVET",
    "GWTHSPYBXIZULVKMRAFDCEONJQ",
    "NOZUTWDCVRJLXKISEFAPMYGHBQ",
    "QWATDSRFHENYVUBMCOIKZGJXPL",
    "WABMCXPLTDSRJQZGOIKFHENYVU",
    "XPLTDAOIKFZGHENYSRUBMCQWVJ",
    "TDSWAYXPLVUBOIKZGJRFHENMCQ",
    "BMCSRFHLTDENQWAOXPYVUIKZGJ",
    "XPHKZGJTDSENYVUBMLAOIRFCQW",
]

# 密文和密钥
codetext = "HCBTSXWCRQGLES"  # 密文
codenum = "2,5,1,3,6,4,9,7,8,14,10,13,11,12"  # 密钥
codenum = [int(i) - 1 for i in codenum.split(",")]  # 将密钥字符串分割成列表并转换为0索引

# 用于存储旋转后的行，保持与密钥顺序一致
rotated_code = []


# 重新排列密码本中的行，并根据密钥顺序旋转
for i, row_index in enumerate(codenum):
    index = code[row_index].index(codetext[i])  # 找到当前密文字符在对应行中的位置
    rotated_row = code[row_index][index:] + code[row_index][:index]  # 旋转行
    rotated_code.append(rotated_row)  # 添加到新的旋转密码本中

# 格式化解码本
spaced_code = ['  '.join(row) for row in rotated_code]
letter_count = len(spaced_code[0].split())  # 计算字母个数

# 生成第一行数字，确保每个数字占用3个字符宽度对齐
number_line = '  '.join([f"{i + 1:>3}" for i in range(letter_count)])

# 打印第一行数字
print(f"{number_line}")
# 格式化输出每一行，确保字母对齐
for row in spaced_code:
    formatted_row = '  '.join([f"{char:>3}" for char in row.split()])
    print(formatted_row)

# 询问用户想查看哪一列
column = int(input("\n请输入想要查看的列号 : "))  # 用户输入列号

# 检查输入是否有效
if 1 <= column <= letter_count:
    column_letters = []  # 用于存储整列的字母
    for row in rotated_code:  # 使用旋转后的密码本
        letter = row[column - 1]  # 获取该列的字母
        column_letters.append(letter)  # 添加到列表中

    # 将列字母拼接成一个字符串并用 flag{} 包裹
    flag_output = "flag{" + ''.join(column_letters) + "}"
    print(f"\n第 {column} 列的内容是: {flag_output}")
else:
    print("无效的列号。")
