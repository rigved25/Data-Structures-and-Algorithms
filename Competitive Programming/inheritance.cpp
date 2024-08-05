#include <iostream>
#include <vector>
#include <queue>
#include <thread>
#include <exception>

using namespace std;

template <class T>
class mycontainer {
    T element;
  public:
    mycontainer (T arg) {element=arg;}
    T increase () {return ++element;}
};

// class template specialization:
template <>
class mycontainer <char> {
    char element;
  public:
    mycontainer (char arg) {element=arg;}
    char uppercase ()
    {
      if ((element>='a')&&(element<='z'))
      element+='A'-'a';
      return element;
    }
};


class base{

public:
    int x;
    base(int y){
        cout<<"in Base constructor" << endl;;
        cout<<"X: "<<x << endl;;
        cout<<"Y: "<<y << endl;;
    }
    virtual ~base(){
        cout<<"in Base destructor" << endl;;
    }
    void doit(){
        cout<<"base did it"<< endl;
    }
};

class derived : public base{

public:
    derived(): base(100) {
        cout<<"in derived constructor" << endl;
    }
    virtual ~derived() {
        cout<<"in derived destructor" << endl;
    }
    virtual void doit() const{
        cout<<"derived did it"<< endl;
    }

    derived operator+(derived param){

    }

};

template<class T, int N>
T add(T a, T b){

    return (a+b) + N;

}

int main() {
    cout<<add<double,6>(3.5,2);
    base* b = new derived();
    b->doit();
    delete b;

    string a = "a", c = "c";
    std::cout<<a+c<<endl;

    try
    {
        int* myarray= new int[1000000000];
    }
    catch (exception& e)
    {
        cout << "Standard exception: " << e.what() << endl;
    }


    return 0;
}
