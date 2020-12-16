import re


def process_boolean_str(s):
    ltt = []
    braces_stack = []
    ext_s = ''
    try:
        for c in s:
            if c == '(':
                braces_stack.append(c)
            elif c == ')':
                braces_stack.pop()
            elif c in ['.', '|', '-']:
                if ext_s:
                    ltt.append(ext_s)
                ext_s = ''
            else:
                ext_s += c
        if(ext_s):
            ltt.append(ext_s)
        return ltt
    except:
        DOCURL = 'https://developers.google.com/custom-search/docs/xml_results_appendices#booleanOperators'
        raise TypeError(f'Invalid boolean string.\nRefer to {DOCURL}')


def param_validator(param, csq, q):
    tp = csq['type']
    res = None
    if tp == 0:
        res = param
    elif tp == 1:
        res = param if param in csq['vals'] else None
    elif tp == 2:
        res = param if param in csq['vals'] else None
        if param in csq['vals'].values():
            res = csq['vals'].index(param)
    elif tp == 3:
        res = param if len(re.findall(csq['vals'], param)) == 1 else None
    return res
