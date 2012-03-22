import random
import sys

def alpha_bld():
	alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	return ''.join(random.sample(alpha,len(alpha)))

def file_read(file):
	f = open(file,"r")
	return f.read()

def gen_seed(key):
    seed = 0
    letter = key[0]
    seed += ord(letter) + len(key)
    return seed

def calc_val(seed,buf,out): #32 - 126
    if buf != "":
        letter = buf[0]
        buf = buf[1:]
        remain = seed % 94 #44
        lCode = ord(letter) #32
        oCode = lCode - remain #-12

        if oCode < 32:
            oCode = oCode + 94

        out.append(chr(oCode)) #R
        seed = lCode + remain
        return calc_val(seed,buf,out)
    else:
        return out

def roller(key,script):
    hold  = []
    buf = file_read(script)
    buf = buf.replace("\t"," ")
    buf = buf.replace("\n"," ")
    seed = gen_seed(key)
    lret = calc_val(seed,buf,hold)
    encoded = ''.join(hold)
    encoded = encoded.replace("\\","\\\\")
    encoded = encoded.replace("'","\\'")
    return decoder(key,encoded)

def decoder(key,encoded):
	vars = alpha_bld()
	tmp = "function %s() {" % vars[0]
	tmp += "%s = window.location.toString();" % vars[1]
	tmp += "%s = %s.charCodeAt(0);" % (vars[2],vars[1])
	tmp += "%s += %s.length;" % (vars[2],vars[1])
	tmp += "var %s = '" % vars[3] + encoded + "';"
	tmp += "%s = '';" % vars[4]
	tmp += "for ( %s=0; %s<%s.length; %s++){" % (vars[5],vars[5],vars[3],vars[5])
	tmp += "%s = %s" % (vars[2],vars[2]) + " % 0x5e;"
	tmp += "%s = %s.charCodeAt(%s) + %s;" % (vars[6],vars[3],vars[5],vars[2])
	tmp += "if (%s >= 0x7e){" % vars[6]
	tmp += "%s = %s-0x5e;" % (vars[6],vars[6])
	tmp += "}"
	tmp += "%s += String.fromCharCode(%s);" % (vars[4],vars[6])
	tmp += "%s += %s;" % (vars[2],vars[6])
	tmp += "}"
	tmp += "return %s;" % vars[4]
	tmp += "}"
	tmp += "var %s = %s();" % (vars[8],vars[0])
	tmp += "eval(%s);" % vars[8] 
	return tmp

def main():
	if len(sys.argv) < 3:
		sys.exit('Usage (2 arguments): %s "%s" %s' % (sys.argv[0],"http://sitekey.blah","js_file"))
	else:
		data = roller(sys.argv[1],sys.argv[2])
		print data	

if __name__ == '__main__':
	main()
