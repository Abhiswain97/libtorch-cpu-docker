FROM abhiswain97/libtorch-cpu

COPY ./src /src

WORKDIR /src

RUN /bin/bash -c "python3 create_CMakeLists.py"

RUN /bin/bash -c "apt install make && mkdir build"

WORKDIR /src/build

RUN /bin/bash -c "cmake -DCMAKE_PREFIX_PATH=/libtorch .. && make"

CMD [ "./run" ]