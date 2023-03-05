#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>

using namespace std;

const int dx[] = {-1, -1, 0, 0,  1, 1, -1, 1}; // delta x for 8 directions
const int dy[] = {0,   1, -1,  1,  0,  1, -1, -1}; // delta y for 8 directions

int n, m; // dimensions of the labyrinth
vector<vector<char>> lab; // 2D vector to store the labyrinth
vector<vector<int>> visited; // 2D vector to mark visited cells
vector<vector<int>> visited_max_path; // var for storing path corresponding to max length
int max_path_length = -1; // the length of the longest path
bool is_longer_path = false;

bool is_valid_neighbour(int nx, int ny){
    return nx >= 0 && nx < n && ny >= 0 && ny < m && lab[nx][ny] == '.' && visited[nx][ny] == -1;
}

void dfs(int x, int y, int cur_path_length) {
    visited[x][y] = cur_path_length; // mark the current cell as visited

    // check if we have reached the bottom
    if (x == n - 1) {
        //check if any neigbouring cell is unvisited
        if(is_valid_neighbour(x, y-1))
            dfs(x, y-1, cur_path_length + 1);
        else if(is_valid_neighbour(x, y+1))
            dfs(x, y+1, cur_path_length + 1);
        else{
            if (cur_path_length > max_path_length){
                // cout << " MAX CONDITION: cur_path_length " << cur_path_length << " max path length " << max_path_length << endl; 
                max_path_length = cur_path_length;
                is_longer_path = true;
            }
        }
        return;
    }

    // recursively explore the neighboring cells
    for (int i = 0; i < 8; ++i) {
        int nx = x + dx[i], ny = y + dy[i];
        if (nx < 0 || nx >= n || ny < 0 || ny >= m || lab[nx][ny] == '#' || visited[nx][ny] != -1) {
            continue; // skip if out of bounds, or wall, or already visited
        }
        dfs(nx, ny, cur_path_length + 1); // recursively explore
    }
}

void print_labyrinth() {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (lab[i][j] == '.') {
                if (visited_max_path[i][j] == -1) {
                    cout << '.'; // unvisited cell
                } else {
                    cout << visited_max_path[i][j]; // visited cell, print its order
                }
            } else {
                cout << lab[i][j]; // wall
            }
        }
        if (i != n - 1) {
            cout << endl;
        }
    }
}

int main() {

    // Read the file and count rows and columns
    string file_name = "input_3.txt";
    ifstream inputfile;
    string line;
    inputfile.open(file_name);

    while (std::getline(inputfile, line))
        ++n;
    // cout << "Number of lines in text file: " << n << "\n";

    stringstream s;
    s << line;// put the line into the stringstream
    m = s.str().length();
    // cout << "Number of columns in text file: " << m << endl;


    // Initialize arrays
    lab.resize(n, vector<char>(m));
    visited.resize(n, vector<int>(m, -1));
    visited_max_path.resize(n, vector<int>(m, -1));

    inputfile.close();
    inputfile.open(file_name);

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(inputfile.eof())          
                break;
            char data;
            inputfile >> data;
            lab[i][j] = data;
            // cout << lab[i][j];
        }
        // cout << "\n";
    }


    // perform DFS from each cell in the top row
    for (int j = 0; j < m; ++j) {
        if (lab[0][j] == '.') {
            
            // reset the visited array and longer path variable
            visited.assign(n, vector<int>(m, -1));
            is_longer_path = false;

            dfs(0, j, 0);
            if (is_longer_path){
                visited_max_path.assign(n, vector<int>(m, -1));
                visited_max_path = visited;
            }
        }
    }

    if (max_path_length == -1) {
        cout << -1 << endl; // no path to the bottom was found
    } else {
        cout << max_path_length + 1 << endl; // print the length of the
    }

    print_labyrinth(); // print the labyrinth with the path
}