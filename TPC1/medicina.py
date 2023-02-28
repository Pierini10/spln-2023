import re

text=open("medicina.xml", 'r').read()

####

def removeXMLTop(t):
    t = re.sub(r'<\?xml.*\n|<!DOCTYPE.*\n|<pdf2xml.*\n|</pdf2xml.*\n', r'', t)
    return t

def removeHeaderFooter(t):
    t = re.sub(r'<text.* font="1">ocabulario.*</text>', r'###', t)
    t = re.sub(r'.*\n###\n.*\n', r'', t)
    t = re.sub(r'<page.*\n|</page>\n|\t<fontspec.*\n', r'', t)

    return t

def removeTextoVazio(t):
    t = re.sub(r'(<text.*>\s+<\/text>|<text.*><(b|i)>\s+<\/(b|i)><\/text>)\n', r'',t)
    return t

####

def marcaE(t):
    t = re.sub(r'<text.*font="3"><b>\s*(\d*.*\w+.*)</b></text>', r'###\1', t)
    t = re.sub(r'###\s*', r'###', t)
    return t

def marcaEC(t):
    t = re.sub(r'###(\d+)\s*(.*\n)', r'_EC_\1_N_\2', t)
    t = re.sub(r'(_EC_\d+_N_(\s?\w)+)\s{3,}(f|m|a)', r'\1_G_\3', t)
    return t

def marcaER(t):
    t = re.sub(r'###\s*(.*\n)', r'_ER_\1', t)
    t = re.sub(r'_ER_[A-Z]\n', r'', t)
    return t

####

def marcaLinguas(t):
    t = re.sub(r'<text.*font="0">\s+(es|pt|en|la)\s+</text>', r'_L_\1_', t)
    t = re.sub(r'\n<text.*font="7"><i>\s*(.*)<\/i></text>', r'\1', t)
    t = re.sub(r'\n<text.*font="0">; </text>', r'; ', t)
    return t

def marcaSIN(t):
    t = re.sub(r'<text.*SIN.-\s*(\w.*)</text>', r'_S_\1', t)
    t = re.sub(r'_S_.*\n(<text.*>\s*(<[ib]>)?\s*(\w.*)(<\/[ib]>?)\s*<\/text>\n)+_L_', r'\3', t)
    return t

def marcaECArea(t):
    t = re.sub(r'<text.*font="6"><i>\s*(.*)</i>\s*</text>', r'_A_\1', t)
    t = re.sub(r'(_A_(\s?\w)+)\s{3,}(\w.*)', r'\1|\3', t)
    t = re.sub(r'_A_\n', r'', t)
    return t

def marcaNotas(t):
    t = re.sub(r'<text.*font="9">\s*Nota.-\s*(\w.*)</text>', r'_NOT_\1', t)
    t = re.sub(r'\n<text.*font="9">\s*(\S.*)</text>', r'\1', t)
    return t

def marcaResto(t):
    t = re.sub(r'<text.*font="5">\s*Vid.-\s*(\w.*)</text>', r'_V_\1', t)
    t = re.sub(r'\n<text.*font="5">\s*(\S.*)</text>', r'\1', t)
    t = re.sub(r'<text.*>\s*Vid.-\s*(\w.*)</text>', r'_V_\1', t)
    t = re.sub(r'<text.*>\s*Vid.\s*(\w.*)</text>', r'_V_\1', t)
    t = re.sub(r'\n<text.*>(<[ib]>)?(<[ib]>)?\s*(\w.*)(</[ib]>)?(</[ib]>)?</text>', r'\3', t)
    t = re.sub(r'\n<text.*>\s*(<[ib]>)?\s*(<[ib]>)?\s*(\S.*)(</[ib]>)?\s*(</[ib]>)?\s*</text>', r'\3', t)
    return t


text = removeXMLTop(text)
text = removeHeaderFooter(text)
text = removeTextoVazio(text)

text = marcaE(text)
text = marcaEC(text)
text = marcaER(text)

text = marcaLinguas(text)
text = marcaSIN(text)
text = marcaECArea(text)
text = marcaNotas(text)
text = marcaResto(text)

open("result.txt", "w").write(text)


