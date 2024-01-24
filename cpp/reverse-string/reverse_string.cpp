#include "reverse_string.h"

using namespace std;

namespace reverse_string {

  string reverse_string(string word)
  {
    string reverse;
    for (int i = word.length() - 1; i > -1; i--)
    {
      reverse += word[i];
    }

    return reverse;
  }

}  // namespace reverse_string
