from os import makedirs
from os.path import join, exists
from random import randint, choice
from time import sleep

class CreateFolder:
    def __init__(self, link:str, number:str):
        '''
        没错！这个类负责创建文件夹，是后端！
        跟我前面的兄弟不一样，我负责与系统交互！
        呃，当然，如果我在创建文件夹出错了，我会甩出报错，提示用户
        不过，既然要让我创建文件夹，你要给我路径和创建数量，我才给你创建

        下面__init__函数说明：
        负责创建文件夹这个核心工作，至于乱码生成和其他？这个是其他函数干的事情
        '''
        try:
            for i in range(int(number)):
                makedirs(join(link, self._set_folder_name())) #创建文件夹
            print('创建成功了！')
        except KeyboardInterrupt:
            '''
            说明：由于创建文件夹可能会有一些不可控因素（例子：系统大粪、用户疏忽、权限不足等）
            try会捕获全部异常，包括KeyboardInterrupt。全局的肯定失效了
            所以需要这样捕获，然后再次甩出KeyboardInterrupt，让全局能够捕获这个异常，从而提示用户已退出。
            '''
            raise KeyboardInterrupt('用户取消了文件夹创建。')
        except FileExistsError: #能触发这个报错的，你运气是真的好
            print('''
【软件惊叹】老天爷！你这运气去买彩票吧！
软件万万没想到随机数竟然能撞车创建出同名文件夹，你居然中奖了！
如果可以的话，建议你今天出门左转买一张彩票，如果这个软件对你有帮助，中了记得分我一些。

不过如果你仍想要创建文件夹，请重启该软件。''')
        except Exception as e: #其他问题报错汇总
            print('''【软件异常】创建文件夹时发生了错误...
通常，文件夹创建出错是由下面的原因导致的：
1)  你输入了一个存在的目录，然后你把它删了。
2)  你没有授予该软件相应的权限去创建相应权限的文件夹。
3)  你想创建的目录所在的磁盘空间已满。
4） 创建文件夹中途你的磁盘坏了。

如果你已排查上述原因，但是还是异常，请联系作者解决。
报错提示：'''+str(e)) #友善化的报错排查提示

    def _choose_letter(self, how_long:int) -> str:
        '''
        我，负责随机生成一段乱文，也是乱码文件夹生成器的一个重要零件。
        不过开始之前，你先给我输入一个数字，决定我到底要生成多长的乱文
        我生成好了后会给你
        '''
        letter = 'abcdefghijklmnopqrstuvwxyz1234567890'
        return ''.join(choice(letter) for _ in range(how_long)) #返回已经搞定的乱文
    
    def _set_folder_name(self) -> str:
        '''
        负责乱码文件夹的命名。
        不需要向该函数提供任何名称，可以直接调用。
        当工作完成时，返回乱码文件夹的值。
        '''
        template = ['%s-%s-%s-%s','%s-%s-%s',
                    '%s-%s','%s'] #乱码文件夹名称的名称模板
        choosed_template = choice(template) #选择一个模板
        word_temp = [] #乱文的暂存列表
        for i in range(choosed_template.count('%s')):
            word_temp.append(self._choose_letter(randint(5, 10)))
        #下方的return将会现场组合好乱码文件夹的名称，然后返回
        return choosed_template%tuple(word_temp)


class Main:
    def __init__(self):
        '''
    这是软件的前端，负责收集必要的信息
    你问创建文件夹？那请你去CreateFolder这个类，你找错人了
    啊不对，我是个类，咳咳，你找错类了，请你找我上面的兄弟

    下面的__init__函数说明：
    这是整个软件的向导，负责询问用户问题。
        '''
        while True: 
            '''
            循环·第一关
            内容：问用户要把文件夹创建在哪里
            如果用户输入正确目录（或者盘符），循环打断
            否则，一直循环。
            '''
            where_to_storage = input('你想在哪里创建文件夹？\n创建位置：') #向用户询问在哪里创建
            if self._check_folder_exists(where_to_storage):
                #若文件夹存在（或者用户输入盘符），则打破循环
                break
            print('请输入一个存在的路径！\n')

        while True:
            '''
            循环·第二关
            内容：问用户要创建多少个文件夹
            与第一关相似，但是会问用户希望创建多少个文件夹
            如果用户输入正确的阿拉伯数字，这关过，否则一直循环
            '''
            folder_number = input('\n你要创建多少个文件夹？\n创建数量：') #向用户询问创建多少文件夹
            if self._check_number_exists(folder_number):
                #数字合规方可过此关
                break
            #到这里，你通过了几关呢？
        print('\n创建中，请稍候...')
        CreateFolder(where_to_storage, folder_number)

    def _check_folder_exists(self, link:str) -> bool:
        '''
        负责检查文件夹地址是否存在。
        如果文件夹地址是存在的，返回True，反之False。
        '''
        return exists(link)

    def _check_number_exists(self, number:str) -> bool:
        '''
        负责检查数字输入是否有效，如果有效则返回Yes。
        如果无效，甚至报错的，会提示（承担了一部分向导工作），并返回False。
        '''
        try:
            if int(number) <= 0: #是否创建小于等于0个文件夹
                print('不可以创建小于或等于0个文件夹！')
                return False
            else: #如果不是
                return True
        except ValueError: #用户输入非阿拉伯数字
            print('请输入阿拉伯整数，而不是其他内容！')
            return False


try: #全局捕捉KeyboardInterrupt错误
    Main()
except KeyboardInterrupt:
    print('\n软件已退出。')