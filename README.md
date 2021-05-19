# libtorch-cpu-docker

1. Your project folder structure should be:

  ```
  |   DockerFile
  |
  \---src
          test.cpp
          test.h
  ```
    Here, `src` folder contains your `.h` and `.cpp` files.

2. Create a `DockerFile` in your project folder. Copy paste the below contents to you `DockerFile`

  ```
  FROM ubuntu:18.04

  RUN apt-get update 
  RUN apt-get install -y gcc g++ build-essential libssl-dev cmake wget unzip python3-dev git

  ARG path=libtorch-cxx11-abi-shared-with-deps-1.8.1+cpu

  RUN wget --no-check-certificate https://download.pytorch.org/libtorch/cpu/libtorch-cxx11-abi-shared-with-deps-1.8.1%2Bcpu.zip \
      && unzip ${path}.zip \
      && rm -r ${path}.zip

  RUN mkdir src && mkdir throwaway

  RUN git clone https://github.com/Abhiswain97/libtorch-cpu-docker.git \
      && cp /libtorch-cpu-docker/create_CMakeLists.py /src \
      && rm -r /libtorch-cpu-docker

  COPY . /throwaway

  RUN [ -f /throwaway/*.cpp ] && cp /throwaway/*.cpp /src 

  RUN [ -f /throwaway/*.h ] && cp /throwaway/*.h /src 

  RUN rm -r /throwaway

  WORKDIR /src

  RUN /bin/bash -c "python3 create_CMakeLists.py"

  RUN /bin/bash -c "apt install make && mkdir build"

  WORKDIR /src/build

  RUN /bin/bash -c "cmake -DCMAKE_PREFIX_PATH=/libtorch .. && make"

  CMD [ "./run" ]

  ```
  
3. Build the container: `docker build -f DockerFile -t my-app .`

4. After build finishes, run the container: `docker run -it my-app`

5. And voila! your libtorch code runs! 
