def orthonormal_exp(variables):
	result = []
	last = []
	for var in variables:
        if last:
            last[-1]+=1
        last.append(var)
        result.append(expression(last))
    last[-1]+=1
	result.append(expression(last))
	return result

def expression(last):
	s = 1
	for i in last:
		s = s*i
	return s

def variables(formula):return list(formula.variables())

def anf_not(formula):return formula+1

def anf_xor(form1,form2):return form1+form2

def anf_and(form1,form2):return form1*form2

def anf_or(form1,form2):return anf_xor(anf_xor(form1,form2),anf_and(form1,form2))
