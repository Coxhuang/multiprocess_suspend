from multiprocess.tornado_process1 import TornadoProcess1
from multiprocess.tornado_process2 import TornadoProcess2
from multiprocess.tornado_process3 import TornadoProcess3



if __name__ == "__main__":

    f1 = TornadoProcess1()
    f2 = TornadoProcess2()
    f3 = TornadoProcess3()
    f1.start()
    f2.start()
    f3.start()
    print("f1.pid:",f1.pid)
    print("f2.pid:",f2.pid)
    print("f3.pid:",f3.pid)