function res = df3(x)
    res = vpa(exp(x)-2^(-x)*log(2)-2*sin(x));
end