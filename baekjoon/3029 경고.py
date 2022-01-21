# 20220121 3029 경고
# String (문자열)
# https://www.acmicpc.net/problem/3029

start = list(map(int, input().split(':')))
end = list(map(int, input().split(':')))

t_start = start[0]*3600 + start[1]*60 + start[2]
t_end = end[0]*3600 + end[1]*60 + end[2]
r_time = 0

#86,400
#3600

if t_start > t_end:
    r_time = 24*3600 - t_start + t_end
elif t_start < t_end:
    r_time = t_end - t_start
elif t_start == t_end:
    r_time = 0

#print(start)
#print(r_time, t_start, t_end)

hh = r_time//3600
mm = (r_time%3600)//60
ss = r_time%60

if len(str(hh)) == 1:
    hh ='0' + str(hh)
if len(str(mm)) == 1:
    mm ='0' + str(mm)
if len(str(ss)) == 1:
    ss ='0' + str(ss)

# 정인이는 적어도 1초를 기다리며, 많아야 24시간을 기다린다.
# 문제 똑바로 읽어라 제발
if(r_time == 0):
    print('24:00:00')
else :
    result = str(hh)+':'+str(mm)+':'+str(ss)
    print(result)


