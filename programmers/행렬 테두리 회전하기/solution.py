def solution(rows, columns, queries):
    m = [[0 for _ in range(columns+1)] for _ in range(rows+1)]
    cnt = 1
    for i in range(1,rows+1):
        for j in range(1,columns+1):
            m[i][j] = cnt
            cnt += 1
    def find(m, q):
        tmp_list = []
        y1,x1,y2,x2 = q[0],q[1],q[2],q[3]
        list1 = [[y1, i] for i in range(x1,x2+1)]
        list2 = [[i, x2] for i in range(y1+1,y2+1)]
        list3 = [[y2, i] for i in range(x2-1,x1-1,-1)]
        list4 = [[i, x1] for i in range(y2-1,y1,-1)]
        before = list1 + list2 + list3 + list4
        after = list1 + list2 + list3 + list4
        last = after.pop()
        after.insert(0,last)
        new_m = [[m[i][j] for j in range(columns+1)] for i in range(rows+1)]
        for be, af in zip(before, after):
            m[be[0]][be[1]] = new_m[af[0]][af[1]]

        for i in before:
            tmp_list.append(m[i[0]][i[1]])
        tmp_min = min(tmp_list)
        
        return m, tmp_min
    answer_list = []
    for q in queries:
        m, tm = find(m, q)
        answer_list.append(tm)

    return answer_list
