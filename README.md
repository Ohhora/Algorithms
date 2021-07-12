
# Algorithms
------
__Here is my summarization about studing Algorithm theory__</br>

source : Introduction to Algorithms - 3rd Edition(Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein)</br>
![스크린샷 2021-07-12 오후 10 37 06](https://user-images.githubusercontent.com/46857352/125296884-b270c580-e361-11eb-9dc5-fbb9f762b513.png)

I just want to figure out details of algorithms, exactly just summarize, so here is no explanation about specific algorithm.</br>

I'm just beginner and right just a little pseudo-code, if you want more specific code or explanation of algorithm, just read above book :).</br>

----------

## Insertion sort(삽입정렬)
```
for j = 2 to A.length
    key = A[j]
    // Insert A[j] in to the sorted sequence A[1...j-1]
    i = j-1
    while i > 0 and A[i] > key
         A[i+1] = A[i]
         i = i - 1
     A[i+1] = key
```


## Merge sort(병합정렬)

The divide-and-conquer paradigm involves three steps at each level of the recursion:

__Divide__ the problem into a number of subprolems that are smaller instances of the same problem.</br>
__Conquer__ the subproblems by solving them recursively. If the subproblem sizes are small enough, however, just solve the subproblems in a straightforward manner.</br>
__Combine__ the solutions to the subproblems into the solution for the original problem.</br>


The *merge sort* algorithm closely follows the divide-and-conquer paradigm. Intuitively, it operates as follows

__Divide__ : Divide the *n*-element sequence to be sorted into two subsequences of n/2 elements each.</br>
__Conquer__ : Sort the two subsequences recursively using merge sort.</br>
__Combine__ : Merge the two sorted subsequences to produce the sorted answer.</br>

MERGE(A,p,q,r)
```
n1 = q - p + 1
n2 = r - q
let L[1 ... n1 + 1] and R[1 ... n2 + 1] be new arrays
for i = 1 to n1
    L[i] = A[p+i-1]
for j = 1 to n2
    R[j] = A[q+j]
L[n1+1] = inf
R[n2+1] = inf
i = 1
j = 1
for k = p to r
    if L[i] <= R[j]
        A[k] = L[i]
        i = i + 1
    else A[k] = R[j]
        j = j + 1
'''

__최대 부분 배열__
