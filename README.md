
# Algorithms
------
__Here is my summarization about studing Algorithm theory__</br>

source : Introduction to Algorithms - 3rd Edition(Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein)</br>
![스크린샷 2021-07-12 오후 10 37 06](https://user-images.githubusercontent.com/46857352/125296884-b270c580-e361-11eb-9dc5-fbb9f762b513.png)

I just want to figure out details of algorithms, exactly just summarize, so here is no explanation about specific algorithm.</br>

I'm just beginner and right just a little pseudo-code, if you want more specific code or explanation of algorithm, just read above book :).</br>

----------

## Insertion sort
```python
`for j = 2 to A.length`
    `key = A[j]`
     // Insert `A[j]` in to the sorted sequence `A[1...j-1]`
     `i = j-1`
     `while i > 0 and A[i] > key`
         `A[i+1] = A[i]`
         `i = i - 1`
     `A[i+1] = key
```
