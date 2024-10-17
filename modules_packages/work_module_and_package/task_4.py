import speedtest
import platform

BITS_PER_MEGABYTE: int = 8 * 1024 ** 2

test: "speedtest" = speedtest.Speedtest()
download: float = test.download()
upload: float = test.upload()
system: str = platform.platform()
processor: str = platform.processor()
comp: str = platform.python_compiler()
py_version: str = platform.python_version()

print(f"Тип системы: {system}")
print(f"Установленный процессор: {processor}")
print(f"Текущая версия компилятора: {comp}")
print(f"Текущая версия Python: {py_version}")
print(f"Скорость загрузки: {round(download / BITS_PER_MEGABYTE, 2)}")
print(f"Скорость отдачи: {round(upload / BITS_PER_MEGABYTE, 2)}")
