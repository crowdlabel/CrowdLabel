from flask import g

def login_required(func):
    """
    用户必须登录装饰器
    使用方法：放在 method_decorators 中
    """
    # @wraps(func)
    def wrapper(*args, **kwargs):
        if False and not g.user_id:
            return {'message': 'User must be authorized.'}, 401
        else:
            return func(*args, **kwargs)
    wrapper.__name__ = 'wrapper' + func.__name__
    return wrapper
