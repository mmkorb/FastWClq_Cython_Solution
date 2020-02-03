CC = g++
CFLAGS = --std=c++11 -DNDEBU -O3 --static -g
target = fast-wclq
all : $(target)

$(target) : teste.cpp 
	$(CC) $(CFLAGS) teste.cpp -o $(target)

clean :
	-rm $(target)
