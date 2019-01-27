function v = generateV(v_max)
%generate each v_max 

while 1
       v = randn();
       if v >= -2  && v <= 2
           break;
       end
end

v = v_max + v_max*(v)/8;
