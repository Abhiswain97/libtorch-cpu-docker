# libtorch-cpu-docker

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

5. And voila! your libtorch code runs! 
