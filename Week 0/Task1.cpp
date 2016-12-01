#include <iostream>
using namespace std;

int main() {
    float a,b,c,d,x,y;

    cout << "Enter a ";
    cin >> a;
    cout << "Enter b ";
    cin >> b;
    cout << "Enter c ";
    cin >> c;
    cout << "Enter d ";
    cin >> d;

    x = a/b;
    y = c/d;

    if (x >= y) {
        cout << "Highest fraction: " << x;
    } else {
        cout << "Highest fraction: " << y;
    }
}
