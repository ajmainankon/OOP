#include<bits/stdc++.h>
using namespace std;

class Cat{
  private:
    string colour,action;
  public:
    Cat(){
      colour="White";
      action="sitting";
    }
    Cat(string col){
      colour=col;
      action="sitting";
    }
    Cat(string col,string act){
      colour=col;
      action=act;
    }
    void printCat(){
      cout<<colour<<" cat is "<<action<<endl;
    }
    void changeColor(string col){
      colour=col;
    }
};

int main() {
    Cat c1;

    Cat c2("Black");

    Cat c3("Brown", "jumping");

    Cat c4("Red", "purring");

    c1.printCat();

    c2.printCat();

    c3.printCat();

    c4.printCat();

    c1.changeColor("Blue");

    c3.changeColor("Purple");

    c1.printCat();

    c3.printCat();

}