# 드디어 내 힘으로 푼 첫 그리디 알고리즘 문제이다.
# 구현 과정이 복잡했지만, 가장 먼 도서부터 처리하는 로직으로 그리디하게 풀어냈다.

n, m = map(int,input().split())
book = list(map(int,input().split()))

book_minus = []
book_plus = []

for b in book:
    if(b<0):
        book_minus.append(abs(b))
    else:
        book_plus.append(b)

book_minus.sort()
book_plus.sort()

answer = 0

if(book_minus and book_plus):
    if(book_minus[-1] > book_plus[-1]):
        answer += book_minus[-1]
        for i in range(m):
            if(book_minus):
                book_minus.pop()
    else:
        answer += book_plus[-1]
        for i in range(m):
            if(book_plus):
                book_plus.pop()

    
    while book_minus or book_plus:

        if(book_minus and book_plus):
            if(book_minus[-1] > book_plus[-1]):
                answer += (book_minus[-1] * 2)
                for i in range(m):
                    if(book_minus):
                        book_minus.pop()
            else:
                answer += (book_plus[-1] * 2)
                for i in range(m):
                    if(book_plus):
                        book_plus.pop()

        elif(book_minus and not book_plus):
            answer += (book_minus[-1] * 2)
            for i in range(m):
                if(book_minus):
                    book_minus.pop()
            
        elif(book_plus and not book_minus):
            answer += (book_plus[-1] * 2)
            for i in range(m):
                if(book_plus):
                    book_plus.pop()


elif(book_minus and not book_plus):
    answer += book_minus[-1]
    for i in range(m):
        if(book_minus):
            book_minus.pop()
    
    while book_minus:
        answer += (book_minus[-1] * 2)
        for i in range(m):
            if(book_minus):
                book_minus.pop()
    
elif(book_plus and not book_minus):
    answer += book_plus[-1]
    for i in range(m):
        if(book_plus):
            book_plus.pop()
    
    while book_plus:
        answer += (book_plus[-1] * 2)
        for i in range(m):
            if(book_plus):
                book_plus.pop()


print(answer)