#include <fstream>
#include <vector>
using namespace std;

int part1(ifstream &infile) {
  int sum = 0;
  string line;
  while (getline(infile, line)) {
    auto it = line.find_first_of("0123456789");
    int num1 = line[it] - '0';
    it = line.find_last_of("0123456789");
    int num2 = line[it] - '0';
    sum += num1 * 10 + num2;
  }
  return sum;
}

int findFirstNumber(const string &line, const vector<string> &lines) {
  size_t firstPos = string::npos;
  int firstNum = -1;

  for (int i = 0; i < lines.size(); i++) {
    size_t pos = line.find(lines[i]);
    if (pos != string::npos && (firstPos == string::npos || pos < firstPos)) {
      firstPos = pos;
      firstNum = i + 1;
    }
  }

  size_t digitPos = line.find_first_of("0123456789");
  if (digitPos != string::npos &&
      (firstPos == string::npos || digitPos < firstPos)) {
    return line[digitPos] - '0';
  }
  return firstNum;
}

int findLastNumber(const string &line, const vector<string> &lines) {
  size_t lastPos = string::npos;
  int lastNum = -1;

  for (int i = 0; i < lines.size(); i++) {
    size_t pos = line.rfind(lines[i]);
    if (pos != string::npos && (lastPos == string::npos || pos > lastPos)) {
      lastPos = pos;
      lastNum = i + 1;
    }
  }

  size_t digitPos = line.find_last_of("0123456789");
  if (digitPos != string::npos &&
      (lastPos == string::npos || digitPos > lastPos)) {
    return line[digitPos] - '0';
  }
  return lastNum;
}

int part2(ifstream &infile) {
  vector<string> lines = {"one", "two",   "three", "four", "five",
                          "six", "seven", "eight", "nine"};
  int sum = 0;
  string line;
  while (getline(infile, line)) {
    int num1 = findFirstNumber(line, lines);
    int num2 = findLastNumber(line, lines);

    if (num1 != -1 && num2 != -1) {
      sum += num1 * 10 + num2;
    }
  }
  return sum;
}
int main() {
  ifstream infile("input");
  printf("Part 1: %d\n", part1(infile));
  infile = ifstream("input");
  printf("Part 2: %d\n", part2(infile));
}
