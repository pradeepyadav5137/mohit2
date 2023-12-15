s="atshak"

ss=s[0:2]    # for n jusr replace 2 by n
sm=s[2:-2]
sl=s[-2:]               # A k s h a t
                        # 0 1 2 3 4 5
                        #  -5  -4 -3 -2 -1

s=sl+sm+ss
print(s)