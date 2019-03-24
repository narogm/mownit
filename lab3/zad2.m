function res = zad2(x0,f,df,eps,precision,max_iter)
if x0 < eps
    disp("Wrong input")
else
    digits(precision);
    x(1) = x0;
    x(2) = x(1) - f(x(1))/df(x(1));
    iter = 2;
    while (abs(f(x(iter))) > eps && max_iter>iter)
        x(iter+1) = x(iter) - f(x(iter))/df(x(iter));
        iter = iter + 1;
    end
   disp(iter-2);
   res =vpa( x(iter));
end