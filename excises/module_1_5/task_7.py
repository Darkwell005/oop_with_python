class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fps = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name: str, cpu: "CPU", total_mem_slots: int = 4):
        self.name = name
        self.cpu = cpu
        self.__total_mem_slots = total_mem_slots
    def get_config(self):
        return


