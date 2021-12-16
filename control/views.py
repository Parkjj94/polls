from django.shortcuts import render

def index(request):
    return render(request, 'control/index.html')

# 회원가입
def register(request):
    if request.method == "POST":
        # 아이디를 넘겨 받음
        userid = request.POST['userid']
        return render(request, 'control/reg_result.html', {'userid':userid})
        # html로 렌더링할때 딕셔너리구조로 자료를 보냄
    else:   # GET 이면
        return render(request, 'control/register.html')

# 반복문 forloop.counter
def counter(request):
    items = ['a', 'b', 'c', 'd']
    return render(request, 'control/counter.html', {'items':items})

# 짝수/홀수 판별하기
def calc_even_odd(request):
    if request.method == "POST":
        try:        # 문자(ex: a, k, 나, 바)가 입력될 경우 예외처리(try~except~else)
            num = int(request.POST['num'])
            # 입력값(숫자-문자형태)을 넘겨 받아 숫자로 변환
        except:
            return render(request, 'control/calc_even_odd.html',
                          {'error': '정수만 입력가능합니다.'})
        else:
            if num % 2 == 0:
                result = "짝수입니다."
            else:
                result = "홀수입니다."
            return render(request, 'control/calc_result.html',
                          {'num':num, 'result':result})
    else:
        return render(request, 'control/calc_even_odd.html')