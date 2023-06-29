# Decorator 设计模式是一种结构型设计模式，它允许你在不修改现有对象结构的情况下，动态地向对象添加功能。这种模式可以看作是在对象外部包装一个装饰器，通过这个装饰器来添加额外的行为。
#
# 在生活中，Decorator 设计模式可以通过以下例子进行解释：
#
# 咖啡店的调味品：假设你在咖啡店点了一杯咖啡，咖啡店提供了多种调味品（如糖、牛奶、巧克力等）。这些调味品可以看作是装饰器，它们可以在不改变咖啡本身的情况下，为咖啡添加额外的味道和特性。
#
# 装饰家具：想象你有一张普通的桌子，你想为它增添一些特殊的装饰。你可以在桌子的表面放置一个精美的桌布，或者用一些花边来装饰桌子的边缘。这些装饰物就是装饰器，它们可以改变桌子的外观，但并不改变桌子本身的基本功能。
#
# 网页设计中的效果：在网页设计中，你可能需要为某些元素添加动画效果或者改变它们的外观。通过使用装饰器，你可以在不改变原始元素的结构的情况下，为其添加动态效果，比如淡入淡出效果、旋转效果等。
# 装饰蛋糕：假设你有一个简单的蛋糕，你想让它更加精美和独特。你可以使用巧克力饰品、水果、糖霜等装饰物来装饰蛋糕，使其看起来更吸引人。这些装饰物可以看作是装饰器，它们可以改变蛋糕的外观和口味，而不影响蛋糕的基本结构。
#
# 室内装饰：在你的家中，你可能有一面普通的墙壁，你希望为其增添一些艺术性和个性化的特点。你可以使用壁纸、墙贴、画作等装饰品来装饰墙壁，使其成为房间的焦点。这些装饰品就是装饰器，它们可以改变墙壁的外观和氛围，使房间更加美观和独特。
#
# 餐厅菜单：在一个餐厅的菜单上，你可能有基本的菜肴选项，但你也希望为顾客提供额外的选择和变化。通过添加特殊配料、烹饪风格或调味品，你可以为菜肴添加装饰器，使其在口味和外观上与普通菜肴不同。
#
# 汽车定制：在购买一辆汽车后，你可能想要对其进行个性化定制，使其符合你的品味和需求。你可以选择添加特殊的车身涂装、合金轮毂、车顶行李架等装饰物来装饰你的汽车。这些装饰物充当装饰器，使你的汽车与其他相同型号的汽车有所区别。
# 示例1：咖啡店的调味品

# 基础咖啡类
# class Coffee:
#     def get_description(self):
#         return "Coffee"
#
# # 调味品装饰器基类
# class CoffeeDecorator(Coffee):
#     def __init__(self, coffee):
#         self.coffee = coffee
#
#     def get_description(self):
#         return self.coffee.get_description()
#
# # 具体调味品装饰器
# class Sugar(CoffeeDecorator):
#     def get_description(self):
#         return f"{self.coffee.get_description()}, Sugar"
#
# class Milk(CoffeeDecorator):
#     def get_description(self):
#         return f"{self.coffee.get_description()}, Milk"
#
# class Chocolate(CoffeeDecorator):
#     def get_description(self):
#         return f"{self.coffee.get_description()}, Chocolate"
#
# # 客户端代码
# coffee = Coffee()
# coffee_with_sugar = Sugar(coffee)
# coffee_with_milk = Milk(coffee_with_sugar)
# coffee_with_chocolate = Chocolate(coffee_with_milk)
#
# print(coffee_with_chocolate.get_description())  # Output: Coffee, Sugar, Milk, Chocolate

# 没有使用装饰器模式的例子

# 基础咖啡类
class Coffee:
    def __init__(self):
        self.description = "Coffee"

    def get_description(self):
        return self.description

# 客户端代码
coffee = Coffee()
coffee_with_sugar = coffee.get_description() + ", Sugar"
coffee_with_sugar_and_milk = coffee_with_sugar + ", Milk"
coffee_with_sugar_and_milk_and_chocolate = coffee_with_sugar_and_milk + ", Chocolate"

print(coffee_with_sugar_and_milk_and_chocolate)  # Output: Coffee, Sugar, Milk, Chocolate
# 在上述代码中，为了为咖啡添加不同的调味品，我们直接在咖啡描述字符串中进行拼接操作。这种方式会导致以下问题：
#
# 修改原始类：为了添加调味品，我们不得不修改咖啡类的描述属性。这违反了开放封闭原则，应该尽量避免直接修改原始类的属性和行为。
#
# 难以扩展和维护：如果需要添加更多的调味品或者调整调味品的顺序，将会变得非常困难和混乱。每次都需要修改拼接操作，代码变得冗长且难以维护。
#
# 使用装饰器模式可以解决以上问题，它提供了一种灵活的方式来动态地为对象添加功能，同时保持代码的可扩展性和可维护性。
