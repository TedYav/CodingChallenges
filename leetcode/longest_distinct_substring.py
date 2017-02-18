"""

    Longest Substring w/at most K Distinct Characters
    Strategy:
        *Create empty dictionary counts to store characters
        *set start,longest to 0, end to 1
        *while end<=len(s):
            *while len(counts) <= k:
                *if end-start > longest: longest = end-start
                *counts[s[end]] += 1 or = 1 if not in counts
                *end += 1
            *while len(counts) > k:
                *counts[start] -= 1
                *if counts[start] == 0: del start
                *start += 1
        return longest

"""
import timeit

class Solution(object):
    # non optimized solution
    def lengthOfLongestSubstringKDistinctSlow(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k<=0 or len(s) == 0: return 0
        elif k>=len(s): return len(s)   # special case optimization. Saves time if k and s are large
        else:
            start = end = longest = 0
            counts = {}
            while end < len(s):
                while len(counts.keys()) <= k and end <= len(s):
                    if end - start > longest: longest = end - start
                    if end < len(s): counts[s[end]] = counts.get(s[end],0) + 1
                    end += 1
                while len(counts.keys()) > k:
                    counts[s[start]] -= 1
                    if counts[s[start]] == 0:
                        del counts[s[start]]
                    start += 1
            return longest

    # optimized solution
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        if k<=0 or n == 0: return 0
        elif k>=n: return n   # special case optimization. Saves time if k and s are large
        else:
            start = end = 0
            counts = {}
            while end < k:
                if s[end] in counts:
                    counts[s[end]] += 1
                else:
                    counts[s[end]] = 1
                end += 1
            longest = k
            while end < n:
                if s[end] in counts:
                    counts[s[end]] += 1
                else:
                    counts[s[end]] = 1
                end += 1
                
                if len(counts) <= k:
                    longest = end - start
                else:
                    counts[s[start]] -= 1
                    if counts[s[start]] == 0:
                        del counts[s[start]]
                    start += 1

            return longest

old_test='JWao7\\t`^GUxC7SXB22Ct[20SKJTS^ybo_Z8j@wGccWogz;37hqFbapRwqgS>Fniq3vzw:X>0ltbPa5@U>xn5WVpaEK>4aT\\@7_e:<lfhM:_RWYc[YZoaW]kOH\\:HQkjMFWz]rr<3D`c0nl8H\\MAHdrIW41V<b6<yXuKu3;nFNAy^y\\9U>S2bj6iGAMOhsiTlOLSezZ:PU<^[^H12MIN9Z7\\XqpwkpT=6^6Ai3[]J7VCPI7DLaaDRRV6jm024NbdGTGi@fCbAfZU2AFrKMp;SwT=DepGQ5?uArF>nC0vFSD@RCSt49YyWG@vX3[\\xslqPGZ2VsL2Hq=ni]cYV6pQo\\_2cT]k6;aH<vW6PI@o?K;f65K6>gvDLNHnEQf91f6:Ja3BPe@G=s^2RaFY87OXyz5_YLG;K\\ANKoA>_N5Ybnxt3tJp`3eO8Lr7=FO<KukOBFD=VQUjETInriCFmg3gzl497e31bb\\rm_7=BhUnNJ?O8W`wCOr9rgd=>QyM:[UJ`1fGM>n4fR<nONqOgR1Jo4j2hscsUYUnLDN@PQT^tt0`ujlAbS9\\KqDezZ9DatO?uQ<dM_S7SvK3h_RnvOVm[6GT2UERjP_mbstNcg]\\X2cfw2wiF2ZzCW420driIIWGe7kG>CRm@z3dM^4A^QhLST^F7d9NxmTDYYElXkujk;^r;tTrzWKQ6cOFGifvyDDEpK93;=\\]^itmLlG314?qCRIUFehLBNO6<JDAV4;?Z0N1pTi?6MlSPxQNIs`?y;uK;S;;F4mPpAgfjTCapD`WoNWEVp@74f72;pUrqh7mhNfsS\\ebeV`O\\3x^ye2Zh;1wXfR\\zt9ps]Lc_Cw9AE7OoV8PYBS7n6pRXCu`t\\pRc;G_k<tvybmWA6@_u5iCE1apA1W@W?lkyI^7g[]NlpMDxpS4Vfet^?F43=EwcIdGJV[gSeGR=yt?_WrfFp[FpHU0hydL7FKrMLPedJ`>L6IQ2iDwEt1TBJo<Y4wCz:0`E:kGFxhGQuG[Be=bfyhhd<hC]rSB]kz46bgTNm^VTd`wvVG<JITd`CxUfBztLiL9:r^83^N7=O[EtYUCtAZz_H^Bf>2<Ar;CtMrlOLNYiqMa5n_CNTaA9YAo3^mT5Poe?4D;Q;wh]u4i7g7e1K0ds6oQu;l6_U]Xe2Wh2yK0zM\\=H<O8?D]E3UE^p3mLHWGV<vN1A:G>]397a_A8OF_<UT1:9^gE`yobqbw[<RgIULXa9K4E0_xel9lywWuqDe<h<ZIT2Gm=ANXITh_w8Yv4fJWNzLgzXB@MYrxCY4E3n=1F<h>r@RcFmG_<MZxDby][5ftiBtbhiHeQI[B\\J=uSdh5ydidbet>E:zsvIo\\Afg<r[:L7iFlYCHv?1pQ@cB:Y0vIEA<TEYMvtdy^dWW9e23b5LgrI_VM6CrR9y7T441Ij5VHsr>sxhkruQ<6EQ_XyQZH=VFC?Ld=Bn>Vo;:7t=T@1j1Tw8@btoSGh\\`S;a9nnrf_tx0Kp99XIMCaIhRzX\\@yTsvb0UIh>YtunzFdz0em0nkyb0;?rDk4``=L`dxW1vgp0dHKM]=B0LOefGP7<x^2NN[G<_^sv]j>WRwN9<4TLBX@X6v2gGHK36zq<6n43H2jOFCRbXtJ7>04?A8oY<;57[Zl@_^evxPr5@o7ogY23U]jY6DE8Yc]4BDdL^JB?iSA@;Jqx\\50t9IyCNooUU?5hwLzE1p\\mztKK;]l]87@m?FMVri=_d2\\8g`wFp7AIMoGwK7pjc25]z=JfNQx7WZeioClkY;bk\\K1_v\\BRh>JNnsp=Vpl2SLc8:j5pPoHhWOftPVL4z?eaOv5^Bcevs;_5zVjg`cbuRo;6CXBCGmTIKq:7V]nwL1Y\\YDNKE^b:IFciG]18H]XBt7=d3fzpYuk8qyid?0<e>[a`lxQ2\\hrF<VGC?x[R`hkJl08s]C7BR1X7f6kIm9?XkcrB1=t@lbfsqL5`5qNqj2H6zSAqjk4eEZQ<IjLFhM0EUJnoXfOBL1JxepepEJex[C>H[b\\vJCBM14TsJ484MB=P<v]:vxosXdUcxK0[Nv[@SIq1yCI:pT][aQuqofJf35Pz8ql2_qL>i2z>SO4uNJq\\Kv^6FED2nyHDgMbX:aMDj_T;^xuSDq1hmE899y@D8A]oDtZgvudBro@Q[__i@kKVB_suPAt3X9sl7bFWefMvZv7<z83WOrTvpE\\UDJC5lt0kI@fZ07W0^4eDA684>jSK8SEDJz^qp@dr0_CBOG3qmN;vVXwIkV3aQ3b9HJh[w8Gcn7]_0`huOD6iAWK[z7hX1ovI>GN6UGHLB<Ej_>bwi20nkkP?z49lkt>z>RQ]KLU1bP>wTBoo_pEJqTEqt:Lqor]4V5UyD]HYw@YVFqEIs7O>>ubWeOt4CEWOGT[[oks]fF\\a1JKM5V0mu9VUz7OHyTO2Rbf3fDEx`PhBkuVqa:5wwDme9Y=QM5r4Ovgl7l>U:\\qOS?7b1<`fOFgpROmPZ?K:A[\\q=UGFCu6em`?X;lC^CwWFwukCYFpsAMQC4Ab6ZlVQR1zBcpO\\[gh[aJC546Q]gV2uSR3w`KcEX>TY13ybXVvU5E@2qBF]]st3bI2Rf4<G>LHW\\<mE2zYDu<[lCSvR2vK94pa713\\mfVs3tC1XW@sUPZAfKT>s>h>LEzi>Q1ed1[o:HeuZQZHLYBSQt^mY??7E;V3gE?@`n:_jWnHi`AK[i`zGmO5e`ttK5qRq:BEOigos6D:u1e[aQAV01m9Uu4X[?<Q1hy5A7ljzOjU?Pbp=]0HVt9cV2jcdwcYgK4LRDLA8^3\\KdOMfGeS=6?@jxcQoXRa_QlE6T:PDRgUy7RnBrN1Uf;QDVAuvyiI<Qe<FyywDCrkgm<Tpxl;Tiq32oqg=`F1^pgZKBypFQyT8Xy??ABwg^TQfMN1roAL<;=R7vYg;RZe_11:T<xSk?]gy9aCzVg3kn3nD\\zD3>duFR2w6^P:HJ;2s0JOaSN[afDzTQm<6`8y?2nz^iTtPjAGG;Qnny8OP[Gvw4xS`qVumzxe4mBpO9MCyYA?O<2=OB]o]_pM6oOqrXa6MwhF5eF3[r9>wkn0n1`?[G0[<aDA`hO2YN5>R1j>f_HAuAdWlRhL`wwYp?\\kskwaytj1HTAt\\w5]lT@`zoVG7ftoI[NChuhJuW1vJzlp[1M\\u4[dzS2<zvp`iWCJW7umpv40<=^c3:4Q<36;=KU6JssKlFR[1AIsj`QxXm053eZ@jWbSdAr78UACFdTz`U5pw6`vzMxP=6?>qs79w24BII`DYAGV8tQJnoGyy?ZFdsqoy0jfPE_<:b1ulh;[a]huGY8EPIO\\oMJV@0fd_IO\\XmzeQe;IEGVZ=kxzZ5[ADWTImZIUY66G5PXeKk5dbI`PXMlb@g<kFY_dSnk?hFic8oI6C:PKMix2P1RRcgYC7<cIM`:2A0tUmpTRg50`lBndkGK1Y^He2MvLURkCBhZ;kt7tYnLL^aYIHlSZ8D7h;Csa_Hteq86P0JTGn@3C8:93W4pyDwWZ>Lb:7B55Ocns?_S5owy@phG<yzZq_S[lx\\=aP00YU9pMrTT7T5Y@am<I3`UZdqGEkcjf3DlvXowsPQa=bAK@idYX8HSbW<RW9\\zWWopH;7XU]ASU\\dnOzgX;_r`dFhp@WiM8KsvyF`KHDJz8TFb2V:]qNXFuE@zS`maukTBuEg?=1xeJP0iB@j]hr4KskRo\\xK[UAv8s0wZ<Nou<cW@4W;ypjkxuuM[GXWuo8=cNxFr2[7NX@64qPFdP:7VFGeOX@Op9T[6<0:Za`yn6M[vPt@:V9>YXFeNmn1vULto7\\`oJ3Z;t;k>\\Zg4]Di?WY9BVTHKhU7A\\nwjz>^g:H0J5LLeE3^Mt[l2=vI:nZQ<i\\d\\C@DYWjjW5kOdRH;C_1?`a??@cJQF\\fhDKoaOeJzLA^n1TPJ`kmACUBL9djZpe>`QE=vEsmW9u91AvLiN6`9RlQg:\\[IF]D8x<0h<8KR\\h16P4GMCZUesjZL0q:rZ09F2PZHc>q?[kNCuEO3i^6<vtv\\lnKezhxg?\\pJn\\t7GWSf0a2<3<;B8Fzgh7[Ll2_2Awlt5b@ao^iljPQ^r?75=SHMB4@CdDxBrWUOSS[eO7ON=@4US=h`WU:5z@A9VFCIEVRAA]>D8TklxErZr<u[Nq\\81?1wapz8<VzUGypaG\\FAq[nb6kC0Zlqv8?8Wjlehpp`IEPKz`Qc2Vt8fcint0n^]ljWRE4yR]JRm`jJwJ7L^N2BzKID1sdQN4K?j=aSlfuy`OZMgWc?1u2mUiCnbMx`<Hc;Id8lHFxbj_oDZoe^c`Yq^4ju^PvUlTz9Weh^m3Wj`wXfbE7vUGBk1qsM3Un[SmXmOg4ylZ6]cbBV>3ysja9MCh_D]QBQ5_iB_i_zAxKrzvY7xg7Dwv9OPtwSUnsICXO1Lx?fv5iW\\RMk2;4?_CCr4V=WPtFid9x0EKWUvel7OPua5zRB0?Q7lH>WIau3hDavYcBn=bk1=i_5V<EH9JK2`bStVXW95l8^V`cpOv04GJfydvWXXzzYwBAr[ajK`<Xv9]zu?\\1]95K3m6LNHz2TRTk[`nD^I6T`jQiTygM6_Qk^bQQNSte=XPOclI[3gOZYGqEfZQ>P?J6[=2YTrTlsql2edIn7;ePMP948A70[89;Qjzuu?ke[stGB:mNUofYzX?ZY96csh2zhjruRk88FnaVem0Y2jT:yN1JgW:wZ2oWXQBIc]gMXIY?3M]Fp>jj\\5:0MK<gid5sXOf8_ItamRhmtVM>WociFDEA<N]G3OAW2tN<nmNCjfhZ=Ce_>9=IoWY9:lP^a:kDtLVKYObC@`L9?g]ai67B7bhB0RLDjw@CEBHn3YEMzduJaf24CfHPlSrQ>UJsy_L?gQC_yVQAVpas7:Zrk^7\\IESJKSLUP=GZQ^J8Ucw0vg:Jr^;ftfwQXJ^?3Iqf3;SrlTKNn>u@`rbj1k9M<>BAFm]kXhm_?k`X3nH6eXaW\\tcMuGi0zkm0QauB9oGMrLm?VS_LGRiRL9jVHhe<xjT5=>`6=ml>zN5[u7L@QEuX[liT_zfk@Ti[5i[:\\D<K2TIX<8T2y=:^040p1\\Xgn3WNR5\\h;v\\p1Opq@7MSiIu=CMpYCasFWjDc9]1[]ww:^1Fn^9Vqo^o11<H:dT5RgtaY:>[Qy0osK32kT2J<=elAQMXBfTo1jB3E;koFft8051yUZ^VpST\\bk>S6jY=@xjc6i2VgwyuAHB8c4DK;nXAsNL7EXN?Sx:]kHq]DJXChCDf\\jW^0f5eSnBrTlO=t4Z]nAX8o@zSXG[@gsotI^@64r5?TX5j^GSRtNsC_CImeXc7:tiKAolr;1x?C\\:[zrk>wQEApk=Ge1b;JJnLg9ossu_G;F]Wk45<McOR:TFlTOmk3xjbKT\\c`rpwtkaqYhR2?VUwIAcEDxmx\\vC\\0>B@m@^bP4oJCv7?Jgo6k\\`lB:MwVorXR>VODM>VPyr7Q:mtYzBgnDCk8z_xmLnEf:YaK4fn;3ewj78s\\ob[U>i;6HGvJnYi;6wo@ti3K\\7B6@g<0hAY5UQ@yvTU2_BNp_i6saL?0f=Ic5G6:Tl2>A@SL=FFfdvY:F2^l<n`6LLH`\\H0fc_oA0idRHwE@]4o0unS^oaywWXOaJBE5TlgJ:1rZLg@=<32c[ZdjWSwxdDgB7<Iz^<uFE?8]E[c9i1O?6etSa`xSJQz8I<uB2MKazOjtxl`;GXP6`_^`350yl6RtqFNxBi?wat7m<VtXfuBiWnVo>Qqs23AfdmBoRc]9:t<l\\UJZgYi?>^43rPU;Lf3yFS0_<p1erc7D9[Ub4[FZOi?7Hm4U:?[23rMQJeBjt:D_VzMF9@FZW[\\GgxBCLu@;hHvh@QdV3:RwuFr1aj<jv;@_]D\\GGz:iGyPny39FDsY0qoYNw\\au2AyE8Bbcmfm?nynRi7fSCPH=?\\\\8=Q\\aew;j>l^xQ4H6SO_<]PVVmhD=bFmoHPBQr=RZ`AeOG7_gXtumQOuIKraoZVC`XxAt0Z`[p\\:0lf`AcD?[=R`jyH<`NB[[XYdp4xrnPd9X_NkApDu2hX7u<3W0DvT>[A^ds9v2DHl^cY0jB?7v=B2Bo2[bpC_6^8<_X]I2iyjkbm9lOpTm1DuHTv248BxSyIYCX6WNSc:MjPZjTjWjm\\N0UuTgXL@xY6g<7o2aBi7D9b@bUyCKqeMZtuv3;l0ZXEIn?2EujGbRQfwpkPxPGy22OBupN6h;kRJzo]1N`Y0pWSgnyVRe\\ha3_^dfGW@2pm38iFBFhk\\DkBWBZ:bN2H\\ZuK@B4qzO?wHYz`s7r]2N=yv6AH]UP4TDx]8It^=UW^TA12=kxXjG1zs;N1Q:^n9Rx;TD2pgKWhlZY<EK5eR?xWq6IoASgINi1h5Pqk:7tu10<MwjlEA2Lw4Vx;PhPpvluD`4uc_N;P9s^F@zfA@<Exuej4nnrzKhiV4=GyTH2gQBoZTP=H7=a@O;KE_zV6\\doE`PyL9nL\\Z9_3O2@i_yyX_oRJurP@:5>pSz]MSKi>Oap6;I:6w9;<hvP44f5`W0Ri2@lFDAL0NT]T?dE`>GlY[tg:<IHPzOp2_CdAUFCb@YoV8Ggh`0awEo93;\\r7b>cFkcL:?t?zj09ZuR:P4x<6R65F?t7kZcg`da[eo6kfZXm=HV@SB<7d;]9R5T6@o4De^]TB7E:7yxS2e<Cja=F1lrFPoI7wiA`t;8xtA3O\\:NksIr_Zfo@lvMH4Xjgn1?Vze_Dnyh`YKaAlXt3mJ1x<F^yE_31LOs13u_aqUnZh5mh?lB0jMNA@M:[]NoOobZsafRZyw228I^Gna1h?V;3M:Db@ay[D\\bEyX6]whoRc9X?GbV\\>=mEbzJ6w;ldD2VGdx0?Iz7r?H7S^@hK2VH=o?=]k870gkgRY:^72l\\arIsoj^Wi:9zCYq^a<j0N?GvcV\\ljlYJ\\Z>Npv16\\;hA[:dx7UrfBnovx4y:i`TGWkH@dgNL:OAGNe8_83KUrlszCB85oyXJiUziil4_:60;qQqHAv=a[@4aE9LTArPcvnLz5OB3:^vfZU9aiNAGtFHYT[Yu^zkck`HAptG2qX9KSUcK2nYAa@@LEmfc:f[juxKcwOStpzaf8fQP3y\\HkyOINuO8Y7^UgW^nJ1nE3kbKzjAy0UwC3tOYZ66ZAIE8SLQ9ONWS5f<QQGPbQedBEzi?Po<5GA186Foty@R4ReRZLPLA`UM=PYH4B^>d0S`Nz?vJBb8NY^P<mvG[H;QhB^2fO?ppl:F0r?9_oM5o0Bm_tFBbFu6dEo][?:8_n[6K@5rXl2Q<:0k:H;p`pZU<@mIx3=@]s]HfLmce>;WWkAdBr]:tfTnlr1^`Ag@WMcUNv`N?tSTsX`bB\\nIexPzHebUhH;JM1IqlsYtQZq9t\\Nu>G<oZt]FpVQs5ztMsc8@f]UjCN:qT8wqDOrk[ab[aqV4]WyhRQ8p0ORLRyAy=m0Cbe_:xq9wDN>Kt>xi3mb9@h8th3g4Xnp=4`ov]RLR:tF7ag?YKir?I;??YR53H:L0@I[:jrmgSIQKMb:qlAmOk\\Wr4i@r<;XFB]JYeh^XFfUH`I>`8AT_3o^f7_;:whPWjrbRKooqw^B0tWaIPR8p0Ir?VZQP_y2YPFlR:k:nXjEt=K>Nq\\U:hy@L>p2SvMb:BhdoOro0>pXmy3FPbC1lMNYzMn502GqLzzeHpAOJaM>2qHZgGxHczbk0:91dbicONd8dFI5<qH:aoF:Qf48tGdKH8b6@B`kgt:pPZhc]lE@>sd<=Xb;aD_1UkmX>17l=6i;J:lGexdH\\?U@mq1Rx_>JjNLI=cPiSG7jOdt>N]wC@CgJal<1i4LlJsdl^bf[o^QYryhjHQfjBx9>U3RsJ\\]fOfX2D<aCjBjLe<qfrbOo]GBAb^:zC405jA:9H;2U:f^`PJ@d[xHi1<QNF2oh8WHSuOi?2Kj6tRz]pKznpX^=z]URd9z1jBAIlIb7q_hvy;R[elMH2dRQsnBO3C3o^c:a5dWJKy2]dmNugxUYtZmY2T3q1BEG9Bx>orzoSlkT]Fc2HP8TKA@3KHZZ`6FSHwqBz2_ONfm2GMTYRmu=igW=C]etvlUIP>FnF1jSbb^No1::9[6\\3K]5v5Aabh^RPUqvRyxuPShANnYAckkmUTDW=c111n@8BX3Es5>=Y:j]0bF;vPSbfxiHGaInp]MNx;`S:rlkqGg^gdc>e4NOAgE]8K<^HRPojYzFXlUKASdS:LHCGT]I=jU=`idbBcG>Mv4YkVJN]5`\\2Ftk97POcl^Iar@tuy\\xvjW>;>eT`07RBE3VY8]9UoqWWg7]8IH;wHFFyAP6DnB=D`vut9i9`N<L3YwN7\\2V2mz3W8t2iEUWASUBAo>o_3IPjroNbA?>Qlu?_WfmRJjF;3uKQ52@F]c7FYLQiazqTzH08g0KFa7gbb4UoulzDUVMO8Co:uc]s@:ME6>_;tJgWT=<wCeu=opIjLIetzo8t=mRVUj46IBviW<HB]6qXO`;pACP_msE7NVr:yQ^Jpj54KJYKmr8lwYj3uUUPrRipJPtgqYiEp\\W\\mlv9^n_5j`qKbD=j0w634oG;QTb[eJDY9kaNauPsf0T\\bxy;\\;ku:c7RT9f4WJ5iK>@[0rwp6P>BQP<Y:jbak]>tuZh=6Bw[6IQ38106;sk2OGAgCDfUu[2m[t;XrENYNEvMj]WfYe@t8>gU_[h6PK6NSvKrJQy9TUc_2C2E<KcG`vz5q=^q;dUfC1qMCIrp27xSs6tay6Od<9\\gvYj:I?0koC:>WPyM6Zz7\\GWQd<Me:=g]Ett\\SrVU7atv9=]M6GWW97H]nrQVcB1MSPg`dQX4M1:DIK6]jWPxJEOjePLK9sBFZ?niqraDOD>t;QN5;5QldaM8UQekeGulREcx?UGiRII<<8iQ3WPO]SZbB]s4e6<;KvPZ`bM;^17eubjWGNuYRnJjufivn[KVl@>b`jcMBNHECXrWbUFmiEBzmjH<PjAJc8]\\`Lt3:rlAupW9VK:2qu]axhR[ny2e>;?<jsVt>HUXZFv[t]LFbox<sbWxhZ@5vzV:p7N9w[ZJiA1dIK9PytR6jyxz0UzRr:cn4FQm_\\8wyB8@y_XSx<16KO9vJKuz]Rq=vIay@[DGTx^[z]ikIBS0\\tt1G\\K<H6M7eqedM9<85VRzoWOxSh<xB<_bh=SiMD1ToMTY`_6XOg:c1pRh9YYP<rj4h4auY`sj]0Zv92H5dXXWIo^2Bu8vfDwJS4LXorQ]]G_sAKQIF:Y`>CMTh9QlKc>unkoB>H]I9f6?gNJ6Dg_:0HmWj4L?pg<[A>_yuOjIXvh9P=PTDF>h2`quB=B^`=G5TpusJI\\UDx=Py\\ag`QP98ti7129SOMX^581vuPby^P`DNLACZGA6OHv@t6>Cs4MMj7RVc_\\PIubc;xKtjff1HB<cUBFMQ71_QeuA\\X_>RcTh<d^Rt25KEhzgTe<Sg<HVZdR6hd=pDa5qMO]PP_uS9Yg>`J6vRd9u8]tNW`b6Xy<t:XE>:@6gT=i?i4vbGVvH[2@SOtuormH:Ed1AvNWULf9M7APrclcfB<R?:zKpKiOK^dxVFiW:=F0?wahSb8B^8e4\\SG]=\\6E0360tLWX[ogK_\\9Dgg\\k]8xw=48H4^ExJ3JPX1nXT^X74N<@^m=O^=A`cBATp=<]GSlr;N[UnSNt4uY_bViPpql?Bd2BDel?kt?zA[IWTI_AdNwCwGAVDT3<NJ[[J9puQ9?6=W79s`=Btdv7usQp80x9Bp>?FzWGoc>HkC5^0qNZ;AapR2DKjNPG6KAUp>8jWBQ8gD[0p99Qt3N>k_\\PFJ?GZHgdb=Pt5Q8Wheq>sdsGGzv2^9jWV`P\\EO^\\J4df@zGvvR2z54vE1BDFgx_UB<wpWfWlLoZEfkyoDQ]:R]^iVzIS@u@hA`PAYi51wPQ;zfPIB[IN3kXoBge^^`H]xN[^ER^R[o2oe_E76i<Zb^56t>zRPn_4teVTh5lX><taBxgAnxGf^wjhbo75]]8I7j4j`grpkv;pKc`'
import random
def time(n=10000,i=10):
    sut = Solution()
    test = "".join([chr(random.randint(ord('0'),ord('z'))) for i in range(n)])
    print(test)
    def a(): sut.lengthOfLongestSubstringKDistinctSlow(test,5)
    def b(): sut.lengthOfLongestSubstringKDistinct(test,5)
    time_slow = timeit.timeit(a,number=i)
    time_fast = timeit.timeit(b,number=i)
    print("ORIGINAL TIME:\t%s" % time_slow)
    print("OPTIMIZED TIME:\t%s" % time_fast)

def test_longest_substring_k_distinct():
    sut = Solution()
    f = sut.lengthOfLongestSubstringKDistinct
    
    s = "A"
    k = 0
    expected = 0
    assert f(s,k) == expected, "TC1"        # PASS
    
    s = ""
    k = 10
    expected = 0
    assert f(s,k) == expected, "TC2"        # PASS
    
    s = "A"
    k = 1
    expected = 1
    assert f(s,k) == expected, "TC3"        # PASS
    
    s = "eceba"
    k = 2
    expected = 3
    assert f(s,k) == expected, "TC4"        # PASS

test_longest_substring_k_distinct()