# 文件系统：在操作系统中，文件系统是一个典型的层次结构。文件夹（目录）可以包含文件和其他文件夹。文件夹可以看作是组合对象，而文件可以看作是叶子对象。使用组合模式可以以统一的方式处理文件和文件夹，例如复制、移动或删除。
#
# 组织结构：在企业或组织中，通常存在层次化的组织结构，如部门、团队和员工。部门可以包含其他部门或团队，而团队可以包含员工。使用组合模式可以以统一的方式处理部门、团队和员工，例如获取总体组织结构、计算部门的总人数等。
#
# 菜单和菜单项：在图形用户界面中，菜单通常具有嵌套的结构。菜单可以包含菜单项和其他菜单。使用组合模式可以以统一的方式处理菜单和菜单项，例如显示菜单、执行菜单项的操作等。
#
# 目录结构：在文件管理工具中，通常会显示计算机上的目录结构。目录可以包含其他目录和文件。使用组合模式可以以统一的方式浏览和操作目录结构，例如创建新目录、复制文件夹等。
#
# 图形绘制：在图形编辑器中，图形对象可以组成复杂的图形结构。图形可以是基本图形（如圆、矩形）或复合图形（如组合多个基本图形）。使用组合模式可以以统一的方式处理基本图形和复合图形，例如移动、缩放或旋转图形。
from abc import ABC, abstractmethod

# 定义组件接口
class Component(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_total_employees(self):
        pass

# 实现叶子对象：员工
class Employee(Component):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_total_employees(self):
        return 1

# 实现组合对象：部门
class Department(Component):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def get_name(self):
        return self.name

    def get_total_employees(self):
        total_employees = 0
        for child in self.children:
            total_employees += child.get_total_employees()
        return total_employees

# 使用示例
employee1 = Employee("John")
employee2 = Employee("Alice")
employee3 = Employee("Bob")

team1 = Department("Team 1")
team1.add(employee1)
team1.add(employee2)

team2 = Department("Team 2")
team2.add(employee3)

department = Department("Department")
department.add(team1)
department.add(team2)

print(department.get_total_employees())  # 输出总员工数
