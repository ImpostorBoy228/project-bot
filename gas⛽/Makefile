TARGET := main
SRC := main.S
OBJ := main.o

.PHONY: all clean run

all: $(TARGET)

$(TARGET): $(OBJ)
	ld -o $@ $<

$(OBJ): $(SRC)
	as -o $@ $<

run: $(TARGET)
	./$(TARGET)

clean:
	rm -f $(OBJ) $(TARGET)
