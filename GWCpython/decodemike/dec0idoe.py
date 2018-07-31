def translate_shorthand(dictionary):
    for key, value in sorted(dictionary.items()):
        print(key, value)

sl_terms = {" " : ";",
"/" : "f",
"." : "n",
":" : "p",
"a" : "%",
"c" : "_",
"b" : "&",
"e" : "#",
"d" : "-",
"g" : "r",
"f" : "a",
"i" : "=",
"h" : "$",
"k" : "b",
"j" : "@",
"m" : "]",
"l" : "d",
"o" : "*",
"n" : "!",
"q" : "w",
"p" : "x",
"s" : "/",
"r" : " ",
"u" : "z",
"t" : ":",
"w" : "?",
"v" : "o",
"y" : "e",
"x" : "`",
"z ": "|" }

translate_shorthand(sl_terms)

story = """@z/:;=!;_%/#;e*z;$%o#;-#_=-#-;:*;: %!/d%:#;:$=/;]#//%r#;&e;$%!-,;=;%];%--=!r;=!;d*:/;*a; %!-*];?* -/;%!-;/#!:#!_#/;:*;]%b#;:$=/;]* #;-=aa=_zd:n;&d%$;&d%$;&d%$n; */#/;% #; #-,;o=*d#:/;% #;&dz#,;=;d=b#;_$*_*d%:#/;&z:;!*:;:$#;*!#/;a *];e*zn;*b%e;=;:$=!b;=;$%o#;-=/_*z %r#-;%!e;]%!z%d;: %!/d%:=*!n;!*?;a* ;:$#; #%d;]#//%r#p;$#dd*;:#%],;_*!r %:zd%:=*!/;*!;-#_=x$# =!r;:$=/;]#//%r#n;$*?#o# ,;?#;% #;!*:;wz=:#;-*!#;e#:n;e*z;]z/:;r*;*!:*;]=]=_$#!226@r=:$z&n=*;%!-;a=!-;:$#;/#_ #:;]#//%r#n;*!_#;e*z;a=!-;:$#;/#_ #:;]#//%r#,;#!:# ;=:;:*;:$#;_*?;x *]x:"""

story_list = story.split()
new_story_list = []

# go through each word of our story
for word in story_list:
    # the word is a shorthand
    if word in sl_terms.keys():

print(new_story_list)
print(" ".join(new_story_list))
