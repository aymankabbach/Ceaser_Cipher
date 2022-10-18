#include <iostream>
#include <cmath>
using namespace std;

char alphabet[26]= {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
string originalWord;
int shift;
int sizeofWord;
string readWord()
{ 
    cout<<"enter your word\n";
    getline(cin,originalWord);
    ::sizeofWord=originalWord.size();
    cout<<"type the shift number\n";
    cin>>shift;
}
int find_element(char letter)
{
    int position=0;
    for (char element : alphabet)
        if (element==letter)
            return position;
        else
            position=position+1;
    return position;
}
string codingTheWord()
{ 
    readWord();
    int sizeofList=26;
    int p=0;
    for (char letter : originalWord)
    { 
        
        int position=find_element(letter);
        originalWord[p]= (position==sizeofList) ? letter : ((position+shift>=sizeofList) ? originalWord[p]=alphabet[position-sizeofList+shift]: originalWord[p]=alphabet[position+shift]);
        p=p+1;
    }
    return originalWord;
}
void PrintWord()
{ 
    string codedWord=codingTheWord();
    cout<<originalWord<<endl;
}
int main()
{ 
    PrintWord();
    system("pause");
    return 0;
}
