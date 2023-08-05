import sys

class Main:
    def __init__(self):
        self.br = sys.stdin
        self.sb = []

    def main(self):
        self.solution()

    def solution(self):
        n = int(self.br.readline())
        while n > 0:
            self.sb.append(
                " @@@   @@@ \n" +
                "@   @ @   @\n" +
                "@    @    @\n" +
                "@         @\n" +
                " @       @ \n" +
                "  @     @  \n" +
                "   @   @   \n" +
                "    @ @    \n" +
                "     @     \n"
            )
            n -= 1
        sys.stdout.write(''.join(self.sb))

if __name__ == "__main__":
    Main().main()
