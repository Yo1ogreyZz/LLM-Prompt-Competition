import json

# 读取JSON文件并压缩为一行
with open('9_Oct_1.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 写入到新文件（一行）
with open('9_Oct_1_compressed.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, separators=(',', ':'))

print("已将JSON压缩为一行并保存到 9_Oct_1_compressed.json")