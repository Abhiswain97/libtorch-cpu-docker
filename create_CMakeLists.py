import os
import shutil

src_files = []

for file in os.listdir("/src"):
    if file.endswith(".h") or file.endswith(".cpp"):
        src_files.append(f"/src/{file}")

src_str = ""

for i in src_files:
    src_str += (i + " ")

file_content = """
cmake_minimum_required (VERSION 3.8)

project(run CXX)

set(Torch_DIR "/libtorch/share/cmake/Torch")
set(PYTHON_EXECUTABLE "/usr/bin/python3")

find_package(Torch REQUIRED)
set(CMAKE_CXX_FLAGS "${} ${}")

file(GLOB files {})

add_executable(run "${}")

target_link_libraries(run "${}")
set_property(TARGET run PROPERTY CXX_STANDARD 14)

""".format(
    r"{CMAKE_CXX_FLAGS}", 
    r"{TORCH_CXX_FLAGS}", 
    src_str.rstrip(), 
    r"{files}", 
    r"{TORCH_LIBRARIES}")

with open("/src/CMakeLists.txt", "w") as f:
    f.writelines(file_content)

f.close()
