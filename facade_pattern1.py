# 外观模式（Facade Pattern）是一种结构性设计模式，它提供了一个简化的接口，用于访问复杂系统、类库或子系统中的一组接口。外观模式通过创建一个高层次的接口，隐藏了底层组件的复杂性，使得客户端更容易使用。
#
# 下面是一些生活中的例子，演示如何使用外观模式：
#
# 电脑开机：当你打开电脑时，你只需要按下电源按钮，而不需要了解电脑内部的复杂启动过程。在这里，电源按钮充当了一个外观，它隐藏了底层启动过程的复杂性。你只需要与电源按钮进行交互，而不需要直接与电脑的各个组件交互。
#
# 咖啡机制作咖啡：假设你使用一台自动咖啡机制作咖啡。咖啡机提供了一个简单的按钮或触摸屏界面，你只需要按下按钮或选择相应的选项，而不需要了解咖啡机内部的复杂操作。这里，咖啡机充当了一个外观，隐藏了底层的研磨咖啡豆、萃取咖啡等复杂过程。
#
# 旅行预订网站：当你使用旅行预订网站预订一次旅行时，你只需要提供出发地、目的地和日期等信息，并点击预订按钮。预订网站会处理底层的航班、酒店和租车等复杂过程，并为你提供一站式的服务。这里，预订网站充当了一个外观，将复杂的预订过程封装在一个简单的界面中。
#
# 家庭影院系统：在家庭影院系统中，你可以使用一个遥控器来控制多个设备，例如电视、音响、投影仪等。遥控器提供了一组按钮和菜单，你可以使用它们来控制不同的设备，而不需要分别操作每个设备。遥控器在这里充当了一个外观，简化了与多个设备交互的复杂性。
# 子系统类 - 电视
class Television:
    def turn_on(self):
        print("TV is turned on")

    def turn_off(self):
        print("TV is turned off")

# 子系统类 - 音响
class Stereo:
    def turn_on(self):
        print("Stereo is turned on")

    def turn_off(self):
        print("Stereo is turned off")

    def set_volume(self, volume):
        print(f"Set volume to {volume}")

# 子系统类 - 投影仪
class Projector:
    def turn_on(self):
        print("Projector is turned on")

    def turn_off(self):
        print("Projector is turned off")

    def set_input(self, source):
        print(f"Set input source to {source}")

# 外观类 - 家庭影院外观
class HomeTheaterFacade:
    def __init__(self, tv, stereo, projector):
        self.tv = tv
        self.stereo = stereo
        self.projector = projector

    def watch_movie(self, movie):
        print("Get ready to watch a movie!")
        self.tv.turn_on()
        self.stereo.turn_on()
        self.projector.turn_on()
        self.projector.set_input("DVD")
        # 一些其他操作，例如调整音量等
        print(f"Playing movie: {movie}")

    def end_movie(self):
        print("Movie is finished!")
        self.tv.turn_off()
        self.stereo.turn_off()
        self.projector.turn_off()

# 客户端代码
def main():
    # 创建子系统对象
    tv = Television()
    stereo = Stereo()
    projector = Projector()

    # 创建家庭影院外观对象
    home_theater = HomeTheaterFacade(tv, stereo, projector)

    # 使用家庭影院外观观看电影
    home_theater.watch_movie("Avengers: Endgame")

    # 结束电影
    home_theater.end_movie()

if __name__ == '__main__':
    main()
