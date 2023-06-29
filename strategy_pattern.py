# 旅行计划：假设你计划去旅行，你可以使用策略模式来选择适合你的旅行策略。例如，你可以根据预算和兴趣选择不同的旅行策略，比如自助旅行、跟团旅行或豪华旅行。每种策略都有不同的特点和费用，你可以根据自己的需求和偏好选择合适的策略。
# 
# 健身计划：在健身领域，你可以使用策略模式来制定适合你的健身计划。不同的人有不同的健身目标和喜好，可以选择不同的策略，比如有氧运动、重力训练、瑜伽等。每种策略都有不同的训练方法和效果，你可以根据自己的目标和喜好选择合适的策略。
# 
# 点餐方式：在餐厅就餐时，你可以使用策略模式来选择点餐的方式。例如，你可以选择自助餐、点菜服务或外卖服务。每种点餐方式都有不同的特点和便利性，你可以根据就餐场合和个人喜好选择合适的策略。
# 
# 金融投资：在金融领域，策略模式可以应用于投资决策。不同的投资策略适用于不同的市场情况和风险偏好。例如，你可以选择价值投资策略、成长投资策略或指数基金投资策略等。每种策略都有不同的投资理念和风险收益特点，你可以根据自己的投资目标和风险承受能力选择合适的策略。
# 假设你正在开发一个电子商务网站，你有一个产品类(Product)表示网站上的商品。每个商品都有基本的属性，如名称、价格和描述。然而，你希望为某些商品添加额外的特性，如折扣、促销标签等，但又不希望修改产品类的代码。
#
# 在这个例子中，你可以使用Decorator模式来添加额外的特性。你可以创建一个抽象的装饰器类(Decorator)，它继承自产品类(Product)，
# 并包含一个产品类的实例作为属性。然后，你可以创建具体的装饰器类，如折扣装饰器(DiscountDecorator)或促销标签装饰器(PromotionDecorator)，来为产品添加相应的特性。
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.discount_strategy = None

    def add_item(self, item):
        self.items.append(item)

    def set_discount_strategy(self, discount_strategy):
        self.discount_strategy = discount_strategy

    def calculate_total_price(self):
        total_price = 0
        for item in self.items:
            total_price += item.price

        if self.discount_strategy:
            total_price = self.discount_strategy.apply_discount(total_price)

        return total_price


class DiscountStrategy:
    def apply_discount(self, total_price):
        pass


class ChristmasDiscount(DiscountStrategy):
    def apply_discount(self, total_price):
        return total_price * 0.9


class BlackFridayDiscount(DiscountStrategy):
    def apply_discount(self, total_price):
        return total_price * 0.8


# 客户端代码
cart = ShoppingCart()

# 添加商品
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

item1 = Item("Shirt", 20)
item2 = Item("Pants", 30)
item3 = Item("Shoes", 50)

cart.add_item(item1)
cart.add_item(item2)
cart.add_item(item3)

# 计算订单总价（无折扣）
total_price = cart.calculate_total_price()
print("Total Price (No Discount):", total_price)

# 设置折扣策略为圣诞节折扣
cart.set_discount_strategy(ChristmasDiscount())

# 计算订单总价（应用圣诞节折扣）
total_price_with_discount = cart.calculate_total_price()
print("Total Price (Christmas Discount):", total_price_with_discount)

# 设置折扣策略为黑色星期五折扣
cart.set_discount_strategy(BlackFridayDiscount())

# 计算订单总价（应用黑色星期五折扣）
total_price_with_discount = cart.calculate_total_price()
print("Total Price (Black Friday Discount):", total_price_with_discount)
