## Snakes
The main idea to get the flag is simple `cat` command.

#### Step-1:
After I downloaded `ropes`, I tried to change permissions and run it by `./ropes`. But alas!

#### Step-2:
I got this errors:

```
./ropes: line 1: $'\317\372\355\376\a': command not found
./ropes: line 11: fg: no job control
./ropes: line 15: syntax error near unexpected token `('
./ropes: line 15: `vml jhry8gt65DFY^*HU(cp,l mnjhbiom		n	jb	bubv		yb	b	hb	v	tvb	b	ibn	jn\[sxemwo'
```

#### Step-3:
So, I just used `cat ropes`

I got this output:

```bash
����    �      �  �          H   __PAGEZERO                                                        �  __TEXT                                                    __text          __TEXT          �     i       �               �            __stubs         __TEXT          �            �             �           __stub_helper   __TEXT          ,     .       ,               �            __cstring       __TEXT          Z     ^       Z                             __unwind_info   __TEXT          �     H       �                                �   __DATA                                                  __nl_symbol_ptr __DATA                                                   __la_symbol_ptr __DATA                                                    H   __LINKEDIT                            H                    "  �0                          (   H   0         �       !  H   
    P                                                �                            
      /usr/lib/dyld          c�z���81��̝N�-2           
  
        �*              (  �   �              
                                                 8         ��   /usr/lib/libSystem.B.dylib      &      x     )      �                                                                                                                            svsvsv
eavriubnm
v

er'.bi	bi	b	ib	b	n	jun	jon	jndjlnuceu9novun 		 	jmb	hjib	ibn	i                                                                                                                                                                                                                    UH��H�� �E�    H�=�   � �M   H�=�   H�u��E�� �D   �}�7  �E��   H�=}   �"   H�=�   �E��   �E�E�H�� ]Ð�%�   �%�   �%�   L��   AS�%�   �h    �����h   �����h�   �����Give me a magic number:  



%d First part is: flag{r0p35_4r3_b45ic411y_5n4k35 



vml jhry8gt65DFY^*HU(cp,l mnjhbiom		n	jb	b	ubv	yb	b	hb	v	tvb	b	ibn	jn\[sxemwo
vr4v
rb
brnhbu9	h	yb	b	n	n	ubn	b		b[b	y9u	b	by	b	bb



Second part is: _101}                        �  4   4   �      4      
                                                                                                 <     F     P                                                                                                                                                           kmcjusd8y bginjdsk'lnv byve8w9uoenjc bgcuhy8su9dkm cnbjghuyewmdkc vnbghyrud8ickm vnbheyudixkmc nvbhfyrduijxkmc nbhrydijxkmc vnvbhndnj 


c
wegv,lmrwkmkvm;
viuwervnhioujdsnv

dvmjh					m	jhu	y80	y		ni	p	oy	n			
	kfmnceonj			m vjnije		 	 	hjg	v	b	h				hbuik	hb 
	insiy	b	 hi 	j 				n	yuoi	bg		i	n	oj	n 	h		iol	n 	on 		l;	 	                                                                                              "S    @dyld_stub_binder Qr � r@_printf � r@_puts � r @_scanf �   _  _mh_execute_header !main %    �       �                      �                  $             *             1                            @           __mh_execute_header _main _printf _puts _scanf dyld_stub_binder       r
```

Maybe I had to reverse it, but who cares when you got the flag. :lol:


#### Step-4:
Finally, the flag becomes:
`flag{r0p35_4r3_b45ic411y_5n4k35_101}`