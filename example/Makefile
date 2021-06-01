.PHONY = build run 

all: build run

build:
	docker build -f Dockerfile -t ${name} .

run:
	docker run -it ${name}