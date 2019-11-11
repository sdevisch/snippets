# local library import
import descriptors as d


def main():
    print("about to instantiate a")
    a = d.A()
    print("about to set x for a")
    a.x = 6
    print("printing a: " + str(a.x))

    abc = d.B()
    abc.x = 7
    print("printing abc: " + str(abc.x))

    print("printing a again: " + str(a.x))
    print("======== about to switch to MyClass ========")

    class MyClass(object):
        print("In MyClass. Using composition to give MyClass an attribute")
        x = d.RevealAccess()
        print("In MyClass after defining x in MyClass. This happens before set_name")

    print("about to instantiate class MyClass")
    m = MyClass()
    print("about to call the attribute as a function. this works if __call__ is implemented")
    # try_call = m.x()
    # print(try_call)  # note the parentheses after x
    print("about to set attribute x for m, the instance of MyClass")
    m.x = 20
    print("about to access the attribute x in m")
    print(m.x)    # not the lack of parentheses for x




if __name__ == "__main__":
    main()
