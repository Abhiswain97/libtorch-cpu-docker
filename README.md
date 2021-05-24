# libtorch-cpu-docker

## How to use

1. Your project folder structure should be:

  ```
  | DockerFile
  |
  \---src
          test.cpp
          test.h
  ```
2. Create an `src` folder, put all your `.h` and `.cpp` files in this folder.

3. Create a `DockerFile` in your project folder. Copy paste the below contents to you `DockerFile`

  ```
  FROM abhiswain97/libtorch-cpu

  COPY ./src /src

  WORKDIR /src

  RUN /bin/bash -c "python3 create_CMakeLists.py"

  RUN /bin/bash -c "apt install make && mkdir build"

  WORKDIR /src/build

  RUN /bin/bash -c "cmake -DCMAKE_PREFIX_PATH=/libtorch .. && make"

  CMD [ "./run" ]

  ```
  
4. Build the container: `docker build -f DockerFile -t my-app .`

5. After build finishes, run the container: `docker run -it my-app`

6. And voila! your libtorch code runs! 

> You can check the complete DockerFile at: [DockerFile](DockerFile)

## Example with docker-compose

1. Clone the repo: 
  ```
  git clone https://github.com/Abhiswain97/libtorch-cpu-docker.git 
  cd libtorch-cpu-docker
  cd test
  ```

2. Do, `docker-compose up`

3. If all goes well, then you shoud see:

  ```
  (base) C:\Users\abhi0\Desktop\libtorch-cpu-docker\example>docker compose up
  [+] Running 1/1
  - Container example_libtorch-service_1  Recreated                                                                                                    0.1s 
  Attaching to libtorch-service_1
  libtorch-service_1  |  1  0  0  0  0  0  0  0  0  0
  libtorch-service_1  |  0  1  0  0  0  0  0  0  0  0
  libtorch-service_1  |  0  0  1  0  0  0  0  0  0  0
  libtorch-service_1  |  0  0  0  1  0  0  0  0  0  0
  libtorch-service_1  |  0  0  0  0  1  0  0  0  0  0
  libtorch-service_1  |  0  0  0  0  0  1  0  0  0  0
  libtorch-service_1  |  0  0  0  0  0  0  1  0  0  0
  libtorch-service_1  |  0  0  0  0  0  0  0  1  0  0
  libtorch-service_1  |  0  0  0  0  0  0  0  0  1  0
  libtorch-service_1  |  0  0  0  0  0  0  0  0  0  1
  libtorch-service_1 exited with code 0
  ```
