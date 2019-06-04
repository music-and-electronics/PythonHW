# A00.The Python Interpreter
a = 5 #변수 a에 5를 대입
print(a) #변수 a에 저장한 값을  출력 

print('Hello world') #문자열 hello world를 출

# B00.The Basics. Variables and pass-by-reference
a = [1, 2, 3] #배열 a에 1,2,3을 대입
b = a #배열 a를 b에 대입 

print(b) #배열 b의 값들을 출력

a.append(4) #배열 a에 값 4를 추가
print(b) #a를 b에 대입하였으므로, 수정된 배열b 를 출력

def append_element(some_list, element) :#함수 append_element를 정의 (매개변수는 some_list와 element)
    some_list.append(element) #some_list에 element를 추가

data = [1, 2, 3] #배열 data를 선언 값 1,2,3을 배열에 저장
append_element(data, 4) #append_element 함수에 배열 data와 값 4를 전달 따라서 data에는 4가 추가된다.

print(data)#배열 data를 출력 

# B01.The Basics. Dynamic refefrences, strong types
a = 5 #변수 a를 선언, 5를 대입
print(type(a))#변수 a에 저장된 값의 형식을 반환하여 출력

b = 'foo'#변수 b를 선언, 'foo'를 대입
print(type(b))#변수 b에 저장된 값의 형식을 반환하여 출력

# '5' + 5

a = 4.5 #변수 a에 4.5 대입
b = 2 #변수 b에 2대입 

print('a is %s, b is %s' % (type(a), type(b))) #a와 b의 형식을 각각 반환하여 출력

print(a/b) #서로 다른 형식을 가진 변수 a와 b를 나눗셈 연산하여 결과 출력

a = 5 #변수 a에 5대입
print(isinstance(a, int)) #변수 a가 int 형식이 맞다면 true 출력

a = 5 ; b = 4.5 #변수 a에 5, 변수 b에 4.5대입
print(isinstance(a, (int, float))) #변수 a가 int 형식 or float 형식이면 true 출력
print(isinstance(b, (int, float))) #변수 b가 int 형식 or float 형식이면 true 출력

# B02.The Basics. Duck typing
def isiterable(obj): #함수 isiterable을 매개 변수 obj와 함께 선언
    try:
        iter(obj) #iter함수에 obj 대입
        return True #obj가 iterable하다면 True 반환 
    except TypeError: # not interable 하다면
        return False # False  반환


print(isiterable([1, 2, 3])) #isiterable 함수에 배열 [1,2,3] 대입 => 배열이므로  iterable 함 따라서 true 반환 
print(isiterable(5)) #isiterable 함수에 변수 5 대입 => 변수 하나 이므로, not iterable 함 따라서 false 반환

# B03.The Basics. Imports
import some_module #some_module.py를 import

result = some_module.f(5) #result에 some_module에 선언 되어있는 함수 f에 5를 대입
print(result) #result값 출력
pi = some_module.PI #pi에 some_module에 선언 되어있는 변수 PI를 대입
print(pi) #pi값 출력 

from some_module import f, g, PI #some module 모듈로 부터 f,g, PI를 불러옴
result = g(5, PI) #result에 함수 g에 5와 PI를 대입한 결과 값을 대입
print(result) #result 값 출력

import some_module as sm #module some_module을 sm이라는 이름으로 선언
from some_module import PI as pi, g as gf #some_module의 변수 PI를 pi로, 함수 g를 gf로 선언

r1 = sm.f(pi) #바뀐 이름 sm을 가진 모듈 sm의 함수 f에 pi 값 대입
print(r1) #r1 출력
r2 = gf(6, pi) #함수 gf에 매개변수로 6과 pi 대입
print(r2) #r2 출력


# B04.The Basics. Binary operators and comparisons

print(5-7) #5-7 출력
print(12 + 21.5) #12+21.5 출력
print(5 <= 2) #5가 2보다 작거나 같은지  bool로 출력

a = [1, 2, 3] #배열 a를 선언하여 1,2,3대입
b = a #b에 a를 대입
c = list(a) #c를 리스트로 선언 하여 a의 값들을 대입
print(a is b) #a가 b와 형식이 동일 한지 출력
print(a is not c) #a가 c와 형식이 동일하지 않은지 출력

