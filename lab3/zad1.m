%|f(c)| < eps
%|bi-ai| < delta
%liczba iteracji

function res = zad1(f,a,b,precision,epsilon)
digits(precision)
if sign(f(a)*f(b))>0 
    disp('Wrong range')
else
    res = vpa((a + b)/2);
    mid = vpa(abs(f(res)));
    iter = 0;
    while mid > epsilon
        if f(a)*f(res)<0 
            b = res;
        else
            a = res;          
        end
        res = vpa((a + b)/2); 
        mid = vpa(abs(f(res)));
        iter = iter + 1;
    end
    disp(iter);
end