# simply importing a module generates a sequence of events
# We can't use the logger yet
print("Before any imports")

# local module imports
import util

print("About to import decorators")
import decorators_basics as db

print("After importing decorators")


def main():
    print("in main")
    log = util.logger()
    log.info("We've got the logger going in main now")
    log.info("About to call summarize")
    log.info("Summary returns " + str(db.summarize([2, 3, 4])))


if __name__ == "__main__":
    print("Before main")
    main()
