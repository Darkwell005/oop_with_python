class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fps = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

    def __str__(self):
        return f'{self.name} - {self.volume}'


class MotherBoard:
    def __init__(self, name: str, cpu: "CPU", *mem_slots):
        self.name = name
        self.cpu = cpu
        self.__total_mem_slots = 4
        self.mem_slots: list['Memory'] = list(mem_slots[:self.__total_mem_slots])

        # print('Память: ', end='')
        # for item in self.mem_slots:
        #     print(item.name, item.volume, sep=' - ', end='; ')
        #
        # '; '.join(f"{item.name} - {item.volume}" for item in self.mem_slots)

    def get_config(self):
        return
