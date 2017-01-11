/*
  Data
*/
#include <iostream>
#include <map>
#include <vector>
#include <cmath>
#include <string>
using namespace std;
int main()
{
  map<float, map<string,vector<int> > > my_map;
  my_map[11]["L"].push_back(10000);
  my_map[22]["R"].push_back(40000);
  my_map[4.4]["L"].push_back(40000);
  my_map[22]["L"].push_back(20000);
  for(int i=0; i<my_map[22].size();i++)
  {
    cout<<my_map[22][i]<<endl;
  }
  return 0;
}