print(a == c) #a 와 c가 가진 값들이 동일한지 출력

a = None #a에 None을 대입

print(a is None) #a가 None이면 True를 출력


# B05.The Basics. Strictness versus laziness

a = b = c = 5 #a,b,c,에 5를 대입
print('a=', a, ', b=', b, ', c=', c) #a=5 b=5 c=5를 출력
d = a + b + c #d에 a+b+c 값을 대입
print('d=', d) #d=15를 출력

# B06.The Basics. Mutable and immutable objects
a_list = ['foo', 2, [4, 5]] #a_list에 문자열 'foo' ,int 값 2, 배열 [4,5]를 대입
print(a_list) #a_list를 출력

a_list[2] = (3, 4) #배열의 2번 인덱스에 (3,4)를 [4,5]를 삭제하고 추가
print(a_list) #a_list를 출력

a_tuple = (3, 5, (4, 5)) #a_tuple에 3,5,(4,5)를 추가
#a_tuple[1] = 'four' #1번 인덱스에 문자열을 대입하여 에러 발생 

# C00.Scalar Types. Numeric types
ival = 17239871 #ival에 17239871대입
print('ival = ', ival ** 6) #17239871의 6제곱을 출력, 형식에 맞지않아 자동적으로 long으로 형변환 되었다.

fval = 7.243 #fval에 float 타입 숫자 7.243대입
print('fval=', fval) #fval 출력
fval2 = 6.78e-5 #fval2에 scientific notation 표현 6.78e-5대입
print('fval2=', fval2) #fval2 출력 

print('3/2 = ', 3/2) #3/2 값 출력, 파이썬은 항상 정수계열 나눗셈에 대해 부동 소숫점으로 출력 

print('3/float(2) =', 3/float(2)) #정수형 숫자 3을 부동소숫점 숫자 2로 나눈값을 출력

