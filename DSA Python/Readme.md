
## Python Concepts for Data Structures and Algorithm
### 1. Array

   a. RAM (Random Access Memory)
   * Ram is Measured in bytes, 1 Byte = 8 bits and bit is a digit 0 or 1, so basically ram help to store the advance data sructure.
   * Integer stores in for of bytes, and 1 integer = 4 Bytes or 32 bits.
   * Ram 2 parts, Values and Address (Bytes). Ex Values: 1, 3, 5 and Its Adress: $0, $4 , $8.
   * Character takes only 1 byte (ASCII Characters).

   b. Arrays and its Properties
   
   **Static Array**
   * Array store in continous store of data
   * 2 parts: Reading(reach there using for loop to index) and Writing(The size to be fixed, and operation is  O(1)). (this can be done easily by Index)
   * Disadvantage of Array(Static Array): . In Static araay you cannot delete the data, can only overwrite the values. *Not observed in python and Java
   * To put the value in middle, you have to move/shift every values in array on different array. (Cannot be done on same array)

   **Dynamic Array**
   * The problme solved here is fixed size and also here pusing, poping and shifiting at the end of the value, all will be O(N)
   * Here to get new array just mutiply it by earlier intizalise a new array.
   * We can deallocate the original array, when modifies the array.
   * Amortise Time Complexity will be O(1).

   * Bit-O-Time of Static and Dynamic is same

   **Stacks**
   * Stack supports 3 operations Pop, Push and Peek/Top (Dynamcic array also have this)
   * Stack is also an array, Stack treats as vertical. (top is end kinda bucket)
   * Pop can happend only at the end (reversed way of pushed, pop goes like)
   * LIFO - Last In First Out DS.

   **Prefix Sums**
   * In prefix, the values on which index we are including, we will consider value of that index + pre sum.
   * Example, to calculate the sum of subarray, Navie way will be O(N). Using Prefix sum, in between values from (n to m) we can get the prefix of (m) - prefix of (n+1) its O(1).
   ![image](https://github.com/vg11072001/Python-programming/assets/67424390/9666304f-a4b7-48b0-a8d6-3ab3a979661c)
 
     
   
### 2. Hash

   **Hash Usage**
   * Hash Map is good with TC of O(1) in Insert, Remove and Search. But the biggest disadvantage is they don't have any order and their ordering on bases of Key TC is O(NlogN).
   * Use case of Hash Map: create dict type data store , then for loop and within it if consition if name is not in then dict. (python doesn't have special Hash thing so use dict) O(N)
   *   
