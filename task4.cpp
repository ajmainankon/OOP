#include <bits/stdc++.h> 
using namespace std; 

class student { 
public: 
	string name;
	int id;
	int marks;

	student(string a, int b,int c) 
	{ 
		name = a;
		id=b;
		marks=c;
	} 
}; 

class sortId { 
public: 

	bool operator()(const student& a, 
					const student& b) 
	{ 

		if (a.id < b.id) { 
			return true; 
		} 
		return false; 
	} 
}; 
class sortMarks { 
public: 

	bool operator()(const student& a, 
					const student& b) 
	{ 

		if (a.marks < b.marks) { 
			return true; 
		} 
		return false; 
	} 
}; 

int main() 
{ 
	student s1("ankon", 3,150); 
	student s2("siam", 4,10); 
	student s3("joly", 1,70); 


	list<student> s; 
	s.push_back(s1); 
	s.push_back(s2); 
	s.push_back(s3); 


	sortId sid;
	sortMarks sm;

	s.sort(sid);

	for (auto stu : s) { 
		cout << stu.name << " "; 
	} 
    s.sort(sm);
    for (auto stu : s) { 
		cout << stu.name << " "; 
	} 
	return 0; 
}