print('3//2 = ', 3//2) #정수형 나눗셈을 부동소숫점으로 출력하지 않고 정수형으로 출력 따라서 1출력

cval = 1 + 2j #변수 cval에 복소수 1+2j 대입 
print('cval * (1 -2j) = ', cval * (1 -2j)) #켤레 복소수를 곱한 결과값 출력

# C01.Scalar Types. Strings
a = 'one way of writing a string' #변수 a에 문자열 'one way of writing a string' 대입
b = "another way"  #변수 b에 문자열 "another way" 대입
c = """
    This is a longer string that
    spans multiple lines
    """ #변수 c에 여러줄의 문자열  """This is a longer string that spans multiple lines """을 집어 넣음
print('a = ', a) #a 출력
print('b = ', b) #b 출력
print('c = ', c) #c 출력

# a[10] = 'f' #문자열을 대입했으므로 하나의 char형 f를 10번째 인덱스에 추가할 수 없다.

b = a.replace('string', 'longer string') #변수b를 a의 문자열중 'string' 문자열을 'longer string'으로 바꿔서 대입  
print('b = ', b) #변수 b 출력

a = 5.6 #변수 a에 5.6 대입
s = str(a) #변수s 를 변수 a를 string 형식으로 변환하여 대입
print('s = ', s) #변수 s 출력

s = 'python' #변수 s에 문자열 python을 대입
list(s) #s를 list로써 각각 문자를 쪼갬
print('s[:3] = ', s[:3]) #s가 list이므로 3번 인덱스까지 출력

s = '12\\34'  #12 와34 를 구분하기 위해 escape character \\를 집어넣음
print('s = ', s) #변수 s를 출력

s = r'this\has\no\special\characters' #앞에 r을 붙여줌으로써 출력 할때 백슬래시가 2개 되게 해줌
print('s = ', s) #변수 s를 출력

a = 'this is the first half ' #변수 a에 문자열 'this is the first half ' 대입
b = 'and this is the second half'#변수 b에 문자열 'and this is the second half' 대입
print('a + b = ', a + b) #문자열 a와 b를 합쳐 출력

template = '%.2f %s are worth $%d' #변수 template에 문자열을 변수에 대한 각각 형식을 지정하여 선언

print(template % (4.5560, 'Argentine Pesos', 1)) #template 문자열에 4.5560, 'Argentine Pesos', 1를 순서대로 대입하여 출력

# C02.Scalar Types. Booleans
print('True and True = ', True and True) #True이고 True이면 True 출력
print('False or Flase = ', False or False) #False 또는 False 이면 False 출력

print('bool([]) = ', bool([])) #bool 함수 안의 배열이 비어있으므로 false를 출력
print('bool([1, 2, 3]) = ', bool([1, 2, 3]))#bool 함수 안의 배열이 비어있지 않으므로 true를 출력
print('bool(''Hello world!'') = ', bool('Hello world!'))#bool 함수 안의 문자열 값이 비어있지 않으므로 true를 출력
print('bool('') = ', bool(''))
print('bool(0) = ', bool(0))
print('bool(1) = ', bool(1))

# C03.Scalar Types. Type casting

s = '3.14159'
print('type(s): ', type(s))
fval = float(s)
print('type(fval): ', type(fval))
print('int(fval) = ', int(fval))
print('bool(fval) = ', bool(fval))
print('bool(0) = ', bool(0))

# C04.Scalar Types. None
a = None
print('a is None: ', a is None)
b = 5
print('b is not None: ', b is not None)

def add_and_maybe_multiply(a, b, c=None):
    result = a + b
    if c is not None:
        result = result * c
    return result
print('Only add:', add_and_maybe_multiply(2, 3))
print('Add and multiply: ', add_and_maybe_multiply(2, 3, 2))

# C05.Scalar Types. Dates and times
from datetime import datetime, date, time
dt = datetime(2019, 5, 21, 16, 42, 11)

print('Day: ', dt.day, ', Mimute: ', dt.minute)
print('Date: ', dt.date())
print('Time: ', dt.time())

print('MM/DD/YYYY HH:MM: ', dt.strftime('%m/%d/%Y %H:%M'))
print('String to Time: ', dt.strptime('20191031', '%Y%m%d'))


dt = datetime(2019, 5, 21, 16, 42, 11)
print('current datetime: ', dt)
print('modified datetime: ', dt.replace(minute=0, second=0))

dt2 = datetime(2011, 11, 15, 22, 30)
delta = dt - dt2
print('delta = ', delta)
print('Type of delta: ', type(delta))

print('dt: ', dt2)
print('dt+delta: ', dt2+delta)

# D00. Control Flow. if, elif, and else
x = -1

if x < 0:
    print('It''s negative')
elif x == 0:
    print('Equal to zero')
elif 0 < x < 5:
    print('Positive but samller than 5')
else:
    print('Positive and larger than or equal 5')

x = 0

if x < 0:
    print('It''s negative')
elif x == 0:
    print('Equal to zero')
elif 0 < x < 5:
    print('Positive but samller than 5')
else:
    print('Positive and larger than or equal 5')

x = 3

if x < 0:
    print('It''s negative')
elif x == 0:
    print('Equal to zero')
elif 0 < x < 5:
    print('Positive but samller than 5')
else:
    print('Positive and larger than or equal 5')

x = 12

if x < 0:
    print('It''s negative')
elif x == 0:
    print('Equal to zero')
elif 0 < x < 5:
    print('Positive but samller than 5')
else:
    print('Positive and larger than or equal 5')

# D01. Control Flow. for loops
sequence = [1, 2, None, 4, None, 5]
total = 0

for value in sequence:
    if value is None:
        continue
    total += value
print('total: ', total)

sequence = [1, 2, 0, 4, 6, 5, 2, 1]
total_until_5 = 0
for value in sequence:
    if value == 5 :
        break
    total_until_5 += value
print('total_until_5: ', total_until_5)

# D02. Control Flow. while loops

x = 256
total = 0
while x>0:
    if total > 500:
        break
    total += x
    x = x // 2
    print('x=', x)
print('total: ', total)

# D03. Control Flow. pass

x = -1

if x < 0:
    print('negative')
elif x == 0:
    pass
else:
    print('positive')

x = 0

if x < 0:
    print('negative')
elif x == 0:
    pass
else:
    print('positive')

# D04. Control Flow. range and xrange

print('range(10): ', list(range(10)))
print('range(0, 20, 2): ', list(range(0, 20, 2)))

seq = [1, 2, 3, 4]
for i in range(len(seq)):
    val = seq[i]
    print('val: ', val)

# Python 3.x에서는 xrange( ) 함수가 별도로 제공되지 않으며, 주요 기능은 range( )에 통합

# D05. Control Flow. Ternary Expression
x = 5
'Non-negative' if x >= 0 else 'Negative' # IDLE Shell에서 직접 실행하세요.

# E00. Data Structures and Sequences. Tuple
tup = 4, 5, 6
print('tup: ', tup)

nested_tup = (4, 5, 6), (7, 8)
print('nested_tup: ', nested_tup)

print('tuple([4, 0, 2]): ', tuple([4, 0, 2]))

tup = tuple('string')
print('tuple(''string'')', tup)
print('tup[0]: ', tup[0])

tup = tuple(['foo', [1, 2], True])
# tup[2] = False

tup[1].append(3)
print('appended tup: ', tup)

long_tup = (4, None, 'foo') + (6, 0) + ('bar', )
print('long tup: ', long_tup)

print('(''foo', 'bar''*4: ', ('foo', 'bar')*4)

# E01. Data Structures and Sequences. Unpacking tuples

tup = (4, 5, 6)
a, b, c = tup
print('b: ', b)

tup = 4, 5, (6, 7)
a, b, (c, d) = tup
print('d: ', d)

tmp = a
print('tmp: ', tmp)
a = b
print('a: ', a)
b = tmp
print('b: ', b)
b, a = a, b
print('a, b: ', a, ', ', b)

seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
print('a, b, c: ', a, b, c)
for a, b, c in seq:
    print('loop using variabel unpacking')
    pass

# E02. Data Structures and Sequences. Tuple methods
a = (1, 2, 2, 2, 3, 4, 2)
print('The number of 2 of the tuple a: ', a.count(2))

# F00. List. Adding and removing elements
a_list = [2, 3, 7, None]
tup = ('foo', 'bar', 'baz')

b_list = list(tup)
print('b_list: ', b_list)

b_list[1] = 'peekaboo'
print('b_list: ', b_list)

b_list.append('dwarf')
print('b_list: ', b_list)

b_list.insert(1, 'red')
print('b_list: ', b_list)

b_list.pop(2)
print('b_list: ', b_list)

b_list.append('foo')
print('b_list: ', b_list)

b_list.remove('foo')
print('b_list: ', b_list)

print('''dwarf' in b_list: ''', 'dwarf' in b_list)

# F01. List. Concatenating and combining lists
lst = [4, None, 'foo'] + [7, 8, (2, 3)]
print('concatenated list: ', lst)

x = [4, None, 'foo']
print('x: ', x)
x.extend([7, 8, (2, 3)])
print('x: ', x)

# F02. List. Sorting
a = [7, 2, 5, 1, 3]
print('a: ', a)
a.sort()
print('sorted a: ', a)

b = ['saw', 'small', 'He', 'foxes', 'six']
print('b: ', b)
b.sort(key=len)
print('sorted b: ', b)

# F03. List. Binary search and maintaining a sorted list

import bisect
c = [1, 2, 2, 2, 3, 4, 7]

print(bisect.bisect(c, 2))
print(bisect.bisect(c, 5))
print(bisect.insort(c, 6))

print('c: ', c)

# F03. List. Slicing
seq = [7, 2, 3, 7, 5, 6, 0, 1]
print('seq: ', seq)
print('seq[1:5]: ', seq[1:5])

seq[3:4] = [6, 3]
print('seq: ', seq)

print('seq[:5]: ', seq[:5])
print('seq[3:] ', seq[3:])
print('seq[-4:]: ', seq[-4:])
print('seq[-6:-2]: ', seq[-6:-2])

print('seq[::2]: ', seq[::2])
print('seq[::-1]: ', seq[::-1])

# G00. Built-in Sequence Functions. enumerate, sorted, zip, and reversed

# enumerate
some_list = ['foo', 'bar', 'baz']
mapping = dict((v, i) for i, v in enumerate(some_list))

print('mapping: ', mapping)

# sorted
print('sorted seq.: ', sorted([7, 1, 2, 6, 0, 3, 2]))
print('sorted str.: ', sorted('horse race'))
print('sorted long str.: ', sorted('this is just some string'))

# zip
seq1 = ['foo', 'bar', 'baz']
seq2 = ['one', 'two', 'three']

zip(seq1, seq2)

seq3 = [False, True]

for i, (a, b, c) in enumerate(zip(seq1, seq2, seq3)):
    print('%d: %s, %s, %s' %(i, a, b, c))

pitchers = [('Nolan', 'Ryan'), ('Roger', 'Clemens'), ('Schilling', 'Curt')]
first_names, last_names = zip(*pitchers)

print('first_names: ', first_names)
print('last_names: ', last_names)

# reversed
print('reversed list: ', list(reversed(range(10))))

# H00. Dict. 

empty_dict = {}
d1 = {'a' : 'some value', 'b':[1, 2, 3, 4]}
print('d1: ', d1)

d1[7] = 'an integer'
print('d1: ', d1)

print(d1['b'])
print('b in d1: ', 'b' in d1)

d1[5] = 'some value'
d1['dummy'] = 'another value'
del d1[5]
ret = d1.pop('dummy')
print('ret: ', ret)

print('keys: ', d1.keys())
print('values: ', d1.values())

d1.update({'b': 'foo', 'c':12})
print('d1: ', d1)

# creating dicts from sequences
mapping = dict(zip(range(5), reversed(range(5))))
print('mapping: ', mapping)

# default values
words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = {}
for word in words:
    letter = word[0]
    if letter not in by_letter:
        by_letter[letter] = [word]
    else :
        by_letter[letter].append(word)

print('by_letter(case1): ', by_letter)

words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = {}
for word in words:
    letter = word[0]
    by_letter.setdefault(letter, []).append(word)

print('by_letter(case2): ', by_letter)

from collections import defaultdict
by_letter = defaultdict(list)
for word in words:
    by_letter[word[0]].append(word)
counts = defaultdict(lambda: 4)
print('counts: ', counts)

# valid dict key types
print('hash: ', hash('string'))
print('hash2: ', hash((1, 2, (2, 3))))
d = {}
d[tuple([1, 2, 3])] = 5
print('d: ', d)


# I00. Set

print('set: ', set([2, 2, 2, 1, 3, 3]))
print({2, 2, 2, 1, 3, 3})

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7, 8}
print('union: a or b: ', a | b)
print('intersection: a and b:', a & b)
print('difference: a - b:', a - b)
print('symmetric difference: a xor b:', a ^ b)

