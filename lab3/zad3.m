function res = zad3(a,b,f,eps,precision,max_iter)

if sign(f(a)*f(b))>0 
    disp('Wrong range')
else
    digits(precision);
    x(1) = a;
    x(2) = b;
    x(3) = x(2) - f(x(2))*(x(2)-x(1))/f(x(2))-f(x(1));
    iter = 3;
    while (abs(f(x(iter))) > eps && max_iter>iter)
        x(iter+1) = x(iter) - f(x(iter))*(x(iter)-x(iter-1))/(f(x(iter))-f(x(iter-1)));
        iter = iter + 1;
    end
   disp(iter-2);
   res = vpa(x(iter));
end

