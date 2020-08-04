printers = []
for i in range(10):
    def printer():
        print(i)
    printers.append(printer)
printers[0]()
printers[5]()
printers[9]()
i = 42
printers[0]()


printers = []
for i in range(10):
    def make_printer(arg):
        def printer():
            print(arg)
        return printer
    p = make_printer(i)
    printers.append(p)
printers[0]()
printers[5]()
