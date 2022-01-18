/* 프로그래머스 > 해시 > 완주하지 못한 선수
*  https://programmers.co.kr/learn/courses/30/lessons/42576
*  
*  
*/ 

#include <string>
#include <vector>
#include <unordered_map>
 
using namespace std;
 
string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    
    unordered_map<string, int> temp;
    for(string name : participant) temp[name]++;
    for(string name : completion) temp[name]--;
    for(auto& p : temp){
        if(p.second > 0){
            answer = p.first;
        }
    }
    
    return answer;
}