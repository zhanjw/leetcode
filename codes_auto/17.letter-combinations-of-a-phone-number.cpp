//
// @lc app=leetcode.cn id=17 lang=cpp
//
// [17] letter-combinations-of-a-phone-number
//
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> output;
        vector<string> first;
        if (digits.size()>0){
            first=letter(digits[0]);
            for (int i=0;i<digits.size()-1;++i){
                vector<string> temp;
                for (int j=0;j<first.size();++j){
                    vector<string> second=letter(digits[i+1]);
                    for (int k=0;k<second.size();++k){
                        temp.push_back(first[j]+second[k]);
                    }
                }
                first=temp;
            }
            for (int i=0;i<first.size();++i){
                output.push_back(first[i]);
            }
        }
        return output;
    }
private:
    vector<string> letter(char digit){
        string str[]={"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"};
        vector<string> two(str,str+3);
        vector<string> three(str+3,str+6);
        vector<string> four(str+6,str+9);
        vector<string> five(str+9,str+12);
        vector<string> six(str+12,str+15);
        vector<string> seven(str+15,str+19);
        vector<string> eight(str+19,str+22);
        vector<string> nine(str+22,str+26);
        vector<string> none;
        switch(digit){
            case '2':
            return two;
            case '3':
            return three;
            case '4':
            return four;
            case '5':
            return five;
            case '6':
            return six;
            case '7':
            return seven;
            case '8':
            return eight;
            case '9':
            return nine;
            default:
            cout<<digit<<endl;     
            return none;
        }

    }
};
// @lc code=end