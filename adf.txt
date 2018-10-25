#include <bits/stdc++.h>
#include <iostream>
#include <string.h>
using namespace std;
#define MAX 400
int res[MAX];
int res_size;

void factorial(int n) {
  res[0] = 1;
  res_size = 1;
  for (int x = 2; x <= n; x++) {
    int carry = 0;
    for (int i = 0; i < res_size; i++) {
      int prod = res[i] * x + carry;
      carry = prod / 10;
      res[i] = prod % 10;
    }
    while (carry) {
      res[res_size] = carry % 10;
      carry /= 10;
      res_size++;
    }
  }
  for (int i = res_size - 1; i >= 0; i--)
    cout << res[i];
}
int main() {
  int n;
  cin >> n;
  factorial(n);
}
