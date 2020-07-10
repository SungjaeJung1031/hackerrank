#include <bits/stdc++.h>

using namespace std;

// Complete the organizingContainers function below.
string organizingContainers(vector<vector<int>> container)
{
    string res = "Possible";

    int szContainer = container.size();
    vector<int> cnt_type(szContainer, 0.0);
    vector<int> cnt_container(szContainer, 0.0);

    for (int i = 0; i < szContainer; ++i)
    {
        for (int j = 0; j < szContainer; ++j)
        {
            cnt_type[j] += container[i][j];
            cnt_container[i] += container[i][j];
        }
    }

    sort(cnt_type.begin(), cnt_type.end());
    sort(cnt_container.begin(), cnt_container.end());

    for (int i = 0; i < szContainer; ++i)
    {
        if (cnt_type[i] != cnt_container[i])
        {
            res = "Impossible";
            break;
        }
    }

    return res;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int q;
    cin >> q;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int q_itr = 0; q_itr < q; q_itr++)
    {
        int n;
        cin >> n;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        vector<vector<int>> container(n);
        for (int i = 0; i < n; i++)
        {
            container[i].resize(n);

            for (int j = 0; j < n; j++)
            {
                cin >> container[i][j];
            }

            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }

        string result = organizingContainers(container);

        fout << result << "\n";
    }

    fout.close();

    return 0;
}
