/**
 * @file 1.cpp  
 * @author Om Londhe 
 * @brief 
 * @version 0.1
 * @date 2023-04-26
 * 
 * @copyright Copyright (c) 2023
 * 
 */

/**

You are given a, b and c. You need to convert a to b.You can perform following operations:
1. Multiply a by c
2. Decrease a by 2
3. Decrease a by 1
You can perform this operation in any order and any number of times. 
You need to find and print minimum number of steps to convert a to b.

Constraints:
1 ≤ t ≤10^4
0 ≤ a, b, c ≤10^9

Input:
First line contains number of test cases.    Next t line for contains three space separated integer a, b, c.

Output:
Print minimum no. of steps as output in new line for each test case.

SAMPLE INPUT 
2
3 10 2
11 6 2

SAMPLE OUTPUT 
3
3

For test case 1:
1. First multiply 3 with 2.
2. Subtract 1 from  6 to get 5. 
3. Multiple 5 with  2  to get  10.
So, 3 steps.

For test case 2:
1. Subtract 2 from 11.
2. Subtract 2 from 9.
3. Subtract 1 from 7.
So, 3 steps.      

*/

#include <iostream>
#include <queue>
#include <unordered_set>

using namespace std;

int minimumStepsBFS(int a, int b, int c) {
    if (a == b || (a < b && c <= 1)) return 0;
    unordered_set<int> visited{a};
    queue<long long> q;
    q.push(a);

    int count = 0;
    int answer = INT_MAX;
    long long result = 0;
    while (!q.empty()) {
        int n = q.size();
        while (n--) {
            long long current = q.front();
            q.pop();

            result = current * c;
            if (result == b) return min(count + 1, answer);
            if (current < b && !visited.count(result)) { 
                if (result < b) {
                    q.push(result);
                    visited.insert(result); 
                } else answer = min(answer, (int)(count + ((result - b) / 2) + ((result - b) & 1) + 1));
            } 

            long long subtract[2] = { current - 2, current - 1 };
            for (int i = 0; i < 2; i++) {
                result = subtract[i];
                if (result == b) return min(count + 1, answer);
                if (result > 0 && !visited.count(result)) {
                    q.push(result);
                    visited.insert(result); 
                }
            } 
        }
        count++;
    }

    return min(answer, count);
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        int a, b, c;
        cin >> a >> b >> c;

        int result = minimumStepsBFS(a, b, c);
        cout << "Ans: " << result << "\n";
    }

    return 0;
}
