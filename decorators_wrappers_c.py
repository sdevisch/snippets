# simply importing a module generates a sequence of events
# We can't use the logger yet
print("Before any imports")

# local module imports
import util

print("About to import decorators")
import decorators_wrappers as dw

print("After importing decorators")


def main():
    print("in main")
    log = util.logger()
    log.info("All the above happened as part of import. Starting main now.")
    log.info("About to call x")
    log.info("x returns " + str(dw.x("string argument", [2, 3, 4])))
    log.info("y returns " + str(dw.y()(2)))  # y now returns a function
    log.info("About to call the decorator without factory")
    log.info(
        "with a decorator hash(es) returned " + str(dw.hash_it("withouth @as_bytes this wouldn't work"))
    )  # y now returns a function
    log.info("About to call the decorator WITH factory")
    log.info(
        "with a decorator factory, hash(es) returned "
        + str(
            dw.hash_it_with_decorator_factory("this now works with a decorator factory")
        )
    )  # y now returns a function
    log.info("About to call the decorator WITH factory CLASS")
    log.info(
        "with a decorator factory class, hash(es) returned "
        + str(
            dw.hash_it_with_decorator_class("this now works with a decorator class", "but not")
        )
    )



if __name__ == "__main__":
    print("Before main")
    main()
