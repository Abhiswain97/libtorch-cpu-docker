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

3. Create a `DockerFile` in your project folder. Copy paste the below contents to you `DockerFile`. If you know a little bit about Docker then, you can customize the below contents. One example can be, if you have extra folders for `model` and `data` then you can simply copy them to the Docker container also. That would just be 2 - 3 lines more

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

6. And voila! your libtorch code runs! You should see:

> You can check the complete DockerFile at: [DockerFile](DockerFile)

## Running the example

### Normal prodecure

1. Clone the repo: 
  ```
  git clone https://github.com/Abhiswain97/libtorch-cpu-docker.git 
  cd libtorch-cpu-docker
  cd test
  ```
  
2. Do, `docker build -f Dockerfile -t my-app .`
  ```
  C:\Users\abhi0\Desktop\libtorch-cpu-docker\example>docker build -f Dockerfile -t my-app .
  [+] Building 59.6s (13/13) FINISHED
   => [internal] load build definition from Dockerfile                                                                                                                                                          0.0s
   => => transferring dockerfile: 318B                                                                                                                                                                          0.0s
   => [internal] load .dockerignore                                                                                                                                                                             0.0s
   => => transferring context: 2B                                                                                                                                                                               0.0s
   => [internal] load metadata for docker.io/abhiswain97/libtorch-cpu:latest                                                                                                                                    4.0s
   => [auth] abhiswain97/libtorch-cpu:pull token for registry-1.docker.io                                                                                                                                       0.0s
   => [internal] load build context                                                                                                                                                                             0.0s
   => => transferring context: 249B                                                                                                                                                                             0.0s
   => [1/7] FROM docker.io/abhiswain97/libtorch-cpu@sha256:bf7a7e8bbb32f76bc311720f0c4cec93d74469142c7800637161c70169645fd9                                                                                    41.5s
   => => resolve docker.io/abhiswain97/libtorch-cpu@sha256:bf7a7e8bbb32f76bc311720f0c4cec93d74469142c7800637161c70169645fd9                                                                                     0.0s
   => => sha256:4bbfd2c87b7524455f144a03bf387c88b6d4200e5e0df9139a9d5e79110f89ca 26.70MB / 26.70MB                                                                                                              2.6s
   => => sha256:889a7173dcfeb409f9d88054a97ab2445f5a799a823f719a5573365ee3662b6f 189B / 189B                                                                                                                    0.8s
   => => sha256:bf7a7e8bbb32f76bc311720f0c4cec93d74469142c7800637161c70169645fd9 2.00kB / 2.00kB                                                                                                                0.0s
   => => sha256:d2e110be24e168b42c1a2ddbc4a476a217b73cccdba69cdcb212b812a88f5726 857B / 857B                                                                                                                    0.9s
   => => sha256:19f0bec7977466f28e7ac8d2ba7a7be29acaf2d269421175e09a84169ad91a39 4.58kB / 4.58kB                                                                                                                0.0s
   => => sha256:f417595c25656c25b8b3678f524fee6c34d1c25f421ae66b1de33787e4befa40 26.06MB / 26.06MB                                                                                                             12.2s
   => => sha256:1b319aa99dc477c8f8808bdcc37598de9abecce4e60d887862d8caf74aa4bec9 182.94MB / 182.94MB                                                                                                           26.0s
   => => sha256:69cceba8b87f9d1d13c8d3b3c348b04c523ff1965247b54f18d96b93b9d9d4d6 180.20MB / 180.20MB                                                                                                           26.1s
   => => extracting sha256:4bbfd2c87b7524455f144a03bf387c88b6d4200e5e0df9139a9d5e79110f89ca                                                                                                                     1.8s
   => => extracting sha256:d2e110be24e168b42c1a2ddbc4a476a217b73cccdba69cdcb212b812a88f5726                                                                                                                     0.0s
   => => extracting sha256:889a7173dcfeb409f9d88054a97ab2445f5a799a823f719a5573365ee3662b6f                                                                                                                     0.0s
   => => sha256:028c72551a281647e1f503ed2335b615c16fe2dde15cbc376675bf7135a4722f 124B / 124B                                                                                                                   12.6s
   => => extracting sha256:f417595c25656c25b8b3678f524fee6c34d1c25f421ae66b1de33787e4befa40                                                                                                                     1.2s
   => => sha256:8735b69bf53976a6e87d6a343cde7e6b5d526f8f94900124c9e67d1179637b58 624B / 624B                                                                                                                   12.9s
   => => extracting sha256:1b319aa99dc477c8f8808bdcc37598de9abecce4e60d887862d8caf74aa4bec9                                                                                                                     6.7s
   => => extracting sha256:69cceba8b87f9d1d13c8d3b3c348b04c523ff1965247b54f18d96b93b9d9d4d6                                                                                                                     8.0s
   => => extracting sha256:028c72551a281647e1f503ed2335b615c16fe2dde15cbc376675bf7135a4722f                                                                                                                     0.0s
   => => extracting sha256:8735b69bf53976a6e87d6a343cde7e6b5d526f8f94900124c9e67d1179637b58                                                                                                                     0.0s
   => [2/7] COPY ./src /src                                                                                                                                                                                     0.8s
   => [3/7] WORKDIR /src                                                                                                                                                                                        0.1s
   => [4/7] RUN /bin/bash -c "python3 create_CMakeLists.py"                                                                                                                                                     0.4s
   => [5/7] RUN /bin/bash -c "apt install make && mkdir build"                                                                                                                                                  1.6s
   => [6/7] WORKDIR /src/build                                                                                                                                                                                  0.0s
   => [7/7] RUN /bin/bash -c "cmake -DCMAKE_PREFIX_PATH=/libtorch .. && make"                                                                                                                                  10.9s
   => exporting to image                                                                                                                                                                                        0.2s
   => => exporting layers                                                                                                                                                                                       0.2s
   => => writing image sha256:dc1f36262ff03bdfc464873f8c5929dd289d8dcd87db32c34a34283f7c650b92                                                                                                                  0.0s
   => => naming to docker.io/library/my-app                                                                                                                                                                     0.0s
  ```

