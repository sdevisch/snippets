# local library import
import descriptors as d


def main():


    class MyClass(object):
        """
        Conclusions:
            __get__, __set__ and _del__ are class methods
            They are not instance methods.
            Below we have defined two RevealAccess attributes: x and y
            x is defined as class attribute
            y is defined as an instance attribute
            When x is retreived, __get__ is executed.
            This is not the case of y.

            You can see in the help section that x is an attribute.
            y is not.
        """

        print("In MyClass. Using composition to give MyClass a CLASS ATTRIBUTE x")
        x = d.RevealAccess()
        print("In MyClass. Using composition to give MyClass a CLASS ATTRIBUTE REVEALACCESS")
        REVEALACCESS = d.RevealAccess # note the lack of parentheses
        print("In MyClass after defining x in MyClass.")
        print("In MyClass type of x: ", type(x))
        print("In MyClass type of REVEALACCESS: ", type(REVEALACCESS))

        # demonstrating __call__
        print("======")
        print("about to call the attribute as a function. this works if __call__ is implemented")
        print("this still happens before the __init__ in MyClass")
        x()  # note the parentheses after x
        print("Now the name x will be set")
        print("======")



        def __init__(self):
            print("==== instantiating y; only run upon instantiation ===")
            print("Starting My_Class __init__")
            self.y = self.REVEALACCESS()
            print("type of y: ", type(self.y))


    print("===== printing MRO ===")
    print(MyClass.__mro__)
    print("===== no longer in MyClass definition ===")
    print("about to instantiate class MyClass and thus trigger MyClass init")
    m = MyClass()

    print("======")
    print("about to set attribute x for m, the instance of MyClass")
    m.x = 20
    print("about to access the attribute x in m")
    print(m.x)    # note the lack of parentheses
    m.x = m.x * 2
    print(m.x)  # note the lack of parentheses

    print("======")
    print("about to set attribute y for m, the instance of MyClass")
    m.y = 200
    print(m.y)  # note the lack of parentheses
    print("about to access the attribute y in m")
    m.y = m.y * 2
    print(m.y)  # note the lack of parentheses

    print("==== confirming x and y don't behave differently with a second instance")
    m2 = MyClass()
    print("======")
    print("about to set attribute x for m, the instance of MyClass")
    m2.x = 30
    print("about to access the attribute x in m")
    print(m2.x)
    m2.x = m2.x * 2
    print("printing m2.x: ", m2.x)
    print("confirming x did not change for m1: ", m.x)


    print("======")
    print("about to set attribute y for m, the instance of MyClass")
    m2.y = 300
    print(m2.y)  # note the lack of parentheses
    print("about to access the attribute y in m")
    m2.y = m2.y * 2
    print("printing m2.y: ", m2.y)
    print("confirming y did not change for m1: ", m.y)

    print("print(help(m2)")
    print(help(m2))
    print(dir(m2))




if __name__ == "__main__":
    main()
