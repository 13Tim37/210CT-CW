#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    int ax,ay,bx,by,cx,cy,px,py,right,left,top,bottom;

    cout << "Enter x co-ord for point a: ";
    cin >> ax;
    cout << "Enter y co-ord for point a: ";
    cin >> ay;
    cout << "Enter x co-ord for point b: ";
    cin >> bx;
    cout << "Enter y co-ord for point b: ";
    cin >> by;
    cout << "Enter x co-ord for point c: ";
    cin >> cx;
    cout << "Enter y co-ord for point c: ";
    cin >> cy;
    cout << "Enter x co-ord for point p: ";
    cin >> px;
    cout << "Enter y co-ord for point p: ";
    cin >> py;

    right = ax;
    if (bx >= ax && bx >= cx) {
        right = bx;
    } else if (cx >= bx && cx >= ax) {
        right = cx;
    }

    left = ax;
    if (bx <= ax && bx <= cx) {
        left = bx;
    } else if (cx <= bx && cx <= ax) {
        left = cx;
    }

    top = ay;
    if (by >= ay && by >= cy) {
        top = by;
    } else if (cy >= by && cy >= ay) {
        top = cy;
    }

    bottom = ay;
    if (by <= ay && by <= cy) {
        bottom = by;
    } else if (cy <= by && cy <= ay) {
        bottom = cy;
    }

    string h,v;

    if (px > right) {
        h = "right";
    } else if (px < left) {
        h = "left";
    } else if (px <= right && px >= left) {
        h = "";
    } else {
        h = "";
    }

    if (py > top) {
        v = "top";
    } else if (py < bottom) {
        v = "bottom";
    } else if (py <= top && py >= bottom) {
        v = "";
    } else {
        v = "";
    }

    cout << "The point is " << v << " " << h << " of the triangle";
}
