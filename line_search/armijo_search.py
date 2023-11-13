from autograd import grad

def armijo_search(
        obj_func, x0, eps=0.2,
        alpha=1.1, max_iter=100):

    f_x = grad(obj_func)
    def lin_approx(x):
        return obj_func(0.0) + x*eps*f_x(0.0)
    x = x0
    k = 0
    if obj_func(x) <= lin_approx(x):
        while obj_func(x) <= lin_approx(x) and k <= max_iter:
            x_prev = x
            x = alpha*x
            k += 1
        step = x_prev
    else:
        while obj_func(x) > lin_approx(x) and k <= max_iter:
            x_prev = x
            x = x/alpha
            k += 1
        step = x_prev
        
    return step