a_set = {1, 2, 3, 4, 5}
print('subset: ', {1, 2, 3}.issubset(a_set))
print('superset: ', a_set.issuperset({1, 2, 3}))
print('set equality: ', {1, 2, 3} == {3, 2, 1})

# J00. List, Set, and Dict Comprehensions
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
print([x.upper() for x in strings if len(x)>2])

unique_lengths = {len(x) for x in strings}
print('unique length: ', unique_lengths)

loc_mapping = {val: index for index, val in enumerate(strings)}
print(loc_mapping)

# Nested list comprehensions

all_data = [ ['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
             ['Susie', 'Casey', 'Jill', 'Nan', 'Eva', 'Jennifer', 'Stephanie']]

names_of_interest = []
for names in all_data:
    enough_es = [name for name in names if name.count('e')>=2]
    names_of_interest.extend(enough_es)

print('names of interest: ', names_of_interest)

result = [name for names in all_data for name in names if name.count('e')>=2]
print('names of interest2: ', result)

some_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
flattened = [x for tup in some_tuples for x in tup]
print('flattened: ', flattened)

flattened = []

for tup in some_tuples:
    for x in tup:
        flattened.append(x)
print('flattened2: ', flattened)


# K00. Functions
def my_function(x, y, z=1.5):
    if z>1:
        return z*(x+y)
    else:
        return z/(x+y)

print('my_function(5, 6, z=0.7): ', my_function(5, 6, z=0.7))
print('my_function(3.14, 7, 3.5): ', my_function(3.14, 7, 3.5))




