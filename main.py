from tqdm import tqdm
import zipfile
import itertools

# 打开压缩文件
zip_file = zipfile.ZipFile('./test.zip')
# 把压缩文件内，所含的单个文件放入列表
zip_list = zip_file.namelist()

# 有可能构成密码字符（穷举字典）
chars_dict = '1234567'
# 这里repeat理解成密码长度为6位，当然可以用循环定制密码长度范围，这里简单处理
passwords = itertools.product(chars_dict, repeat=7)

# 用一个列表，来装itertools穷举出的密码字符串
list_password = list()

# 把itertools.product方法穷举的密码，类型转换成字符串，放入密码列表
for password in passwords:
    password = ''.join(password)
    list_password.append(password)

# 把文件列表中的文件取出来，尝试用密码列表中的密码解密
for f in zip_list:
    # 从密码列表中循环去除密码测试解密
    for key in tqdm(list_password):
        # 成功解密后，把正确的解压密码打印出来，并结束循环
        try:
            zip_file.extract(f, pwd=key.encode('utf-8'))
            print(f'you password is : {key}')
            break
        # 如果密码错误，打印报错信息
        except Exception as Error:
            continue
