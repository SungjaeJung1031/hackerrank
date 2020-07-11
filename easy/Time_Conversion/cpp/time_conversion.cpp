#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the timeConversion function below.
 */
string timeConversion(string s)
{
    /*
     * Write your code here.
     */
    string period_unit = s.substr(8, -1);
    string s_converted = s.substr(0, 8);
    string hh = s_converted.substr(0, 2);

    // https://en.wikipedia.org/wiki/12-hour_clock
    if ((hh.compare("12") != 0) && period_unit.compare("PM") == 0)
    {
        hh = to_string(stoi(s_converted) + 12);
    }
    else if ((hh.compare("12") == 0) && period_unit.compare("AM") == 0)
    {
        hh = "00";
    }

    s_converted = hh + s_converted.substr(2, -1);

    return s_converted;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = timeConversion(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
