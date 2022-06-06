from django.http import JsonResponse

from django.contrib.auth import authenticate, login, logout


def sign_in(request):
    # 登录处理
    # 从 HTTP POST 请求中获取用户名、密码参数
    user_name = request.POST.get('username')
    passwd = request.POST.get('password')

    # 登陆过程:
    # step 1: 校验用户的账户密码
    # step 2: 校验用户(is_active, is_superuser)

    # 使用 Django auth 库里面的 方法校验用户名、密码
    # 校验成功: 返回用户信息; 校验不成功: 返回None
    user = authenticate(username=user_name, password=passwd)

    # 如果能找到用户，并且密码正确
    if user is not None:
        if user.is_active:
            if user.is_superuser:
                login(request, user)
                # 在session中存入用户类型
                request.session['usertype'] = 'mgr'

                return JsonResponse({'ret': 0})
            else:
                return JsonResponse({'ret': 1, 'msg': '请使用管理员账户登录'})
        else:
            return JsonResponse({'ret': 0, 'msg': '用户已经被禁用'})

    # 否则就是用户名、密码有误
    else:
        return JsonResponse({'ret': 1, 'msg': '用户名或者密码错误'})


def sign_out(request):
    # 使用登出方法
    logout(request)
    return JsonResponse({'ret': 0})