3. Now run it, `docker run -it my-app`. You should see:
  ```
  C:\Users\abhi0\Desktop\libtorch-cpu-docker\example>docker run -it my-app
   1  0  0  0  0  0  0  0  0  0
   0  1  0  0  0  0  0  0  0  0
   0  0  1  0  0  0  0  0  0  0
   0  0  0  1  0  0  0  0  0  0
   0  0  0  0  1  0  0  0  0  0
   0  0  0  0  0  1  0  0  0  0
   0  0  0  0  0  0  1  0  0  0
   0  0  0  0  0  0  0  1  0  0
   0  0  0  0  0  0  0  0  1  0
   0  0  0  0  0  0  0  0  0  1
  [ CPUFloatType{10,10} ]
  ```


### With docker-compose

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

### With `Makefile`

1. Clone the repo: 
  ```
  git clone https://github.com/Abhiswain97/libtorch-cpu-docker.git 
  cd libtorch-cpu-docker
  cd test
  ```

2. Do, `make name=<your-target-name>`
  
    eg: `make name=my-app`

3. If all goes well, then you shoud see:

  ```
  docker build -f Dockerfile -t app .
  [+] Building 3.3s (13/13) FINISHED
  => [internal] load build definition from Dockerfile                                                                                              0.0s 
  => => transferring dockerfile: 32B                                                                                                               0.0s 
  => [internal] load .dockerignore                                                                                                                 0.0s 
  => => transferring context: 2B                                                                                                                   0.0s 
  => [internal] load metadata for docker.io/abhiswain97/libtorch-cpu:latest                                                                        3.1s 
  => [auth] abhiswain97/libtorch-cpu:pull token for registry-1.docker.io                                                                           0.0s 
  => [internal] load build context                                                                                                                 0.0s 
  => => transferring context: 85B                                                                                                                  0.0s 
  => [1/7] FROM docker.io/abhiswain97/libtorch-cpu@sha256:bf7a7e8bbb32f76bc311720f0c4cec93d74469142c7800637161c70169645fd9                         0.0s 
  => CACHED [2/7] COPY ./src /src                                                                                                                  0.0s 
  => CACHED [3/7] WORKDIR /src                                                                                                                     0.0s 
  => CACHED [4/7] RUN /bin/bash -c "python3 create_CMakeLists.py"                                                                                  0.0s 
  => CACHED [5/7] RUN /bin/bash -c "apt install make && mkdir build"                                                                               0.0s 
  => CACHED [6/7] WORKDIR /src/build                                                                                                               0.0s 
  => CACHED [7/7] RUN /bin/bash -c "cmake -DCMAKE_PREFIX_PATH=/libtorch .. && make"                                                                0.0s 
  => exporting to image                                                                                                                            0.1s 
  => => exporting layers                                                                                                                           0.0s 
  => => writing image sha256:e9d05d07009936f76611e624d8edbf6809534ddda2a703cff3f34f5506434cdc                                                      0.0s 
  => => naming to docker.io/library/app                                                                                                            0.0s 
  docker run -it app
  1  0  0  0  0  0  0  0  0  0
  0  1  0  0  0  0  0  0  0  0
  0  0  1  0  0  0  0  0  0  0
  0  0  0  1  0  0  0  0  0  0
  0  0  0  0  1  0  0  0  0  0
  0  0  0  0  0  1  0  0  0  0
  0  0  0  0  0  0  1  0  0  0
  0  0  0  0  0  0  0  1  0  0
  0  0  0  0  0  0  0  0  1  0
  0  0  0  0  0  0  0  0  0  1
  [ CPUFloatType{10,10} ]
  ```

