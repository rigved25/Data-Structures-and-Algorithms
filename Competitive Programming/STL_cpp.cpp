#include<bits/stdc++.h>
using namespace std;

void deque_usage(){
    // deque - like vectors but insert and remove from both ends. But, performs bad in insert/ remove from between.
    // dosent store elements contiguously like vectors.
    // Bad - access by incrementing a pointer etc... but can access index directly
    deque<int> first;                                // empty deque of ints
    deque<int> second (4,100);                       // four ints with value 100
    deque<int> third (second.begin(),second.end());  // iterating through second
    deque<int> fourth (third);

    second = first;
    first = deque<int>();

    // the iterator constructor can be used to copy arrays:
    int myints[] = {16,2,77,29};
    deque<int> fifth (myints, myints + sizeof(myints) / sizeof(int));

    cout << "The contents of fifth are:";
    for (deque<int>::iterator it = fifth.begin(); it!=fifth.end(); ++it)
        cout << ' ' << *it;
    cout << '\n';

    fourth.push_front(77);
    fourth.push_back(20);

    fourth.front() -= fourth.back();  //fourth.front() is now 57

    while (!fourth.empty())
    {
        fourth.pop_back();
        fourth.pop_front();
    }

    deque<int>::iterator it = fifth.begin(); // 16,2,77,29
    ++it;

    it = fifth.insert (it,10);                  // 16,10,77,29 "it" now points to the newly inserted 10
    fifth.erase (fifth.begin()+2);              // 16,10,29

}


void priority_queue_MAXHEAP(){

    // priority queue - MAX heap
    // vectors are used internally to implement it
    int myints[]= {10,60,50,20};

    priority_queue<int> first;
    priority_queue<int> second (myints,myints+4);
    priority_queue<int, vector<int>, greater<int>> third (myints,myints+4); // MIN-HEAP

    priority_queue<int> mypq;

    mypq.push(30);
    mypq.push(100);
    mypq.push(25);
    mypq.push(40);

    cout << "Popping out elements...";   // Popping out elements... 100 40 30 25

    while (!mypq.empty())
    {
        cout << ' ' << mypq.top();
        mypq.pop();
    }

}

void queue_usage(){

    // queue
    // internally deque is used. list can also be used.
    deque<int> mydeck (3,100);        // deque with 3 elements
    list<int> mylist (2,200);         // list with 2 elements

    queue<int> first;                 // empty queue
    queue<int> second (mydeck);       // queue initialized to copy of deque

    queue<int, list<int>> third; // empty queue with list as underlying container
    queue<int, list<int>> fourth (mylist);

    queue<int> myqueue;
    myqueue.push(77);
    myqueue.push(16);

    myqueue.front() -= myqueue.back();    // 77-16=61

    cout << "myqueue contains: ";           // 61, 16
    while (!myqueue.empty())
    {
        cout << ' ' << myqueue.front();
        myqueue.pop();
    }
}

void stack_usage(){
    // stack
    // vectors, deque, list can be used for implementation. deque is used by default.
    deque<int> mydeque (3,100);          // deque with 3 elements
    vector<int> myvector (2,200);        // vector with 2 elements

    stack<int> first;                    // empty stack
    stack<int> second (mydeque);         // stack initialized to copy of deque

    stack<int, vector<int>> third;  // empty stack using vector
    stack<int, vector<int>> fourth (myvector);

    stack<int> mystack;

    for (int i=0; i<5; ++i) mystack.push(i);

    cout << "Popping out elements...";       // Popping out elements... 4 3 2 1 0
    while (!mystack.empty())
    {
        cout << ' ' << mystack.top();
        mystack.pop();
    }
}

void set_usage() {

    // set - implemented as binary search trees
    // cant modify any value, CAN remove or insert only
    // In sets - value (only unique) is itself the key for ordering

    // multiset - same like set but
    // in multiset the duplicate values can be inserted. ERASE removes all the elements with the key provided
    // lower_bound(x) returns (<=x) and upper_bound(x) returns (>x) make more sense in multisets

    set<int> first;                           // empty set of ints

    int myints[]= {10,20,30,40,50};
    set<int> second (myints,myints+5);        // range
    set<int> third (second);                  // a copy of second

    set<int> fourth (second.begin(), second.end());  // iterator ctor.

    set<int> myset;
    set<int>::iterator it;

    // set some initial values:
    for (int i=1; i<10; i++) myset.insert(i*10); // 10 20 30 40 50 60 70 80 90

    it=myset.find(20);    // finds the iterator if it exists or return set::end()
    myset.erase (it);
    myset.erase (myset.find(40));
                                                 // 10 20 30 40 50 60 70 80 90
    itlow=myset.lower_bound (30);                //       ^
    itup=myset.upper_bound (60);                 //                   ^

    cout << "myset contains:";
    for (it=myset.begin(); it!=myset.end(); ++it)
        cout << ' ' << *it;
    cout << '\n';
}

