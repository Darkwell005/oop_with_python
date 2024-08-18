class CPU:
    def __init__(self, name: str, fr: int):
        self.name = name
        self.fr = fr

    def __str__(self):
        return f"{self.name}, {self.fr}"


class Memory:
    def __init__(self, name: str, volume: int):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name: str, cpu: "CPU", *mem_slots):
        self.name = name
        self.cpu = cpu
        self.__total_mem_slots = 4
        self.mem_slots: list['Memory'] = list(mem_slots[:self.__total_mem_slots])

    def _get_mem_slots(self) -> str:
        return '; '.join(f"{item.name} - {item.volume}" for item in self.mem_slots)

    def get_config(self) -> str:
        return (f"Материнская плата: {self.name}, "
                f"\nЦентральный процессор: {self.cpu}, "
                f"\nСлотов памяти: {self.__total_mem_slots}, "
                f"\nПамять: {self._get_mem_slots()}")


cp = CPU("Intel Core i5", 3000)
mem = Memory("SIMM", 512)
mem_2 = Memory("DIMM", 1024)
mem_3 = Memory("FB-DIMM", 256)
mem_4 = Memory("SODIMM", 128)
mem_5 = Memory("RIMM", 64)
mb = MotherBoard("Micro-ATX", cp, mem, mem_2, mem_3, mem_4, mem_5)
print(mb.get_config())