void unordered_set_usage() {
    // unordered_set, unordered_multiset - Hash tables - NO ORDERING (not sorted)
    // only stores unique values, CANT modify, CAN insert, erase
    // can iterate but it is not sorted
    unordered_set<string> first;                                // empty
    unordered_set<string> second ( {"red","green","blue"} );    // init list
    unordered_set<string> third ( {"orange","pink","yellow"} ); // init list
    unordered_set<string> fourth ( second );                    // copy
    unordered_set<string> sixth ( third.begin(), third.end() ); // range

    unordered_set<string> myset =
    {"USA","Canada","France","UK","Japan","Germany","Italy"};

    myset.erase ( myset.begin() );                    // erasing by iterator
    myset.erase ( "France" );                         // erasing by key
    myset.erase ( myset.find("Japan"), myset.end() ); // erasing by range -- But you dont know in which order it will erase

    unordered_set<string>::const_iterator got = myset.find("Germany");

    string mystring = "red";

    myset.insert (mystring);                        // copy insertion
    myset.insert (mystring+"dish");                 // move insertion
    myset.insert (myarray.begin(), myarray.end());  // range insertion
    myset.insert ( {"purple","orange"} );           // initializer list insertion

    for (const string& x: myset) cout << " " << x;
}

void map_usage() {
    // map, multimap
    map<char,int> first;

    first['a']=10;
    first['b']=30;
    first['c']=50;
    first['d']=70;

    map<char,int> second (first.begin(),first.end());

    map<char,int> third (second);

    map<char,int> mymap;
    map<char,int>::iterator itlow,itup;

    mymap['a']=20;
    mymap['b']=40;
    mymap['c']=60;
    mymap['d']=80;
    mymap['e']=100;

    itlow=mymap.lower_bound ('b');  // itlow points to b
    itup=mymap.upper_bound ('d');   // itup points to e (not d!)

    mymap.erase(itlow,itup);        // erases [itlow,itup)

    // print content:
    for (map<char,int>::iterator it=mymap.begin(); it!=mymap.end(); ++it)
        cout << it->first << " => " << it->second << '\n';

    map<char,string> mymap;

    mymap['a']="an element";
    mymap['b']="another element";
    mymap['c']=mymap['b'];

    cout << "mymap['a'] is " << mymap['a'] << '\n';     //mymap['a'] is an element
    cout << "mymap['b'] is " << mymap['b'] << '\n';     //mymap['b'] is another element
    cout << "mymap['c'] is " << mymap['c'] << '\n';     //mymap['c'] is another element
    cout << "mymap['d'] is " << mymap['d'] << '\n';     //mymap['d'] is (nothing because string::empty is default which is added)
    cout << "mymap now contains " << mymap.size() << " elements.\n";  //mymap now contains 4 elements.

    map<char,int>::iterator it;

    it = mymap.find('b');
    if (it != mymap.end())
        mymap.erase (it);

    // MULTIMAP
    multimap<char,int> mymultimap;

    // insert some values:
    mymultimap.insert(pair<char,int>('a',10));
    mymultimap.insert(pair<char,int>('b',20));
    mymultimap.insert(pair<char,int>('b',30));
    mymultimap.insert(pair<char,int>('c',40));
    mymultimap.insert(pair<char,int>('d',50));
    mymultimap.insert(pair<char,int>('d',60));
    mymultimap.insert(pair<char,int>('e',70));
    mymultimap.insert(pair<char,int>('f',80));

    multimap<char,int>::iterator it = mymultimap.find('b');

    mymultimap.erase (it);                     // erasing by iterator (1 element)

    mymultimap.erase ('d');                    // erasing by key (2 elements)

    it=mymultimap.find ('e');
    mymultimap.erase ( it, mymultimap.end() ); // erasing by range

    // show content:
    for (it=mymultimap.begin(); it!=mymultimap.end(); ++it)
        cout << (*it).first << " => " << (*it).second << '\n';


}

struct TreeNode{
    int val;
    TreeNode *left, *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}

};

struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
};

int main() {

    // for every DS, there are these things that we need

    // Create, Insert, Update, Deletion, Search
    // These requires DSes to give us these functionalities
    // 1. insert, erase - at its ends, inbetween
    // 2. access - Update
    // 3. find, lower_bound, upper_bound - Search




    // unordered_map, unordered_multimap
    typedef unordered_map<string,string> stringmap;

    stringmap first;                              // empty
    stringmap second ( {{"apple","red"},{"lemon","yellow"}} );       // init list
    stringmap third ( {{"orange","orange"},{"strawberry","red"}} );  // init list
    stringmap fourth (second);                    // copy
    stringmap fifth (merge(third,fourth));        // move
    stringmap sixth (fifth.begin(),fifth.end());  // range

    cout << "sixth contains:";
    for (auto& x: sixth) cout << " " << x.first << ":" << x.second; // sixth contains: apple:red lemon:yellow orange:orange strawberry:red

    stringmap mymap;

    // populating container:
    mymap["U.S."] = "Washington";
    mymap["U.K."] = "London";
    mymap["France"] = "Paris";
    mymap["Russia"] = "Moscow";
    mymap["China"] = "Beijing";
    mymap["Germany"] = "Berlin";
    mymap["Japan"] = "Tokyo";

    // erase examples:
    mymap.erase ( mymap.begin() );      // erasing by iterator
    mymap.erase ("France");             // erasing by key
    mymap.erase ( mymap.find("China"), mymap.end() ); // erasing by range

    // show content:
    for ( auto& x: mymap )
        cout << x.first << ": " << x.second << endl;


    // list - doubly linked list, forward_list - singly linked list
}
