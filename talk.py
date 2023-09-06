from manim_slide import *
import math

############################################################################################

# BG = "#161c20"
BG = "#101518"
# BG = "#0b0e10"

TEN_BLUE = BLUE
TEN_RED = RED
TEN_YELLOW = YELLOW_D
TEN_GREEN = GREEN
TEN_PURPLE = PURPLE
config.background_color = BG

############################################################################################

temp = TexTemplate()
temp.add_to_preamble(r"""
    \usepackage{stmaryrd,mathtools,marvosym,fontawesome}
    \newcommand{\comm}[2]     {\left\llbracket#1,#2\right\rrbracket}
    \newcommand{\bra}[1]      {\left\langle #1\right|}
    \newcommand{\ket}[1]      {\left|#1\right\rangle}
    \newcommand{\braket}[2]   {\left\langle #1\middle|#2\right\rangle}
    \newcommand{\ketbra}[2]   {\left|#1\middle\rangle\!\middle\langle#2\right|}
    \newcommand{\braopket}[3] {\left\langle #1\middle|#2\middle|#3\right\rangle}
    \newcommand{\proj}[1]     {\left| #1\middle\rangle\!\middle\langle#1\right|}
    \newcommand{\abs}[1]      {\left| #1 \right|}
    \newcommand{\norm}[1]     {\left\| #1 \right\|}
    \newcommand{\Tr}          {\mathrm{Tr}}
""")
temp.add_to_document(r"""
    \fontfamily{lmss}\selectfont
""")

def MyTex(*x,tex_environment="center",color=WHITE):
    return Tex(*x,
        tex_template=temp,
        tex_environment=tex_environment,
        color=color
    )

def MyMathTex(*x,tex_environment="align*",color=WHITE):
    return MyTex(*x,
        tex_environment=tex_environment,
        color=color
    )

def OffsetBezier(p1,o1,p2,o2,*x):
    return CubicBezier(
        p1,p1+o1,p2+o2,p2,*x)

# self.play(*[FadeOut(mob) for mob in self.mobjects if mob!=toc and mob!=footer])

############################################################################################
project_name = "Paris2023"

toc=VGroup(
    VGroup(
        MyTex(r"\bfseries Part 1:~Dimension 0"),
        MyTex(r"1.1:~TN introduction"),
        MyTex(r"1.2:~Linear Algebra"),
        MyTex(r"1.3:~Basic QI"),
    ),
    VGroup(
        MyTex(r"\bfseries Part 2:~Dimension 1"),
        MyTex(r"2.1:~Matrix Product States"),
        MyTex(r"2.2:~DMRG"),
        MyTex(r"2.3:~TEBD"),
    ),
    VGroup(
        MyTex(r"\bfseries Part 3:~Dimension 2"),
        MyTex(r"3.1:~2D contraction"),
        MyTex(r"3.2:~PEPS"),
        # MyTex(r"3.3:~Higher-dim TEBD"),
    ),
)
for t in toc:
    t[0].scale(6/8)
    t[1:].scale(5/8)
    t.arrange(DOWN,buff=1/4,aligned_edge=LEFT)
    t[0].shift(LEFT/2)
toc.arrange(DOWN,buff=1/2,aligned_edge=LEFT)
toc.move_to(ORIGIN)

footer=VGroup(
    MyTex(r"\faGithubSquare~$\texttt{chubbc/%s}$" % project_name),
    MyTex(r"\faExternalLinkSquare~$\texttt{christopherchubb.com/%s}$" % project_name),
    MyTex(r"\faTwitterSquare~\faYoutubePlay~$\texttt{@QuantumChubb}$"),
).arrange(RIGHT,buff=3).to_corner(DOWN).shift(0.5*DOWN).scale(1/2).set_opacity(.5)

############################################################################################

# Bentley Ottman stuff
big=True; width_thin=2.5; width_medium=5; width_thick=5
radius_int=0.025; radius_crosshair=0.1
time_shift=0; time_colour=0; time_indicate=0; time_wait=1/10; ints=[]
def findIntersection(A,B):
    (x1,y1,x2,y2)=A
    (x3,y3,x4,y4)=B
    if (x1,y1)==(x3,y3):# or (x2,y2)==(x4,y4):
        return None
    px= ( (x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4) ) / ( (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) )
    py= ( (x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4) ) / ( (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) )
    if px<=x1 or px>=x2 or px<=x3 or px>=x4:
        return None
    return (px, py, 0.0)
def checkIntersection(scene,i,M,R,m,r,Q,int_num):
    if m[i-1][:2]==m[i][:2]:
        return
    int = findIntersection(m[i-1],m[i])
    if not big:
        scene.play(
            M[i-1].animate.set_color(YELLOW).set_stroke(width=width_thick),
            M[i].animate.set_color(YELLOW).set_stroke(width=width_thick),
            # Transform(int_text[1],Text(str(int_num)).move_to(int_text[1]).scale(0.5)),
            run_time=time_indicate
        )
    if int==None:
        if not big:
            scene.play(
                M[i-1].animate.set_color(GREEN).set_stroke(width=width_medium),
                M[i].animate.set_color(GREEN).set_stroke(width=width_medium),
                run_time=time_indicate
            )
    if int!=None:
        C=Circle(radius_int,color=YELLOW).set_fill(YELLOW,opacity=1).move_to(int)
        ints.append(C)
        Q.append((int[0],int[1],'r'))
        Q.append((int[0],int[1],'r'))
        Q.append((int[0],int[1],'l'))
        Q.append((int[0],int[1],'l'))
        r.append((int[0],int[1],m[i][2],m[i][3]))
        R.append(Line([r[-1][0],r[-1][1],0],[r[-1][2],r[-1][3],0],stroke_width=width_thick,color=YELLOW))
        r.append((int[0],int[1],m[i-1][2],m[i-1][3]))
        R.append(Line([r[-1][0],r[-1][1],0],[r[-1][2],r[-1][3],0],stroke_width=width_thick,color=YELLOW))
        Q.sort(key=lambda x:x[0])

        scene.remove(M[i-1],M[i])
        m[i-1]=(m[i-1][0],m[i-1][1],int[0],int[1])
        m[i]=(m[i][0],m[i][1],int[0],int[1])
        M[i-1]=Line([m[i-1][0],m[i-1][1],0],[m[i-1][2],m[i-1][3],0],stroke_width=width_thick,color=YELLOW)
        M[i]=Line([m[i][0],m[i][1],0],[m[i][2],m[i][3],0],stroke_width=width_thick,color=YELLOW)
        if not big:
            scene.add(M[i-1],M[i],R[-2],R[-1])

        if not big:
            scene.play(
                FadeIn(C),
                Flash(C,flash_radius=.5),
                run_time=time_indicate
            )
        else:
            scene.add(C)
        scene.add_foreground_mobjects(C)
        if not big:
            scene.play(
                M[i-1].animate.set_color(GREEN).set_stroke(width=width_medium),
                M[i].animate.set_color(GREEN).set_stroke(width=width_medium),
                R[-2].animate.set_color(RED).set_stroke(width=width_thin),
                R[-1].animate.set_color(RED).set_stroke(width=width_thin),
                run_time=time_indicate
            )
        else:
            scene.add(
                M[i-1].set_color(GREEN).set_stroke(width=width_medium),
                M[i].set_color(GREEN).set_stroke(width=width_medium),
                R[-2].set_color(RED).set_stroke(width=width_thin),
                R[-1].set_color(RED).set_stroke(width=width_thin)
            )
def BO(self):
    # global big
    # global ints
    # global width_thin
    # global width_medium
    # global width_thick
    # global radius_int
    # global radius_crosshair
    # global time_shift
    # global time_colour
    # global time_indicate
    # global time_wait

    for r in [1]:

        int_num = 0;

        x1=[0.11493933380458837, 1.032577587887923, 1.57259368626231, 0.10947977441156963, 1.5483271062146389, 1.5831672441537312, 0.6226566034873973, 0.3150280154291049, 0.27799550590043454, 1.5829777459608483, 2.1863019496957694, 2.075233082457493, 1.767528406977902, 2.109158420791115, 2.3656973182664394, 2.3606096669388883, 0.9285568708598094, 1.696026949193289, 1.1020597899826752, 2.36432313785255, 2.1216831718090186, 1.8842342029638521, 3.034350463194465, 3.073357628180778, 2.869593335464893, 1.6660458546277677, 2.088559630460572, 3.201807323747802, 2.1431865013180658, 2.207980087195986, 3.780223245716716, 2.4849648099073987, 2.526581929371461, 3.4159579869502488, 3.4527196346219204, 3.624678094336166, 2.712443326208465, 3.27657604984964, 2.5302171703107192, 2.4437342168653062, 4.055496427927968, 3.3957895105277736, 3.2232218004568356, 4.111046934637176, 3.4041676209038427, 3.1510348750408537, 3.5551033700282986, 4.434728521395294, 4.28556444386915, 4.439144885540443, 4.59262927965325, 4.980217262292354, 5.296677370038571, 4.376214869283702, 4.023902152838578, 3.7144470017716777, 5.35136251832477, 5.33492861288324, 3.921737656865788, 4.332003537738292, 5.2537920222270476, 4.885417101306826, 6.1262769755824875, 5.267281668010867, 4.622597730101429, 5.5762687344353985, 5.5022595854972645, 5.207570537022315, 5.303557366099704, 5.938381215690296, 6.647389944391414, 6.150790943260413, 6.046121800778077, 6.773626071673727, 6.784286189589266, 6.467573892944444, 6.801699810526401, 6.115121655074915, 6.830703184205493, 6.12114739048844, 5.96635548353056, 7.771569745336433, 6.414011745003453, 6.8792425090548015, 6.885245296994751, 7.593880428152528, 6.163087376100378, 7.648009717233887, 6.830437535934872, 6.988108181490127, 7.8643466930757135, 7.017388729008823, 8.418128035835776, 8.084374002344749, 7.013770138375966, 7.100924221541914, 8.43263376852688, 7.191916864839956, 8.000701664025868, 8.298248620979953, 9.091415764987758, 7.634342360108446, 8.402750763463489, 9.040965143052983, 8.78950543757134, 8.971772320219928, 8.779781441655164, 8.737401528802689, 8.513158204562266, 8.111792083684046, 8.406179217717877, 9.712735200051965, 8.860869905074102, 8.817918061044384, 9.68013398076804, 8.966774953672234, 8.815937430659082, 9.56699344142437, 9.000315613922032, 9.339802956819774, 10.033724135759137, 9.198989838007922, 10.018712279105191, 9.693134563175624, 9.749065411656911, 10.082327431169855, 10.341066876320614, 10.204515997509416, 10.23083656330571, 9.576078622118738, 10.212843500940693, 10.105366894447934, 9.946033443723012, 10.170189483486691, 11.215348730483319, 11.23274108809946, 11.182972456401606, 10.81530037729945, 10.161944426639627, 11.26551064598933, 10.86585897189286, 11.883717555574364, 11.006625768141815, 10.572193928905826, 11.925586196847654, 10.626202299217388, 10.719417007855592, 12.065167860416688, 10.843072923759607, 11.482833529042162, 11.364024541514121, 12.873411416947338, 11.315478722124148, 12.21423235596041, 12.127917058105112, 11.756361971777071, 11.435770270365788, 12.36932082123891, 11.59659835522766, 12.381279971987743, 13.353505168609459, 12.107774555223987, 13.67217408603733, 12.822705406772117, 13.352675271533336, 13.698768540210972, 12.88992056662973, 13.231916852419872, 12.1142856898257, 13.238127460294782, 14.195969089009866, 14.253398931240108, 14.132542777532894, 13.607874800304183, 14.378802873242385, 13.950011217208562, 13.327681221746245, 14.07291535226767, 13.959882936008894, 14.46381596644848, 14.79119074928622, 14.157784781669926, 15.00775029797158, 13.605651283500032, 13.646100393286988, 15.08410995780659, 14.695452340883223, 14.157298894205443, 13.816987225479448, 13.84130286707715, 15.572105648457743, 14.989291000052328, 15.836646251654344, 14.988105767586909, 14.465584467401543, 14.577595998836644, 14.638936211898251, 14.619920764691607, 15.150829684270052, 14.584216125132647]
        x2=[1.7088581384455046, 0.6312579375280964, 0.3413639328650765, 1.561678707075797, 0.0, 0.019638844775074455, 1.1011334886851307, 1.5854826365310095, 1.4998544952475603, 0.1469738483583033, 1.1199305887597424, 1.3274890713366008, 1.6286171029617769, 1.227088468640776, 0.9114261006149807, 0.8426603829810911, 2.4068584162416746, 1.8648388672204992, 2.436646818306055, 0.9714211877789817, 2.665074885924928, 3.2066942315761846, 1.4998161212618932, 1.867570289035344, 1.9450237343287873, 3.228780435069475, 3.0438008240383136, 1.831635140720708, 2.7683231190730706, 2.5968733248361553, 2.3747624012379984, 3.844047713140313, 3.8760141916216857, 2.9387576977785055, 2.7658428137648627, 2.831381361388647, 3.6812514603064592, 3.3060920196226165, 3.9459738751999702, 3.787359315963348, 3.603230938549295, 4.145857855786865, 4.6323570087261094, 3.663822420348158, 4.26240856748801, 4.4714569819343, 4.281844715397794, 3.190454159296274, 3.262216560518987, 3.3810610625169084, 4.6052341350930055, 4.232210563484078, 3.765063695812228, 4.891033186156741, 5.3957417054168815, 5.36834487288248, 3.7394788118814573, 4.143302775493783, 5.542117571499854, 4.715445589852059, 5.320301257426527, 6.021642371898629, 4.703902987631475, 5.48669449494382, 6.239536893283754, 5.423855507479922, 5.04083568951724, 5.530595570447005, 5.6974446647918215, 4.98171299376519, 5.650710740659264, 5.780653373313112, 6.538034694275898, 5.608823678801783, 5.483437334352814, 5.912351859877528, 5.478657993499422, 5.790778048484352, 5.348244697538394, 6.12274552229153, 7.622730690193763, 6.112721510334819, 7.398923353175563, 6.728824790303581, 7.046408229409355, 6.17580580145615, 7.3032848651014755, 6.383317217000869, 6.866746475734069, 6.8345904810102684, 7.184469216944808, 8.089192718287437, 6.839107961868108, 7.066415587633836, 8.297126904647984, 8.249954343384445, 6.937287378489906, 8.05207902178774, 7.175411196905645, 7.089613336800285, 7.576568563535971, 9.098880849574254, 8.148834902729682, 7.603927155856869, 8.08572469178967, 7.809792351368217, 7.876917138707122, 8.149959180203357, 8.34965911184299, 8.834747212877685, 9.811569672553368, 8.400222945983163, 9.32403637553454, 9.339737820860051, 8.432485603464798, 9.20766081636843, 9.573967693353316, 8.852534661287683, 9.17985361549831, 8.900780913464335, 9.876288068366721, 10.477746498255815, 9.82907031131962, 9.870575283334018, 9.853756691754453, 9.93348247026053, 9.334483209546681, 9.721190139078818, 9.428098992040255, 10.246441831626301, 11.127482617354923, 10.906312703683193, 11.280217442281531, 11.347658182666832, 10.041464922754725, 9.991341364313161, 10.049646363892528, 10.34643638274621, 11.148306775424658, 9.89809909816464, 11.691909407186252, 10.846310231156334, 11.950989712862368, 11.878836962702376, 10.647846570767783, 12.024401538430936, 12.000771398906444, 10.524271691933844, 11.88899346745146, 11.353253186688415, 12.686543691178306, 11.281672769165128, 12.801745725036684, 11.684467399655631, 12.027719473409455, 12.138566637180967, 12.664310440731699, 12.018025101567424, 12.609216345971218, 11.776362559830506, 12.291203503153575, 13.419737468993333, 12.028618917451714, 12.678043408494409, 12.16836058111937, 12.06841043510512, 12.833524917246535, 12.572232753159827, 13.39743079231002, 12.407572899058284, 13.006773877561287, 13.136996368103059, 12.796986396336843, 13.792133428278765, 12.784692985295852, 13.200852903301435, 13.745619339358473, 13.219403809844225, 13.222593491658072, 12.84626552601209, 13.678261040192341, 14.440865791499476, 13.71588956141344, 14.931985723003468, 14.877382836985895, 13.667868818637412, 14.13006136781591, 14.623229558111472, 14.917597915034284, 15.105124110294259, 14.667113651942772, 15.039494677877242, 14.593760266960308, 15.085843483712985, 16.0, 15.725293925137457, 15.630259072212072, 15.596825237373181, 15.05532629912285, 15.64185981804377]
        y1=[1.5856561858976415, 4.443777891122051, 4.990914446085037, 6.175933490725344, 7.252486631542152, 8.708438135114536, 11.468876261122997, 12.413631897349806, 13.493858971236842, 14.887108602261515, 0.662970935645573, 2.27937394827739, 5.933319551143039, 6.798413677337944, 6.860426161187939, 9.39802129432178, 9.528792789646065, 10.357353235782877, 12.684608081258778, 15.239444918519249, 0.34650257534025714, 3.206125900057949, 4.074833148257337, 5.0825857538253345, 5.93963876348458, 9.043010798279097, 11.44878962811183, 10.765846207800658, 11.839848534289287, 12.85133545675168, 0.6654453647991352, 2.4531919668593973, 4.959394373506231, 4.235219117967593, 6.110730340292223, 7.451569214199452, 8.755466864997226, 10.00287884582712, 13.126339967841613, 13.905955290717285, 0.0, 4.044333673861601, 3.819275567227549, 4.254666955040691, 8.172865929687282, 9.057514910237703, 11.381311038420135, 10.709845631194845, 11.863038029147464, 15.113164500844135, 3.1055747481885883, 1.721330990751722, 3.8387137734936743, 7.0264600256148695, 7.584015384961737, 8.658464618907708, 9.846086699152908, 10.762517735458529, 13.210511453323637, 12.607989415423512, 0.3381935339770651, 2.4404212555019784, 4.583315417500095, 4.6138503242553845, 7.42822499759745, 9.936770551636549, 11.47459014923197, 9.787545481578631, 11.440564192736776, 15.48491930590339, 0.7481649526083546, 4.534430341450456, 2.8006936436150136, 4.996085996775795, 6.32221729004765, 7.743397459099875, 10.373651830579767, 10.14990340815141, 13.118350832787733, 15.768414024137673, 1.9575994396718641, 2.9269364840641257, 3.405192952055888, 7.428101692736269, 5.716116326269514, 8.851679274547903, 10.708076208254111, 10.727761350241284, 11.16429846035075, 13.061131114795248, 0.5621013829854493, 1.8625246188615983, 4.520968198763902, 4.992789315887424, 6.723334328159327, 9.657013319245111, 10.643356325461848, 10.353656040057231, 11.381978567124747, 13.335708014238431, 2.1551084911941008, 3.022642624440059, 3.2196774255217746, 6.574159094638301, 8.521452844275904, 7.812655460694102, 11.545866823161159, 10.256619251500668, 11.54390979275164, 15.405598633565928, 1.7830797012365005, 3.0947776635406985, 3.150883029900918, 7.40985969619531, 6.189836238503804, 7.255530927542582, 8.826729561628852, 12.441701038179701, 14.268743750872797, 13.044716653474081, 0.10671434512195421, 2.038219396036952, 5.725854625346177, 7.301860431603537, 8.404673461085709, 7.264286410315394, 8.961544723108227, 9.95504007754021, 14.234935918811539, 15.50515831822466, 2.4694514268791483, 1.699640162166485, 3.7232736447733172, 6.699438699383669, 8.227103994126574, 9.321290938638828, 11.01485240507028, 12.813799733551225, 13.926816489724482, 14.647454341172152, 3.1248205400565183, 2.0503064286272807, 2.9370918985718935, 6.277536657781565, 7.577442294714729, 8.839384100808909, 10.45297099290988, 11.03292697287972, 11.629606978025503, 16.0, 2.397180282008632, 3.546114819813145, 4.670599904883352, 4.645009836024881, 8.466732112135537, 7.267233580857886, 10.641441660133607, 12.649985221448508, 13.695219282926294, 15.217672147881188, 0.7890800539701236, 3.554974667030231, 4.621651296162111, 4.258693697728292, 6.2065895365695845, 8.697941951373359, 11.553222679646616, 10.118648614281268, 12.209618743145352, 15.618784974909207, 2.2436002698208903, 2.243938030316944, 5.055143950882703, 4.6115273212408106, 7.468876690123224, 7.434480889318309, 11.428557462664445, 12.590163268158696, 14.210064213698741, 14.5891907800736, 0.62831687571484, 1.6314857623487717, 5.5740243931258275, 5.883763044856005, 6.411294843088561, 8.353388110378917, 11.267512223796171, 10.241505346660677, 12.08360140681116, 13.571389483954508, 0.5557725365349845, 4.491512601510919, 3.5424507478404696, 4.380313851599532, 7.658783064541807, 9.539072703797844, 10.915241627011358, 12.441933150847248, 11.156845324645785, 15.42751990236369]
        y2=[1.3153590749925752, 1.57171284515969, 3.722603772147809, 5.918606429933606, 7.662400554833665, 8.239441701178494, 8.755760344718338, 10.477213196503222, 12.15892173656844, 13.95519439167614, 2.8168569217275325, 4.505444206348337, 2.980173394567716, 4.8842830699224855, 7.357076204356735, 8.550525250163323, 10.21517173597445, 13.175910677636068, 13.166176478667005, 13.514073987295795, 3.1128620305774244, 3.0360477884346118, 4.405641820560285, 6.742285127581572, 8.26389013561227, 8.07693680299838, 9.068487726324081, 12.418980109662932, 14.212477074044793, 15.566133857337318, 2.2901583485785495, 3.9026917429298096, 3.924245098407792, 7.163782935657489, 8.523930488355752, 9.492436834680127, 10.949607398856715, 13.108741437230508, 12.643697839132745, 14.959329764288972, 2.9937688938629012, 1.5580954062370496, 5.425163834039666, 7.226704873580419, 6.1686736980719425, 8.196255239005533, 8.76679932722849, 12.170832712925261, 14.001885106837673, 13.443683056711908, 0.5634408363784784, 4.0812649977247935, 4.89639757772385, 4.5632513068150296, 6.865184234035734, 8.73675371415092, 10.34325871443951, 12.297189690091168, 12.910308173855864, 15.486232877335995, 2.8008311767485217, 3.704128383760019, 4.89798182487452, 7.1559542180213676, 7.119050041160789, 7.436465599917057, 8.561222475683092, 12.705792612887766, 14.079998816460058, 13.106660991285663, 2.6163208980857684, 1.8137523302281657, 5.663837323318572, 6.46300711020778, 8.273841406554332, 10.044134614739521, 9.212239517651364, 12.824250121990266, 12.288293442664227, 13.006669419561646, 1.5785607194210745, 3.1651138094691462, 5.318439227567184, 4.46212027690151, 8.315908167265123, 8.384038796902988, 9.387452125897624, 12.310295418645138, 14.037507718546175, 15.823366810084684, 3.2224345874265965, 3.407557193147304, 4.030843792451135, 6.63966575931723, 7.740924824087859, 7.803584302562989, 9.395354307719431, 12.551654569372293, 14.119700105406075, 15.503591711534416, 0.808512118718929, 3.0141608235190915, 5.935451382952144, 5.040518615568268, 5.884019589361578, 9.037960938401854, 8.998146676893438, 12.802131796674715, 14.137630876911986, 12.92724749359471, 1.3362003507153535, 2.967918366691506, 5.924952971342003, 4.441287615064988, 8.29258566575253, 10.00077300843135, 11.101989801804196, 10.358070022436456, 11.315128225427546, 15.428249114540536, 2.614752631666064, 4.0149360177526665, 3.190140808083258, 4.7146399031232935, 5.884435924365336, 10.120101044388738, 11.163733324441438, 12.901877353589596, 11.773691283426905, 12.850755136074783, 0.7098563703064423, 4.299841983934877, 4.92296090463545, 4.713596627734442, 6.68105134965068, 7.559744951716793, 9.737065188177766, 10.4301486081612, 11.782909597093196, 13.634428901767846, 0.3889280794130778, 3.8314733997426007, 5.353274051829527, 5.388164687545803, 6.337119188328112, 8.861256599734412, 9.684466003171137, 11.90853723044623, 13.89499643231836, 12.916966718206597, 0.8925231128379615, 2.6975304153957826, 4.333740330390614, 7.1926476738053555, 5.5896158956007, 10.035007315091432, 9.587929993061424, 10.213724392028425, 11.972401051261821, 12.907469259541475, 2.640954970536358, 2.6123319773758644, 4.0454144628811, 7.071552044618608, 7.751359656214497, 8.48342554568709, 8.925241805761633, 12.942503876079284, 13.249144371543332, 13.450595248553356, 0.3349199764974009, 3.9093407343123054, 4.126798627478502, 7.148256555578529, 6.828622655546672, 9.658114447346836, 8.618619178784504, 10.221904486186933, 11.666765336059413, 13.810567184974742, 2.4913540549368967, 4.517477619013386, 3.83326441878995, 6.320102116867833, 7.742081506838137, 9.203091317790816, 8.746891226279352, 12.854658028715873, 13.527228180797813, 14.499829546774645, 2.5195137372151146, 1.5693678761583874, 4.764019028251394, 6.898057260479723, 6.78528599209355, 7.82966406461238, 9.036143237679704, 10.273061663661474, 14.280562846076092, 13.374449153577311]
        n=100
        p=np.random.permutation(len(x1))[:n]
        x1=[x1[i] for i in p]
        x2=[x2[i] for i in p]
        y1=[y1[i] for i in p]
        y2=[y2[i] for i in p]

        # x1=x1[::2]
        # x2=x2[::2]
        # y1=y1[::2]
        # y2=y2[::2]
        for i in range(len(x1)):
            x1[i]=1.25*(x1[i]-8)+8
            x2[i]=1.25*(x2[i]-8)+8
            y1[i]=1.25*(y1[i]-8)+8
            y2[i]=1.25*(y2[i]-8)+8
            if x1[i]>x2[i]:
                x1[i],x2[i]=x2[i],x1[i]

        r=[(.6*(x1[i]-8),.25*(y1[i]-9),.6*(x2[i]-8),.25*(y2[i]-9)) for i in range(len(x1))]
        R=[Line([r[i][0],r[i][1],0],[r[i][2],r[i][3],0],stroke_width=width_thin,color=RED) for i in range(len(r))]
        m=[]
        M=[]
        l=[]
        L=[]

        Q=[*[(rr[0],rr[1],'l') for rr in r],*[(rr[2],rr[3],'r') for rr in r]]
        Q.sort(key=lambda x:x[0])

        # self.play(FadeIn(subtitle))
        self.play(*[Write(r) for r in R])
        self.slide_break()

        S=DashedLine([-6.25,-3,0],[-6.25,2.5,0],dash_length=.1)
        P0=Circle(radius_crosshair,BG).move_to(S).set_fill(BG,opacity=1)
        P1=Circle(radius_crosshair,WHITE).move_to(S)
        self.play(FadeIn(S,shift=RIGHT))
        self.slide_break()

        self.bring_to_front(*R)

        done_break=False

        while len(Q)>0:
            print("len(Q) = ",len(Q))
            q=Q.pop(0)
            print("x = ",q[0])
            print("int_num = ",int_num)
            if int_num>=100 and done_break==False:
                done_break=True
                self.slide_break()
            if S.get_x()!=q[0]:
                self.wait(time_wait)
                if time_shift>0:
                    self.play(
                        S.animate.move_to(q[0]*RIGHT+S.get_y()*UP),
                        run_time=time_shift
                    )
                else:
                    S.move_to(q[0]*RIGHT+S.get_y()*UP)
            if q[2]=='l':
                ind=[i for i in range(len(r)) if q[:2]==r[i][:2]][0]
                m.append(r.pop(ind))
                M.append(R.pop(ind))
                n=len(m)-1
                while n>0:
                    if m[n][:2]==m[n-1][:2] and m[n-1][3]>m[n][3]:
                        break
                    Y = ((m[n-1][3]-m[n-1][1])*q[0] - m[n-1][0]*m[n-1][3] +m[n-1][1]*m[n-1][2] ) /(m[n-1][2]-m[n-1][0])
                    if m[n][-2:]!=m[n-1][-2:] and Y>q[1]:
                        break

                    m[n-1],m[n]=m[n],m[n-1]
                    M[n-1],M[n]=M[n],M[n-1]
                    n-=1
                if time_colour>0:
                    self.play(M[n].animate.set_color(GREEN).set_stroke(width=width_medium),run_time=time_colour)
                else:
                    M[n].set_color(GREEN).set_stroke(width=width_medium)
                if n>0:
                    int_num+=1
                    checkIntersection(self,n,M,R,m,r,Q,int_num)
                if n<len(m)-1:
                    int_num+=1
                    checkIntersection(self,n+1,M,R,m,r,Q,int_num)

            else:
                ind=[i for i in range(len(m)) if q[:2]==m[i][-2:]][0]
                if time_colour>0:
                    self.play(M[ind].animate.set_color(BLUE).set_stroke(width=width_thin),run_time=time_colour)
                else:
                    M[ind].set_color(BLUE).set_stroke(width=width_thin)
                # self.wait(.1)
                l.append(m.pop(ind))
                L.append(M.pop(ind))
                if len(M)>1 and ind!=0 and ind!=len(M):
                    int_num+=1
                    checkIntersection(self,ind,M,R,m,r,Q,int_num)

        if time_shift>0:
            self.play(
                S.animate.move_to(6.25*RIGHT+UP*S.get_y()),
                run_time=time_shift
            )
        else:
            S.move_to(6.25*RIGHT+UP*S.get_y())

        self.wait()

        self.play(
            FadeOut(S,shift=RIGHT)
        )
        self.slide_break()
        self.play(*[Unwrite(l) for l in L],*[Unwrite(c) for c in ints])
        self.slide_break()

############################################################################################


class Title(SlideScene):
    def construct(self):
        title = MyTex(r"{Tensor networks}").scale(3).shift(2.75*UP)
        loc = MyTex("QI Paris Summer School '23").shift(1.25*UP)
        arxiv = MyTex(r"Loosely based on \texttt{arXiv:1603.03039}").scale(.75)#.shift(UP/2)
        name = MyTex(r"\em{Christopher T.\ Chubb}").shift(1.25*DOWN).scale(1)
        ethz = SVGMobject("ethz_logo_white.svg").scale(1/4).shift(2*DOWN)
        footer_big=footer.copy().arrange(RIGHT,buff=.375).to_corner(DOWN).shift(0.25*UP).scale(1.25).set_opacity(1)

        self.add(title,loc,arxiv,name,ethz,footer_big)

        self.play(Unwrite(loc),Unwrite(arxiv),Unwrite(name),Unwrite(ethz))#,Unwrite(title))
        self.play(ReplacementTransform(footer_big,footer),Transform(title,MyTex("Tensor networks").scale(2).to_corner(UP)))
        self.slide_break()

        # self.play(Write(heading))
        points=VGroup(
            MyTex(r"\textbullet~Notation to study multi-linear operations"),
            MyTex(r"\textbullet~Middleground between Penrose and string diagrams"),
            MyTex(r"\textbullet~Makes certain things `obvious'"),
            MyTex(r"\textbullet~Scales better than Einstein notation"),
        ).scale(7/8).arrange(DOWN,aligned_edge=LEFT)
        images=Group(
            Group(),
            Group(
                ImageMobject("string1.png").scale(1.2),
                ImageMobject("string2.png"),
                ImageMobject("string3.png").scale(1.2).shift(UP/2),
            ),
            Group(
                ImageMobject("cyclic.png").scale(1.5).shift(DOWN*1.5),
            ),
            Group(
                ImageMobject("HaPPY2.png").scale(1.2),
            ),
        ).shift(DOWN/2)

        for i in range(len(points)):
            self.play(Write(points[i]))
            self.slide_break()
            for im in images[i]:
                self.play(FadeIn(im))
                self.slide_break()
                self.play(FadeOut(im))
                self.slide_break()

        self.play(FadeOut(points))
        self.slide_break()
        citations=VGroup(
            MyMathTex(r"\text\textbullet~&\textbf{DMRG \& DMRG in the age of MPS}\\&\qquad\textit{U.\ Schollwoeck}~(\text{2004, }\texttt{arxiv:cond-mat/0409292})~(\text{2010, }\texttt{arxiv:1008.3477})"),

            MyMathTex(r"\text\textbullet~&\textbf{Matrix product state representations}\\&\qquad\textit{D.\ Perez-Garcia, F.\ Verstraete, M.M.\ Wolf}~(\text{2008, }\texttt{arxiv:quant-ph/0608197})"),

            MyMathTex(r"\text\textbullet~&\textbf{Matrix product states, projected entangled pair states}\\&\qquad\textit{F.\ Verstraete, V.\ Murg, J.I.\ Cirac}~(\text{2009, }\texttt{arxiv:0907.2796})"),

            MyMathTex(r"\text\textbullet~&\textbf{A practical introduction to tensor networks}\\&\qquad\textit{R.\ Orus}~(\text{2013, }\texttt{arxiv:1306.2164})"),

            MyMathTex(r"\text\textbullet~&\textbf{Hand-waving and Interpretive Dance}\\&\qquad\textit{CTC and J.\ Bridgeman}~(\text{2016, }\texttt{arXiv:1603.03039})"),

            MyMathTex(r"\text\textbullet~&\textbf{Matrix product states and projected entangled pair states}\\&\qquad\textit{J.I.\ Cirac, D.\ Perez-Garcia, N.\ Schuch, F.\ Verstraete}~(\text{2020, }\texttt{arxiv:2011.12127})"),

            MyMathTex(r"\text\textbullet~&\textbf{ITensor}, \textit{Flatiron Institute, }\texttt{itensor.org}")
        ).scale(1/2).arrange(DOWN,aligned_edge=LEFT).shift(DOWN/4)
        citations[4].set_color(YELLOW)
        self.play(Write(citations))
        self.slide_break()

        self.play(FadeOut(citations),FadeOut(title))
        self.slide_break()

        self.play(FadeIn(toc))
        self.slide_break()

        for i in range(3):
            self.play(
                toc.animate.set_color(WHITE),
                toc[i].animate.set_color(YELLOW),
            )
            self.slide_break()

        self.play(toc.animate.set_color(WHITE))
        self.slide_break()

        self.play(
            toc[1:].animate.set_opacity(.25),
        )

#
class Lec1_1(SlideScene):
    def construct(self):
        tocindex=(0,1)
        toc.set_opacity(0.25)
        toc[tocindex[0]].set_opacity(1)
        toc.save_state()
        heading = toc[tocindex[0]][tocindex[1]]
        self.add(toc,footer)
        self.play(
            toc.animate.set_opacity(0),
            heading.animate.scale(2).to_corner(UP).set_x(0),
        )
        heading.set_opacity(1)
        self.slide_break()

        subsec = -1
        # 1     what is a tensor
        # 2     Reimann
        # 3     Penrose
        # 4     Unitary
        # 5     addition
        # 6     ten product
        # 7     trace
        # 8     contract
        # 9     examples
        # 10    grouping
        # 11    TN
        # 12    cyclic
        # 13    ladder 1
        # 14    ladder 2

        if subsec==1 or subsec==-1:
            what=MyTex("What is a tensor?").scale(1.5)
            self.play(Write(what))
            self.slide_break()

            ten=MyMathTex(r"\text{index assignments}",r"\quad\to\quad",r"\text{values}").shift(DOWN)
            ten=VGroup(*ten)
            self.play(what.animate.shift(1*UP))
            self.play(FadeIn(ten))
            self.slide_break()

            X=MyMathTex(r"[d_1]\times\dots\times[d_r]").move_to(ten[0],aligned_edge=RIGHT)
            self.play(FadeTransform(ten[0],X))
            ten[0]=X
            self.slide_break()

            X=MyMathTex(r"\mathbb{R}\text{ or }\mathbb{C}").move_to(ten[2],aligned_edge=LEFT)
            self.play(FadeTransform(ten[2],X))
            self.slide_break()
            ten[2]=X

            self.play(FadeOut(ten),FadeOut(what))
            self.slide_break()
        if subsec==2 or subsec==-1:
            ten=VGroup(
                MyMathTex(r"R^{\rho}_{~\sigma\mu\nu}"),
                MyMathTex(r"\longrightarrow"),
                VGroup(
                    Line(start=ORIGIN,end=UP),
                    Line(start=ORIGIN,end=DOWN),
                    # Line(start=[-0.5*np.sin(.5),-0.5*np.cos(.5),0],end=[-np.sin(.5),-np.cos(.5),0]),
                    # Line(start=[0.5*np.sin(.5),-0.5*np.cos(.5),0],end=[np.sin(.5),-np.cos(.5),0]),
                    Line(start=ORIGIN,end=[-np.sin(.5),-np.cos(.5),0]),
                    Line(start=ORIGIN,end=[np.sin(.5),-np.cos(.5),0]),
                    Circle(radius=0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE),
                    MyTex(r"$R$",color=BLACK),
                )
            ).arrange(RIGHT,buff=1)
            ten.save_state()
            ten.set_color(BG)
            self.add(ten)
            self.play(Restore(ten))
            self.slide_break()
            self.play(ten.animate.set_color(BG))
            self.remove(ten)
            self.slide_break()
        if subsec==3 or subsec==-1:
            penrose=VGroup(
                Line([0,0,0],[0,0,0]+DOWN),
                Line([0.75,0,0],[0.75,0,0]+DOWN),
                Line([1.625,1,0],[1.625,0,0]+DOWN),
                Line([2,1.75,0],[2,2.25,0]+UP),
                Circle(radius=1,fill_opacity=1,color=TEN_BLUE).move_to([0.5,1,0]),
                Polygon(*[
                    [-0.5,1,0],
                    [-0.5,0,0],
                    [1.25,0,0],
                    [1.25,.25,0],
                    [2,.25,0],
                    [2.5,2,0],
                    [0.5,2,0]
                ],color=TEN_BLUE,fill_opacity=1),
                Line(start=[-0.5,0,0],end=[1.25,0,0]),
                Line(start=[-0.5,0,0],end=[-0.5,1,0]),
                Line(start=[1.25,0,0],end=[1.25,.25,0]),
                Line(start=[1.25,.25,0],end=[2,.25,0]),
                Line(start=[2,.25,0],end=[2.5,2,0]),
                Line(start=[2.5,2,0],end=[0.5,2,0]),
                ArcBetweenPoints(start=[-0.5,1,0],end=[0.5,2,0],angle=-TAU/4),
            ).move_to(ORIGIN).scale(0.75)
            penrose.save_state()
            penrose.set_color(BG)
            self.play(Restore(penrose))
            self.slide_break()
            self.play(penrose.animate.set_color(BG))
            self.remove(penrose)
            self.slide_break()
        if subsec==4 or subsec==-1:
            unitary=VGroup(
                VGroup(
                    Line(start=0.75*LEFT,end=0.75*LEFT+1*DOWN),
                    Line(start=0.75*RIGHT,end=0.75*RIGHT+1*DOWN),
                    Line(start=ORIGIN,end=1*DOWN),

                    Line(start=.375*LEFT,end=0.375*LEFT+1*UP),
                    Line(start=.375*RIGHT,end=0.375*RIGHT+1*UP),

                    Polygon(
                        [-1.5,-.5,0],
                        [1.5,-.5,0],
                        [.75,.5,0],
                        [-.75,.5,0],
                        color=WHITE,
                        fill_color=TEN_BLUE,
                        fill_opacity=1,
                    ).scale(0.75),
                ),
                MyTex(r"$\longrightarrow$"),
                VGroup(
                    Line(start=DOWN,end=UP).shift(0.75*LEFT),
                    Line(start=DOWN,end=UP).shift(0.75*RIGHT),
                    Line(start=DOWN,end=UP),

                    Line(start=.5*DOWN,end=.5*UP).shift(1.75*UP+.375*LEFT),
                    Line(start=.5*DOWN,end=.5*UP).shift(1.75*UP+.375*RIGHT),
                    Line(start=.5*DOWN,end=.5*UP).shift(1.75*DOWN+.375*LEFT),
                    Line(start=.5*DOWN,end=.5*UP).shift(1.75*DOWN+.375*RIGHT),

                    Polygon(
                        [-1.5,.5,0],
                        [1.5,.5,0],
                        [.75,1.5,0],
                        [-.75,1.5,0],
                        color=WHITE,
                        fill_color=TEN_BLUE,
                        fill_opacity=1,
                    ).scale(0.75),
                    Polygon(
                        [-1.5,-.5,0],
                        [1.5,-.5,0],
                        [.75,-1.5,0],
                        [-.75,-1.5,0],
                        color=WHITE,
                        fill_color=TEN_BLUE,
                        fill_opacity=1,
                    ).scale(0.75),
                    MyMathTex("=").shift(2*RIGHT),
                    Line(start=1.5*DOWN,end=1.5*UP).shift(3.5*RIGHT+.375*LEFT),
                    Line(start=1.5*DOWN,end=1.5*UP).shift(3.5*RIGHT+.375*RIGHT),
                ).scale(0.75),
            ).scale(0.75).arrange(RIGHT,buff=1.25).move_to(ORIGIN)

            unit0=unitary[0].copy().move_to(ORIGIN)
            unit0.save_state()
            unit0.set_color(BG)
            self.play(Restore(unit0))
            self.slide_break()

            self.remove(unit0)
            unitary[0].save_state()
            unitary[0].move_to(ORIGIN)
            otherunit=VGroup(*unitary[1:])
            otherunit.save_state()
            otherunit.set_color(BG)
            self.play(Restore(unitary[0]))
            self.play(Restore(otherunit))
            self.slide_break()
            self.play(unitary.animate.set_color(BG))
            self.remove(unitary)
            self.slide_break()
        if subsec==5 or subsec==-1:
            addition=VGroup(
                VGroup(
                    Line(start=ORIGIN,end=UP),
                    Line(start=ORIGIN,end=[-np.sin(.5),-np.cos(.5),0]),
                    Line(start=ORIGIN,end=[np.sin(.5),-np.cos(.5),0]),
                    Circle(.5,fill_opacity=1,color=WHITE,fill_color=TEN_GREEN),
                    MyMathTex("i").move_to(1.35*UP).set_opacity(0),
                    MyMathTex("j~~~~~~k").move_to(1.2*DOWN).set_opacity(0),
                ),
                MyMathTex(r"\qquad\qquad\qquad\qquad=\qquad"),
                VGroup(
                    Line(start=ORIGIN,end=UP),
                    Line(start=ORIGIN,end=[-np.sin(.5),-np.cos(.5),0]),
                    Line(start=ORIGIN,end=[np.sin(.5),-np.cos(.5),0]),
                    Circle(.5,fill_opacity=1,color=WHITE,fill_color=TEN_BLUE),
                    MyMathTex("i").move_to(1.35*UP).set_opacity(0),
                    MyMathTex("j~~~~~~k").move_to(1.2*DOWN).set_opacity(0),
                ),
                MyMathTex(r"+"),
                VGroup(
                    Line(start=ORIGIN,end=UP),
                    Line(start=ORIGIN,end=[-np.sin(.5),-np.cos(.5),0]),
                    Line(start=ORIGIN,end=[np.sin(.5),-np.cos(.5),0]),
                    Circle(.5,fill_opacity=1,color=WHITE,fill_color=TEN_YELLOW),
                    MyMathTex("i").move_to(1.35*UP).set_opacity(0),
                    MyMathTex("j~~~~~~k").move_to(1.2*DOWN).set_opacity(0),
                ),
            ).arrange(RIGHT)
            addition[0].shift(.25*LEFT)
            addition[2:].shift(.25*RIGHT)
            addition.move_to(ORIGIN)
            addition.save_state()
            addition.set_color(BG)
            self.play(Restore(addition))
            self.slide_break()
            self.play(addition.animate.set_opacity(1))
            self.slide_break()
            self.play(addition.animate.set_color(BG))
            self.remove(addition)
            self.slide_break()
        if subsec==6 or subsec==-1:
            tenproduct=VGroup(
                VGroup(
                    Line(start=ORIGIN,end=DOWN).shift(.5*LEFT),
                    Line(start=ORIGIN,end=[-np.sin(.5),1,0]).shift(.5*LEFT),
                    Line(start=ORIGIN,end=[np.sin(.5),1,0]).shift(.5*LEFT),

                    Line(start=ORIGIN,end=UP).shift(.5*RIGHT),
                    Line(start=ORIGIN,end=DOWN).shift(.5*RIGHT),

                    Ellipse(width=2,height=1,fill_opacity=1,color=WHITE,fill_color=TEN_GREEN),
                    MyMathTex(r"\alpha~~~~\beta~~i").move_to(1.3*UP+0.2*LEFT).set_opacity(0),
                    MyMathTex(r"\gamma~~~~j").move_to(1.3*DOWN).set_opacity(0),
                ),
                MyMathTex(r"="),
                VGroup(
                    Line(start=ORIGIN,end=DOWN),
                    Line(start=ORIGIN,end=[-np.sin(.5),np.cos(.5),0]),
                    Line(start=ORIGIN,end=[np.sin(.5),np.cos(.5),0]),
                    Circle(.5,fill_opacity=1,color=WHITE,fill_color=TEN_BLUE),
                    MyMathTex(r"\alpha~~~~~~\beta").move_to(1.3*UP).set_opacity(0),
                    MyMathTex(r"\gamma").move_to(1.3*DOWN).set_opacity(0),
                ),
                MyMathTex(r"\times").set_opacity(0),
                VGroup(
                    Line(start=ORIGIN,end=UP),
                    Line(start=ORIGIN,end=DOWN),
                    Circle(.5,fill_opacity=1,color=WHITE,fill_color=TEN_YELLOW),
                    MyMathTex("i").move_to(1.3*UP).set_opacity(0),
                    MyMathTex("j").move_to(1.3*DOWN).set_opacity(0),
                ),
            ).arrange(RIGHT)
            tenproduct[0].shift(.25*LEFT)
            tenproduct[2:].shift(.25*RIGHT)
            tenproduct.save_state()
            tenproduct.set_color(BG)
            self.play(Restore(tenproduct))
            self.slide_break()
            self.play(tenproduct.animate.set_opacity(1))
            self.slide_break()
            self.play(tenproduct.animate.set_color(BG))
            self.remove(tenproduct)
            self.slide_break()
        if subsec==7 or subsec==-1:
            trace=VGroup(
                VGroup(
                    Line(start=ORIGIN,end=LEFT),
                    Line(start=ORIGIN,end=UR/np.sqrt(2)),
                    Line(start=ORIGIN,end=DR/np.sqrt(2)),
                    Circle(0.5,fill_opacity=1,color=WHITE,fill_color=TEN_RED),
                    CubicBezier(UR/np.sqrt(2),1.5*UR,1.5*DR,DR/np.sqrt(2)).set_color(BG),
                    MyMathTex(r"i").move_to(1.3*LEFT).set_opacity(0),
                ),
                MyMathTex(r":="),
                VGroup(
                    Line(start=ORIGIN,end=LEFT),
                    Line(start=ORIGIN,end=UR/np.sqrt(2)),
                    Line(start=ORIGIN,end=DR/np.sqrt(2)),
                    Circle(0.5,fill_opacity=1,color=WHITE,fill_color=TEN_RED),
                    MyMathTex(r"i").move_to(1.3*LEFT),
                    MyMathTex(r"j").move_to(1.1*RIGHT+.8*UP),
                    MyMathTex(r"j").move_to(1.1*RIGHT+.8*DOWN),
                    MyMathTex(r"\sum_j").move_to(2*LEFT+0.2*DOWN),
                ),
            ).arrange(RIGHT,buff=1.5).move_to(ORIGIN)
            trace[-1].shift(LEFT/2)
            x=trace[0].get_x()
            trace[0].shift(LEFT*x)
            trace[0].save_state()
            trace[0].set_color(BG)
            self.play(Restore(trace[0]))
            self.slide_break()
            trace[0][-2].set_color(WHITE)
            self.play(Write(trace[0][-2]))
            self.slide_break()
            self.play(trace[0][-1].animate.set_opacity(1))
            self.slide_break()
            self.play(trace[0].animate.move_to(x*RIGHT))
            trace[1].save_state()
            trace[2].save_state()
            trace[1:].set_color(BG)
            self.play(Restore(trace[1]),Restore(trace[2]))
            self.slide_break()
            self.play(trace.animate.set_color(BG))
            self.remove(trace)
            self.slide_break()
        if subsec==8 or subsec==-1:
            contract=VGroup(
                VGroup(
                    Line(start=1.5*LEFT,end=2*LEFT),
                    Line(start=1.5*RIGHT,end=2*RIGHT),
                    CubicBezier(LEFT,0.75*UP,0.75*UP,RIGHT),
                    CubicBezier(LEFT,0.75*DOWN,0.75*DOWN,RIGHT),
                    Circle(0.5,fill_opacity=1,color=WHITE,fill_color=TEN_BLUE).shift(LEFT),
                    Circle(0.5,fill_opacity=1,color=WHITE,fill_color=TEN_RED).shift(RIGHT),
                    MyMathTex(r"i").move_to(2.3*LEFT),
                    MyMathTex(r"j").move_to(2.3*RIGHT),
                ),
                MyMathTex(r":="),
                MyMathTex(r"\sum_{\alpha,\beta}"),
                VGroup(
                    Line(start=ORIGIN,end=LEFT),
                    Line(start=ORIGIN,end=UR/np.sqrt(2)),
                    Line(start=ORIGIN,end=DR/np.sqrt(2)),
                    Circle(0.5,fill_opacity=1,color=WHITE,fill_color=TEN_BLUE),
                    MyMathTex(r"i").move_to(1.3*LEFT),
                    MyMathTex(r"\alpha").move_to(1.1*RIGHT+.8*UP),
                    MyMathTex(r"\beta").move_to(1.1*RIGHT+.8*DOWN),
                ),
                MyMathTex(r"\times"),
                VGroup(
                    Line(start=ORIGIN,end=-LEFT),
                    Line(start=ORIGIN,end=-UR/np.sqrt(2)),
                    Line(start=ORIGIN,end=-DR/np.sqrt(2)),
                    Circle(0.5,fill_opacity=1,color=WHITE,fill_color=TEN_RED),
                    MyMathTex(r"j").move_to(-1.3*LEFT),
                    MyMathTex(r"\alpha").move_to(-1.1*RIGHT+.8*UP),
                    MyMathTex(r"\beta").move_to(-1.1*RIGHT+.8*DOWN),
                ),
            ).arrange(RIGHT,buff=.25)
            contract[:2].shift(0.25*LEFT)
            contract[2].shift(0.125*DOWN)
            contract.move_to(ORIGIN)
            x=contract[0].get_x()
            for i in range(1,6):
                contract[i].save_state()
            contract[0][-2:].set_opacity(0)
            contract[0].shift(x*LEFT)
            contract[0].save_state()
            contract.set_color(BG)
            self.play(Restore(contract[0]))
            self.slide_break()
            self.play(contract[0].animate.shift(x*RIGHT))
            self.play(contract[0][-2:].animate.set_opacity(1))
            self.play(*[Restore(contract[i]) for i in range(1,6)])
            self.slide_break()
            self.play(contract.animate.set_color(BG))
            self.remove(contract)
            self.slide_break()
        if subsec==9 or subsec==-1:
            examples=VGroup(
                MyTex(r"Conventional"),
                MyTex(r"Einstein"),
                MyTex(r"Tensor network"),

                MyMathTex(r"\langle\vec{x},\vec{y}\rangle"),
                MyMathTex(r"x_\mu y^\mu"),
                VGroup(
                    Line(start=RIGHT/2,end=LEFT/2),
                    Square(side_length=1,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(LEFT),
                    Square(side_length=1,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(RIGHT),
                    MyMathTex(r"x",color=BLACK).shift(LEFT),
                    MyMathTex(r"y",color=BLACK).shift(RIGHT),
                ).scale(0.75),

                MyMathTex(r"M\vec{v}"),
                MyMathTex(r"M^{\mu}_{~\nu}v^\nu"),
                VGroup(
                    Line(start=RIGHT/2,end=LEFT/2),
                    Line(start=3*LEFT/2,end=4*LEFT/2),
                    Square(side_length=1,color=WHITE,fill_opacity=1,fill_color=TEN_RED).shift(LEFT),
                    Square(side_length=1,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(RIGHT),
                    MyMathTex(r"M",color=BLACK).shift(LEFT),
                    MyMathTex(r"v",color=BLACK).shift(RIGHT),
                ).scale(0.75),

                MyMathTex(r"AB"),
                MyMathTex(r"A^{\mu}_{~\rho}B^{\rho}_{~\nu}"),
                VGroup(
                    Line(start=RIGHT/2,end=LEFT/2),
                    Line(start=3*LEFT/2,end=4*LEFT/2),
                    Line(start=3*RIGHT/2,end=4*RIGHT/2),
                    Square(side_length=1,color=WHITE,fill_opacity=1,fill_color=TEN_RED).shift(LEFT),
                    Square(side_length=1,color=WHITE,fill_opacity=1,fill_color=TEN_RED).shift(RIGHT),
                    MyMathTex(r"A",color=BLACK).shift(LEFT),
                    MyMathTex(r"B",color=BLACK).shift(RIGHT),
                ).scale(0.75),

                MyMathTex(r"\mathrm{Tr}(T)"),
                MyMathTex(r"T^{\mu}_{~\mu}"),
                VGroup(
                    Square(side_length=1,color=WHITE,fill_opacity=1,fill_color=TEN_RED),
                    MyMathTex(r"T",color=BLACK),
                    ArcBetweenPoints(start=LEFT/2,end=LEFT/2+DOWN,angle=TAU/2),
                    ArcBetweenPoints(start=RIGHT/2+DOWN,end=RIGHT/2,angle=TAU/2),
                    Line(start=LEFT/2+DOWN,end=RIGHT/2+DOWN),
                ).scale(0.75),
            ).arrange_in_grid(rows=5,cols=3,buff=.25)
            examples[8].shift(LEFT*.75/4)
            examples[0::3].shift(LEFT/2)
            examples[2::3].shift(RIGHT/2)
            for i in range(3):
                self.play(Write(examples[i]))
            self.slide_break()
            for i in range(3,15,3):
                self.play(Write(examples[i]))
                self.slide_break()
                self.play(Write(examples[i+1]))
                self.slide_break()
                self.play(FadeIn(examples[i+2]))
                self.slide_break()
            self.play(FadeOut(examples))
            self.slide_break()
        if subsec==10 or subsec==-1:
            grouping=VGroup(
                VGroup(
                    Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(LEFT),
                    Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_RED).shift(RIGHT),
                    Line(start=LEFT/2,end=1.5*LEFT).shift(LEFT),
                    Line(start=RIGHT/2,end=1.5*RIGHT).shift(RIGHT),
                ),
                VGroup(
                    Line(start=[-0.5*np.cos(TAU/12),-0.5*np.sin(TAU/12),0],end=[-1.5*np.cos(TAU/12),-1.5*np.sin(TAU/12),0]).shift(LEFT),
                    Line(start=[-0.5*np.cos(TAU/12),0.5*np.sin(TAU/12),0],end=[-1.5*np.cos(TAU/12),1.5*np.sin(TAU/12),0]).shift(LEFT),
                    ArcBetweenPoints(
                        start=[-1+0.5*np.cos(TAU/12),0.5*np.sin(TAU/12),0],
                        end=[1-0.5*np.cos(TAU/12),0.5*np.sin(TAU/12),0],
                        angle=-2*TAU/8),
                    ArcBetweenPoints(
                        start=[-1+0.5*np.cos(TAU/12),-0.5*np.sin(TAU/12),0],
                        end=[1-0.5*np.cos(TAU/12),-0.5*np.sin(TAU/12),0],
                        angle=2*TAU/8),
                ),
                VGroup(
                    Line(start=[-0.5*np.cos(TAU/12),-0.5*np.sin(TAU/12),0],end=[-1.5,-0.5*np.sin(TAU/12),0]).shift(LEFT),
                    Line(start=[-0.5*np.cos(TAU/12),0.5*np.sin(TAU/12),0],end=[-1.5,0.5*np.sin(TAU/12),0]).shift(LEFT),
                    Line(start=[-1+0.5*np.cos(TAU/24),0.5*np.sin(TAU/24),0],
                        end=[1-0.5*np.cos(TAU/24),0.5*np.sin(TAU/24),0]),
                    Line(start=[-1+0.5*np.cos(TAU/12),-0.5*np.sin(TAU/24),0],
                        end=[1-0.5*np.cos(TAU/24),-0.5*np.sin(TAU/24),0]),
                ),
            )
            self.play(FadeIn(grouping[:2]))
            self.slide_break()
            self.play(Transform(grouping[1],grouping[2]))
            self.slide_break()

            iq=ImageMobject("matrix.jpeg").scale(.8)
            self.play(FadeIn(iq))
            self.remove(*grouping)
            self.slide_break()
            self.play(FadeOut(iq))
            self.slide_break()
        if subsec==11 or subsec==-1:
            tn=VGroup(
                VGroup(
                    Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_RED),
                    Line((0.5/np.sqrt(2))*UL,(1/np.sqrt(2))*UL),
                    Line(RIGHT/2,RIGHT),
                    Line(DOWN/2,DOWN),
                ).shift(UL),
                VGroup(
                    Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN),
                    Line((0.5/np.sqrt(2))*UR,(1/np.sqrt(2))*UR),
                    Line(LEFT/2,LEFT),
                    Line(DOWN/2,DOWN),
                ).shift(UR),
                VGroup(
                    Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE),
                    # Line((0.5/np.sqrt(2))*UR,(1/np.sqrt(2))*UR),
                    Line(UP/2,UP),
                    Line(RIGHT/2,RIGHT),
                ).shift(DL),
                VGroup(
                    Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW),
                    # Line((0.5/np.sqrt(2))*UR,(1/np.sqrt(2))*UR),
                    Line(UP/2,UP),
                    Line(LEFT/2,LEFT),
                ).shift(DR),
                MyMathTex(r"i").shift(2*UL),
                MyMathTex(r"j").shift(2*UR),
                VGroup(
                    MyMathTex(r"\alpha").shift(1.67*UP+0.4*RIGHT),
                    MyMathTex(r"\alpha").shift(1.67*UP-0.4*RIGHT),
                    MyMathTex(r"\beta").shift(1.67*LEFT+0.4*UP),
                    MyMathTex(r"\beta").shift(1.67*LEFT-0.4*UP),
                    MyMathTex(r"\gamma").shift(1.67*DOWN+0.4*RIGHT),
                    MyMathTex(r"\gamma").shift(1.67*DOWN-0.4*RIGHT),
                    MyMathTex(r"\delta").shift(1.67*RIGHT+0.4*UP),
                    MyMathTex(r"\delta").shift(1.67*RIGHT-0.4*UP),
                ),
                VGroup(
                    BraceBetweenPoints(1.5*UL,1.5*DL).shift(1.5*LEFT).scale(2),
                    BraceBetweenPoints(1.5*DR,1.5*UR).shift(1.5*RIGHT).scale(2),
                    MyMathTex(r"\prod").shift(4.5*LEFT).scale(1.5),
                ),

                MyMathTex(r"\sum_{\alpha,\beta,\gamma,\delta}").shift(6.5*LEFT+0.325*DOWN).scale(1.5),
            ).scale(.75)

            self.play(FadeIn(tn[0:4]))
            self.slide_break()
            self.play(Write(tn[4:6]))
            self.slide_break()
            x=0.5
            self.play(
                tn[0].animate.shift(x*UL),
                tn[1].animate.shift(x*UR),
                tn[2].animate.shift(x*DL),
                tn[3].animate.shift(x*DR),
                tn[4].animate.shift(x*UL),
                tn[5].animate.shift(x*UR),
            )
            self.slide_break()
            self.play(Write(tn[6]))
            self.slide_break()
            self.play(tn[:7].animate.shift(RIGHT/2))
            tn[7:].shift(RIGHT/2)
            self.play(Write(tn[7]))
            self.slide_break()
            self.play(tn[:8].animate.shift(RIGHT))
            tn[8:].shift(RIGHT)
            self.play(Write(tn[8]))
            self.slide_break()
            self.play(FadeOut(tn))
            self.slide_break()
        if subsec==12 or subsec==-1:
            cyclic=VGroup(
                MyMathTex(r"\mathrm{Tr}(AB)",r"=",r"\mathrm{Tr}(BA)").shift(3*UP),
                ArcBetweenPoints(ORIGIN,1.5*UP,angle=-TAU/2).shift(.75*LEFT),
                ArcBetweenPoints(ORIGIN,1.5*UP,angle=TAU/2).shift(0.75*RIGHT),
                Line(.75*LEFT,.75*RIGHT),
                Line(.75*LEFT,.75*RIGHT).shift(1.5*UP),
                VGroup(
                    Square(.75,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE),
                    MyMathTex("A",color=BLACK),
                ).shift(3*LEFT/4),
                VGroup(
                    Square(.75,color=WHITE,fill_opacity=1,fill_color=TEN_RED),
                    MyMathTex("B",color=BLACK),
                ).shift(3*RIGHT/4),
            ).move_to(ORIGIN)

            self.play(FadeIn(cyclic[0]))
            self.slide_break()

            cyclic[0][0].set_color(YELLOW)
            cyclic.save_state()
            cyclic[0][0].set_color(WHITE)
            cyclic[1:].set_color(BG)

            self.play(Restore(cyclic))
            self.slide_break()

            self.play(
                Rotate(cyclic[5],angle=-TAU/2,about_point=cyclic[5].get_center()+0.75*UP),
                cyclic[0].animate.set_color(WHITE),
                rate_func=rate_functions.ease_in_sine,run_time=1,
            )
            self.play(
                cyclic[1].animate.shift((3/8)*RIGHT),
                cyclic[2].animate.shift((3/8)*LEFT),
                cyclic[3].animate.scale(1/2),
                cyclic[4].animate.scale(1/2),
                cyclic[5].animate.shift(.75*RIGHT),
                cyclic[6].animate.shift(.75*LEFT),
            )
            self.slide_break()

            transposed=MyMathTex(r"A^T",color=BLACK).move_to(cyclic[5][1])
            cyclic[5][1].save_state()
            self.play(Transform(cyclic[5][1],transposed))
            self.slide_break()

            self.play(Restore(cyclic[5][1]))
            self.slide_break()

            self.play(
                cyclic[1].animate.shift(-(3/8)*RIGHT),
                cyclic[2].animate.shift(-(3/8)*LEFT),
                cyclic[3].animate.scale(2),
                cyclic[4].animate.scale(2),
                cyclic[5].animate.shift(.75*RIGHT),
                cyclic[6].animate.shift(.75*LEFT),
            )
            self.play(
                Rotate(cyclic[5],angle=-TAU/2,about_point=cyclic[5].get_center()+0.75*DOWN),
                cyclic[0][2].animate.set_color(YELLOW),
            )
            self.slide_break()
            self.play(cyclic.animate.set_color(BG))
            self.remove(*cyclic)
            self.slide_break()
        if subsec==13 or subsec==-1:
            ladder=VGroup(
                Line([-2.5,-1,0],[-1.5,-1,0]),
                Line([-0.5,-1,0],[+0.5,-1,0]),
                Line([+1.5,-1,0],[+2.5,-1,0]),

                Line([-2.5,1,0],[-1.5,1,0]),
                Line([-0.5,1,0],[+0.5,1,0]),
                Line([+1.5,1,0],[+2.5,1,0]),

                Line([-3,-0.5,0],[-3,+0.5,0]),
                Line([-1,-0.5,0],[-1,+0.5,0]),
                Line([+1,-0.5,0],[+1,+0.5,0]),
                Line([+3,-0.5,0],[+3,+0.5,0]),

                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift([-3,-1,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift([-1,-1,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift([+1,-1,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift([+3,-1,0]),

                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift([-3,+1,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift([-1,+1,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift([+1,+1,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift([+3,+1,0]),
            )
            self.play(FadeIn(ladder))
            self.slide_break()
            newladder=VGroup(
                Line([-2.5,-1,0],[-1.5,-1,0]),
                Line([-0.5,-1,0],[+0.5,-1,0]),
                Line([+1.5,-1,0],[+2.5,-1,0]),

                Line([-2,1,0],[-2,1,0]),
                Line([-1.5,1,0],[+0.5,1,0]),
                Line([+1.5,1,0],[+2.5,1,0]),

                Line([-3+0.5*np.sin(TAU/12),-1+0.5*np.cos(TAU/12),0],
                    [-2-0.5*np.sin(TAU/12),+1-0.5*np.cos(TAU/12),0]),
                Line([-1-0.5*np.sin(TAU/12),-1+0.5*np.cos(TAU/12),0],
                    [-2+0.5*np.sin(TAU/12),+1-0.5*np.cos(TAU/12),0]),
                Line([+1,-0.5,0],[+1,+0.5,0]),
                Line([+3,-0.5,0],[+3,+0.5,0]),

                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift([-3,-1,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift([-1,-1,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift([+1,-1,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift([+3,-1,0]),

                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift([-2,+1,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift([-2,+1,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift([+1,+1,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift([+3,+1,0]),
            )
            self.play(Transform(ladder,newladder))
            self.slide_break()
            newladder=VGroup(
                Line([-2.5,-1,0],[-1.5,-1,0]),
                Line([-0.5,-1,0],[+0.5,-1,0]),
                Line([+1.5,-1,0],[+2.5,-1,0]),

                Line([-2,1,0],[-2,1,0]),
                Line([-1.5,1,0],[+1.5,1,0]),
                Line([+2,1,0],[+2,1,0]),

                Line([-3+0.5*np.sin(TAU/12),-1+0.5*np.cos(TAU/12),0],
                    [-2-0.5*np.sin(TAU/12),+1-0.5*np.cos(TAU/12),0]),
                Line([-1-0.5*np.sin(TAU/12),-1+0.5*np.cos(TAU/12),0],
                    [-2+0.5*np.sin(TAU/12),+1-0.5*np.cos(TAU/12),0]),
                Line([1+0.5*np.sin(TAU/12),-1+0.5*np.cos(TAU/12),0],
                    [2-0.5*np.sin(TAU/12),+1-0.5*np.cos(TAU/12),0]),
                Line([3-0.5*np.sin(TAU/12),-1+0.5*np.cos(TAU/12),0],
                    [2+0.5*np.sin(TAU/12),+1-0.5*np.cos(TAU/12),0]),

                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift([-3,-1,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift([-1,-1,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift([+1,-1,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift([+3,-1,0]),

                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift([-2,+1,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift([-2,+1,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift([+2,+1,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift([+2,+1,0]),
            )
            self.play(Transform(ladder,newladder))
            self.slide_break()
            newladder=VGroup(
                Line([-2.5,-1,0],[-1.5,-1,0]),
                Line([-0.5,-1,0],[+0.5,-1,0]),
                Line([+1.5,-1,0],[+2.5,-1,0]),

                VGroup(),
                Line([-0,1,0],[+0,1,0]),
                VGroup(),

                Line([-3+0.5*np.sin(TAU/6),-1+0.5*np.cos(TAU/6),0],
                    [0-0.5*np.sin(TAU/6),+1-0.5*np.cos(TAU/6),0]),
                Line([-1+0.5*np.sin(TAU/12),-1+0.5*np.cos(TAU/12),0],
                    [0-0.5*np.sin(TAU/12),+1-0.5*np.cos(TAU/12),0]),
                Line([1-0.5*np.sin(TAU/12),-1+0.5*np.cos(TAU/12),0],
                    [0+0.5*np.sin(TAU/12),+1-0.5*np.cos(TAU/12),0]),
                Line([3-0.5*np.sin(TAU/6),-1+0.5*np.cos(TAU/6),0],
                    [0+0.5*np.sin(TAU/6),+1-0.5*np.cos(TAU/6),0]),

                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift([-3,-1,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift([-1,-1,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift([+1,-1,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift([+3,-1,0]),

                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_RED).shift([0,+1,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_RED).shift([0,+1,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_RED).shift([0,+1,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_RED).shift([0,+1,0]),
            )
            self.play(Transform(ladder,newladder))
            self.slide_break()
            self.play(ladder.animate.set_color(BG))
            self.remove(ladder)
            self.slide_break()
        if subsec==14 or subsec==-1:
            ladder=VGroup(
                Line([-2.5,-1,0],[-1.5,-1,0]),
                Line([-0.5,-1,0],[+0.5,-1,0]),
                Line([+1.5,-1,0],[+2.5,-1,0]),

                Line([-2.5,1,0],[-1.5,1,0]),
                Line([-0.5,1,0],[+0.5,1,0]),
                Line([+1.5,1,0],[+2.5,1,0]),

                Line([-3,-0.5,0],[-3,+0.5,0]),
                Line([-1,-0.5,0],[-1,+0.5,0]),
                Line([+1,-0.5,0],[+1,+0.5,0]),
                Line([+3,-0.5,0],[+3,+0.5,0]),

                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift([-3,-1,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift([-1,-1,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift([+1,-1,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift([+3,-1,0]),

                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift([-3,+1,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift([-1,+1,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift([+1,+1,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift([+3,+1,0]),
            )
            self.play(FadeIn(ladder))
            self.slide_break()
            newladder=VGroup(
                Line([-2.5,-.1,0],[-1.5,-.1,0]),
                Line([-0.5,-.1,0],[+0.5,-.1,0]),
                Line([+1.5,-.1,0],[+2.5,-.1,0]),

                Line([-2.5,.1,0],[-1.5,.1,0]),
                Line([-0.5,.1,0],[+0.5,.1,0]),
                Line([+1.5,.1,0],[+2.5,.1,0]),

                Line([-3,-0,0],[-3,+0,0]),
                Line([-1,-0,0],[-1,+0,0]),
                Line([+1,-0,0],[+1,+0,0]),
                Line([+3,-0,0],[+3,+0,0]),

                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift([-3,0,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift([-1,0,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift([+1,0,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift([+3,0,0]),

                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift([-3,0,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift([-1,0,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift([+1,0,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift([+3,0,0]),
            )
            self.play(Transform(ladder,newladder))
            self.slide_break()
            newladder=VGroup(
                Line([-1.5,-.1,0],[-1.5,-.1,0]),
                Line([-0.5,-.1,0],[+0.5,-.1,0]),
                Line([+1.5,-.1,0],[+1.5,-.1,0]),

                Line([-1.5,.1,0],[-1.5,.1,0]),
                Line([-0.5,.1,0],[+0.5,.1,0]),
                Line([+1.5,.1,0],[+1.5,.1,0]),

                VGroup(),
                VGroup(),
                VGroup(),
                VGroup(),

                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift([-1,0,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift([-1,0,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift([+1,0,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift([+1,0,0]),

                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift([-1,0,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift([-1,0,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift([+1,0,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift([+1,0,0]),
            )
            self.play(Transform(ladder,newladder))
            self.slide_break()
            newladder=VGroup(
                VGroup(),
                Line([-0,-.1,0],[+0,-.1,0]),
                VGroup(),

                VGroup(),
                Line([-0,.1,0],[+0,.1,0]),
                VGroup(),

                VGroup(),
                VGroup(),
                VGroup(),
                VGroup(),

                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift([0,0,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift([0,0,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift([0,0,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift([0,0,0]),

                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift([0,0,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift([0,0,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift([0,0,0]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift([0,0,0]),
            )
            self.play(Transform(ladder,newladder))
            self.slide_break()
            self.play(ladder.animate.set_color(BG))
            self.remove(ladder)
            self.slide_break()

        self.play(Restore(toc))

class Lec1_2(SlideScene):
    def construct(self):
        tocindex=(0,2)
        toc.set_opacity(0.25)
        toc[tocindex[0]].set_opacity(1)
        toc.save_state()
        heading = toc[tocindex[0]][tocindex[1]]
        self.add(toc,footer)
        self.play(
            toc.animate.set_opacity(0),
            heading.animate.scale(2).to_corner(UP).set_x(0),
        )
        heading.set_opacity(1)
        self.slide_break()

        subsec = -1
        # 1     breakup
        # 2     grouping
        # 3     decomp
        # 4     svdtn
        # 5     multisvd
        # 6     w state

        if subsec==1 or subsec==-1:
            breakup=VGroup(
                Line(2*LEFT,2*RIGHT),
                *[Line(ORIGIN,UP).shift(i*LEFT) for i in range(-2,3)],
                *[Square(.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(i*LEFT) for i in range(-2,3)],
            )
            bigboy=Rectangle(width=5,height=1,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE)
            breakup.save_state()
            for i in range(6,11):
                breakup[i]=bigboy.copy()
            invis=breakup.copy().set_color(BG)
            self.play(ReplacementTransform(invis,breakup))
            self.slide_break()
            self.play(Restore(breakup))
            self.slide_break()
            self.play(breakup.animate.set_color(BG))
            self.remove(breakup)
            self.slide_break()
        if subsec==2 or subsec==-1:
            grouping=VGroup(
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_PURPLE),
                VGroup(
                    Line(start=[-0.5*np.cos(TAU/12),-0.5*np.sin(TAU/12),0],end=[-1.5*np.cos(TAU/12),-1.5*np.sin(TAU/12),0]),
                    Line(start=[-0.5*np.cos(TAU/12),0.5*np.sin(TAU/12),0],end=[-1.5*np.cos(TAU/12),1.5*np.sin(TAU/12),0]),
                    Line(0.5*LEFT,1.5*LEFT),
                    Line(start=[0.5*np.cos(TAU/24),-0.5*np.sin(TAU/24),0],end=[1.5*np.cos(TAU/24),-1.5*np.sin(TAU/24),0]),
                    Line(start=[0.5*np.cos(TAU/24),0.5*np.sin(TAU/24),0],end=[1.5*np.cos(TAU/24),1.5*np.sin(TAU/24),0]),
                ),
                VGroup(
                    Line(start=[-0.5*np.cos(TAU/12),-0.5*np.sin(TAU/12),0],end=[-1.5,-0.5*np.sin(TAU/12),0]),
                    Line(start=[-0.5*np.cos(TAU/12),0.5*np.sin(TAU/12),0],end=[-1.5,0.5*np.sin(TAU/12),0]),
                    Line(0.5*LEFT,1.5*LEFT),
                    Line(start=[0.5*np.cos(TAU/24),-0.5*np.sin(TAU/24),0],end=[1.5,-0.5*np.sin(TAU/24),0]),
                    Line(start=[0.5*np.cos(TAU/24),0.5*np.sin(TAU/24),0],end=[1.5,0.5*np.sin(TAU/24),0]),
                ),
            )

            grouping2=VGroup(
                VGroup(
                    Line(start=[-0.5*np.cos(TAU/12),-0.5*np.sin(TAU/12),0],end=[-1.5,-0.5*np.sin(TAU/12),0]),
                    Line(start=[-0.5*np.cos(TAU/12),0.5*np.sin(TAU/12),0],end=[-1.5,0.5*np.sin(TAU/12),0]),
                    Line(0.5*LEFT,1.5*LEFT),
                ),
                VGroup(
                    Line(start=[0.5*np.cos(TAU/24),-0.5*np.sin(TAU/24),0],end=[1.5,-0.5*np.sin(TAU/24),0]),
                    Line(start=[0.5*np.cos(TAU/24),0.5*np.sin(TAU/24),0],end=[1.5,0.5*np.sin(TAU/24),0]),
                ),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_PURPLE),
            )
            grouping3=VGroup(
                Line(LEFT*3/8,RIGHT*3/8),
                VGroup(
                    Line(0.375*LEFT,1.5*LEFT).shift(0.5*np.sin(TAU/12)*DOWN),
                    Line(0.375*LEFT,1.5*LEFT).shift(0.5*np.sin(TAU/12)*UP),
                    Line(0.375*LEFT,1.5*LEFT),
                ).shift(LEFT*3/4),
                VGroup(
                    Line(RIGHT*3/8,1.5*RIGHT).shift(-0.5*np.sin(TAU/24)*DOWN),
                    Line(RIGHT*3/8,1.5*RIGHT).shift(-0.5*np.sin(TAU/24)*UP),
                ).shift(RIGHT*3/4),
                Square(0.75,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(LEFT*3/4),
                Polygon(
                    *[0.75*np.array([np.cos(TAU*(i+0.5)/6),np.sin(TAU*(i+0.5)/6),0])/np.sqrt(3) for i in range(6)],
                    color=WHITE,fill_opacity=1,fill_color=TEN_RED
                ).shift(RIGHT*3/4),
            )

            self.play(FadeIn(grouping[:2]))
            self.slide_break()
            self.play(Transform(grouping[1],grouping[2]))
            self.slide_break()
            self.remove(*grouping)
            self.add(grouping2)
            self.play(
                FadeIn(grouping3[0]),
                ReplacementTransform(grouping2[0],grouping3[1]),
                ReplacementTransform(grouping2[1],grouping3[2]),
                ReplacementTransform(grouping2[2].copy().rotate(TAU/8),grouping3[3]),
                ReplacementTransform(grouping2[2],grouping3[4]),
            )
            self.slide_break()
            # self.play(*[FadeOut(mob) for mob in self.mobjects if mob!=toc and mob!=footer])
            # self.slide_break()

            self.play(FadeOut(grouping3))
            self.slide_break()
        if subsec==3 or subsec==-1:
            eigen=MyMathTex(r"M=\sum_i \lambda_i \left| v_i \middle\rangle\!\middle\langle v_i\right|").scale(1.25)
            self.play(Write(eigen))
            self.slide_break()

            singular=MyMathTex(r"M=\sum_i \sigma_i \left| l_i \middle\rangle\!\middle\langle r_i\right|").scale(1.25)
            self.play(ReplacementTransform(eigen,singular))
            self.slide_break()

            sing_properties=VGroup(
                MyMathTex(r"\left\langle l_i \middle| l_j \right\rangle=\left\langle r_i \middle| r_j \right\rangle=\delta_{i,j}"),
                MyMathTex(r"\sigma_i\geq 0"),
                MyTex(r"Always defined"),
                MyTex(r"Eckhart-Young-Mirsky"),
            ).arrange(DOWN).shift(1.5*DOWN)
            self.play(singular.animate.shift(1.25*UP))
            self.slide_break()
            for i in range(4):
                self.play(Write(sing_properties[i]))
                self.slide_break()
            self.play(FadeOut(sing_properties))
            self.slide_break()

            eym=VGroup(
                MyTex("Closest $X$ to $M$ with $\mathrm{rank}(X)=r$?").shift(UP/4),
                MyMathTex(
                    r"X=\sum_{i=1}^r",
                    r"c_i",
                    r"\left| u_i \middle\rangle\!\middle\langle v_i\right|").shift(DOWN),
                MyMathTex(
                    r"X=\sum_{i=1}^r",
                    r"\sigma_i",
                    r"\left| l_i \middle\rangle\!\middle\langle r_i\right|").shift(DOWN),
            ).shift(DOWN)
            self.play(Write(eym[0]))
            self.slide_break()
            self.play(Write(eym[1]))
            self.slide_break()
            self.play(Transform(eym[1],eym[2]))
            self.slide_break()
            self.play(FadeOut(eym[0:2]),FadeOut(singular))
            self.slide_break()
        if subsec==4 or subsec==-1:
            svdtn1=VGroup(
                MyMathTex(r"M=USV^\dag").shift(ORIGIN).scale(1.5).shift(UP/2),
                MyMathTex(r"U^\dag U=I").shift(ORIGIN),
                MyMathTex(r"V^\dag V=I").shift(DOWN*3/4),
                MyTex(r"$S>0$ diagonal").shift(DOWN*3/2),
            )

            svdtn2=VGroup(
                VGroup(
                    Line(1.5*LEFT,1*LEFT),
                    Line(0.5*LEFT,.15*LEFT),
                    Line(1.5*RIGHT,1*RIGHT),
                    Line(0.5*RIGHT,.15*RIGHT),
                    Polygon(ORIGIN,DL/2,UL/2,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift(0.5*LEFT),
                    Polygon(ORIGIN,DR/2,UR/2,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift(0.5*RIGHT),
                    Circle(0.15,color=WHITE,fill_opacity=1,fill_color=TEN_RED),
                ).scale(1.25).shift(UP/2),
                VGroup(
                    VGroup(
                        Polygon(ORIGIN,DL/2,UL/2,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift(.75*RIGHT),
                        Polygon(ORIGIN,DR/2,UR/2,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift(.75*LEFT),
                        Line(LEFT/4,RIGHT/4),
                        Line(3*LEFT/4,LEFT),
                        Line(3*RIGHT/4,RIGHT),
                    ),
                    MyMathTex("="),
                    VGroup(
                        Polygon(ORIGIN,DL/2,UL/2,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift(.75*RIGHT),
                        Polygon(ORIGIN,DR/2,UR/2,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift(.75*LEFT),
                        Line(LEFT/4,RIGHT/4),
                        Line(3*LEFT/4,LEFT),
                        Line(3*RIGHT/4,RIGHT),
                    ),
                    MyMathTex("="),
                    Line(LEFT/2,RIGHT/2),
                ).scale(.75).arrange(RIGHT).shift(DOWN),
            ).shift(3*RIGHT)
            svdtn1.shift(DOWN/2)
            svdtn2.shift(DOWN/2)

            self.play(FadeIn(svdtn1[0]))
            self.slide_break()
            self.play(svdtn1[0].animate.shift(1.25*UP))
            self.play(FadeIn(svdtn1[1:]))
            self.slide_break()
            self.play(svdtn1.animate.shift(3*LEFT))
            self.play(Write(svdtn2[0]))
            self.play(
                svdtn1[0][0][2].animate.set_color(GREEN),
                svdtn1[0][0][3].animate.set_color(RED),
                svdtn1[0][0][4].animate.set_color(YELLOW),
                svdtn1[1][0][0].animate.set_color(GREEN),
                svdtn1[1][0][2].animate.set_color(GREEN),
                svdtn1[2][0][0].animate.set_color(YELLOW),
                svdtn1[2][0][2].animate.set_color(YELLOW),
                svdtn1[3][0][0].animate.set_color(RED),
            )
            self.slide_break()
            self.play(svdtn2[0].animate.shift(1.25*UP))
            self.play(FadeIn(svdtn2[1]))
            self.slide_break()
            self.play(FadeOut(svdtn1),FadeOut(svdtn2))
            self.slide_break()
        if subsec==5 or subsec==-1:
            # multi svd
            multisvd1 = VGroup(
                VGroup(*[
                    Line(0.5*LEFT,1.25*LEFT).rotate(TAU*(i-1)/6,about_point=ORIGIN) for i in range(3)
                ]),
                VGroup(*[
                    Line(0.5*RIGHT,1.25*RIGHT).rotate(TAU*(i-1)/6,about_point=ORIGIN) for i in range(3)
                ]),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).rotate(UP*TAU/2),
                Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).rotate(TAU/2),
            )
            dashed=DashedLine(2*DOWN,2*UP,dash_length=.1).set_opacity(0.5)

            multisvd2 = VGroup(
                VGroup(
                    Line(ORIGIN,.75*LEFT+UP/4).shift(UP/4),
                    Line(ORIGIN,.75*LEFT),
                    Line(ORIGIN,.75*LEFT+DOWN/4).shift(DOWN/4),
                ).shift(LEFT),
                VGroup(
                    Line(ORIGIN,.75*RIGHT+DOWN/4).shift(DOWN/4),
                    Line(ORIGIN,.75*RIGHT),
                    Line(ORIGIN,.75*RIGHT+UP/4).shift(UP/4),
                ).shift(RIGHT),
                Polygon(RIGHT/2,UP/2,DOWN/2,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift(LEFT),
                Polygon(LEFT/2,DOWN/2,UP/2,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift(RIGHT),
                Line(LEFT/2,RIGHT/2),
                Circle(0.15,color=WHITE,fill_opacity=1,fill_color=TEN_RED),
            )
            self.play(FadeIn(multisvd1))
            self.slide_break()

            self.play(Write(dashed),run_time=0.5)
            self.add_foreground_mobject(dashed)
            self.slide_break()

            for i in range(4):
                multisvd1[i].save_state()
            self.play(
                *[Transform(multisvd1[i],multisvd2[i]) for i in range(4)],
                FadeIn(multisvd2[4:],scale=0),
            )
            self.slide_break()
            self.play(
                *[Restore(multisvd1[i]) for i in range(4)],
                FadeOut(multisvd2[4:],scale=0),
            )
            self.slide_break()

            self.play(Rotate(dashed,angle=-TAU/6))
            self.slide_break()
            multisvd1.rotate(-TAU/6)
            multisvd2.rotate(-TAU/6)

            for i in range(4):
                multisvd1[i].save_state()
            self.play(
                *[Transform(multisvd1[i],multisvd2[i]) for i in range(4)],
                FadeIn(multisvd2[4:],scale=0),
            )
            self.slide_break()
            self.play(
                *[Restore(multisvd1[i]) for i in range(4)],
                FadeOut(multisvd2[4:],scale=0),
            )
            self.slide_break()
            self.remove_foreground_mobject(dashed)
            self.play(FadeOut(dashed))
            self.slide_break()

            self.remove(multisvd1)
            multisvd3 = VGroup(
                *[Line(0.0*LEFT,1.25*LEFT).rotate(TAU*i/6,about_point=ORIGIN) for i in range(6)],
                *[Circle(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).rotate(TAU*i/6) for i in range(6)],
            )
            self.add(multisvd3)
            multisvd4 = VGroup(
                *[Line(0.0*LEFT,1.25*LEFT).rotate(TAU*i/6,about_point=ORIGIN) for i in range(6)],
                *[
                Polygon(RIGHT/4,UP/4,DOWN/4,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift(3*LEFT/4).rotate(TAU*i/6,about_point=ORIGIN) for i in range(6)
                ],
                Circle(0.15,color=WHITE,fill_opacity=1,fill_color=TEN_RED),
            )
            self.play(
                *[ReplacementTransform(multisvd3[i],multisvd4[i]) for i in range(12)],
                FadeIn(multisvd4[-1],scale=0),
            )
            self.slide_break()
            self.play(multisvd4.animate.shift(5.5*LEFT))

            tenrank_def=MyMathTex(r"\mathrm{rank}(T):=\mathrm{min}\left\lbrace r ~\middle|~ \exists \lbrace v_{i,j}\rbrace_{i,j}: T=\sum_{i=1}^r \bigotimes_j \left|v_{i,j}\right\rangle \right\rbrace  ").shift(1.5*RIGHT)
            tenrank_prop=VGroup(
            MyTex(r"\textbullet~",r"Multiplicative?"),
            MyTex(r"\textbullet~",r"Semi-continuous?"),
            MyTex(r"\textbullet~",r"Efficiently computable?"),
            ).arrange(DOWN,aligned_edge=LEFT,buff=.5).shift(1.5*RIGHT+1.5*DOWN)
            crosses=VGroup(*[Cross(t[1]) for t in tenrank_prop])

            self.play(Write(tenrank_def))
            self.slide_break()
            self.play(tenrank_def.animate.shift(1.5*UP))
            self.slide_break()
            for t in tenrank_prop:
                self.play(Write(t))
                self.slide_break()
            for c in crosses:
                self.play(Write(c))
            self.slide_break()

            self.play(FadeOut(multisvd4),FadeOut(tenrank_def),FadeOut(tenrank_prop),FadeOut(crosses))
            self.slide_break()
        if subsec==6 or subsec==-1:
            # w state

            W1=MyMathTex(r"\left| W \right\rangle:=\left|001\right\rangle+\left|010\right\rangle+\left|100\right\rangle").scale(1.25)

            W2=MyMathTex(
                r"\lim_{\epsilon\to0}",
                r"\epsilon^{-1}\left(\left|0\right\rangle +\epsilon\left|1\right\rangle \right)^{\otimes 3}-\epsilon^{-1}\left|000\right\rangle",
                r"=",
                r"\left| W \right\rangle")
            W2.add(VGroup(
                    Brace(W2[1]),
                    MyTex("rank-2").scale(0.75).next_to(W2[1],2.5*DOWN),
            ).set_color(RED))

            W2.add(VGroup(
                    Brace(W2[3]),
                    MyTex("rank-3").scale(0.75).next_to(W2[3],2*DOWN),
            ).set_color(BLUE))
            W2[-1][0].set_y(W2[-2][0].get_y())
            W2[-1][1].set_y(W2[-2][1].get_y())

            self.play(Write(W1))
            self.slide_break()

            self.play(W1.animate.shift(2*UP))
            self.play(FadeIn(W2[:-2]))
            self.slide_break()
            self.play(FadeIn(W2[-2]),W2[1].animate.set_color(RED))
            self.slide_break()
            self.play(FadeIn(W2[-1]),W2[3].animate.set_color(BLUE))
            self.slide_break()

            W3=VGroup(
                MyMathTex(r"\mathrm{rank}\left(\left| W \right\rangle\right)=3"),
                MyMathTex(r"\mathrm{rank}\left(\left| W \right\rangle^{\otimes 2}\right)=",r"8")
            ).arrange(RIGHT,buff=1).shift(2.5*DOWN)
            W3[-1][-1].set_color(RED)
            W3[0].save_state()
            W3[0].set_x(0)
            self.play(Write(W3[0]))
            self.slide_break()
            self.play(Restore(W3[0]))
            self.play(Write(W3[1][0]))
            self.slide_break()
            self.play(FadeIn(W3[1][1]),Flash(W3[1][1],color=RED))
            self.slide_break()
            self.play(FadeOut(W2),FadeOut(W3))
            self.slide_break()
            wpaper=ImageMobject("./w.png").shift(DOWN)
            self.play(FadeIn(wpaper))
            self.slide_break()
            self.play(FadeOut(W1),FadeOut(wpaper))
            self.slide_break()

        self.play(Restore(toc))

class Lec1_3(SlideScene):
    def construct(self):
        tocindex=(0,3)
        toc.set_opacity(0.25)
        toc[tocindex[0]].set_opacity(1)
        toc.save_state()
        heading = toc[tocindex[0]][tocindex[1]]
        self.add(toc,footer)
        self.play(
            toc.animate.set_opacity(0),
            heading.animate.scale(2).to_corner(UP).set_x(0),
        )
        heading.set_opacity(1)
        self.slide_break()

        subsec = -1
        # 1     glossary states
        # 2     glossary operations
        # 3     adjoint
        # 4     unitality
        # 5     superoperator + choi
        # 6     Choi's theorem
        # 7     Stinespring
        # 8     Bell states
        # 9     teleportation

        if subsec==1 or subsec==-1:
            # glossary states
            gloss1=VGroup(
                VGroup(
                    VGroup(
                        MyMathTex(r"\left|\psi\right\rangle~=").next_to(ORIGIN,2*LEFT),
                        Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).move_to(RIGHT*0.75),
                        Line(RIGHT/2,ORIGIN),
                    ).shift(1.5*UP),
                    VGroup(
                        MyMathTex(r"\left\langle\psi\right|~=").next_to(ORIGIN,2*LEFT),
                        Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).move_to(RIGHT*0.75),
                        Line(RIGHT,1.5*RIGHT),
                    ),
                    VGroup(
                        MyMathTex(r"\rho~=").next_to(ORIGIN,2*LEFT),
                        Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).move_to(RIGHT*0.75),
                        Line(RIGHT/2,ORIGIN),
                        Line(RIGHT,RIGHT*1.5),
                    ).shift(1.5*DOWN),
                ),
                VGroup(
                    VGroup(
                        Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).move_to(1.75*LEFT),
                        Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).move_to(0.75*LEFT),
                        Line(1.5*LEFT,LEFT),
                        MyTex("=~1").shift(RIGHT/4),
                    ),
                    VGroup(
                        Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).move_to(1.25*LEFT+DOWN),
                        ArcBetweenPoints(1.5*LEFT+DOWN,1.5*LEFT+1.5*DOWN,angle=TAU/2),
                        ArcBetweenPoints(1*LEFT+DOWN,1*LEFT+1.5*DOWN,angle=-TAU/2),
                        Line(LEFT+1.5*DOWN,1.5*LEFT+1.5*DOWN),
                        MyTex("=~1").shift(DOWN+RIGHT/4),
                    ).shift(DOWN/2),
                ),
            ).arrange(RIGHT,buff=2)
            gloss1[0].save_state()
            gloss1[0].move_to(ORIGIN)
            for i in range(3):
                self.play(FadeIn(gloss1[0][i]))
                self.slide_break()
            self.play(Restore(gloss1[0]))
            self.slide_break()
            for i in range(2):
                self.play(FadeIn(gloss1[1][i]))
            self.slide_break()
            self.play(FadeOut(gloss1))
            self.slide_break()
        if subsec==2 or subsec==-1:
            # glossary states
            gloss2=VGroup(
                VGroup(
                    MyMathTex(r"U~=").shift(LEFT*1.75),
                    Square(1/2,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW),
                    Line(LEFT/4,LEFT*3/4),
                    Line(RIGHT/4,RIGHT*3/4),
                    MyMathTex("U",color=BLACK).scale(.75),
                ),
                VGroup(
                    Square(1/2,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift(0.5*LEFT),
                    Square(1/2,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift(0.5*RIGHT),
                    MyMathTex("U",color=BLACK).scale(.75).shift(0.5*LEFT),
                    MyMathTex(r"U^\dag",color=BLACK).scale(.75).shift(0.5*RIGHT),
                    Line(LEFT*3/4,LEFT*5/4),
                    Line(RIGHT*3/4,RIGHT*5/4),
                    Line(LEFT/4,RIGHT/4),
                    VGroup(
                        MyMathTex("="),
                        Line(0.75*RIGHT,1.5*RIGHT),
                    ).shift(2*RIGHT),
                ),

                VGroup(
                    MyMathTex(r"\mathcal E~=").shift(2.75*LEFT),
                    Polygon(
                        [+5/4, -1/4, 0],
                        [+3/4, -1/4, 0],
                        [+3/4, +2/4, 0],
                        [-3/4, +2/4, 0],
                        [-3/4, -1/4, 0],
                        [-5/4, -1/4, 0],
                        [-5/4, +4/4, 0],
                        [+5/4, +4/4, 0],
                        color=WHITE,fill_opacity=1,fill_color=TEN_RED
                    ),
                    Line(LEFT*3/4,LEFT/4),
                    Line(RIGHT*3/4,RIGHT/4),
                    Line(LEFT*5/4,LEFT*7/4),
                    Line(RIGHT*5/4,RIGHT*7/4),
                    # MyMathTex(r"\mathcal E",color=BLACK).scale(.75).shift(UP*3/4),
                ),
                VGroup(
                    Polygon(
                        [+5/4, -1/4, 0],
                        [+3/4, -1/4, 0],
                        [+3/4, +2/4, 0],
                        [-3/4, +2/4, 0],
                        [-3/4, -1/4, 0],
                        [-5/4, -1/4, 0],
                        [-5/4, +4/4, 0],
                        [+5/4, +4/4, 0],
                        color=WHITE,fill_opacity=1,fill_color=TEN_RED
                    ),
                    Line(LEFT*3/4,LEFT/4),
                    Line(RIGHT*3/4,RIGHT/4),
                    Line(LEFT*5/4,LEFT*6/4),
                    Line(RIGHT*5/4,RIGHT*6/4),
                    Line(LEFT*6/4,RIGHT*6/4).shift(DOWN/2),
                    ArcBetweenPoints(LEFT*6/4,LEFT*6/4+DOWN/2,angle=TAU/2),
                    ArcBetweenPoints(RIGHT*6/4,RIGHT*6/4+DOWN/2,angle=-TAU/2),
                    VGroup(
                        MyMathTex("=").shift(LEFT*1.5+DOWN/4),
                        Line(LEFT/2,RIGHT/2).shift(DOWN/2),
                        Line(LEFT/2,LEFT/4),
                        Line(RIGHT/4,RIGHT/2),
                        ArcBetweenPoints(LEFT/2,LEFT/2+DOWN/2,angle=TAU/2),
                        ArcBetweenPoints(RIGHT/2,RIGHT/2+DOWN/2,angle=-TAU/2),
                    ).shift(RIGHT*4),
                ),
            ).arrange_in_grid(rows=2,cols=2)
            gloss2[2:4].shift(1*DOWN)
            gloss2[0:4:2].shift(LEFT)
            gloss2[0].shift(LEFT)
            gloss2[1].shift(RIGHT/8)

            gloss2[0].save_state()
            gloss2[2].save_state()
            gloss2[0:4:2].move_to(ORIGIN)

            self.play(FadeIn(gloss2[0]))
            self.play(FadeIn(gloss2[2]))
            self.slide_break()
            self.play(Restore(gloss2[0]),Restore(gloss2[2]))
            self.play(FadeIn(gloss2[1]),FadeIn(gloss2[3]))
            self.slide_break()
            self.play(FadeOut(gloss2))
            self.slide_break()
        if subsec==3 or subsec==-1:

            adjoint=MyMathTex(r"\langle A,\Phi(B)\rangle=\langle \Phi^\dag(A),B\rangle\text{ where }\langle X,Y\rangle:=\mathrm{Tr}(X^\dag Y)")

            r=.95
            P1=Polygon(
                [-5/4, -4/4, 0], [-5/4, +1/4, 0], [+5/4, +1/4, 0], [+5/4, -4/4, 0],
                [+3/4, -4/4, 0], [+3/4, -1/4, 0], [-3/4, -1/4, 0], [-3/4, -4/4, 0],
                color=WHITE,fill_opacity=1,fill_color=TEN_RED
            ).shift(DOWN)
            P12=Polygon(
                [-1-np.sqrt(1/2)*(r+1/4),-np.sqrt(1/2)*(r-1/4),0], [-9/8, +1/4, 0], [+9/8, +1/4, 0], [+1+np.sqrt(1/2)*(r+1/4),-np.sqrt(1/2)*(r-1/4),0],
                [+1+np.sqrt(1/2)*(r-1/4),-np.sqrt(1/2)*(r+1/4),0], [+7/8, -1/4, 0], [-7/8, -1/4, 0], [-1-np.sqrt(1/2)*(r-1/4),-np.sqrt(1/2)*(r+1/4),0],
                color=WHITE,fill_opacity=1,fill_color=TEN_RED
            ).shift(DOWN)
            P2=Polygon(
                [-8/4, +1/4, 0], [-1, +1/4, 0], [+1, +1/4, 0], [+8/4, +1/4, 0],
                [+8/4, -1/4, 0], [+1, -1/4, 0], [-1, -1/4, 0], [-8/4, -1/4, 0],
                color=WHITE,fill_opacity=1,fill_color=TEN_RED
            ).shift(DOWN)
            P23=Polygon(
                [-1-np.sqrt(1/2)*(r-1/4),+np.sqrt(1/2)*(r+1/4),0], [-7/8, +1/4, 0], [+7/8, +1/4, 0], [+1+np.sqrt(1/2)*(r-1/4),+np.sqrt(1/2)*(r+1/4),0],
                [+1+np.sqrt(1/2)*(r+1/4),+np.sqrt(1/2)*(r-1/4),0], [+9/8, -1/4, 0], [-9/8, -1/4, 0], [-1-np.sqrt(1/2)*(r+1/4),+np.sqrt(1/2)*(r-1/4),0],
                color=WHITE,fill_opacity=1,fill_color=TEN_RED
            ).shift(DOWN)
            P3=Polygon(
                [-3/4, +4/4, 0], [-3/4, +1/4, 0], [+3/4, +1/4, 0], [+3/4, +4/4, 0],
                [+5/4, +4/4, 0], [+5/4, -1/4, 0], [-5/4, -1/4, 0], [-5/4, +4/4, 0],
                color=WHITE,fill_opacity=1,fill_color=TEN_RED
            ).shift(DOWN)

            V=VGroup(
                Line(LEFT,RIGHT).shift(DOWN*3/4),
                Line(LEFT,RIGHT).shift(UP*3/4),
                ArcBetweenPoints(LEFT+DOWN*3/4,LEFT+UP*3/4,angle=-TAU/2),
                ArcBetweenPoints(RIGHT+DOWN*3/4,RIGHT+UP*3/4,angle=+TAU/2),
                Square(0.5,color=WHITE,fill_opacity=1,fill_color=YELLOW).shift(DOWN*3/4),
                MyMathTex(r"B",color=BLACK).scale(0.75).shift(DOWN*3/4),
                Square(0.5,color=WHITE,fill_opacity=1,fill_color=YELLOW).shift(UP*3/4),
                MyMathTex(r"A^\dag",color=BLACK).scale(0.75).shift(UP*3/4),
            ).shift(DOWN)


            self.play(Write(adjoint))
            self.slide_break()
            self.play(adjoint.animate.shift(2*UP))
            self.add(V,P1)
            P1.save_state()
            V.save_state()
            P1.set_color(BG)
            V.set_color(BG)
            self.play(Restore(P1),Restore(V))
            self.slide_break()
            self.play(Transform(P1,P12,rate_func=rate_functions.ease_in_sine))
            self.play(Transform(P1,P2,rate_func=rate_functions.ease_out_sine))
            self.slide_break()
            self.play(Transform(P1,P23,rate_func=rate_functions.ease_in_sine))
            self.play(Transform(P1,P3,rate_func=rate_functions.ease_out_sine))
            self.slide_break()
            self.play(V.animate.set_color(BG),P1.animate.set_color(BG),FadeOut(adjoint))
            self.remove(V,P1)
            self.slide_break()
        if subsec==4 or subsec==-1:
            # unitality

            unitality1=VGroup(
                MyTex(r"$\mathcal E$ is trace-preserving").shift(1.5*UP),
                MyMathTex(r"\iff").rotate(TAU/4),
                MyTex(r"$\mathcal E^\dag$ is unital").shift(1.5*DOWN),
            )
            unitality2=VGroup(
                MyMathTex(r"\mathrm{Tr}\left(\mathcal E\left(\cdot\right)\right)=\mathrm{Tr}\left(\cdot\right)").shift(1.5*UP),
                MyMathTex(r"\iff").rotate(TAU/4),
                MyMathTex(r"\mathcal E^\dag(I)=I").shift(1.5*DOWN),
            )
            unitality3=VGroup(
                VGroup(
                    Polygon(
                        [+5/4, -1/4, 0],
                        [+3/4, -1/4, 0],
                        [+3/4, +2/4, 0],
                        [-3/4, +2/4, 0],
                        [-3/4, -1/4, 0],
                        [-5/4, -1/4, 0],
                        [-5/4, +4/4, 0],
                        [+5/4, +4/4, 0],
                        color=WHITE,fill_opacity=1,fill_color=TEN_RED
                    ),
                    Line(LEFT*3/4,LEFT/4),
                    Line(RIGHT*3/4,RIGHT/4),
                    Line(LEFT*5/4,LEFT*6/4),
                    Line(RIGHT*5/4,RIGHT*6/4),
                    Line(LEFT*6/4,RIGHT*6/4).shift(DOWN/2),
                    ArcBetweenPoints(LEFT*6/4,LEFT*6/4+DOWN/2,angle=TAU/2),
                    ArcBetweenPoints(RIGHT*6/4,RIGHT*6/4+DOWN/2,angle=-TAU/2),
                    VGroup(
                        MyMathTex("=").shift(LEFT*1.5+DOWN/4),
                        Line(LEFT/2,RIGHT/2).shift(DOWN/2),
                        Line(LEFT/2,LEFT/4),
                        Line(RIGHT/4,RIGHT/2),
                        ArcBetweenPoints(LEFT/2,LEFT/2+DOWN/2,angle=TAU/2),
                        ArcBetweenPoints(RIGHT/2,RIGHT/2+DOWN/2,angle=-TAU/2),
                    ).shift(RIGHT*4),
                ).shift(1.5*UP+2*LEFT),
                MyMathTex(r"\iff").rotate(TAU/4),
                VGroup(
                    Line(1.75*LEFT,1.75*RIGHT).shift(UP*3/4),
                    Polygon(
                        [-3/4, +4/4, 0], [-3/4, +1/4, 0], [+3/4, +1/4, 0], [+3/4, +4/4, 0],
                        [+5/4, +4/4, 0], [+5/4, -1/4, 0], [-5/4, -1/4, 0], [-5/4, +4/4, 0],
                        color=WHITE,fill_opacity=1,fill_color=TEN_RED
                    ),
                    MyMathTex("=").shift(2.5*RIGHT+UP/2),
                    Line(ORIGIN,RIGHT*1.5).shift(3.25*RIGHT+UP/2),
                ).shift(1.75*DOWN+2*LEFT),
            ).shift(3*RIGHT)

            unitality4=VGroup(
                VGroup(
                    Polygon(
                        [+5/4, -1/4, 0],
                        [+3/4, -1/4, 0],
                        [+3/4, +2/4, 0],
                        [-3/4, +2/4, 0],
                        [-3/4, -1/4, 0],
                        [-5/4, -1/4, 0],
                        [-5/4, +4/4, 0],
                        [+5/4, +4/4, 0],
                        color=WHITE,fill_opacity=1,fill_color=TEN_RED
                    ),
                    Line(LEFT*3/4,LEFT/4),
                    Line(RIGHT*3/4,RIGHT/4),
                    Line(LEFT*5/4,LEFT*6/4),
                    Line(RIGHT*5/4,RIGHT*6/4),
                    Line(LEFT*6/4,RIGHT*6/4).shift(1.25*UP),
                    ArcBetweenPoints(LEFT*6/4,LEFT*6/4+1.25*UP,angle=-TAU/2),
                    ArcBetweenPoints(RIGHT*6/4,RIGHT*6/4+1.25*UP,angle=TAU/2),
                    VGroup(
                        MyMathTex("=").shift(LEFT*1.5+DOWN/4),
                        Line(LEFT/2,RIGHT/2).shift(UP/2),
                        Line(LEFT/2,LEFT/4),
                        Line(RIGHT/4,RIGHT/2),
                        ArcBetweenPoints(LEFT/2,LEFT/2+UP/2,angle=-TAU/2),
                        ArcBetweenPoints(RIGHT/2,RIGHT/2+UP/2,angle=TAU/2),
                    ).shift(RIGHT*4),
                ).shift(1.5*UP+2*LEFT),
                MyMathTex(r"\iff").rotate(TAU/4),
                VGroup(
                    Line(1.75*LEFT,1.75*RIGHT).shift(UP*3/4),
                    Polygon(
                        [-3/4, +4/4, 0], [-3/4, +1/4, 0], [+3/4, +1/4, 0], [+3/4, +4/4, 0],
                        [+5/4, +4/4, 0], [+5/4, -1/4, 0], [-5/4, -1/4, 0], [-5/4, +4/4, 0],
                        color=WHITE,fill_opacity=1,fill_color=TEN_RED
                    ),
                    MyMathTex("=").shift(2.5*RIGHT+UP/2),
                    Line(ORIGIN,RIGHT*1.5).shift(3.25*RIGHT+UP/2),
                ).shift(1.75*DOWN+2*LEFT),
            ).shift(3*RIGHT)

            unitality1.shift(DOWN/2)
            unitality2.shift(DOWN/2)
            unitality3.shift(DOWN/2)
            unitality4.shift(DOWN/2)
            # unitality4.move_to(unitality3).shift(LEFT*3/16)

            self.play(FadeIn(unitality1))
            self.slide_break()
            self.play(Transform(unitality1[0],unitality2[0]))
            self.slide_break()
            self.play(Transform(unitality1[2],unitality2[2]))
            self.remove(unitality1,unitality2)
            self.add(unitality2)
            self.slide_break()
            self.play(unitality2.animate.shift(4*LEFT))
            unitality3.save_state()
            unitality3.set_color(BG)
            self.play(Restore(unitality3))
            self.slide_break()
            # self.add(unitality4)
            self.play(Transform(unitality3,unitality4))
            self.slide_break()
            self.play(FadeOut(unitality2),unitality3.animate.set_color(BG))
            self.remove(*unitality3)
            self.slide_break()
        if subsec==5 or subsec==-1:
            # superoperator + choi

            superop=VGroup(
                Polygon(
                    [+5/4, -1/4, 0],
                    [+3/4, -1/4, 0],
                    [+3/4, +2/4, 0],
                    [-3/4, +2/4, 0],
                    [-3/4, -1/4, 0],
                    [-5/4, -1/4, 0],
                    [-5/4, +4/4, 0],
                    [+5/4, +4/4, 0],
                    color=WHITE,fill_opacity=1,fill_color=TEN_RED
                ),
                CubicBezier(LEFT*3/4,LEFT/2,LEFT/4,LEFT/4+DOWN),
                CubicBezier(RIGHT*3/4,RIGHT/2,RIGHT/4,RIGHT/4+DOWN),
                CubicBezier(LEFT*5/4,LEFT*8/4,LEFT*8/4+UP*1.5,LEFT*5/4+UP*1.5),
                CubicBezier(LEFT*5/4+UP*1.5,LEFT*2/4+UP*1.5,LEFT/4+2*UP,LEFT/4+2.5*UP),
                CubicBezier(RIGHT*5/4,RIGHT*8/4,RIGHT*8/4+UP*1.5,RIGHT*5/4+UP*1.5),
                CubicBezier(RIGHT*5/4+UP*1.5,RIGHT*2/4+UP*1.5,RIGHT/4+2*UP,RIGHT/4+2.5*UP),
            ).move_to(3*LEFT)
            choi=VGroup(
                Polygon(
                    [+5/4, -1/4, 0],
                    [+3/4, -1/4, 0],
                    [+3/4, +2/4, 0],
                    [-3/4, +2/4, 0],
                    [-3/4, -1/4, 0],
                    [-5/4, -1/4, 0],
                    [-5/4, +4/4, 0],
                    [+5/4, +4/4, 0],
                    color=WHITE,fill_opacity=1,fill_color=TEN_RED
                ),
                ArcBetweenPoints(LEFT*3/4,LEFT*3/4+DOWN*3/4,angle=-TAU/2),
                ArcBetweenPoints(RIGHT*3/4,RIGHT*3/4+DOWN*3/4,angle=+TAU/2),
                Line(LEFT*5/4,LEFT*9/4+DOWN*0/8),
                Line(RIGHT*5/4,RIGHT*9/4+DOWN*0/8),
                CubicBezier(
                    LEFT*3/4+DOWN*3/4,
                    LEFT*3/4+DOWN*3/4+LEFT/2,
                    LEFT*9/4+DOWN*4/8+RIGHT/2,
                    LEFT*9/4+DOWN*4/8),
                CubicBezier(
                    RIGHT*3/4+DOWN*3/4,
                    RIGHT*3/4+DOWN*3/4+RIGHT/2,
                    RIGHT*9/4+DOWN*4/8+LEFT/2,
                    RIGHT*9/4+DOWN*4/8),
            ).move_to(3*RIGHT+DOWN/2)

            superop.save_state()
            superop.set_color(BG)
            choi.save_state()
            choi.set_color(BG)
            self.play(Restore(superop))
            self.slide_break()
            self.play(Restore(choi))
            self.slide_break()
            self.play(superop.animate.set_color(BG),choi.animate.set_color(BG))
            self.remove(superop,choi)
            self.slide_break()
        if subsec==6 or subsec==-1:
            # chois theorem

            pos=MyMathTex(r"\rho\geq 0 ~\implies~\mathcal E(\rho)\geq 0")
            self.play(Write(pos))
            self.slide_break()
            self.play(pos.animate.shift(2.5*DOWN))

            E=VGroup(
                Polygon(
                    [+5/4, -1/4, 0],
                    [+3/4, -1/4, 0],
                    [+3/4, +2/4, 0],
                    [-3/4, +2/4, 0],
                    [-3/4, -1/4, 0],
                    [-5/4, -1/4, 0],
                    [-5/4, +4/4, 0],
                    [+5/4, +4/4, 0],
                    color=WHITE,fill_opacity=1,fill_color=TEN_RED
                ),
                Line(LEFT*5/4,LEFT*7/4),
                Line(RIGHT*5/4,RIGHT*7/4),
                Line(LEFT*3/4,LEFT*1/4),
                Line(RIGHT*3/4,RIGHT*1/4),
            )
            S=VGroup(
                VGroup(
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE),
                ),
                VGroup(
                    Rectangle(width=0.5,height=1.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).move_to(DOWN/2),
                    Line(LEFT*7/4,LEFT/4).shift(DOWN),
                    Line(RIGHT*7/4,RIGHT/4).shift(DOWN),
                ),

                VGroup(
                    Line(LEFT*7/4,LEFT/4).shift(DOWN),
                    Line(RIGHT*7/4,RIGHT/4).shift(DOWN),
                    CubicBezier(
                        LEFT/4,
                        LEFT/4+RIGHT/4,
                        LEFT/4+DOWN+RIGHT/4,
                        LEFT/4+DOWN,
                    ),
                    CubicBezier(
                        RIGHT/4,
                        RIGHT/4+LEFT/4,
                        RIGHT/4+DOWN+LEFT/4,
                        RIGHT/4+DOWN,
                    ),
                ),
            )
            E.shift(UP/2)
            S.shift(UP/2)

            self.play(FadeIn(E))
            self.slide_break()
            self.play(FadeIn(S[0]))
            self.slide_break()
            self.play(FadeIn(S[1]))
            self.remove(S[0])
            self.slide_break()
            self.add(S[2])
            self.add(S[1])
            self.play(FadeOut(S[1]))
            self.slide_break()

            self.play(E.animate.shift(3*LEFT),S[2].animate.shift(3*LEFT))
            eq=MyMathTex("=")
            rhs=VGroup(
                VGroup(
                    Rectangle(width=0.5,height=1.5,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift(LEFT*3/4),
                    Rectangle(width=0.5,height=1.5,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift(RIGHT*3/4),
                    Line(LEFT/2,RIGHT/2),
                    Line(LEFT,LEFT*1.5).shift(UP/2),
                    Line(LEFT,LEFT*1.5).shift(DOWN/2),
                    Line(RIGHT,RIGHT*1.5).shift(UP/2),
                    Line(RIGHT,RIGHT*1.5).shift(DOWN/2),
                ),
                VGroup(
                    Polygon(LEFT/2,RIGHT/2,DOWN/2,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift(LEFT*3/4),
                    Polygon(LEFT/2,RIGHT/2,DOWN/2,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift(RIGHT*3/4),
                    CubicBezier(
                        LEFT/2,
                        LEFT/2+UP/2,
                        RIGHT/2+UP/2,
                        RIGHT/2),
                    CubicBezier(
                        LEFT*2/2,
                        LEFT*2/2+UP/4,
                        LEFT*5/4+UP/2,
                        LEFT*3/2+UP/2),
                    CubicBezier(
                        RIGHT*2/2,
                        RIGHT*2/2+UP/4,
                        RIGHT*5/4+UP/2,
                        RIGHT*3/2+UP/2),
                    CubicBezier(
                        DOWN/2+LEFT*3/4,
                        DOWN/2+LEFT*3/4+DOWN/4,
                        LEFT*3/2+DOWN+RIGHT/4,
                        LEFT*3/2+DOWN),
                    CubicBezier(
                        DOWN/2+RIGHT*3/4,
                        DOWN/2+RIGHT*3/4+DOWN/4,
                        RIGHT*3/2+DOWN+LEFT/4,
                        RIGHT*3/2+DOWN),
                ),
            ).shift(3*RIGHT+UP/4)
            self.play(FadeIn(eq),FadeIn(rhs[0]))
            self.slide_break()
            self.play(FadeOut(rhs[0]))
            self.play(FadeIn(rhs[1]))
            self.slide_break()

            self.play(FadeOut(eq),FadeOut(rhs[1]),FadeOut(E),FadeOut(S[-1]),FadeOut(pos))
            self.slide_break()
        if subsec==7 or subsec==-1:
            # stinespring
            krauss=VGroup(
                VGroup(
                    Polygon(
                        [+5/4, -1/4, 0],
                        [+3/4, -1/4, 0],
                        [+3/4, +2/4, 0],
                        [-3/4, +2/4, 0],
                        [-3/4, -1/4, 0],
                        [-5/4, -1/4, 0],
                        [-5/4, +4/4, 0],
                        [+5/4, +4/4, 0],
                        color=WHITE,fill_opacity=1,fill_color=TEN_RED
                    ),
                    Line(LEFT*5/4,LEFT*7/4),
                    Line(RIGHT*5/4,RIGHT*7/4),
                    Line(LEFT*3/4,LEFT*1/4),
                    Line(RIGHT*3/4,RIGHT*1/4),
                ).shift(3*LEFT),
                MyMathTex("="),
                VGroup(
                    Polygon(UL/2,DL/2,ORIGIN,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift(LEFT/2),
                    Polygon(UR/2,DR/2,ORIGIN,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift(RIGHT/2),
                    ArcBetweenPoints(LEFT+UP/4,LEFT+UP*3/4,angle=-TAU/2),
                    ArcBetweenPoints(RIGHT+UP/4,RIGHT+UP*3/4,angle=TAU/2),
                    Line().shift(UP*3/4),
                    Line(LEFT/2,LEFT/4),
                    Line(RIGHT/2,RIGHT/4),
                    Line(ORIGIN,LEFT/2).shift(DOWN/4,LEFT),
                    Line(ORIGIN,RIGHT/2).shift(DOWN/4,RIGHT),
                ).shift(3*RIGHT+UP/4)
            )
            self.play(FadeIn(krauss))
            self.slide_break()
            self.play(krauss.animate.shift(UP))
            self.slide_break()

            dilation=MyMathTex(
                r"&\mathcal E\text{  CP}",r"& &\implies & ",r"\mathcal E(\rho)&=\sum_i K_i \rho K_i^\dag\\",
                r"&\mathcal E\text{  CPTP}",r" & &\implies & ",r"\mathcal E(\rho)&=\mathrm{Tr}_E\left( V\rho V^\dag\right)",
            )
            dilation[0:6:3].shift(RIGHT*1.5)
            dilation[2:6:3].shift(LEFT*1.5)
            dilation.move_to(DOWN*1.25)

            self.play(Write(dilation[:3]))
            self.slide_break()
            self.play(Write(dilation[3:]))
            self.slide_break()

            self.play(FadeOut(dilation),FadeOut(krauss))
            self.slide_break()
        if subsec==8 or subsec==-1:
            # bell states
            bell=VGroup(
                MyMathTex(r"\left|\Phi^+\right\rangle\propto \left|00\right\rangle+\left|11\right\rangle",r"=\left|\Omega(I)\right\rangle"),
                MyMathTex(r"\left|\Phi^-\right\rangle\propto \left|00\right\rangle-\left|11\right\rangle",r"=\left|\Omega(Z)\right\rangle"),
                MyMathTex(r"\left|\Psi^+\right\rangle\propto \left|01\right\rangle+\left|10\right\rangle",r"=\left|\Omega(X)\right\rangle"),
                MyMathTex(r"\left|\Psi^-\right\rangle\propto \left|01\right\rangle-\left|10\right\rangle",r"=\left|\Omega(Y)\right\rangle"),
            ).arrange(DOWN,aligned_edge=LEFT).shift(RIGHT)
            bell2=VGroup(
                VGroup(
                    Rectangle(width=1,height=2,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE),
                    Line(ORIGIN,LEFT*.5).shift(UP*.75,LEFT*.5),
                    Line(ORIGIN,LEFT*.5).shift(DOWN*.75,LEFT*.5),
                    MyMathTex(r"\Omega(U)",color=BLACK).scale(.75),
                ),
                MyMathTex(":="),
                VGroup(
                    Line(ORIGIN,LEFT*.5).shift(UP*.75),
                    Line(RIGHT*.5,LEFT*.5).shift(DOWN*.75),
                    Square(.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(UP*.75+RIGHT*.25),
                    MyMathTex(r"U",color=BLACK).scale(.75).move_to(UP*.75+RIGHT*.25),
                    ArcBetweenPoints(RIGHT/2+UP*3/4,RIGHT/2+DOWN*3/4,angle=-TAU/2),
                ),
            ).arrange(RIGHT,buff=0.5).move_to(3.75*LEFT)
            bell2[-1].shift(UP/8)
            self.play(*[FadeIn(bell[i][0]) for i in range(4)])
            self.slide_break()
            self.play(*[bell[i][0].animate.shift(1.75*RIGHT) for i in range(4)])
            for i in range(4):
                bell[i][1].shift(1.75*RIGHT)
            self.play(FadeIn(bell2))
            self.slide_break()
            self.play(*[FadeIn(bell[i][1]) for i in range(4)])
            self.slide_break()
            self.play(FadeOut(bell),FadeOut(bell2))
            self.slide_break()
        if subsec==9 or subsec==-1:

            teleport1=VGroup(
                MyMathTex(
                    r"\bigl(",
                    r"\langle\Omega|",
                    r"\otimes ",
                    r"I",
                    r"\bigr)~ \bigl(|\psi\rangle\otimes",
                    r"|\Omega\rangle",
                    r"\bigr)",
                ),
                MyMathTex(
                    r"\bigl(",
                    r"\langle\Omega(p)|",
                    r"\otimes ",
                    r"p",
                    r"\bigr)~ \bigl(|\psi\rangle\otimes",
                    r"|\Omega\rangle",
                    r"\bigr)",
                ),
                MyMathTex(
                    r"\bigl(",
                    r"\langle\Omega(p)|",
                    r"\otimes ",
                    r"Up U^\dag",
                    r"\bigr)~ \bigl(|\psi\rangle\otimes",
                    r"|\Omega(U^{\mathrm T})\rangle",
                    r"\bigr)",
                ),
            ).move_to(1.5*UP)

            teleport2=VGroup(
                VGroup(
                    DashedLine(DOWN*3/2,UP*3/2,dash_length=.1).set_opacity(1/2),
                    DashedLine(2*LEFT,2*RIGHT,dash_length=.1).set_opacity(1/2).shift(DOWN/2),
                    Line(LEFT/2,RIGHT/2).shift(UP),
                    Line(LEFT/2,RIGHT/2),
                    Line(LEFT*3/2,RIGHT/2).shift(DOWN),
                    ArcBetweenPoints(UP+LEFT/2,LEFT/2,angle=TAU/2),
                    ArcBetweenPoints(RIGHT/2,DOWN+RIGHT/2,angle=-TAU/2),

                    Square(1/2,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(RIGHT/2+UP),
                    MyMathTex(r"\psi",color=BLACK).shift(RIGHT/2+UP).scale(.75),
                ),
                VGroup(
                    VGroup(
                        Square(1/2,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift(LEFT/2+UP),
                        MyMathTex(r"p^\dag",color=BLACK).shift(LEFT/2+UP).scale(.75),
                    ),
                    VGroup(
                        Square(1/2,color=WHITE,fill_opacity=1,fill_color=TEN_RED).shift(LEFT/2+DOWN),
                        MyMathTex(r"p",color=BLACK).shift(LEFT/2+DOWN).scale(.75),
                    ),
                ),
                VGroup(
                    VGroup(
                        Square(1/2,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift(LEFT/2+UP),
                        MyMathTex(r"p^\dag",color=BLACK).shift(LEFT/2+UP).scale(.75),
                    ),
                    VGroup(
                        Rectangle(height=1/2,width=1,color=WHITE,fill_opacity=1,fill_color=TEN_RED).shift(LEFT*3/4+DOWN),
                        MyMathTex(r"UpU^\dag",color=BLACK).shift(LEFT*3/4+DOWN).scale(.75),
                    ),
                    VGroup(
                        Square(1/2,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(RIGHT/2),
                        MyMathTex(r"U^{\mathrm T}",color=BLACK).shift(RIGHT/2).scale(.7),
                    ),
                ),
            ).shift(DOWN)
            self.play(FadeIn(teleport1[0]))
            self.slide_break()
            teleport2[0].save_state()
            teleport2[0].set_color(BG)
            self.play(Restore(teleport2[0]))
            self.slide_break()

            self.play(Transform(teleport1[0],teleport1[1]))
            self.slide_break()
            self.play(FadeIn(teleport2[1]))
            self.slide_break()

            self.play(Transform(teleport1[0],teleport1[2]))
            self.slide_break()

            self.play(
                ReplacementTransform(teleport2[1][0],teleport2[2][0]),
                ReplacementTransform(teleport2[1][1],teleport2[2][1]),
                FadeIn(teleport2[2][2]),
            )
            self.slide_break()

            self.play(
                FadeOut(teleport1[0]),
                teleport2[0].animate.set_color(BG),
                teleport2[2].animate.set_color(BG),
            )
            self.remove(teleport2[0],teleport2[2])
            self.slide_break()

        self.play(Restore(toc))
        self.slide_break()
        self.play(
            toc[tocindex[0]].animate.set_opacity(0.25),
            toc[tocindex[0]+1].animate.set_opacity(1),
        )

class Lec2_1(SlideScene):
    def construct(self):
        tocindex=(1,1)
        toc.set_opacity(0.25)
        toc[tocindex[0]].set_opacity(1)
        toc.save_state()
        heading = toc[tocindex[0]][tocindex[1]]
        self.add(toc,footer)
        self.play(
            toc.animate.set_opacity(0),
            heading.animate.scale(2).to_corner(UP).set_x(0),
        )
        heading.set_opacity(1)
        self.slide_break()

        subsec = -1
        # 1     intro
        # 2     schmidt
        # 3     entanglement
        # 4     truncation, gauge
        # 5     vidal
        # 6     simulations
        # 7     ?
        # 8     ?
        # 9     ?
        # 10    ?

        if subsec==1 or subsec==-1:
            mps1=VGroup(
                MyMathTex(
                    r"\ket{\psi}=",
                    r"\ket{v_1}\otimes \ket{v_2}\otimes \cdots \otimes \ket{v_n}"
                ),
                MyMathTex(
                    r"\ket{\psi}=",
                    r"\sum_{\lbrace b\rbrace}",
                    r"\alpha_{b_1}^{(1)}\alpha_{b_2}^{(2)}\cdots\alpha_{b_n}^{(n)}",
                    r"~\ket{b_1 b_2\cdots b_n}"),
                MyMathTex(
                    r"\ket{\psi}=",
                    r"\sum_{\lbrace b\rbrace}",
                    r"\Tr\left(A_{b_1}^{(1)}A_{b_2}^{(2)}\cdots A_{b_n}^{(n)}\right)",
                    r"~\ket{b_1 b_2\cdots b_n}"
                ),

                MyMathTex(
                    r"\ket{\psi}=",
                    r"\sum_{\lbrace b\rbrace}",
                    r"\Tr\left(",
                    r"A_{b_1}^{(1)}A_{b_2}^{(2)}\cdots A_{b_n}^{(n)}",
                    r"\right)",
                    r"~\ket{b_1 b_2\cdots b_n}"
                ),
                MyMathTex(
                    r"\ket{\psi}=",
                    r"\sum_{\lbrace b\rbrace}",
                    r" ",
                    r"A_{b_1}^{(1)}A_{b_2}^{(2)}\cdots A_{b_n}^{(n)}",
                    r" ",
                    r"~\ket{b_1 b_2\cdots b_n}"
                ),

            )

            mps2=VGroup(
                VGroup(), # product state
                VGroup(), # internal bonds
                VGroup(), # trace
                VGroup(), # phantoms
                VGroup(), # labels
            )
            n=5
            for i in range(n):
                mps2[0]+=Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).move_to(i*RIGHT)
                mps2[0]+=Line(UP/4,UP*3/4).shift(i*RIGHT)
                mps2[4]+=MyMathTex("(%d)"%(i+1)).set_color(BLACK).move_to(i*RIGHT).scale(.75)
            for i in range(n-1):
                mps2[1]+=Line(LEFT/4,RIGHT/4).move_to(i*RIGHT+RIGHT/2)
            mps2[2]+=Line(LEFT/4,RIGHT/4+(n-1)*RIGHT).shift(DOWN/2)
            mps2[2]+=ArcBetweenPoints(ORIGIN,DOWN/2,angle=TAU/2).shift(LEFT/4)
            mps2[2]+=ArcBetweenPoints(ORIGIN,DOWN/2,angle=-TAU/2).shift((n-3/4)*RIGHT)
            mps2[3]+=DashedLine(LEFT/4,RIGHT/4).move_to(LEFT/2)
            mps2[3]+=DashedLine(LEFT/4,RIGHT/4).move_to((n-1/2)*RIGHT)
            mps2.scale(1.25).move_to(1.25*DOWN)

            self.play(Write(mps1[0]))
            self.slide_break()

            self.play(
                FadeTransform(mps1[0][0],mps1[1][0]),
                FadeTransform(mps1[0][1],mps1[1][1:]),
            )
            self.slide_break()
            self.play(
                mps1[1][1].animate.set_color(RED),
                mps1[1][2].animate.set_color(YELLOW),
                mps1[1][3].animate.set_color(RED),
            )
            self.slide_break()

            mps1[2][1].set_color(RED)
            mps1[2][2].set_color(YELLOW)
            mps1[2][3].set_color(RED)

            mps1[3][1].set_color(RED)
            mps1[3][2:5].set_color(YELLOW)
            mps1[3][5].set_color(RED)

            mps1[4][1].set_color(RED)
            mps1[4][2:5].set_color(YELLOW)
            mps1[4][5].set_color(RED)

            self.play(mps1[1].animate.shift(1.25*UP))
            mps1[2:].shift(1.25*UP)
            self.play(FadeIn(mps2[0]))
            self.slide_break()

            self.play(FadeTransform(mps1[1],mps1[2]))
            self.slide_break()
            self.play(FadeIn(mps2[1]),FadeIn(mps2[2]))
            self.slide_break()

            self.play(FadeOut(mps2[2]))
            self.slide_break()
            self.remove(mps1[2])
            # self.remove(mps2[3])
            self.play(ReplacementTransform(mps1[3],mps1[4]))
            self.slide_break()
            self.play(FadeIn(mps2[3]))
            self.slide_break()
            self.play(FadeOut(mps2[3]))
            self.slide_break()
            self.play(Write(mps2[4]))
            self.slide_break()

            self.play(
                FadeOut(mps1[4]),
                VGroup(mps2[0],mps2[1],mps2[4]).animate.set_color(BG),
            )
            self.remove(*mps2)
            self.slide_break()
        if subsec==2 or subsec==-1:

            # schmidt = svd, truncation
            schmidt1 = MyMathTex(
                r"\ket\psi&=",
                r"\sum_{i,j}",
                r"c_{i,j} \ket{i}\otimes \ket{j}\\",
                r"&=\sum_{k}",
                r"\sqrt{\lambda_k}",
                r"\ket{l_k}",
                r"\otimes",
                r"\ket{r_k}",
            )
            schmidt1[2].set_color(TEN_BLUE)
            schmidt1[4].set_color(TEN_RED)
            schmidt1[5].set_color(TEN_GREEN)
            schmidt1[7].set_color(TEN_YELLOW)

            self.play(Write(schmidt1[:3]))
            self.slide_break()
            self.play(Write(schmidt1[3:]))
            self.slide_break()
            self.play(schmidt1.animate.shift(UP))
            self.slide_break()

            schmidt2= VGroup(
                MyMathTex(" = "),

                VGroup(
                    Rectangle(width=1.5,height=0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE),
                ),
                VGroup(
                    Line(UP/4,UP*3/4).shift(LEFT/2),
                    Line(UP/4,UP*3/4).shift(RIGHT/2),
                ),
                VGroup(
                    OffsetBezier(UP/4,UP/4,LEFT+UP/2,RIGHT/2).shift(LEFT/2),
                    OffsetBezier(UP/4,UP/4,RIGHT+UP/2,LEFT/2).shift(RIGHT/2),
                ),

                VGroup(
                    Polygon(LEFT/2,UP/2+LEFT,DOWN/2+LEFT,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN),
                    Polygon(RIGHT/2,UP/2+RIGHT,DOWN/2+RIGHT,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW),
                    Line(LEFT/2,RIGHT/2),
                    Circle(3/16,color=WHITE,fill_opacity=1,fill_color=TEN_RED),
                ),
                VGroup(
                    OffsetBezier(LEFT,LEFT/2,LEFT*1.5+UP,DOWN),
                    OffsetBezier(RIGHT,RIGHT/2,RIGHT*1.5+UP,DOWN),
                ),
                VGroup(
                    Line(LEFT,LEFT*2),
                    Line(RIGHT,RIGHT*2),
                ),
            ).move_to(DOWN*1.5)

            schmidt2[1:4].shift(2.5*LEFT)
            schmidt2[4:7].scale(.75).shift(2.5*RIGHT)
            schmidt2.move_to(DOWN*2)

            self.play(
                FadeIn(schmidt2[1]),
                FadeIn(schmidt2[2]),
            )
            self.slide_break()

            self.play(
                FadeIn(schmidt2[0]),
                FadeIn(schmidt2[4]),
                FadeIn(schmidt2[5]),
            )
            self.slide_break()

            self.play(
                ReplacementTransform(schmidt2[2],schmidt2[3]),
                ReplacementTransform(schmidt2[5],schmidt2[6]),
            )
            self.slide_break()

            self.play(schmidt1.animate.shift(3*LEFT))
            schmidt3=MyMathTex(
                r"S_1:=&-\sum_k \lambda_k \log \lambda_k\\",
                r"S_{\alpha}:=&\frac 1{1-\alpha}\log \sum_k \lambda_k^\alpha",
            ).move_to(UP+3.5*RIGHT)
            self.play(FadeIn(schmidt3[0]))
            self.slide_break()
            self.play(FadeIn(schmidt3[1]))
            self.slide_break()

            self.play(*[FadeOut(mob) for mob in self.mobjects if mob!=toc and mob!=footer])
            self.slide_break()
        if subsec==3 or subsec==-1:
            # entanglement

            ent1=VGroup(
                VGroup(
                    Line(RIGHT/4,RIGHT*3/4),
                    Line(RIGHT/4,RIGHT*3/4).shift(RIGHT*2),
                    Line(RIGHT/4,RIGHT*3/4).shift(RIGHT*3),
                ),
                VGroup(
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE),
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(RIGHT),
                ),
                VGroup(
                    Line(UP/4,UP*3/4),
                    Line(UP/4,UP*3/4).shift(RIGHT),
                ),

                Line(RIGHT/4,RIGHT*3/4).shift(RIGHT),

                VGroup(
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(RIGHT*2),
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(RIGHT*3),
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(RIGHT*4),
                ),
                VGroup(
                    Line(UP/4,UP*3/4).shift(RIGHT*2),
                    Line(UP/4,UP*3/4).shift(RIGHT*3),
                    Line(UP/4,UP*3/4).shift(RIGHT*4),
                ),
                DashedLine(DOWN/2,1*UP,dash_length=0.1,color=GRAY).shift(RIGHT*1.5),
            ).move_to(ORIGIN).scale(1.5)

            ent2=VGroup(
                Rectangle(height=0.5,width=1,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).next_to(RIGHT*6/4,LEFT),
                VGroup(
                    Line(UP/4,UP*3/4).shift(RIGHT/2),
                    Line(UP/4,UP*3/4).shift(RIGHT),
                ),

                Line(RIGHT/4,RIGHT*3/4).shift(RIGHT),

                Rectangle(height=0.5,width=1.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).next_to(RIGHT*6/4,RIGHT),
                VGroup(
                    Line(UP/4,UP*3/4).shift(RIGHT*2),
                    Line(UP/4,UP*3/4).shift(RIGHT*2.5),
                    Line(UP/4,UP*3/4).shift(RIGHT*3),
                ),
                DashedLine(DOWN/2,1*UP,dash_length=0.1,color=GRAY).shift(RIGHT*1.5),
            ).move_to(ORIGIN).scale(1.5)

            self.play(FadeIn(ent1[:-1]))
            self.slide_break()
            self.play(Write(ent1[-1]))
            self.slide_break()
            self.play(
                *[FadeTransform(ent1[i+1],ent2[i]) for i in range(len(ent2))],
                FadeOut(ent1[0]),
            )
            self.slide_break()

            ent3=VGroup(
                MyTex(r"MPS with $\text{BD}=\chi$"),
                MyMathTex(r"\implies"),
                MyTex(r"Entanglement rank $\leq \chi$"),
            ).arrange(RIGHT,buff=1).move_to(UP*1)

            self.play(ent2.animate.shift(DOWN*1.5))
            self.play(FadeIn(ent3))
            self.slide_break()
            self.play(Transform(ent3[1],MyMathTex(r"\iff").move_to(ent3[1])))
            self.slide_break()
            self.play(FadeOut(ent2))
            self.slide_break()

            ent4_1=VGroup(
                Line(UP/4,UP*3/4).shift(RIGHT*0/2),
                Line(UP/4,UP*3/4).shift(RIGHT*1/2),
                Line(UP/4,UP*3/4).shift(RIGHT*2/2),
                Line(UP/4,UP*3/4).shift(RIGHT*3/2),
                Line(UP/4,UP*3/4).shift(RIGHT*4/2),
                Rectangle(height=0.5,width=2.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(RIGHT),
                DashedLine(DOWN/2,1*UP,dash_length=0.1,color=GRAY).shift(RIGHT/4),
            ).move_to(DOWN*1.5).scale(1.5)
            ent4_2=VGroup(
                Line(UP/4,UP*3/4).shift(RIGHT*0/2),
                Line(UP/4,UP*3/4).shift(RIGHT*2/2),
                Line(UP/4,UP*3/4).shift(RIGHT*3/2),
                Line(UP/4,UP*3/4).shift(RIGHT*4/2),
                Line(UP/4,UP*3/4).shift(RIGHT*5/2),
                VGroup(
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(RIGHT*0),
                    Rectangle(height=0.5,width=2,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(RIGHT*1.75),
                    Line(RIGHT/4,RIGHT*3/4)
                ),
                DashedLine(DOWN/2,1*UP,dash_length=0.1,color=GRAY).shift(RIGHT/2),
            ).move_to(DOWN*1.5).scale(1.5)
            self.play(FadeIn(ent4_1[:-1]))
            self.slide_break()
            self.play(Write(ent4_1[-1]))
            self.slide_break()
            self.play(*[FadeTransform(ent4_1[i],ent4_2[i]) for i in range(len(ent4_1))])
            self.slide_break()

            self.remove(*ent4_2)
            ent4_1=VGroup(
                Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(RIGHT*0),
                Line(UP/4,UP*3/4).shift(RIGHT*0/2),
                Line(RIGHT/4,RIGHT*3/4),

                Line(UP/4,UP*3/4).shift(RIGHT*2/2),
                Line(UP/4,UP*3/4).shift(RIGHT*3/2),
                Line(UP/4,UP*3/4).shift(RIGHT*4/2),
                Line(UP/4,UP*3/4).shift(RIGHT*5/2),
                Rectangle(height=0.5,width=2,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(RIGHT*1.75),
                DashedLine(DOWN/2,1*UP,dash_length=0.1,color=GRAY).shift(RIGHT/2),
                DashedLine(DOWN/2,1*UP,dash_length=0.1,color=GRAY).shift(RIGHT*5/4),
            ).move_to(DOWN*1.5).scale(1.5)
            ent4_2=VGroup(
                Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(RIGHT*0),
                Line(UP/4,UP*3/4).shift(RIGHT*0),
                Line(RIGHT/4,RIGHT*3/4),

                Line(UP/4,UP*3/4).shift(RIGHT*1),
                Line(UP/4,UP*3/4).shift(RIGHT*4/2),
                Line(UP/4,UP*3/4).shift(RIGHT*5/2),
                Line(UP/4,UP*3/4).shift(RIGHT*6/2),
                VGroup(
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(RIGHT*1),
                    Rectangle(height=0.5,width=1.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(RIGHT*10/4),
                    Line(RIGHT/4,RIGHT*3/4).shift(RIGHT),
                ),
                DashedLine(DOWN/2,1*UP,dash_length=0.1,color=GRAY).shift(RIGHT/2),
                DashedLine(DOWN/2,1*UP,dash_length=0.1,color=GRAY).shift(RIGHT*6/4),
            ).move_to(DOWN*1.5).scale(1.5)
            self.add(ent4_1[:-1])
            self.play(Write(ent4_1[-1]))
            self.slide_break()
            self.play(*[FadeTransform(ent4_1[i],ent4_2[i]) for i in range(len(ent4_1))])
            self.slide_break()

            self.remove(*ent4_2)
            ent4_1=VGroup(
                VGroup(
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(RIGHT*0),
                    Line(UP/4,UP*3/4).shift(RIGHT*0/2),
                    Line(RIGHT/4,RIGHT*3/4),
                    DashedLine(DOWN/2,1*UP,dash_length=0.1,color=GRAY).shift(RIGHT/2),
                ),
                VGroup(
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(RIGHT*0),
                    Line(UP/4,UP*3/4).shift(RIGHT*0/2),
                    Line(RIGHT/4,RIGHT*3/4),
                    DashedLine(DOWN/2,1*UP,dash_length=0.1,color=GRAY).shift(RIGHT/2),
                ).shift(RIGHT),
                Line(UP/4,UP*3/4).shift(RIGHT*4/2),
                Line(UP/4,UP*3/4).shift(RIGHT*5/2),
                Line(UP/4,UP*3/4).shift(RIGHT*6/2),
                Rectangle(height=0.5,width=3/2,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(RIGHT*10/4),
                DashedLine(DOWN/2,1*UP,dash_length=0.1,color=GRAY).shift(RIGHT*9/4),
            ).move_to(DOWN*1.5).scale(1.5)
            ent4_2=VGroup(
                VGroup(
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(RIGHT*0),
                    Line(UP/4,UP*3/4).shift(RIGHT*0/2),
                    Line(RIGHT/4,RIGHT*3/4),
                    DashedLine(DOWN/2,1*UP,dash_length=0.1,color=GRAY).shift(RIGHT/2),
                ),
                VGroup(
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(RIGHT*0),
                    Line(UP/4,UP*3/4).shift(RIGHT*0/2),
                    Line(RIGHT/4,RIGHT*3/4),
                    DashedLine(DOWN/2,1*UP,dash_length=0.1,color=GRAY).shift(RIGHT/2),
                ).shift(RIGHT),
                Line(UP/4,UP*3/4).shift(RIGHT*4/2),
                Line(UP/4,UP*3/4).shift(RIGHT*6/2),
                Line(UP/4,UP*3/4).shift(RIGHT*7/2),
                VGroup(
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(RIGHT*2),
                    Rectangle(height=0.5,width=2/2,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(RIGHT*13/4),
                    Line(RIGHT/4,RIGHT*3/4).shift(2*RIGHT),
                ),
                DashedLine(DOWN/2,1*UP,dash_length=0.1,color=GRAY).shift(RIGHT*10/4),
            ).move_to(DOWN*1.5).scale(1.5)
            self.add(ent4_1[:-1])
            self.play(Write(ent4_1[-1]))
            self.slide_break()
            self.play(*[FadeTransform(ent4_1[i],ent4_2[i]) for i in range(len(ent4_1))])
            self.slide_break()

            self.remove(*ent4_2)
            ent4_1=VGroup(
                VGroup(
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(RIGHT*0),
                    Line(UP/4,UP*3/4).shift(RIGHT*0/2),
                    Line(RIGHT/4,RIGHT*3/4),
                    DashedLine(DOWN/2,1*UP,dash_length=0.1,color=GRAY).shift(RIGHT/2),
                ),
                VGroup(
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(RIGHT*0),
                    Line(UP/4,UP*3/4).shift(RIGHT*0/2),
                    Line(RIGHT/4,RIGHT*3/4),
                    DashedLine(DOWN/2,1*UP,dash_length=0.1,color=GRAY).shift(RIGHT/2),
                ).shift(RIGHT),
                VGroup(
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(RIGHT*0),
                    Line(UP/4,UP*3/4).shift(RIGHT*0/2),
                    Line(RIGHT/4,RIGHT*3/4),
                    DashedLine(DOWN/2,1*UP,dash_length=0.1,color=GRAY).shift(RIGHT/2),
                ).shift(RIGHT*2),
                Line(UP/4,UP*3/4).shift(RIGHT*6/2),
                Line(UP/4,UP*3/4).shift(RIGHT*7/2),
                Rectangle(height=0.5,width=2/2,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(RIGHT*13/4),
                DashedLine(DOWN/2,1*UP,dash_length=0.1,color=GRAY).shift(RIGHT*13/4),
            ).move_to(DOWN*1.5).scale(1.5)
            ent4_2=VGroup(
                VGroup(
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(RIGHT*0),
                    Line(UP/4,UP*3/4).shift(RIGHT*0/2),
                    Line(RIGHT/4,RIGHT*3/4),
                    DashedLine(DOWN/2,1*UP,dash_length=0.1,color=GRAY).shift(RIGHT/2),
                ),
                VGroup(
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(RIGHT*0),
                    Line(UP/4,UP*3/4).shift(RIGHT*0/2),
                    Line(RIGHT/4,RIGHT*3/4),
                    DashedLine(DOWN/2,1*UP,dash_length=0.1,color=GRAY).shift(RIGHT/2),
                ).shift(RIGHT),
                VGroup(
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(RIGHT*0),
                    Line(UP/4,UP*3/4).shift(RIGHT*0/2),
                    Line(RIGHT/4,RIGHT*3/4),
                    DashedLine(DOWN/2,1*UP,dash_length=0.1,color=GRAY).shift(RIGHT/2),
                ).shift(RIGHT*2),
                Line(UP/4,UP*3/4).shift(RIGHT*6/2),
                Line(UP/4,UP*3/4).shift(RIGHT*8/2),
                VGroup(
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(RIGHT*3),
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(RIGHT*4),
                    Line(RIGHT/4,RIGHT*3/4).shift(3*RIGHT),
                ),
                DashedLine(DOWN/2,1*UP,dash_length=0.1,color=GRAY).shift(RIGHT*14/4),
            ).move_to(DOWN*1.5).scale(1.5)

            self.add(ent4_1[:-1])
            self.play(Write(ent4_1[-1]))
            self.slide_break()
            self.play(*[FadeTransform(ent4_1[i],ent4_2[i]) for i in range(len(ent4_1))])
            self.slide_break()

            self.play(*[FadeOut(mob) for mob in self.mobjects if mob!=toc and mob!=footer])
            self.slide_break()
        if subsec==4 or subsec==-1:
            # truncation

            trunc1=VGroup(
                VGroup(
                    *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(RIGHT*i) for i in range(5)],
                    *[Line(UP/4,UP*3/4).shift(RIGHT*i) for i in range(5)],
                    *[Line(RIGHT/4,RIGHT*3/4,stroke_width=20,color=TEN_RED).shift(RIGHT*i) for i in range(4)],
                ),
                MyMathTex(r"\xlongrightarrow{?}"),
                VGroup(
                    *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(RIGHT*i) for i in range(5)],
                    *[Line(UP/4,UP*3/4).shift(RIGHT*i) for i in range(5)],
                    *[Line(RIGHT/4,RIGHT*3/4).shift(RIGHT*i) for i in range(4)],
                ),
            ).arrange(RIGHT,buff=1)
            trunc1[0].save_state()
            trunc1[0].move_to(ORIGIN)
            self.play(FadeIn(trunc1[0]))
            self.slide_break()
            self.play(Restore(trunc1[0]))
            self.play(Write(trunc1[1]))
            self.play(FadeIn(trunc1[2]))
            self.slide_break()
            self.play(*[trunc1[0][i+10].animate.set_stroke_width(5).set_color(WHITE) for i in [0,2,3]])
            self.slide_break()

            trunc2=VGroup(
                trunc1[0].copy(),
                trunc1[1].copy(),
                VGroup(
                    Circle(1/8,color=WHITE,fill_opacity=1,fill_color=TEN_RED),
                    VGroup(
                        Polygon(UP/4,LEFT/2+UP*2/4,RIGHT/2+UP*2/4,
                            color=WHITE,fill_opacity=1,fill_color=TEN_GREEN),
                        Line(UP*2/4,UP*4/4).shift(LEFT/4),
                        Line(UP*2/4,UP*4/4).shift(RIGHT/4),
                    ).shift(LEFT),
                    VGroup(
                        Polygon(UP/4,LEFT*3/4+UP*2/4,RIGHT*3/4+UP*2/4,
                            color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW),
                        Line(UP*2/4,UP*4/4).shift(LEFT/2),
                        Line(UP*2/4,UP*4/4).shift(RIGHT/2),
                        Line(UP*2/4,UP*4/4).shift(ORIGIN),
                    ).shift(RIGHT*1.25),
                    OffsetBezier(LEFT/16,LEFT/2,
                        LEFT+UP/4,DOWN/4),
                    OffsetBezier(RIGHT/16,RIGHT/2,
                        RIGHT*1.25+UP/4,DOWN/4),
                ),
            ).arrange(RIGHT,buff=1)

            self.play(
                ReplacementTransform(trunc1[0],trunc2[0]),
                ReplacementTransform(trunc1[1],trunc2[1]),
                FadeTransform(trunc1[2],trunc2[2]),
            )
            self.slide_break()

            self.play(trunc2.animate.shift(UP))
            self.slide_break()

            trunc3=VGroup(
                VGroup(
                    VGroup(
                        Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE),
                        Line(LEFT/4,LEFT*3/4),
                        Line(RIGHT/4,RIGHT*3/4),
                        Line(UP/4,UP*3/4),
                        DashedLine(UP*2/4+RIGHT/2,DOWN*2/4+LEFT/2,dash_length=.1).set_opacity(0),
                    ).shift(LEFT/2),
                    VGroup(
                        Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE),
                        Line(RIGHT/4,RIGHT*3/4),
                        Line(UP/4,UP*3/4),
                    ).shift(RIGHT/2),
                ),
                MyMathTex(r"\to"),
                VGroup(
                    VGroup(
                        Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE),
                        Line(LEFT/4,LEFT*3/4),
                        Line(UP/4,UP*3/4),
                        Line(RIGHT/4,RIGHT*3/4),
                        Square(1/4,color=WHITE,fill_opacity=1,fill_color=BLACK).shift(RIGHT*6/8),
                        MyMathTex(r"X").scale(0.75).shift(RIGHT*6/8+UP*2/4),
                    ).shift(LEFT*1.5),
                    VGroup(
                        Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE),
                        Line(LEFT/4,LEFT*3/4),
                        Line(RIGHT/4,RIGHT*3/4),
                        Line(UP/4,UP*3/4),
                        Square(1/4,color=WHITE,fill_opacity=1,fill_color=BLACK).shift(LEFT*6/8),
                        MyMathTex(r"X^{-1}").scale(0.75).shift(LEFT*6/8+UP*2/4+UP/32),
                    ).shift(RIGHT*1.5),
                    Line(LEFT*5/8,RIGHT*5/8),
                ),
            ).arrange(RIGHT,buff=.75).shift(DOWN*1.5)

            self.play(FadeIn(trunc3))
            self.slide_break()
            trunc3.set_opacity(1)
            self.play(Write(trunc3[0][0][-1]))
            self.slide_break()

            trunc4=VGroup(
                trunc3[0].copy(),
                trunc3[1].copy(),
                VGroup(
                    VGroup(
                        Line(RIGHT/8,LEFT*3/4),
                        OffsetBezier(UP/8+RIGHT/8,LEFT/4,
                            UP*3/4+LEFT/8,DOWN/4),
                        Polygon(DOWN/4,UP/4,RIGHT*3/8, color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift(RIGHT/8),
                    ),
                    Line(RIGHT*2/4,RIGHT*7/8),
                    VGroup(
                        Circle(1/8,color=WHITE,fill_opacity=1,fill_color=TEN_RED).shift(RIGHT),
                        Polygon(DOWN/4,UP/4,LEFT*3/8,
                        color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift(RIGHT*15/8),
                        Line(RIGHT+RIGHT/8,RIGHT*12/8),
                        Line(LEFT/4,LEFT*9/8).shift(3*RIGHT),
                        Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(3*RIGHT),
                    ),
                    VGroup(
                        Line(RIGHT/4,RIGHT).shift(3*RIGHT),
                        Line(UP/4,UP*3/4).shift(3*RIGHT),
                    ),
                ),
            ).arrange(RIGHT,buff=.75).shift(DOWN*1.5)

            self.play(
                ReplacementTransform(trunc3[0],trunc4[0]),
                ReplacementTransform(trunc3[1],trunc4[1]),
                FadeTransform(trunc3[2],trunc4[2]),
            )
            self.slide_break()

            trunc5=VGroup(
                trunc4[0].copy(),
                trunc4[1].copy(),
                VGroup(
                    VGroup(
                        Line(RIGHT/8,LEFT*3/4),
                        OffsetBezier(UP/8+RIGHT/8,LEFT/4,
                            UP*3/4+LEFT/8,DOWN/4),
                        Polygon(DOWN/4,UP/4,RIGHT*3/8, color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift(RIGHT/8),
                    ),
                    Line(RIGHT*2/4,RIGHT*11/8),
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_PURPLE).shift(1.5*RIGHT),
                    VGroup(
                        Line(RIGHT/4,RIGHT).shift(1.5*RIGHT),
                        Line(UP/4,UP*3/4).shift(1.5*RIGHT),
                    ),
                ),
            ).arrange(RIGHT,buff=.75).shift(DOWN*1.5)

            self.play(
                ReplacementTransform(trunc4[0],trunc5[0]),
                ReplacementTransform(trunc4[1],trunc5[1]),
                *[ReplacementTransform(trunc4[2][i],trunc5[2][i]) for i in range(len(trunc4[2]))],
            )
            self.slide_break()

            self.play(FadeOut(trunc5))
            self.play(trunc2.animate.shift(DOWN))
            self.slide_break()

            trunc6=VGroup(
                trunc2[0].copy(),
                MyMathTex(r"\xlongrightarrow{~}"),
                VGroup(
                    VGroup(
                        OffsetBezier(UP/8,LEFT/4,
                            UP*3/4+LEFT/4,DOWN/4),
                        Polygon(DOWN/4,UP/4,RIGHT*3/8, color=WHITE,fill_opacity=1,fill_color=TEN_GREEN),
                        Line(RIGHT*3/8,RIGHT*3/4),
                    ),
                    VGroup(
                        OffsetBezier(UP/8,LEFT/4,
                            UP*3/4+LEFT/4,DOWN/4),
                        Polygon(DOWN/4,UP/4,RIGHT*3/8, color=WHITE,fill_opacity=1,fill_color=TEN_GREEN),
                        Line(RIGHT*3/8,RIGHT*3/4),
                    ).shift(RIGHT*3/4),
                    Circle(1/8,color=WHITE,fill_opacity=1,fill_color=TEN_RED).shift(RIGHT*13/8),
                    VGroup(
                        OffsetBezier(UP/8,RIGHT/4,
                            UP*3/4+RIGHT/4,DOWN/4),
                        Polygon(DOWN/4,UP/4,LEFT*3/8, color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW),
                        Line(LEFT*3/8,LEFT*3/4),
                    ).shift((.75*3+1/4)*RIGHT),
                    VGroup(
                        OffsetBezier(UP/8,RIGHT/4,
                            UP*3/4+RIGHT/4,DOWN/4),
                        Polygon(DOWN/4,UP/4,LEFT*3/8, color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW),
                        Line(LEFT*3/8,LEFT*3/4),
                    ).shift((.75*4+1/4)*RIGHT),
                    VGroup(
                        OffsetBezier(UP/8,RIGHT/4,
                            UP*3/4+RIGHT/4,DOWN/4),
                        Polygon(DOWN/4,UP/4,LEFT*3/8, color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW),
                        Line(LEFT*3/8,LEFT*3/4),
                    ).shift((.75*5+1/4)*RIGHT),
                ),
            ).arrange(RIGHT,buff=1)

            self.play(
                ReplacementTransform(trunc2[0],trunc6[0]),
                ReplacementTransform(trunc2[1],trunc6[1]),
                FadeTransform(trunc2[2],trunc6[2]),
            )
            self.slide_break()
            trunc7=trunc6[2].copy().move_to(ORIGIN).scale(1.5)
            self.play(
                FadeOut(trunc6[0]),
                FadeOut(trunc6[1]),
                ReplacementTransform(trunc6[2],trunc7),
            )
            self.slide_break()
            trunc8=VGroup(
                VGroup(
                    OffsetBezier(UP/8,LEFT/4,
                        UP*3/4+LEFT/4,DOWN/4),
                    Polygon(DOWN/4,UP/4,RIGHT*3/8, color=WHITE,fill_opacity=1,fill_color=TEN_GREEN),
                    Line(RIGHT*3/8,RIGHT*3/4),
                ),
                VGroup(
                    OffsetBezier(UP/8,LEFT/4,
                        UP*3/4+LEFT/4,DOWN/4),
                    Polygon(DOWN/4,UP/4,RIGHT*3/8, color=WHITE,fill_opacity=1,fill_color=TEN_GREEN),
                    Line(RIGHT*3/8,RIGHT*3/4),
                ).shift(RIGHT*3/4),
                VGroup(
                    OffsetBezier(UP/8,LEFT/4,
                        UP*3/4+LEFT/4,DOWN/4),
                    Polygon(DOWN/4,UP/4,RIGHT*3/8, color=WHITE,fill_opacity=1,fill_color=TEN_GREEN),
                    Line(RIGHT*3/8,RIGHT*3/4),
                ).shift(RIGHT*6/4),
                Circle(1/8,color=WHITE,fill_opacity=1,fill_color=TEN_RED).shift(RIGHT*19/8),
                VGroup(
                    OffsetBezier(UP/8,RIGHT/4,
                        UP*3/4+RIGHT/4,DOWN/4),
                    Polygon(DOWN/4,UP/4,LEFT*3/8, color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW),
                    Line(LEFT*3/8,LEFT*3/4),
                ).shift((.75*4+1/4)*RIGHT),
                VGroup(
                    OffsetBezier(UP/8,RIGHT/4,
                        UP*3/4+RIGHT/4,DOWN/4),
                    Polygon(DOWN/4,UP/4,LEFT*3/8, color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW),
                    Line(LEFT*3/8,LEFT*3/4),
                ).shift((.75*5+1/4)*RIGHT),
            ).move_to(ORIGIN).scale(1.5)
            self.play(*[ReplacementTransform(trunc7[i],trunc8[i]) for i in range(len(trunc7))])
            self.slide_break()
            trunc9=VGroup(
                VGroup(
                    OffsetBezier(UP/8,LEFT/4,
                        UP*3/4+LEFT/4,DOWN/4),
                    Polygon(DOWN/4,UP/4,RIGHT*3/8, color=WHITE,fill_opacity=1,fill_color=TEN_GREEN),
                    Line(RIGHT*3/8,RIGHT*3/4),
                ),
                VGroup(
                    OffsetBezier(UP/8,LEFT/4,
                        UP*3/4+LEFT/4,DOWN/4),
                    Polygon(DOWN/4,UP/4,RIGHT*3/8, color=WHITE,fill_opacity=1,fill_color=TEN_GREEN),
                    Line(RIGHT*3/8,RIGHT*3/4),
                ).shift(RIGHT*3/4),
                VGroup(
                    OffsetBezier(UP/8,LEFT/4,
                        UP*3/4+LEFT/4,DOWN/4),
                    Polygon(DOWN/4,UP/4,RIGHT*3/8, color=WHITE,fill_opacity=1,fill_color=TEN_GREEN),
                    Line(RIGHT*3/8,RIGHT*3/4),
                ).shift(RIGHT*6/4),
                VGroup(
                    OffsetBezier(UP/8,LEFT/4,
                        UP*3/4+LEFT/4,DOWN/4),
                    Polygon(DOWN/4,UP/4,RIGHT*3/8, color=WHITE,fill_opacity=1,fill_color=TEN_GREEN),
                    Line(RIGHT*3/8,RIGHT*3/4),
                ).shift(RIGHT*9/4),
                Circle(1/8,color=WHITE,fill_opacity=1,fill_color=TEN_RED).shift(RIGHT*25/8),
                VGroup(
                    OffsetBezier(UP/8,RIGHT/4,
                        UP*3/4+RIGHT/4,DOWN/4),
                    Polygon(DOWN/4,UP/4,LEFT*3/8, color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW),
                    Line(LEFT*3/8,LEFT*3/4),
                ).shift((.75*5+1/4)*RIGHT),
            ).move_to(ORIGIN).scale(1.5)
            self.play(*[ReplacementTransform(trunc8[i],trunc9[i]) for i in range(len(trunc8))])
            self.slide_break()
            self.play(FadeOut(trunc9))
            self.slide_break()
        if subsec==5 or subsec==-1:
            # vidal
            vidal1=VGroup(
                VGroup(
                    Circle(0.25,color=WHITE,fill_opacity=1,fill_color=TEN_PURPLE),
                    Line(UP/4,UP*3/4),
                ).shift(2*LEFT),
                Line(2*LEFT,LEFT,buff=0.25),
                VGroup(
                    Circle(0.25,color=WHITE,fill_opacity=1,fill_color=TEN_PURPLE),
                    Line(UP/4,UP*3/4),
                ).shift(1*LEFT),
                Line(LEFT,ORIGIN,buff=0.25),
                VGroup(
                    Circle(0.25,color=WHITE,fill_opacity=1,fill_color=TEN_PURPLE),
                    Line(UP/4,UP*3/4),
                ).shift(0*LEFT),
                Line(ORIGIN,RIGHT,buff=0.25),
                VGroup(
                    Circle(0.25,color=WHITE,fill_opacity=1,fill_color=TEN_PURPLE),
                    Line(UP/4,UP*3/4),
                ).shift(-1*LEFT),
                Line(RIGHT,2*RIGHT,buff=0.25),
                VGroup(
                    Circle(0.25,color=WHITE,fill_opacity=1,fill_color=TEN_PURPLE),
                    Line(UP/4,UP*3/4),
                ).shift(-2*LEFT),
            ).move_to(ORIGIN).scale(1.25)
            self.play(FadeIn(vidal1))
            self.slide_break()

            vidal2=VGroup(
                VGroup(
                    VGroup(
                        Line(LEFT,ORIGIN,buff=0.25),
                        VGroup(
                            Circle(0.25,color=WHITE,fill_opacity=1,fill_color=TEN_PURPLE),
                            Line(UP/4,UP*3/4),
                        ).shift(0*LEFT),
                        Line(ORIGIN,RIGHT,buff=0.25),
                    ),
                    MyMathTex("="),
                    VGroup(
                        Line(ORIGIN,LEFT*3/4),
                        OffsetBezier(UP/8,LEFT/4,
                            UP*3/4+LEFT/4,DOWN/4),
                        Polygon(DOWN/4,UP/4,RIGHT*3/8, color=WHITE,fill_opacity=1,fill_color=TEN_GREEN),
                        Line(RIGHT*3/8,RIGHT*3/4),
                    ),
                ).arrange(RIGHT,buff=0.25),
                MyTex("OR"),
                VGroup(
                    VGroup(
                        Line(LEFT,ORIGIN,buff=0.25),
                        VGroup(
                            Circle(0.25,color=WHITE,fill_opacity=1,fill_color=TEN_PURPLE),
                            Line(UP/4,UP*3/4),
                        ).shift(0*LEFT),
                        Line(ORIGIN,RIGHT,buff=0.25),
                    ),
                    MyMathTex("="),
                    VGroup(
                        Line(ORIGIN,RIGHT*3/4),
                        OffsetBezier(UP/8,RIGHT/4,
                            UP*3/4+RIGHT/4,DOWN/4),
                        Polygon(DOWN/4,UP/4,LEFT*3/8, color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW),
                        Line(LEFT*3/8,LEFT*3/4),
                    ),
                ).arrange(RIGHT,buff=0.25),
            ).arrange(RIGHT,buff=1).shift(1.5*DOWN)

            self.play(vidal1.animate.shift(UP))
            self.play(
                TransformFromCopy(vidal1[3:6],vidal2[0][0]),
                TransformFromCopy(vidal1[3:6],vidal2[2][0]),
            )
            self.play(
                FadeIn(vidal2[0][1:]),
                FadeIn(vidal2[2][1:]),
            )
            self.slide_break()
            self.play(FadeIn(vidal2[1]))
            self.slide_break()

            self.play(Transform(vidal2[1],MyTex("AND?").move_to(vidal2[1])))
            self.slide_break()
            self.remove(*self.mobjects)
            self.add(toc,footer,vidal1,vidal2)

            vidal3=VGroup(
                VGroup(
                    VGroup(
                        ArcBetweenPoints(DOWN/2,UP/2,angle=-TAU/2).shift(LEFT/4),
                        VGroup(
                            Circle(0.25,color=WHITE,fill_opacity=1,fill_color=TEN_PURPLE).shift(DOWN/2),
                            Circle(0.25,color=WHITE,fill_opacity=1,fill_color=TEN_PURPLE).shift(UP/2),
                            Line(DOWN/2,UP/2,buff=0.25),
                            Line(ORIGIN,RIGHT,buff=0.25).shift(UP/2),
                            Line(ORIGIN,RIGHT,buff=0.25).shift(DOWN/2),
                        ),
                    ),
                    MyMathTex("="),
                    ArcBetweenPoints(ORIGIN,UP,angle=-TAU/2),
                ).arrange(RIGHT,buff=0.5),

                VGroup(
                    VGroup(
                        ArcBetweenPoints(DOWN/2,UP/2,angle=TAU/2).shift(RIGHT/4),
                        VGroup(
                            Circle(0.25,color=WHITE,fill_opacity=1,fill_color=TEN_PURPLE).shift(DOWN/2),
                            Circle(0.25,color=WHITE,fill_opacity=1,fill_color=TEN_PURPLE).shift(UP/2),
                            Line(DOWN/2,UP/2,buff=0.25),
                            Line(ORIGIN,LEFT,buff=0.25).shift(UP/2),
                            Line(ORIGIN,LEFT,buff=0.25).shift(DOWN/2),
                        ),
                    ),
                    MyMathTex("="),
                    ArcBetweenPoints(ORIGIN,UP,angle=TAU/2),
                ).arrange(RIGHT,buff=0.5),
            ).arrange(RIGHT,buff=2).shift(1.5*DOWN)

            self.play(FadeOut(vidal2))
            self.play(FadeIn(vidal3))
            self.slide_break()

            a=1.5
            vidal4=VGroup(
                VGroup(
                    Circle(0.25,color=WHITE,fill_opacity=1,fill_color=TEN_PURPLE),
                    Line(UP/4,UP*3/4),
                ).shift(2*a*LEFT),
                VGroup(
                    Line(LEFT*(a/2-1/4),LEFT/16),
                    Line(RIGHT*(a/2-1/4),RIGHT/16),
                    Circle(1/8,color=WHITE,fill_opacity=1,fill_color=TEN_RED),
                ).shift(1.5*a*LEFT),
                VGroup(
                    Circle(0.25,color=WHITE,fill_opacity=1,fill_color=TEN_PURPLE),
                    Line(UP/4,UP*3/4),
                ).shift(1*a*LEFT),
                VGroup(
                    Line(LEFT*(a/2-1/4),LEFT/16),
                    Line(RIGHT*(a/2-1/4),RIGHT/16),
                    Circle(1/8,color=WHITE,fill_opacity=1,fill_color=TEN_RED),
                ).shift(0.5*a*LEFT),
                VGroup(
                    Circle(0.25,color=WHITE,fill_opacity=1,fill_color=TEN_PURPLE),
                    Line(UP/4,UP*3/4),
                ).shift(0*a*LEFT),
                VGroup(
                    Line(LEFT*(a/2-1/4),LEFT/16),
                    Line(RIGHT*(a/2-1/4),RIGHT/16),
                    Circle(1/8,color=WHITE,fill_opacity=1,fill_color=TEN_RED),
                ).shift(-0.5*a*LEFT),
                VGroup(
                    Circle(0.25,color=WHITE,fill_opacity=1,fill_color=TEN_PURPLE),
                    Line(UP/4,UP*3/4),
                ).shift(-1*a*LEFT),
                VGroup(
                    Line(LEFT*(a/2-1/4),LEFT/16),
                    Line(RIGHT*(a/2-1/4),RIGHT/16),
                    Circle(1/8,color=WHITE,fill_opacity=1,fill_color=TEN_RED),
                ).shift(-1.5*a*LEFT),
                VGroup(
                    Circle(0.25,color=WHITE,fill_opacity=1,fill_color=TEN_PURPLE),
                    Line(UP/4,UP*3/4),
                ).shift(-2*a*LEFT),
            ).move_to(UP).scale(1.25)

            self.play(Transform(vidal1,vidal4))
            self.slide_break()

            vidal5=VGroup(
                VGroup(
                    VGroup(
                        VGroup(
                            Line(LEFT*11/16,LEFT/4).shift(UP/2),
                            Circle(1/8,color=WHITE,fill_opacity=1,fill_color=TEN_RED).shift(LEFT*3/4+UP/2),
                            ArcBetweenPoints(DOWN/2,UP/2,angle=-TAU/2).shift(LEFT*13/16),
                            Circle(1/8,color=WHITE,fill_opacity=1,fill_color=TEN_RED).shift(LEFT*3/4+DOWN/2),
                            Line(LEFT*11/16,LEFT/4).shift(DOWN/2),
                        ),
                        VGroup(
                            Circle(0.25,color=WHITE,fill_opacity=1,fill_color=TEN_PURPLE).shift(DOWN/2),
                            Circle(0.25,color=WHITE,fill_opacity=1,fill_color=TEN_PURPLE).shift(UP/2),
                            Line(DOWN/2,UP/2,buff=0.25),
                            Line(ORIGIN,RIGHT,buff=0.25).shift(UP/2),
                            Line(ORIGIN,RIGHT,buff=0.25).shift(DOWN/2),
                        ),
                    ),
                    MyMathTex("="),
                    ArcBetweenPoints(ORIGIN,UP,angle=-TAU/2),
                ).arrange(RIGHT,buff=0.5),
                VGroup(
                    VGroup(
                        VGroup(
                            Line(-LEFT*11/16,-LEFT/4).shift(UP/2),
                            Circle(1/8,color=WHITE,fill_opacity=1,fill_color=TEN_RED).shift(-LEFT*3/4+UP/2),
                            ArcBetweenPoints(DOWN/2,UP/2,angle=TAU/2).shift(-LEFT*13/16),
                            Circle(1/8,color=WHITE,fill_opacity=1,fill_color=TEN_RED).shift(-LEFT*3/4+DOWN/2),
                            Line(-LEFT*11/16,-LEFT/4).shift(DOWN/2),
                        ),
                        VGroup(
                            Circle(0.25,color=WHITE,fill_opacity=1,fill_color=TEN_PURPLE).shift(DOWN/2),
                            Circle(0.25,color=WHITE,fill_opacity=1,fill_color=TEN_PURPLE).shift(UP/2),
                            Line(DOWN/2,UP/2,buff=0.25),
                            Line(ORIGIN,-RIGHT,buff=0.25).shift(UP/2),
                            Line(ORIGIN,-RIGHT,buff=0.25).shift(DOWN/2),
                        ),
                    ),
                    MyMathTex("="),
                    ArcBetweenPoints(ORIGIN,UP,angle=TAU/2),
                ).arrange(RIGHT,buff=0.5),
            ).arrange(RIGHT,buff=2).shift(1.5*DOWN)

            self.play(
                FadeTransform(vidal3[0][0][0],vidal5[0][0][0]),
                ReplacementTransform(vidal3[0][0][1:],vidal5[0][0][1:]),
                ReplacementTransform(vidal3[0][1:],vidal5[0][1:]),
            )
            self.play(
                FadeTransform(vidal3[1][0][0],vidal5[1][0][0]),
                ReplacementTransform(vidal3[1][0][1:],vidal5[1][0][1:]),
                ReplacementTransform(vidal3[1][1:],vidal5[1][1:]),
            )
            self.slide_break()

            self.play(*[FadeOut(mob) for mob in self.mobjects if mob!=toc and mob!=footer])
            self.slide_break()
        if subsec==6 or subsec==-1:
            # mps simulations
            sims=VGroup(
                VGroup(
                    MyTex("Statics"),
                    VGroup(
                        MyTex(r"\textbullet~Estimate spectra"),
                        MyTex(r"\textbullet~Sample from thermal states"),
                        MyTex(r"\textbullet~Approximate ground state"),
                    ),
                    MyMathTex(r"\ket\Lambda \approx \mathrm{arg\,min}_{\psi} \braopket{\psi}{H}{\psi}"),
                    MyTex(r"DMRG"),
                ).arrange(DOWN),
                VGroup(
                    MyTex("Dynamics"),
                    VGroup(
                        MyTex(r"\textbullet~Open syststem dynamics"),
                        MyTex(r"\textbullet~Thermalisation"),
                        MyTex(r"\textbullet~Hamiltonian evolution"),
                    ),
                    MyMathTex(r"\ket{\psi(t)}\approx e^{-iHt}\ket{\psi(0)}"),
                    MyTex(r"TEBD"),
                ),
            )
            for i in range(2):
                sims[i][0].scale(1.5)
                sims[i][1].arrange(DOWN,aligned_edge=LEFT)
                sims[i].arrange(DOWN,buff=.75)
            sims.arrange(RIGHT,buff=1,aligned_edge=UP)
            sims[0][-1].set_y(sims[1][-1].get_y())
            VGroup(sims[0][-1],sims[1][-1]).shift(UP/4)
            sims.move_to(DOWN/4)

            self.play(Write(sims[0][0]))
            self.slide_break()
            self.play(Write(sims[1][0]))
            self.slide_break()
            for i in range(2):
                for j in range(3):
                    self.play(Write(sims[i][1][j]))
                    self.slide_break()
            for i in range(2):
                self.play(sims[i][1][2].animate.set_color(YELLOW))
                self.slide_break()
                self.play(Write(sims[i][2]))
                self.slide_break()
                self.play(FadeIn(sims[i][3]))
                self.slide_break()

            self.play(*[FadeOut(mob) for mob in self.mobjects if mob!=toc and mob!=footer])
            self.slide_break()

        if subsec==7 or subsec==-1:
            pass
        if subsec==8 or subsec==-1:
            pass
        if subsec==9 or subsec==-1:
            pass
        if subsec==10 or subsec==-1:
            pass

        self.play(Restore(toc))

class Lec2_2(SlideScene):
    def construct(self):
        tocindex=(1,2)
        toc.set_opacity(0.25)
        toc[tocindex[0]].set_opacity(1)
        toc.save_state()
        heading = toc[tocindex[0]][tocindex[1]]
        self.add(toc,footer)
        self.play(
            toc.animate.set_opacity(0),
            heading.animate.scale(2).to_corner(UP).set_x(0),
        )
        heading.set_opacity(1)
        self.slide_break()

        subsec = -1
        # 1     Rayleigh quotient
        # 2     local Ham and MPO
        # 3     environments
        # 4     DMRG1
        # 5     DMRG2
        # 6     ?
        # 7     ?
        # 8     ?
        # 9     ?
        # 10    ?

        if subsec==1 or subsec==-1:

            rayleigh1=MyMathTex(
                r"\mathrm{arg\,min}_{\psi}",r"&~~~\braopket \psi H \psi\\~\\",
                r"\text{where}",r"&~~~\braket\psi\psi",r"=1,\\",
                r"&~~~\text{BD}(\ket \psi)\leq \chi",
            )
            rayleigh2=MyMathTex(
                r"\mathrm{arg\,min}_{\psi}",r"&~~~{\braopket \psi H \psi ", r"\over", r"\braket\psi\psi}\\~\\",
                r"\text{where}",r"&~~~\text{BD}(\ket \psi)\leq \chi",
            )

            self.play(Write(rayleigh1[:2]))
            self.slide_break()
            self.play(FadeIn(rayleigh1[2:5]))
            self.slide_break()
            self.play(FadeIn(rayleigh1[5:]))
            self.slide_break()

            self.play(rayleigh1[1].animate.set_color(YELLOW))
            self.slide_break()
            self.play(rayleigh1[3:].animate.set_color(BLUE))
            self.slide_break()
            rayleigh2[1:4].set_color(YELLOW)
            rayleigh2[5].set_color(BLUE)

            self.play(
                ReplacementTransform(rayleigh1[0],rayleigh2[0]),
                ReplacementTransform(rayleigh1[1],rayleigh2[1]),
                ReplacementTransform(rayleigh1[2],rayleigh2[4]),
                ReplacementTransform(rayleigh1[3],rayleigh2[3]),
                FadeOut(rayleigh1[4]),
                ReplacementTransform(rayleigh1[5],rayleigh2[5]),
            )
            self.play(FadeIn(rayleigh2[2]))
            self.slide_break()

            self.play(*[FadeOut(mob) for mob in self.mobjects if mob!=toc and mob!=footer])
            self.slide_break()

        if subsec==2 or subsec==-1:
            # local Ham -> MPO

            local1=MyMathTex(r"H=\sum_i h_i")
            self.play(Write(local1))
            self.slide_break()
            self.play(local1.animate.shift(UP*1.5))
            self.slide_break()

            local2=VGroup(
                MyMathTex(r"\cdots").shift(4*LEFT),
                VGroup(*[Circle(1/8,color=WHITE,fill_opacity=1).shift(i*RIGHT) for i in range(-3,4)]),
                MyMathTex(r"\cdots").shift(4*RIGHT),
                VGroup(
                    Ellipse(width=3,height=1),
                    MyMathTex(r"h_{i-1}").shift(DOWN),
                ).shift(LEFT).set_color(YELLOW),
                VGroup(
                    Ellipse(width=3,height=1),
                    MyMathTex(r"h_{i}").shift(UP),
                ).shift(ORIGIN).set_color(GREEN),
                VGroup(
                    Ellipse(width=3,height=1),
                    MyMathTex(r"h_{i+1}").shift(DOWN),
                ).shift(RIGHT).set_color(BLUE),
            ).shift(DOWN)
            self.play(Write(local2[:3]))
            self.slide_break()
            for i in range(3,6):
                self.play(Write(local2[i][0]))
                self.play(FadeIn(local2[i][1]))
            self.slide_break()

            local3=VGroup(
                *[Polygon(UP/3,RIGHT/3,DOWN/3,LEFT/3,color=WHITE,fill_opacity=1,fill_color=RED).shift(i*RIGHT) for i in range(-3,4)],
                *[Line(UP/3,UP*2/3).shift(i*RIGHT) for i in range(-3,4)],
                *[Line(DOWN/3,DOWN*2/3).shift(i*RIGHT) for i in range(-3,4)],
                *[Line(LEFT/3,LEFT*2/3).shift(i*RIGHT) for i in range(-3,5)],
                MyMathTex(r"\cdots").shift(4.25*RIGHT),
                MyMathTex(r"\cdots").shift(4.25*LEFT),
            ).shift(UP*1.5)
            self.play(FadeOut(local1))
            self.play(FadeIn(local3))
            self.slide_break()

            local4=VGroup(
                *[VGroup(
                    VGroup(
                        Rectangle(width=8/3,height=1/2,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW),
                        Line(UP/4,UP/2).shift(LEFT),
                        Line(DOWN/4,DOWN/2).shift(LEFT),
                        Line(UP/4,UP/2).shift(ORIGIN),
                        Line(DOWN/4,DOWN/2).shift(ORIGIN),
                        Line(UP/4,UP/2).shift(RIGHT),
                        Line(DOWN/4,DOWN/2).shift(RIGHT),
                    ).shift(3*LEFT),
                    VGroup(
                        Rectangle(width=8/3,height=1/2,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW),
                        Line(UP/4,UP/2).shift(LEFT),
                        Line(DOWN/4,DOWN/2).shift(LEFT),
                        Line(UP/4,UP/2).shift(ORIGIN),
                        Line(DOWN/4,DOWN/2).shift(ORIGIN),
                        Line(UP/4,UP/2).shift(RIGHT),
                        Line(DOWN/4,DOWN/2).shift(RIGHT),
                    ),
                    VGroup(
                        Rectangle(width=8/3,height=1/2,color=WHITE,fill_opacity=1),
                        Line(UP/4,UP/2).shift(LEFT),
                        Line(DOWN/4,DOWN/2).shift(LEFT),
                        Line(UP/4,UP/2).shift(ORIGIN),
                        Line(DOWN/4,DOWN/2).shift(ORIGIN),
                        Line(UP/4,UP/2).shift(RIGHT),
                        Line(DOWN/4,DOWN/2).shift(RIGHT),
                    ).shift(3*RIGHT),
                ).shift(s).set(fill_color=c) for s,c in zip([LEFT+UP*1.5,ORIGIN,RIGHT+1.5*DOWN],[TEN_YELLOW,TEN_GREEN,TEN_BLUE])],
            ).shift(ORIGIN)
            self.play(FadeOut(local3),FadeOut(local2))
            for l in local4:
                self.play(FadeIn(l))
            self.slide_break()

            self.play(*[FadeOut(mob) for mob in self.mobjects if mob!=toc and mob!=footer])
            self.slide_break()

        if subsec==3 or subsec==-1:
            # environment

            env00=MyMathTex(
                r"\langle ",
                r"\psi ",
                r"| ",
                r"H ",
                r"| ",
                r"\psi ",
                r"\rangle ",
            ).scale(2)

            n=6
            k=2
            env0=VGroup(
                VGroup(
                    *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(i*RIGHT+UP) for i in range(n)],
                    *[Line(RIGHT/4,RIGHT*3/4).shift(i*RIGHT+UP) for i in range(n-1)],
                ),
                VGroup(
                    *[Polygon(UP/3,RIGHT/3,DOWN/3,LEFT/3,color=WHITE,fill_opacity=1,fill_color=TEN_RED).shift(i*RIGHT) for i in range(n)],
                    *[Line(RIGHT/3,RIGHT*2/3).shift(i*RIGHT) for i in range(n-1)],
                    *[Line(UP/3,UP*3/4).shift(i*RIGHT) for i in range(n)],
                    *[Line(DOWN/3,DOWN*3/4).shift(i*RIGHT) for i in range(n)],
                ),
                VGroup(
                    *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(i*RIGHT+DOWN) for i in range(n)],
                    *[Line(RIGHT/4,RIGHT*3/4).shift(i*RIGHT+DOWN) for i in range(n-1)],
                ),
            )
            env1=VGroup(
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(i*RIGHT+UP) for i in range(n) if i!=k],
                *[Polygon(UP/3,RIGHT/3,DOWN/3,LEFT/3,color=WHITE,fill_opacity=1,fill_color=TEN_RED).shift(i*RIGHT) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(i*RIGHT+DOWN) for i in range(n) if i!=k],
                *[Line(UP/3,UP*3/4).shift(i*RIGHT) for i in range(n)],
                *[Line(DOWN/3,DOWN*3/4).shift(i*RIGHT) for i in range(n)],
                *[Line(RIGHT/3,RIGHT*2/3).shift(i*RIGHT) for i in range(n-1)],
                *[Line(RIGHT/4,RIGHT*3/4).shift(i*RIGHT+UP) for i in range(n-1) if i!=k and i!=k-1],
                *[Line(RIGHT/4,RIGHT*3/4).shift(i*RIGHT+DOWN) for i in range(n-1) if i!=k and i!=k-1],
                VGroup(
                    Line(LEFT/4,LEFT*3/4).shift(DOWN),
                    Line(LEFT/4,LEFT*3/4).shift(UP),
                    Line(DOWN*3/4,DOWN*3/4),
                    Line(UP*3/4,UP*3/4),
                    Line(RIGHT/4,RIGHT*3/4).shift(DOWN),
                    Line(RIGHT/4,RIGHT*3/4).shift(UP),
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(DOWN),
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(UP),
                ).shift(k*RIGHT),
            )

            c=0.5
            env2=VGroup(
                *env1.copy()[:-1],
                VGroup(
                    OffsetBezier(LEFT/4+2*DOWN,c*LEFT,
                        LEFT*3/4+DOWN,c*RIGHT),
                    OffsetBezier(LEFT/4+2*UP,c*LEFT,
                        LEFT*3/4+UP,c*RIGHT),
                    Line(DOWN*3/4,DOWN*7/4),
                    Line(UP*3/4,UP*7/4),
                    OffsetBezier(RIGHT/4+2*DOWN,c*RIGHT,
                        RIGHT*3/4+DOWN,c*LEFT),
                    OffsetBezier(RIGHT/4+2*UP,c*RIGHT,
                        RIGHT*3/4+UP,c*LEFT),
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift(2*DOWN),
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift(2*UP),
                ).shift(k*RIGHT),
            )

            env0.move_to(ORIGIN)
            env1.move_to(ORIGIN)
            env2.move_to(ORIGIN)

            self.play(Write(env00))
            self.slide_break()
            self.play(
                env00[1].animate.set_color(BLUE),
                env00[3].animate.set_color(RED),
                env00[5].animate.set_color(BLUE),
            )
            self.play(
                Rotate(env00,angle=-TAU/4)
            )
            self.slide_break()
            self.play(
                ReplacementTransform(env00[1],env0[0]),
                ReplacementTransform(env00[3],env0[1]),
                ReplacementTransform(env00[5],env0[2]),
                FadeOut(env00[0::2]),
            )
            self.remove(*env0)
            self.add(env1)
            self.play(ReplacementTransform(env1,env2))
            self.slide_break()

            c=0.5
            env3=VGroup(
                VGroup(
                    OffsetBezier(LEFT/4+2*DOWN,c*LEFT/2,
                        LEFT/2+DOWN*3/2,c*DOWN/2),
                    Line(DOWN*7/4,DOWN*4/4),
                    OffsetBezier(RIGHT/4+2*DOWN,c*RIGHT/2,
                        RIGHT/2+DOWN*3/2,c*DOWN/2),
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift(2*DOWN),
                ).shift(k*RIGHT),
                VGroup(
                    OffsetBezier(LEFT/4+2*UP,c*LEFT/2,
                        LEFT/2+UP*3/2,c*UP/2),
                    Line(UP*7/4,UP*4/4),
                    OffsetBezier(RIGHT/4+2*UP,c*RIGHT/2,
                        RIGHT/2+UP*3/2,c*UP/2),
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift(2*UP),
                ).shift(k*RIGHT),
                Polygon(
                    (0.375)*LEFT+1.5*UP,
                    (0.375)*LEFT+1.5*UP,
                    (k-1/4)*RIGHT+1.5*UP,
                    (k-1/4)*RIGHT+1*UP,
                    (k+1/4)*RIGHT+1*UP,
                    (k+1/4)*RIGHT+1.5*UP,
                    (n+0.375-1)*RIGHT+1.5*UP,
                    (n+0.375-1)*RIGHT+1.5*DOWN,
                    (k+1/4)*RIGHT+1.5*DOWN,
                    (k+1/4)*RIGHT+1*DOWN,
                    (k-1/4)*RIGHT+1*DOWN,
                    (k-1/4)*RIGHT+1.5*DOWN,
                    (0.375)*LEFT+1.5*DOWN,
                    color=WHITE,fill_opacity=1,fill_color=TEN_PURPLE,
                ),
                MyMathTex(r"\mathcal H_i",color=BLACK).shift(RIGHT*(n-1)/2).scale(1.5),
                MyMathTex(r"T_i",color=BLACK).shift(k*RIGHT+2*UP).scale(0.75),
                MyMathTex(r"T_i",color=BLACK).shift(k*RIGHT+2*DOWN).scale(0.75),
            ).shift((n-1)*LEFT/2)
            self.play(FadeIn(env3[:-3]))
            self.remove(env2)
            self.slide_break()
            self.play(Write(env3[-3:]))
            self.slide_break()

            c=0.5
            env4=VGroup(
                VGroup(
                    Line(DOWN,DOWN/2).shift(LEFT/4),
                    Line(DOWN,DOWN/2),
                    Line(DOWN,DOWN/2).shift(RIGHT/4),
                    Rectangle(height=0.5,width=1,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift(1.25*DOWN),
                ),
                VGroup(
                    Line(UP,UP/2).shift(LEFT/4),
                    Line(UP,UP/2),
                    Line(UP,UP/2).shift(RIGHT/4),
                    Rectangle(height=0.5,width=1,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift(1.25*UP),
                ),
                Polygon(
                    *[UP/2+(i-2.5)*RIGHT/5 for i in range(6)],
                    *[DOWN/2+(i-2.5)*LEFT/5 for i in range(6)],
                    color=WHITE,fill_opacity=1,fill_color=TEN_PURPLE,
                ),
                MyMathTex(r"\mathcal H_i",color=BLACK).scale(1.0),
                MyMathTex(r"T_i",color=BLACK).shift(1.25*UP).scale(0.75),
                MyMathTex(r"T_i",color=BLACK).shift(1.25*DOWN).scale(0.75),
            ).move_to(ORIGIN)
            self.play(ReplacementTransform(env3,env4))
            self.slide_break()
            self.remove(env4)
            env4 = VGroup(
                env4[1]+env4[4],
                VGroup(env4[2],env4[3]),
                env4[0]+env4[5])

            env5=MyMathTex(
                r"\frac{\braopket \psi H \psi}{\braket \psi \psi} = ",
                r"{ \langle ",
                r"T_i ",
                r"| ",
                r"\mathcal H_i ",
                r"| ",
                r"T_i ",
                r"\rangle ",
                r"\over \langle ",
                r"T_i ",
                r"| ",
                r"\mathcal I_i ",
                r"| ",
                r"T_i ",
                r"\rangle }",
            )
            env5[0][1].set_color(BLUE)
            env5[0][3].set_color(RED)
            env5[0][5].set_color(BLUE)
            env5[0][9].set_color(BLUE)
            env5[0][11].set_color(BLUE)
            env5[2].set_color(GREEN)
            env5[4].set_color(PURPLE)
            env5[6].set_color(GREEN)
            env5[9].set_color(GREEN)
            env5[11].set_color(BLUE)
            env5[13].set_color(GREEN)

            self.play(
                ReplacementTransform(env4[0],env5[2]),
                ReplacementTransform(env4[1],env5[4]),
                ReplacementTransform(env4[2],env5[6]),
                FadeIn(env5[1:8:2]),
            )
            self.play(FadeIn(env5[0]),FadeIn(env5[8:]))
            self.slide_break()

            env6=VGroup(
                VGroup(
                    OffsetBezier(LEFT*2/3,RIGHT/4,
                        UP+LEFT/4,DOWN).shift(k*RIGHT+UP),
                    OffsetBezier(LEFT*2/3,RIGHT/4,
                        DOWN+LEFT/4,UP).shift(k*RIGHT),
                    *[VGroup(
                        Line(UP/4,ORIGIN),
                        Line(DOWN/4,ORIGIN),
                        Polygon(
                            UL/4,DL/4,DR/4,UR/4,
                            color=WHITE,fill_opacity=1,fill_color=BLUE).shift(UP/2),
                        Polygon(
                            UL/4,DL/4,DR/4,UR/4,
                            color=WHITE,fill_opacity=1,fill_color=BLUE).shift(DOWN/2),
                        Line(RIGHT/4,RIGHT*3/4).shift(UP/2),
                        Line(RIGHT/4,RIGHT*3/4).shift(DOWN/2),
                    ).shift(i*RIGHT+UP/2) for i in range(k)],
                ),
                Line(2*UP,DOWN).shift(k*RIGHT),
                VGroup(
                    *[VGroup(
                        Line(UP/4,ORIGIN),
                        Line(DOWN/4,ORIGIN),
                        Polygon(
                            UR/4,DR/4,DL/4,UL/4,
                            color=WHITE,fill_opacity=1,fill_color=BLUE).shift(UP/2),
                        Polygon(
                            UR/4,DR/4,DL/4,UL/4,
                            color=WHITE,fill_opacity=1,fill_color=BLUE).shift(DOWN/2),
                        Line(LEFT/4,LEFT*3/4).shift(UP/2),
                        Line(LEFT/4,LEFT*3/4).shift(DOWN/2),
                    ).shift(i*RIGHT+UP/2) for i in range(k+1,n)],
                    OffsetBezier(RIGHT*2/3,LEFT/4,
                        UP+RIGHT/4,DOWN).shift(k*RIGHT+UP),
                    OffsetBezier(RIGHT*2/3,LEFT/4,
                        DOWN+RIGHT/4,UP).shift(k*RIGHT),
                ),
            ).move_to(1.25*DOWN)
            env6[0][-1] = env6[0][-1][:-2]
            env6[2][0]  = env6[2][0][:-2]

            env7=VGroup(
                VGroup(
                    OffsetBezier(LEFT*2/3,RIGHT/4,
                        UP+LEFT/4,DOWN).shift(k*RIGHT+UP),
                    OffsetBezier(LEFT*2/3,RIGHT/4,
                        DOWN+LEFT/4,UP).shift(k*RIGHT),
                    *[VGroup(
                        OffsetBezier(UP*3/8,LEFT/16,
                            LEFT/4,UP/2),
                        OffsetBezier(DOWN*3/8,LEFT/16,
                            LEFT/4,DOWN/2),
                        Polygon(
                            UP/4,DOWN/4,RIGHT/3,RIGHT/3,
                            color=WHITE,fill_opacity=1,fill_color=BLUE).shift(UP/2),
                        Polygon(
                            UP/4,DOWN/4,RIGHT/3,RIGHT/3,
                            color=WHITE,fill_opacity=1,fill_color=BLUE).shift(DOWN/2),
                        Line(RIGHT/3,RIGHT).shift(UP/2),
                        Line(RIGHT/3,RIGHT).shift(DOWN/2),
                    ).shift(i*RIGHT+UP/2) for i in range(k)],
                ),
                Line(2*UP,DOWN).shift(k*RIGHT),
                VGroup(
                    *[VGroup(
                        OffsetBezier(UP*3/8,RIGHT/16,
                            RIGHT/4,UP/2),
                        OffsetBezier(DOWN*3/8,RIGHT/16,
                            RIGHT/4,DOWN/2),
                        Polygon(
                            UP/4,DOWN/4,LEFT/3,LEFT/3,
                            color=WHITE,fill_opacity=1,fill_color=BLUE).shift(UP/2),
                        Polygon(
                            UP/4,DOWN/4,LEFT/3,LEFT/3,
                            color=WHITE,fill_opacity=1,fill_color=BLUE).shift(DOWN/2),
                        Line(LEFT/3,LEFT).shift(UP/2),
                        Line(LEFT/3,LEFT).shift(DOWN/2),
                    ).shift(i*RIGHT+UP/2) for i in range(k+1,n)],
                    OffsetBezier(RIGHT*2/3,LEFT/4,
                        UP+RIGHT/4,DOWN).shift(k*RIGHT+UP),
                    OffsetBezier(RIGHT*2/3,LEFT/4,
                        DOWN+RIGHT/4,UP).shift(k*RIGHT),
                ),
            ).move_to(1.25*DOWN)
            env7[0][-1] = env7[0][-1][:-2]
            env7[2][0]  = env7[2][0][:-2]

            env8=VGroup(
                Line(2*UP,DOWN).shift(LEFT/4),
                Line(2*UP,DOWN).shift(ORIGIN),
                Line(2*UP,DOWN).shift(RIGHT/4),
            ).shift(1.75*DOWN)

            self.play(env5.animate.shift(2*UP))
            self.play(TransformFromCopy(env5[11],env6))
            self.slide_break()
            self.play(ReplacementTransform(env6,env7))
            self.slide_break()
            self.play(
                FadeTransform(env7[0],env8[0]),
                ReplacementTransform(env7[1],env8[1]),
                FadeTransform(env7[2],env8[2]),
            )
            self.slide_break()

            self.play(FadeOut(env8))
            self.play(env5.animate.move_to(ORIGIN))
            self.slide_break()

            env9=MyMathTex(
                r"\frac{\braopket \psi H \psi}{\braket \psi \psi} = ",
                r"{ \langle ",
                r"T_i ",
                r"| ",
                r"\mathcal H_i ",
                r"| ",
                r"T_i ",
                r"\rangle ",
                r"\over \langle ",
                r"T_i ",
                r"| ",
                r"T_i ",
                r"\rangle }",
            )
            env9[0][1].set_color(BLUE)
            env9[0][3].set_color(RED)
            env9[0][5].set_color(BLUE)
            env9[0][9].set_color(BLUE)
            env9[0][11].set_color(BLUE)
            env9[2].set_color(GREEN)
            env9[4].set_color(PURPLE)
            env9[6].set_color(GREEN)
            env9[9].set_color(GREEN)
            env9[11].set_color(GREEN)
            self.play(
                ReplacementTransform(env5[:10],env9[:10]),
                ReplacementTransform(env5[10:13],env9[10]),
                ReplacementTransform(env5[13:],env9[11:]),
            )
            self.slide_break()

            self.play(FadeOut(env9))
            self.slide_break()

        if subsec==4 or subsec==-1:
            # dmrg1_1=
            # pass

            code="""
                ψ = rand_MPS(n,χ)
                for r ∈ 1:rounds
                    for i ∈ union(1:n, n:1)
                        move_canon_centre!(ψ,i)
                        h = calc_ham(H,ψ,i)
                        ψ[i] = min_evec(h)
                    end
                end"""
            dmrg=Code(code=code,language="julia",line_spacing=1.5,style="vim")
            self.play(FadeIn(dmrg[0]))
            self.play(Write(dmrg[1]))
            self.slide_break()

            self.play(Write(dmrg[2][0]))
            self.slide_break()
            self.play(Write(dmrg[2][1]),Write(dmrg[2][7]))
            self.slide_break()
            self.play(Write(dmrg[2][2]),Write(dmrg[2][6]))
            self.slide_break()
            self.play(Write(dmrg[2][3]))
            self.slide_break()
            self.play(Write(dmrg[2][4]))
            self.slide_break()
            self.play(Write(dmrg[2][5]))
            self.slide_break()

            self.play(FadeOut(dmrg))
            self.slide_break()

        if subsec==5 or subsec==-1:

            n=10
            k=3
            dmrg2=VGroup(
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(i*RIGHT+UP) for i in range(n) if i!=k and i!=k+1],
                *[Polygon(UP/3,RIGHT/3,DOWN/3,LEFT/3,color=WHITE,fill_opacity=1,fill_color=TEN_RED).shift(i*RIGHT) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(i*RIGHT+DOWN) for i in range(n) if i!=k and i!=k+1],
                *[Line(UP/3,UP*3/4).shift(i*RIGHT) for i in range(n)],
                *[Line(DOWN/3,DOWN*3/4).shift(i*RIGHT) for i in range(n)],
                *[Line(RIGHT/3,RIGHT*2/3).shift(i*RIGHT) for i in range(n-1)],
                *[Line(RIGHT/4,RIGHT*3/4).shift(i*RIGHT+UP) for i in range(n-1) if i!=k and i!=k-1 and i!=k+1],
                *[Line(RIGHT/4,RIGHT*3/4).shift(i*RIGHT+DOWN) for i in range(n-1) if i!=k and i!=k-1 and i!=k+1],
                VGroup(
                    Line(LEFT/4,LEFT*3/4).shift(DOWN),
                    Line(LEFT/4,LEFT*3/4).shift(UP),
                    Line(DOWN*3/4,DOWN*3/4),
                    Line(UP*3/4,UP*3/4),
                    Line(RIGHT/4,RIGHT*3/4).shift(DOWN),
                    Line(RIGHT/4,RIGHT*3/4).shift(UP),
                    Line(DOWN*3/4,DOWN*3/4).shift(RIGHT),
                    Line(UP*3/4,UP*3/4).shift(RIGHT),
                    Line(RIGHT/4,RIGHT*3/4).shift(DOWN+RIGHT),
                    Line(RIGHT/4,RIGHT*3/4).shift(UP+RIGHT),
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(DOWN),
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(UP),
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(DOWN+RIGHT),
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(UP+RIGHT),
                ).shift(k*RIGHT),
            ).shift((n-1)*LEFT/2)

            dmrg3=VGroup(
                *dmrg2.copy()[:-1],
                VGroup(
                    OffsetBezier(LEFT/4+2*DOWN,LEFT/2,
                        LEFT*3/4+DOWN,RIGHT/2),
                    OffsetBezier(LEFT/4+2*UP,LEFT/2,
                        LEFT*3/4+UP,RIGHT/2),
                    Line(DOWN*3/4,DOWN*7/4),
                    Line(UP*3/4,UP*7/4),
                    Line(RIGHT/4,RIGHT*3/4).shift(2*DOWN),
                    Line(RIGHT/4,RIGHT*3/4).shift(2*UP),
                    Line(DOWN*3/4,DOWN*7/4).shift(RIGHT),
                    Line(UP*3/4,UP*7/4).shift(RIGHT),
                    OffsetBezier(RIGHT/4+2*DOWN,RIGHT/2,
                        RIGHT*3/4+DOWN,LEFT/2).shift(RIGHT),
                    OffsetBezier(RIGHT/4+2*UP,RIGHT/2,
                        RIGHT*3/4+UP,LEFT/2).shift(RIGHT),
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift(2*DOWN),
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift(2*UP),
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift(2*DOWN+RIGHT),
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift(2*UP+RIGHT),
                ).shift(k*RIGHT+(n-1)*LEFT/2),
            )

            dmrg4=VGroup(
                *dmrg2.copy()[:-1],
                VGroup(
                    OffsetBezier(LEFT/4+2*DOWN,LEFT/2,
                        LEFT*3/4+DOWN,RIGHT/2),
                    OffsetBezier(LEFT/4+2*UP,LEFT/2,
                        LEFT*3/4+UP,RIGHT/2),
                    Line(DOWN*3/4,DOWN*7/4),
                    Line(UP*3/4,UP*7/4),
                    # Line(RIGHT/4,RIGHT*3/4).shift(2*DOWN),
                    # Line(RIGHT/4,RIGHT*3/4).shift(2*UP),
                    Line(DOWN*3/4,DOWN*7/4).shift(RIGHT),
                    Line(UP*3/4,UP*7/4).shift(RIGHT),
                    OffsetBezier(RIGHT/4+2*DOWN,RIGHT/2,
                        RIGHT*3/4+DOWN,LEFT/2).shift(RIGHT),
                    OffsetBezier(RIGHT/4+2*UP,RIGHT/2,
                        RIGHT*3/4+UP,LEFT/2).shift(RIGHT),
                    Rectangle(width=1.5,height=0.5,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift(2*DOWN+RIGHT/2),
                    Rectangle(width=1.5,height=0.5,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift(2*UP+RIGHT/2),
                ).shift(k*RIGHT+(n-1)*LEFT/2),
            )

            self.play(FadeIn(dmrg2))
            self.slide_break()
            self.play(ReplacementTransform(dmrg2,dmrg3))
            self.slide_break()
            self.play(FadeIn(dmrg4))
            self.remove(dmrg3)
            self.slide_break()
            self.play(FadeOut(dmrg4))
            self.slide_break()

        if subsec==6 or subsec==-1:
            pass
        if subsec==7 or subsec==-1:
            pass
        if subsec==8 or subsec==-1:
            pass
        if subsec==9 or subsec==-1:
            pass
        if subsec==10 or subsec==-1:
            pass

        self.play(Restore(toc))

class Lec2_3(SlideScene):
    def construct(self):
        tocindex=(1,3)
        toc.set_opacity(0.25)
        toc[tocindex[0]].set_opacity(1)
        toc.save_state()
        heading = toc[tocindex[0]][tocindex[1]]
        self.add(toc,footer)
        self.play(
            toc.animate.set_opacity(0),
            heading.animate.scale(2).to_corner(UP).set_x(0),
        )
        heading.set_opacity(1)
        self.slide_break()

        subsec = -1
        # 1     Suzuki trotter
        # 2     Real/imaginary time
        # 3     TEBD
        # 4     ?
        # 5     ?
        # 6     ?
        # 7     ?
        # 8     ?
        # 9     ?
        # 10    ?

        if subsec==1 or subsec==-1:
            # Suzuk-Trotter
            suzuki1=MyMathTex("U(t):=e^{-i","H","t}")

            n=10
            suzuki2=VGroup(
                VGroup(
                    *[Circle(0.1,fill_opacity=1,color=WHITE).shift(i*RIGHT) for i in range(0,n)],
                ),
                VGroup(
                    *[Ellipse(width=1.75,height=0.75,color=TEN_RED).shift((i+0.5)*RIGHT) for i in range(0,n,2)],
                ),
                VGroup(
                    *[Ellipse(width=1.75,height=0.75,color=TEN_YELLOW).shift((i+0.5)*RIGHT) for i in range(1,n-1,2)],
                ),
                MyMathTex("H=A+B").shift((n-1)*RIGHT/2+DOWN),
            ).shift(1.5*UP+(n-1)*LEFT/2)
            suzuki2[-1][0][2].set_color(RED)
            suzuki2[-1][0][4].set_color(TEN_YELLOW)

            suzuki3=MyMathTex("U(t):=e^{-i",r"(A+B)",r"t}")
            suzuki3[1][1].set_color(RED)
            suzuki3[1][3].set_color(TEN_YELLOW)

            self.play(FadeIn(suzuki1))
            self.slide_break()
            self.play(suzuki1.animate.shift(1*DOWN))
            suzuki3.move_to(suzuki1)
            self.slide_break()

            self.play(FadeIn(suzuki2[0]))
            self.slide_break()

            self.play(Write(suzuki2[1]))
            self.play(Write(suzuki2[2]))
            self.slide_break()

            self.play(Write(suzuki2[3]))
            self.slide_break()

            self.play(ReplacementTransform(suzuki1,suzuki3))
            self.slide_break()

            suzuki4=MyMathTex("U(t):=e^{-i",r"(A+B)",r"t}=","e^{-itA}","e^{-itB}","+O(t^","2",")")
            suzuki4[1][1].set_color(RED)
            suzuki4[1][3].set_color(TEN_YELLOW)
            suzuki4[3].set_color(RED)
            suzuki4[4].set_color(TEN_YELLOW)
            suzuki4.move_to(DOWN)

            self.play(ReplacementTransform(suzuki3,suzuki4[:3]))
            self.play(FadeIn(suzuki4[3:]))
            self.slide_break()

            suzuki5=MyMathTex("U(t):=e^{-i",r"(A+B)",r"t}=","e^{-itA/2}","e^{-itB}","e^{-itA/2}","+O(t^","3",")")
            suzuki5[1][1].set_color(RED)
            suzuki5[1][3].set_color(TEN_YELLOW)
            suzuki5[3].set_color(RED)
            suzuki5[4].set_color(TEN_YELLOW)
            suzuki5[5].set_color(RED)
            suzuki5.move_to(DOWN)

            self.play(
                ReplacementTransform(suzuki4[:5],suzuki5[:5]),
                TransformFromCopy(suzuki4[3],suzuki5[5]),
                ReplacementTransform(suzuki4[5:],suzuki5[6:]),
            )
            self.slide_break()

            suzuki6=MyMathTex(
                "U(t)=U(t/n)^n=",
                "e^{-iAt/n}",
                "e^{-iBt/n}",
                "\cdots ",
                "e^{-iBt/n}",
                "+O(1/n^2)"
            ).move_to(2*DOWN)
            suzuki6[1].set_color(RED)
            suzuki6[2].set_color(TEN_YELLOW)
            suzuki6[4].set_color(TEN_YELLOW)
            self.play(FadeIn(suzuki6))
            self.slide_break()

            suzuki7=MyMathTex(
                "U(t)=U(t/n)^n=",
                "e^{-iAt/2n}",
                "e^{-iBt/n}",
                "\cdots ",
                "e^{-iBt/n}",
                "e^{-iAt/2n}",
                "+O(1/n^3)"
            )
            suzuki7[1].set_color(RED)
            suzuki7[2].set_color(TEN_YELLOW)
            suzuki7[4].set_color(TEN_YELLOW)
            suzuki7[5].set_color(RED)
            suzuki7.move_to(2*DOWN)
            self.play(
                ReplacementTransform(suzuki6[:-1],suzuki7[:-2]),
                FadeIn(suzuki7[-2]),
                ReplacementTransform(suzuki6[-1],suzuki7[-1]),
            )
            self.slide_break()

            self.play(FadeOut(suzuki5,shift=UP/2),suzuki7.animate.shift(UP*3/2))
            self.slide_break()

            suzuki8=VGroup(
                MyMathTex("e^{-iA\delta}=e^{-iA_1\delta}e^{-iA_3\delta}e^{-iA_5\delta}\cdots").set_color(RED),
                MyMathTex("e^{-iB\delta}=e^{-iB_2\delta}e^{-iB_4\delta}e^{-iB_6\delta}\cdots").set_color(TEN_YELLOW),
            ).arrange(DOWN).shift(2*DOWN)
            self.play(FadeIn(suzuki8))
            self.slide_break()

            self.play(*[FadeOut(mob) for mob in self.mobjects if mob!=toc and mob!=footer])
            self.slide_break()

        if subsec==2 or subsec==-1:

            imagtime=VGroup()

            imagtime += MyMathTex("U(","t",")=e^{-iH","t}")
            imagtime += MyMathTex("U(",r"-i\tau",")=e^{-iH",r"(-i\tau)}")
            imagtime += MyMathTex(r"U(-i\tau)=e^{-","i","H","(-i",r"\tau",")}")
            imagtime += MyMathTex(r"U(-i\tau)=e^{-","H",r"\tau}")

            self.play(Write(imagtime[0]))
            self.slide_break()
            self.play(ReplacementTransform(imagtime[0],imagtime[1]))
            self.slide_break()
            self.remove(imagtime[1])
            self.add(imagtime[2])

            self.play(
                ReplacementTransform(imagtime[2][0],imagtime[3][0]),
                FadeOut(imagtime[2][1]),
                ReplacementTransform(imagtime[2][2],imagtime[3][1]),
                FadeOut(imagtime[2][3]),
                ReplacementTransform(imagtime[2][4],imagtime[3][2]),
                FadeOut(imagtime[2][5]),
            )
            self.slide_break()

            self.play(imagtime[3].animate.shift(UP*3/4))
            self.slide_break()

            imagtime+=MyMathTex(
                r"\ket\psi&=c_1\ket{E_1}+c_2\ket{E_2}+c_3\ket{E_3}+\cdots\\",
                r"e^{-H\tau}\ket\psi&=",
                r"c_1e^{-E_1\tau}\ket{E_1}",
                r"+c_2e^{-E_1\tau}\ket{E_2}",
                r"+c_3e^{-E_1\tau}\ket{E_3}+",
                r"\cdots",
                ).shift(DOWN)

            self.play(FadeIn(imagtime[-1][0]))
            self.slide_break()
            self.play(FadeIn(imagtime[-1][1:]))
            self.slide_break()

            self.play(*[FadeOut(mob) for mob in self.mobjects if mob!=toc and mob!=footer])
            self.slide_break()

        if subsec==3 or subsec==-1:
            tebd1=MyMathTex(
                "\cdots ",
                r"e^{-i\delta A} ",
                r"e^{-i\delta B} ",
                r"e^{-i\delta A} ",
                r"e^{-i\delta B} ",
                r"\ket \psi",
            )
            tebd1[1::2].set_color(RED)
            tebd1[2::2].set_color(TEN_YELLOW)
            tebd1[-1].set_color(BLUE)
            self.play(FadeIn(tebd1))
            self.slide_break()

            n=8
            tebd2=VGroup(
                *[Line(ORIGIN,4.75*UP).shift(i*RIGHT) for i in range(n)],
                Line(ORIGIN,(n-1)*RIGHT).shift(4*UP),
                Line(ORIGIN,(n-1)*RIGHT).shift(3*UP),
                Line(ORIGIN,(n-1)*RIGHT).shift(2*UP),
                Line(ORIGIN,(n-1)*RIGHT).shift(1*UP),
                Line(ORIGIN,(n-1)*RIGHT).shift(0*UP),
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_RED).shift(i*RIGHT+4*UP) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift(i*RIGHT+3*UP) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_RED).shift(i*RIGHT+2*UP) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift(i*RIGHT+UP) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(i*RIGHT) for i in range(n)],
            ).scale(7/8).shift(3*DOWN+(n-1)*LEFT/2)
            self.play(tebd1.animate.shift(2.25*UP))
            tebd2.save_state()
            tebd2.set_color(BG)
            self.play(Restore(tebd2))
            self.slide_break()

            tebd3=VGroup(
                *[Line(ORIGIN,4.75*UP).shift(i*RIGHT) for i in range(n)],
                Line(ORIGIN,(n-1)*RIGHT).shift(4*UP),
                Line(ORIGIN,(n-1)*RIGHT).shift(3*UP),
                Line(ORIGIN,(n-1)*RIGHT).shift(2*UP),
                Line(ORIGIN,(n-1)*RIGHT).shift(UP/16),
                Line(ORIGIN,(n-1)*RIGHT).shift(DOWN/16),
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_RED).shift(i*RIGHT+4*UP) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift(i*RIGHT+3*UP) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_RED).shift(i*RIGHT+2*UP) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift(i*RIGHT) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift(i*RIGHT) for i in range(n)],
            ).scale(7/8).shift(3*DOWN+(n-1)*LEFT/2)
            self.play(Transform(tebd2,tebd3))
            self.slide_break()

            tebd3=VGroup(
                *[Line(ORIGIN,4.75*UP).shift(i*RIGHT) for i in range(n)],
                Line(ORIGIN,(n-1)*RIGHT).shift(4*UP),
                Line(ORIGIN,(n-1)*RIGHT).shift(3*UP),
                Line(ORIGIN,(n-1)*RIGHT).shift(2*UP),
                Line(ORIGIN,(n-1)*RIGHT).shift(ORIGIN),
                Line(ORIGIN,(n-1)*RIGHT).shift(ORIGIN),
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_RED).shift(i*RIGHT+4*UP) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift(i*RIGHT+3*UP) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_RED).shift(i*RIGHT+2*UP) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(i*RIGHT) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(i*RIGHT) for i in range(n)],
            ).scale(7/8).shift(3*DOWN+(n-1)*LEFT/2)
            self.play(Transform(tebd2,tebd3))
            self.slide_break()

            tebd3=VGroup(
                *[Line(ORIGIN,4.75*UP).shift(i*RIGHT) for i in range(n)],
                Line(ORIGIN,(n-1)*RIGHT).shift(4*UP),
                Line(ORIGIN,(n-1)*RIGHT).shift(3*UP),
                Line(ORIGIN,(n-1)*RIGHT).shift(UP/16),
                Line(ORIGIN,(n-1)*RIGHT).shift(DOWN/16),
                Line(ORIGIN,(n-1)*RIGHT).shift(DOWN/16),
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_RED).shift(i*RIGHT+4*UP) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift(i*RIGHT+3*UP) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift(i*RIGHT) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift(i*RIGHT) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift(i*RIGHT) for i in range(n)],
            ).scale(7/8).shift(3*DOWN+(n-1)*LEFT/2)
            self.play(Transform(tebd2,tebd3))
            self.slide_break()

            tebd3=VGroup(
                *[Line(ORIGIN,4.75*UP).shift(i*RIGHT) for i in range(n)],
                Line(ORIGIN,(n-1)*RIGHT).shift(4*UP),
                Line(ORIGIN,(n-1)*RIGHT).shift(3*UP),
                Line(ORIGIN,(n-1)*RIGHT).shift(ORIGIN),
                Line(ORIGIN,(n-1)*RIGHT).shift(ORIGIN),
                Line(ORIGIN,(n-1)*RIGHT).shift(ORIGIN),
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_RED).shift(i*RIGHT+4*UP) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_YELLOW).shift(i*RIGHT+3*UP) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(i*RIGHT) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(i*RIGHT) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(i*RIGHT) for i in range(n)],
            ).scale(7/8).shift(3*DOWN+(n-1)*LEFT/2)
            self.play(Transform(tebd2,tebd3))
            self.slide_break()

            tebd3=VGroup(
                *[Line(ORIGIN,4.75*UP).shift(i*RIGHT) for i in range(n)],
                Line(ORIGIN,(n-1)*RIGHT).shift(4*UP),
                Line(ORIGIN,(n-1)*RIGHT).shift(UP/16),
                Line(ORIGIN,(n-1)*RIGHT).shift(DOWN/16),
                Line(ORIGIN,(n-1)*RIGHT).shift(DOWN/16),
                Line(ORIGIN,(n-1)*RIGHT).shift(DOWN/16),
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_RED).shift(i*RIGHT+4*UP) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift(i*RIGHT) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift(i*RIGHT) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift(i*RIGHT) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift(i*RIGHT) for i in range(n)],
            ).scale(7/8).shift(3*DOWN+(n-1)*LEFT/2)
            self.play(Transform(tebd2,tebd3))
            self.slide_break()

            tebd3=VGroup(
                *[Line(ORIGIN,4.75*UP).shift(i*RIGHT) for i in range(n)],
                Line(ORIGIN,(n-1)*RIGHT).shift(4*UP),
                Line(ORIGIN,(n-1)*RIGHT).shift(ORIGIN),
                Line(ORIGIN,(n-1)*RIGHT).shift(ORIGIN),
                Line(ORIGIN,(n-1)*RIGHT).shift(ORIGIN),
                Line(ORIGIN,(n-1)*RIGHT).shift(ORIGIN),
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_RED).shift(i*RIGHT+4*UP) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(i*RIGHT) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(i*RIGHT) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(i*RIGHT) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(i*RIGHT) for i in range(n)],
            ).scale(7/8).shift(3*DOWN+(n-1)*LEFT/2)
            self.play(Transform(tebd2,tebd3))
            self.slide_break()

            tebd3=VGroup(
                *[Line(ORIGIN,4.75*UP).shift(i*RIGHT) for i in range(n)],
                Line(ORIGIN,(n-1)*RIGHT).shift(UP/16),
                Line(ORIGIN,(n-1)*RIGHT).shift(DOWN/16),
                Line(ORIGIN,(n-1)*RIGHT).shift(DOWN/16),
                Line(ORIGIN,(n-1)*RIGHT).shift(DOWN/16),
                Line(ORIGIN,(n-1)*RIGHT).shift(DOWN/16),
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift(i*RIGHT) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift(i*RIGHT) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift(i*RIGHT) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift(i*RIGHT) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_GREEN).shift(i*RIGHT) for i in range(n)],
            ).scale(7/8).shift(3*DOWN+(n-1)*LEFT/2)
            self.play(Transform(tebd2,tebd3))
            self.slide_break()

            tebd3=VGroup(
                *[Line(ORIGIN,4.75*UP).shift(i*RIGHT) for i in range(n)],
                Line(ORIGIN,(n-1)*RIGHT).shift(ORIGIN),
                Line(ORIGIN,(n-1)*RIGHT).shift(ORIGIN),
                Line(ORIGIN,(n-1)*RIGHT).shift(ORIGIN),
                Line(ORIGIN,(n-1)*RIGHT).shift(ORIGIN),
                Line(ORIGIN,(n-1)*RIGHT).shift(ORIGIN),
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(i*RIGHT) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(i*RIGHT) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(i*RIGHT) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(i*RIGHT) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(i*RIGHT) for i in range(n)],
            ).scale(7/8).shift(3*DOWN+(n-1)*LEFT/2)
            self.play(Transform(tebd2,tebd3))
            self.slide_break()

            tebd3=VGroup(
                *[Line(ORIGIN,.75*UP).shift(i*RIGHT) for i in range(n)],
                Line(ORIGIN,(n-1)*RIGHT).shift(ORIGIN),
                Line(ORIGIN,(n-1)*RIGHT).shift(ORIGIN),
                Line(ORIGIN,(n-1)*RIGHT).shift(ORIGIN),
                Line(ORIGIN,(n-1)*RIGHT).shift(ORIGIN),
                Line(ORIGIN,(n-1)*RIGHT).shift(ORIGIN),
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(i*RIGHT) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(i*RIGHT) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(i*RIGHT) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(i*RIGHT) for i in range(n)],
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(i*RIGHT) for i in range(n)],
            ).scale(7/8).shift(1*DOWN+(n-1)*LEFT/2)
            self.play(Transform(tebd2,tebd3))
            self.slide_break()

            self.play(FadeOut(tebd1),tebd2.animate.set_color(BG))
            self.remove(tebd2)
            self.slide_break()
        if subsec==4 or subsec==-1:
            pass
        if subsec==5 or subsec==-1:
            pass
        if subsec==6 or subsec==-1:
            pass
        if subsec==7 or subsec==-1:
            pass
        if subsec==8 or subsec==-1:
            pass
        if subsec==9 or subsec==-1:
            pass
        if subsec==10 or subsec==-1:
            pass

        self.play(Restore(toc))

class Lec3_1(SlideScene):
    def construct(self):
        tocindex=(2,1)
        toc.set_opacity(0.25)
        toc[tocindex[0]].set_opacity(1)
        toc.save_state()
        heading = toc[tocindex[0]][tocindex[1]]
        self.add(toc,footer)
        self.play(
            toc.animate.set_opacity(0),
            heading.animate.scale(2).to_corner(UP).set_x(0),
        )
        heading.set_opacity(1)
        self.slide_break()

        subsec = -1
        # 1     how?
        # 2     hardness
        # 3     mps method
        # 4     random network
        # 5     BO
        # 6     sweep
        # 7     ?
        # 8     ?
        # 9     ?
        # 10    ?

        if subsec==1 or subsec==-1:
            n=10
            ladder1=VGroup()
            for i in range(n):
                ladder1 += VGroup(
                    Line(UP/4,UP*3/4).shift(RIGHT*i),
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=BLUE).shift(i*RIGHT),
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=BLUE).shift(i*RIGHT+UP),
                )
                ladder1 += VGroup(
                    Line(RIGHT/4,RIGHT*3/4).shift(RIGHT*i),
                    Line(RIGHT/4,RIGHT*3/4).shift(RIGHT*i+UP),
                )
            ladder1=ladder1[:-1]
            ladder1.move_to(ORIGIN)
            self.play(FadeIn(ladder1))
            self.slide_break()

            ladder2=VGroup()
            for i in range(n):
                ladder2 += VGroup(
                    Line(ORIGIN,ORIGIN).shift(RIGHT*i),
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=GREEN).shift(i*RIGHT),
                    Square(0.5,color=WHITE,fill_opacity=1,fill_color=GREEN).shift(i*RIGHT),
                )
                ladder2 += VGroup(
                    Line(RIGHT/4,RIGHT*3/4).shift(RIGHT*i),
                    Line(RIGHT/4,RIGHT*3/4).shift(RIGHT*i),
                )
            ladder2=ladder2[:-1]
            ladder2.move_to(ORIGIN)

            self.play(ReplacementTransform(ladder1,ladder2))
            self.slide_break()

            self.play(*[FadeOut(mob,shift=ladder2[-1].get_center()-mob.get_center()) for mob in ladder2[:-1]])
            self.play(FadeOut(ladder2[-1]))
            self.slide_break()

            grid=VGroup(
                *[Square(0.5,color=WHITE,fill_opacity=1,fill_color=BLUE).shift(i*RIGHT+j*UP) for i in range(5) for j in range(5)],
                *[Line(RIGHT/4,RIGHT*3/4).shift(i*RIGHT+j*UP) for i in range(4) for j in range(5)],
                *[Line(UP/4,UP*3/4).shift(i*RIGHT+j*UP) for i in range(5) for j in range(4)],
                MyTex("?").shift(5*RIGHT+2*UP)
            ).move_to(ORIGIN)
            self.play(FadeIn(grid))
            self.slide_break()
            self.play(FadeOut(grid))
            self.slide_break()

        if subsec==2 or subsec==-1:
            graphcol=VGroup()
            graphcol += VGroup(
                VGroup(
                    Line(LEFT*3/4,RIGHT*3/4),
                    Circle(0.25,color=WHITE,fill_opacity=1,fill_color=WHITE),
                    MyMathTex("i").move_to(LEFT),
                    MyMathTex("j").move_to(RIGHT),
                    MyMathTex(r":=\lbrace i\neq j\rbrace").next_to(1.25*RIGHT,RIGHT),
                ),
                VGroup(
                    Line(RIGHT/4,RIGHT*3/4),
                    Line(RIGHT/4,RIGHT*3/4).rotate(TAU/3,about_point=ORIGIN),
                    Line(RIGHT/4,RIGHT*3/4).rotate(-TAU/3,about_point=ORIGIN),
                    Circle(0.25,color=WHITE,fill_opacity=1,fill_color=BLACK),
                    MyMathTex(r"\alpha").move_to([np.cos(TAU/3),np.sin(TAU/3),0]),
                    MyMathTex(r"\beta").move_to(RIGHT),
                    MyMathTex(r"\gamma").move_to([np.cos(TAU/3),-np.sin(TAU/3),0]),
                    MyMathTex(r":=\lbrace \alpha=\beta=\cdots\rbrace").next_to(1.25*RIGHT,RIGHT),
                ),
            ).arrange(DOWN,buff=1,aligned_edge=LEFT).move_to(DOWN/2)
            self.play(FadeIn(graphcol[0][0]))
            self.play(FadeIn(graphcol[0][1]))
            self.slide_break()

            self.play(graphcol[0].animate.shift(3*LEFT).scale(.75))

            Gpos=[
                RIGHT,
                2.5*RIGHT+0.5*UP,
                DOWN,
                1.5*DOWN+1.5*RIGHT,
                2*DOWN+0.5*RIGHT,
                2.5*DOWN+2*RIGHT,
            ]
            Gcol=[
                RED,
                BLUE,
                GREEN,
                RED,
                BLUE,
                GREEN,
            ]

            Gedges=[
                [0,1],[0,2],[1,3],[3,4],[4,5],[3,5],[2,4],
            ]
            graphcol+=VGroup(
                *[Line(Gpos[e[0]],0.5*Gpos[e[0]]+0.5*Gpos[e[1]]) for e in Gedges],
                *[Line(Gpos[e[1]],0.5*Gpos[e[0]]+0.5*Gpos[e[1]]) for e in Gedges],
                *[Circle(.1,fill_opacity=1,color=WHITE).move_to(0.5*Gpos[e[0]]+0.5*Gpos[e[1]]) for e in Gedges],
                *[Circle(0.2,color=WHITE,fill_opacity=1,fill_color=BLACK).shift(pos) for pos in Gpos],
            ).move_to(3*RIGHT+DOWN/2).scale(1.25)
            self.play(FadeIn(graphcol[1]))
            self.slide_break()

            graphcol+=VGroup(
                *[Line(Gpos[e[0]],0.5*Gpos[e[0]]+0.5*Gpos[e[1]],color=Gcol[e[0]],stroke_width=20) for e in Gedges],
                *[Line(Gpos[e[1]],0.5*Gpos[e[0]]+0.5*Gpos[e[1]],color=Gcol[e[1]],stroke_width=20) for e in Gedges],
                *[Circle(.1,fill_opacity=1,color=WHITE).move_to(0.5*Gpos[e[0]]+0.5*Gpos[e[1]]) for e in Gedges],
                *[Circle(0.2,color=WHITE,fill_opacity=1,fill_color=BLACK).shift(pos) for pos in Gpos],
            ).move_to(3*RIGHT+DOWN/2).scale(1.25)
            self.play(ReplacementTransform(graphcol[-2],graphcol[-1]))
            self.slide_break()

            graphcol+=VGroup(
                *[Line(Gpos[e[0]],0.5*Gpos[e[0]]+0.5*Gpos[e[1]]) for e in Gedges],
                *[Line(Gpos[e[1]],0.5*Gpos[e[0]]+0.5*Gpos[e[1]]) for e in Gedges],
                *[Circle(0,fill_opacity=1,color=WHITE).move_to(0.5*Gpos[e[0]]+0.5*Gpos[e[1]]) for e in Gedges],
                *[Circle(0.2,color=WHITE,fill_opacity=1,fill_color=Gcol[i]).shift(Gpos[i]) for i in range(len(Gpos))],
            ).move_to(3*RIGHT+DOWN/2).scale(1.25)
            self.play(ReplacementTransform(graphcol[-2],graphcol[-1]))
            self.slide_break()

            self.play(*[FadeOut(mob) for mob in self.mobjects if mob!=toc and mob!=footer])
            self.slide_break()

            tnd=ImageMobject("tnd.png").scale(.8)
            self.play(FadeIn(tnd))
            self.slide_break()
            self.play(FadeOut(tnd))
            self.slide_break()

        if subsec==3 or subsec==-1:
            a=1.5   # lattice spacing
            r=.75   # MPS square radius
            g=0.1   # gap between multi-edges

            TN_ten=VGroup(*[
                VGroup(*[
                    Square(r).set_fill(TEN_RED,opacity=1).move_to([i*a,j*a,0])
                for j in range(4)])
            for i in range(4)])
            TN_ver=VGroup(*[Line([0,i*a,0],[3*a,i*a,0]) for i in range(4)])
            TN_hor=VGroup(*[Line([j*a,0,0],[j*a,3*a,0]) for j in range(4)])

            self.add_foreground_mobjects(TN_ten)

            TN=VGroup(TN_ten,TN_hor,TN_ver).move_to(DOWN/2)

            TN.save_state()
            TN.set_color(BG)
            self.play(Restore(TN))
            self.slide_break()

            self.play(Indicate(TN_ten[0]))
            self.slide_break()

            MPS=VGroup(*[
                Square(r).set_fill(TEN_BLUE,opacity=1).move_to([0,j*a,0])
            for j in range(4)]).move_to(TN_ten[0])
            self.play(ReplacementTransform(TN_ten[0],MPS))
            self.slide_break()

            self.play( *[Circumscribe(Group(MPS[j],TN_ten[1][j]),run_time=2) for j in range(4)] )
            self.slide_break()

            self.play(
                MPS.animate.set_fill(TEN_PURPLE),
                FadeOut(TN_ten[1],target_position=MPS),
                TN_hor[1].animate.shift((a-g)*LEFT),
                TN_hor[0].animate.shift(g*LEFT),
            )
            self.slide_break()

            self.play(
                MPS.animate.set_fill(TEN_BLUE),
                TN_hor[1].animate.shift(g*LEFT),
                TN_hor[0].animate.shift(g*RIGHT),
            )
            self.remove(TN_hor[1])
            self.slide_break()


            self.play(
                MPS.animate.set_fill(TEN_PURPLE),
                FadeOut(TN_ten[2],target_position=MPS),
                TN_hor[2].animate.shift((2*a-g)*LEFT),
                TN_hor[0].animate.shift(g*LEFT),
            )
            self.slide_break()
            self.play(
                MPS.animate.set_fill(TEN_BLUE),
                TN_hor[2].animate.shift(g*LEFT),
                TN_hor[0].animate.shift(g*RIGHT),
            )
            self.remove(TN_hor[2])
            self.slide_break()

            self.play(
                MPS.animate.set_fill(TEN_PURPLE),
                FadeOut(TN_ten[3],target_position=MPS),
                TN_hor[3].animate.shift((3*a-g)*LEFT),
                TN_hor[0].animate.shift(g*LEFT),
                Uncreate(TN_ver[0]),
                Uncreate(TN_ver[1]),
                Uncreate(TN_ver[2]),
                Uncreate(TN_ver[3]),
            )
            self.slide_break()
            self.play(
                MPS.animate.set_fill(TEN_BLUE),
                TN_hor[3].animate.shift(g*LEFT),
                TN_hor[0].animate.shift(g*RIGHT),
            )
            self.remove(TN_hor[3])
            self.slide_break()

            self.play(
                FadeOut(MPS[3],target_position=MPS[2]),
                FadeOut(MPS[0],target_position=MPS[1]),
                TN_hor[0].animate.scale(0.5)
            )
            self.slide_break()

            res_ten=Square(r).set_fill(TEN_BLUE,opacity=1).move_to(MPS[1]).shift(a*UP/2)

            self.play(
                FadeOut(MPS[1],target_position=res_ten),
                FadeOut(MPS[2],target_position=res_ten),
                FadeIn(res_ten),
                TN_hor[0].animate.scale(0)
            )
            self.remove(TN_hor[0])
            self.slide_break()

            self.play(res_ten.animate.shift(1.5*a*RIGHT))
            self.slide_break()

            self.play(FadeOut(res_ten))
            self.slide_break()

        if subsec==4 or subsec==-1:
            x=[1.3,1.7,1.3,1.7,1.3,1.7,1.3,1.7,1.3,1.7,1.3,1.7,1.3,1.7,1.3,1.7,1.3,1.7,1.3,1.7,1.3444444444444446,1.3444444444444446,1.3888888888888888,1.3888888888888888,1.4333333333333333,1.4333333333333333,1.4777777777777779,1.4777777777777779,1.5222222222222221,1.5222222222222221,1.5666666666666667,1.5666666666666667,1.6111111111111112,1.6111111111111112,1.6555555555555554,1.6555555555555554,1.3146813455822222,1.6912318334888399,1.5850679390100162,1.6319041184368146,1.5632087030796582,1.3416744470853277,1.305245260397479,1.3811807139547028,1.569732522555214,1.5785703957531692,1.6133768961582222,1.370792387719675,1.530272418142219,1.3056797657862247,1.4041724456267217,1.3806761576857094,1.3521130704205586,1.6875568789065925,1.5407077986943307,1.4664156431599455,1.312469896388232,1.333653349987466,1.4765216656769649,1.3141972728230162,1.6109951956925297,1.3058567568855493,1.450966636453833,1.5969861759376947,1.4607555525784381,1.4247069038002123,1.4381532553562153,1.3287438309458095,1.5106084295516307,1.4433715587469933,1.6259024727635076,1.5473531511714207,1.6501312873591296,1.6246685939241396,1.6434257877961684,1.4955602831683201,1.4635552909349492,1.4499980598752185,1.3702106338933064,1.683032389939865,1.5080595538334756,1.4354133855200084,1.5709643711990129,1.5574387438211326,1.3535311121777251,1.3792891538734415,1.358499083532044,1.5943229148270064,1.653097921417943,1.4651973129733942,1.5702280107423296,1.535439447882288,1.4868458849361934,1.4395202229401662,1.672350891060311,1.6895922250618451,1.3158083310050592,1.3629271216283554,1.49377095517567,1.3855970089329892]
            y=[1.3,1.3,1.3444444444444446,1.3444444444444446,1.3888888888888888,1.3888888888888888,1.4333333333333333,1.4333333333333333,1.4777777777777779,1.4777777777777779,1.5222222222222221,1.5222222222222221,1.5666666666666667,1.5666666666666667,1.6111111111111112,1.6111111111111112,1.6555555555555554,1.6555555555555554,1.7,1.7,1.3,1.7,1.3,1.7,1.3,1.7,1.3,1.7,1.3,1.7,1.3,1.7,1.3,1.7,1.3,1.7,1.5113452063287771,1.4511336497881024,1.4057566700292579,1.4477286572000834,1.5978347288919257,1.5234947157417724,1.5670646552922136,1.3598802812388457,1.492522325435982,1.627550821948484,1.362535735717852,1.4792866329042915,1.3556228022353756,1.3720582944547748,1.4669270404028365,1.433934769345092,1.5531813433020358,1.651996056147321,1.6820481405154526,1.4547148843312103,1.472789354825991,1.4618178025321447,1.4545264059178775,1.3404986235678609,1.348067427930161,1.5711414081903796,1.3335821603949216,1.662273584837917,1.4713300385008048,1.3897202061426563,1.3271343085213245,1.5710479693322343,1.5351186633914506,1.64427984499828,1.3082307046745767,1.338714238384548,1.309310794439587,1.367351013475362,1.5844767556471793,1.6276639188355855,1.4027458341739096,1.3204534059287927,1.6282588726180156,1.5948070390587552,1.3179928368288134,1.6597584769377647,1.4494037784652756,1.6134630080742174,1.6946445695269203,1.392562409917996,1.4457265765701024,1.4959687909385995,1.6549067684382384,1.3784802486485463,1.573721113430063,1.3094752535248082,1.5959336238216797,1.5020366704935635,1.6839143728565418,1.4570994392495145,1.5160991563849382,1.4281432635629987,1.4412238481653536,1.6504295417711745]
            e=[(1, 3),(1, 34),(1, 72),(88, 94),(10, 42),(10, 36),(10, 12),(10, 96),(28, 30),(28, 91),(28, 80),(56, 57),(30, 91),(30, 71),(30, 60),(30, 32),(69, 99),(69, 92),(69, 75),(69, 78),(69, 81),(32, 70),(32, 34),(32, 60),(25, 27),(25, 81),(48, 76),(48, 80),(48, 71),(48, 98),(48, 89),(83, 92),(3, 73),(3, 5),(3, 72),(92, 93),(53, 79),(53, 88),(53, 94),(49, 59),(49, 85),(76, 98),(76, 89),(79, 88),(39, 87),(39, 82),(39, 73),(39, 95),(33, 88),(33, 35),(33, 63),(78, 99),(78, 92),(78, 84),(70, 72),(75, 92),(75, 83),(11, 74),(11, 13),(11, 39),(11, 87),(15, 53),(15, 79),(15, 17),(61, 67),(20, 22),(20, 59),(20, 43),(9, 39),(9, 95),(9, 11),(9, 37),(87, 90),(71, 91),(71, 80),(27, 69),(27, 75),(27, 81),(27, 29),(4, 6),(4, 49),(4, 97),(4, 85),(62, 77),(62, 65),(62, 80),(62, 66),(62, 89),(14, 67),(14, 16),(14, 61),(14, 78),(40, 83),(40, 68),(40, 92),(40, 90),(40, 45),(67, 96),(67, 78),(38, 46),(38, 82),(38, 39),(38, 73),(38, 98),(38, 71),(38, 48),(45, 74),(45, 54),(45, 88),(45, 63),(45, 83),(45, 90),(84, 99),(24, 77),(24, 66),(24, 26),(54, 63),(54, 75),(54, 83),(65, 76),(65, 85),(65, 66),(65, 89),(41, 67),(41, 52),(41, 57),(41, 47),(41, 96),(57, 86),(58, 68),(58, 98),(58, 64),(7, 9),(7, 39),(7, 37),(19, 35),(19, 94),(13, 74),(13, 79),(13, 15),(51, 65),(51, 97),(51, 85),(51, 86),(17, 53),(17, 94),(17, 19),(68, 98),(68, 92),(68, 93),(68, 90),(34, 70),(34, 72),(82, 98),(82, 87),(16, 18),(16, 78),(16, 21),(16, 84),(63, 88),(64, 68),(64, 93),(43, 59),(43, 49),(43, 65),(43, 85),(43, 66),(36, 41),(36, 57),(36, 96),(36, 56),(44, 82),(44, 68),(44, 98),(44, 87),(44, 90),(12, 42),(12, 61),(12, 14),(85, 97),(66, 77),(0, 59),(0, 2),(0, 20),(29, 54),(29, 31),(29, 75),(46, 71),(46, 60),(46, 73),(31, 54),(31, 33),(31, 63),(81, 99),(6, 8),(6, 97),(6, 57),(6, 86),(6, 56),(42, 67),(42, 61),(42, 96),(74, 90),(74, 79),(74, 88),(74, 87),(8, 36),(8, 10),(8, 56),(86, 97),(2, 59),(2, 49),(2, 4),(60, 70),(60, 71),(60, 73),(60, 72),(37, 39),(37, 95),(47, 52),(47, 57),(47, 86),(47, 93),(47, 50),(47, 51),(35, 88),(35, 94),(80, 91),(80, 89),(18, 21),(50, 65),(50, 64),(50, 93),(50, 55),(50, 51),(21, 84),(21, 23),(5, 39),(5, 73),(5, 7),(23, 25),(23, 99),(23, 81),(23, 84),(72, 73),(52, 67),(52, 92),(52, 93),(52, 78),(22, 24),(22, 66),(22, 43),(26, 62),(26, 77),(26, 80),(26, 28),(55, 76),(55, 65),(55, 98),(55, 64),(55, 58)]
            randnet=VGroup(
                *[Line([x[ee[0]],y[ee[0]],0],[x[ee[1]],y[ee[1]],0],stroke_width=2) for ee in e],
            )#.set_color(RED)
            randnet.height=5
            randnet.move_to(DOWN/4)

            # self.play(Write(randnet))
            self.play(*[Write(r) for r in randnet])
            self.slide_break()

            # self.play(Unwrite(randnet))
            self.play(*[Unwrite(r) for r in randnet])
            self.slide_break()

        if subsec==5 or subsec==-1:
            BO(self)

        if subsec==6 or subsec==-1:
            x=[3,1,5,2,0,6,4]
            y=[0,1,2,3,4,5,6]
            e=[(0,1),(0,2),(1,3),(1,4),(2,3),(2,5),(3,4),(3,5),(3,6),(4,6),(5,6)]
            if False:
                sweep_example=Group(
                    DashedLine([-8,-3.5,0],[-8,3.5,0], dash_length=0.25).shift(RIGHT),
                    Rectangle(height=7, width=14 ,color=WHITE),
                    *[Circle(0.25,color=WHITE).set_fill(GREEN,opacity=1).move_to([1.5*(y[i]-3),.9*(x[i]-3),0]) for i in range(7)]
                ).scale(0.75).move_to(DOWN/2)

                self.play(FadeIn(sweep_example[2:]))
                self.slide_break(t=0.6)
                self.add_foreground_mobjects(sweep_example[2:])

                self.play(FadeIn(sweep_example[0].shift(RIGHT/2),shift=RIGHT/2))
                self.slide_break(t=0.6)

                self.play(sweep_example[0].animate.shift(1.375*RIGHT))
                self.slide_break(t=0.6)

                # self.play(Flash(sweep_example[2],line_length=0.5,color=GREEN))
                # self.play(FadeOut(sweep_example[2]))
                self.play(
                    Flash(sweep_example[2],line_length=0.25,color=GREEN),
                    FadeOut(sweep_example[2])
                )
                self.slide_break(t=0.6)

                for i in range(3,9):
                    self.play(sweep_example[0].animate.shift(1.125*RIGHT))
                    self.play(
                        Flash(sweep_example[i],line_length=0.25,color=GREEN),
                        FadeOut(sweep_example[i])
                    )
                self.play(sweep_example[0].animate.shift(1.125*RIGHT))
                self.play(FadeOut(sweep_example[0],shift=RIGHT/2))
                self.slide_break()

                self.remove(sweep_example[0])

            sweep_l=DashedLine([-7*.75,-3.5*.75-.5,0],[-7*.75,3.5*.75-.5,0], dash_length=0.25*.75)
            sweep_t=Group(*[
                Circle(0.25,color=WHITE).set_fill(TEN_RED,opacity=1).move_to([.75*1.5*(y[i]-3),.75*.9*(x[i]-3)-.5,0])
            for i in range(7)])
            sweep_e=Group(*[
                Line([.75*1.5*(y[ee[0]]-3),.75*(x[ee[0]]-3)-.5,0],[.75*1.5*(y[ee[1]]-3),.75*.9*(x[ee[1]]-3)-.5,0])
            for ee in e])


            self.play(FadeIn(sweep_t))
            self.add_foreground_mobjects(sweep_t)
            self.play(FadeIn(sweep_e))
            self.slide_break()

            self.play(FadeIn(sweep_l.shift(RIGHT/2),shift=RIGHT/2))
            self.slide_break()

            self.play(sweep_l.animate.shift(1.375*RIGHT))
            self.slide_break()

            new_ten=Circle(0.25,color=WHITE).set_fill(TEN_PURPLE,opacity=1).move_to([-4.5,-0.5,0])

            self.play(
                ReplacementTransform(sweep_t[0],new_ten),
                Transform(sweep_e[0],Line(new_ten.get_center(),sweep_e[0].end)),
                Transform(sweep_e[1],Line(new_ten.get_center(),sweep_e[1].end)),
            )
            self.slide_break()
            mps=VGroup(
                Line([-4.5,-0.5-.25,0],[-4.5,-0.5+.25,0]),
                Square(0.75*.75,color=WHITE).set_fill(TEN_BLUE,opacity=1).move_to([-4.5,-0.5-.5,0]),
                Square(0.75*.75,color=WHITE).set_fill(TEN_BLUE,opacity=1).move_to([-4.5,-0.5+.5,0]),
            )
            self.play(
                ReplacementTransform(new_ten,mps),
                Transform(sweep_e[0],Line(mps[1].get_right(),sweep_e[0].end)),
                Transform(sweep_e[1],Line(mps[2].get_right(),sweep_e[1].end)),
            )
            self.slide_break()


            self.play(sweep_l.animate.shift(1.125*RIGHT))
            self.slide_break()
            self.play(
                Uncreate(sweep_e[0]),
                Transform(mps[1],Circle(0.25,color=WHITE).set_fill(TEN_PURPLE,opacity=1).move_to(mps[1])),
                FadeOut(sweep_t[1],target_position=mps[1]),
                Transform(sweep_e[2],Line([-4.5,-0.5-.5,0],sweep_e[2].end)),
                Transform(sweep_e[3],Line([-4.5,-0.5-.5,0],sweep_e[3].end)),
            )
            self.slide_break()
            oldmps=mps
            mps=VGroup(
                Line([-4.5,-0.5-1,0],[-4.5,-0.5+1,0]),
                Square(0.75*.75,color=WHITE).set_fill(TEN_BLUE,opacity=1).move_to([-4.5,-0.5-1,0]),
                Square(0.75*.75,color=WHITE).set_fill(TEN_BLUE,opacity=1).move_to([-4.5,-0.5  ,0]),
                Square(0.75*.75,color=WHITE).set_fill(TEN_BLUE,opacity=1).move_to([-4.5,-0.5+1,0]),
            )
            self.play(
                ReplacementTransform(oldmps[0],mps[0]),
                ReplacementTransform(oldmps[1],mps[1:3]),
                ReplacementTransform(oldmps[2],mps[3]),
                Transform(sweep_e[1],Line(mps[3].get_right(),sweep_e[1].end)),
                Transform(sweep_e[2],Line(mps[2].get_right(),sweep_e[2].end)),
                Transform(sweep_e[3],Line(mps[1].get_right(),sweep_e[3].end)),
            )
            self.slide_break()


            self.play(sweep_l.animate.shift(1.125*RIGHT))
            self.slide_break()
            self.play(
                Uncreate(sweep_e[1]),
                Transform(mps[3],Circle(0.25,color=WHITE).set_fill(TEN_PURPLE,opacity=1).move_to(mps[3])),
                FadeOut(sweep_t[2],target_position=mps[3]),
                Transform(sweep_e[4],Line(mps[3].get_center(),sweep_e[4].end)),
                Transform(sweep_e[5],Line(mps[3].get_center(),sweep_e[5].end)),
            )
            self.slide_break()
            oldmps=mps
            mps=VGroup(
                Line([-4.5,-0.5-1.5,0],[-4.5,-0.5+1.5,0]),
                Square(0.75*.75,color=WHITE).set_fill(TEN_BLUE,opacity=1).move_to([-4.5,-0.5-1.5,0]),
                Square(0.75*.75,color=WHITE).set_fill(TEN_BLUE,opacity=1).move_to([-4.5,-0.5-0.5,0]),
                Square(0.75*.75,color=WHITE).set_fill(TEN_BLUE,opacity=1).move_to([-4.5,-0.5+0.5,0]),
                Square(0.75*.75,color=WHITE).set_fill(TEN_BLUE,opacity=1).move_to([-4.5,-0.5+1.5,0]),
            )
            self.play(
                ReplacementTransform(oldmps[0],mps[0]),
                ReplacementTransform(oldmps[1],mps[1]),
                ReplacementTransform(oldmps[2],mps[2]),
                ReplacementTransform(oldmps[3],mps[3:5]),
                Transform(sweep_e[5],Line(mps[4].get_right(),sweep_e[5].end)),
                Transform(sweep_e[4],Line(mps[3].get_right(),sweep_e[4].end)),
                Transform(sweep_e[2],Line(mps[2].get_right(),sweep_e[2].end)),
                Transform(sweep_e[3],Line(mps[1].get_right(),sweep_e[3].end)),
            )
            self.slide_break()

            self.play(sweep_l.animate.shift(1.125*RIGHT))
            self.slide_break()
            self.play(
                Uncreate(sweep_e[4]),
                Uncreate(sweep_e[2]),
                Transform(mps[2:4],Circle(0.25,color=WHITE).set_fill(TEN_PURPLE,opacity=1).move_to(mps[3]).shift(0.5*DOWN)),
                FadeOut(sweep_t[3],target_position=mps[3]),
                Transform(sweep_e[6],Line(mps[3].get_center()+0.5*DOWN,sweep_e[6].end)),
                Transform(sweep_e[7],Line(mps[3].get_center()+0.5*DOWN,sweep_e[7].end)),
                Transform(sweep_e[8],Line(mps[3].get_center()+0.5*DOWN,sweep_e[8].end)),
            )
            self.slide_break()
            oldmps=mps
            mps=VGroup(
                Line([-4.5,-0.5-2,0],[-4.5,-0.5+2,0]),
                Square(0.75*.75,color=WHITE).set_fill(TEN_BLUE,opacity=1).move_to([-4.5,-0.5-2,0]),
                Square(0.75*.75,color=WHITE).set_fill(TEN_BLUE,opacity=1).move_to([-4.5,-0.5-1,0]),
                Square(0.75*.75,color=WHITE).set_fill(TEN_BLUE,opacity=1).move_to([-4.5,-0.5  ,0]),
                Square(0.75*.75,color=WHITE).set_fill(TEN_BLUE,opacity=1).move_to([-4.5,-0.5+1,0]),
                Square(0.75*.75,color=WHITE).set_fill(TEN_BLUE,opacity=1).move_to([-4.5,-0.5+2,0]),
            )
            self.play(
                ReplacementTransform(oldmps[0],mps[0]),
                ReplacementTransform(oldmps[1],mps[1]),
                ReplacementTransform(oldmps[2],mps[2:5]),
                ReplacementTransform(oldmps[4],mps[5]),
                Transform(sweep_e[5],Line(mps[5].get_right(),sweep_e[5].end)),
                Transform(sweep_e[7],Line(mps[4].get_right(),sweep_e[7].end)),
                Transform(sweep_e[8],Line(mps[3].get_right(),sweep_e[8].end)),
                Transform(sweep_e[6],Line(mps[2].get_right(),sweep_e[6].end)),
                Transform(sweep_e[3],Line(mps[1].get_right(),sweep_e[3].end)),
            )
            self.slide_break()

            self.play(sweep_l.animate.shift(1.125*RIGHT))
            self.slide_break()
            self.play(
                Uncreate(sweep_e[3]),
                Uncreate(sweep_e[6]),
                Transform(mps[1:3],Circle(0.25,color=WHITE).set_fill(TEN_PURPLE,opacity=1).move_to(mps[1])),
                FadeOut(sweep_t[4],target_position=mps[1]),
                Transform(sweep_e[9],Line(mps[1].get_center(),sweep_e[9].end)),
            )
            self.slide_break()
            oldmps=mps
            mps=VGroup(
                Line([-4.5,-0.5-1.5,0],[-4.5,-0.5+1.5,0]),
                Square(0.75*.75,color=WHITE).set_fill(TEN_BLUE,opacity=1).move_to([-4.5,-0.5-1.5,0]),
                Square(0.75*.75,color=WHITE).set_fill(TEN_BLUE,opacity=1).move_to([-4.5,-0.5-0.5,0]),
                Square(0.75*.75,color=WHITE).set_fill(TEN_BLUE,opacity=1).move_to([-4.5,-0.5+0.5,0]),
                Square(0.75*.75,color=WHITE).set_fill(TEN_BLUE,opacity=1).move_to([-4.5,-0.5+1.5,0]),
            )
            self.play(
                ReplacementTransform(oldmps,mps),
                Transform(sweep_e[5],Line(mps[4].get_right(),sweep_e[5].end)),
                Transform(sweep_e[7],Line(mps[3].get_right(),sweep_e[7].end)),
                Transform(sweep_e[8],Line(mps[2].get_right(),sweep_e[8].end)),
                Transform(sweep_e[9],Line(mps[1].get_right(),sweep_e[9].end)),
            )
            self.slide_break()

            self.play(sweep_l.animate.shift(1.125*RIGHT))
            self.slide_break()
            self.remove(*oldmps)
            self.play(
                Uncreate(sweep_e[5]),
                Uncreate(sweep_e[7]),
                Transform(mps[3:5],Circle(0.25,color=WHITE).set_fill(TEN_PURPLE,opacity=1).move_to(mps[4])),
                FadeOut(sweep_t[5],target_position=mps[4]),
                Transform(sweep_e[10],Line(mps[4].get_center(),sweep_e[10].end)),
            )

            self.slide_break()
            oldmps=mps
            mps=VGroup(
                Line([-4.5,-0.5-1,0],[-4.5,-0.5+1,0]),
                Square(0.75*.75,color=WHITE).set_fill(TEN_BLUE,opacity=1).move_to([-4.5,-0.5-1,0]),
                Square(0.75*.75,color=WHITE).set_fill(TEN_BLUE,opacity=1).move_to([-4.5,-0.5  ,0]),
                Square(0.75*.75,color=WHITE).set_fill(TEN_BLUE,opacity=1).move_to([-4.5,-0.5+1,0]),
            )
            self.play(
                ReplacementTransform(oldmps[0],mps[0]),
                ReplacementTransform(oldmps[1],mps[1]),
                ReplacementTransform(oldmps[2],mps[2]),
                ReplacementTransform(oldmps[3],mps[3]),
                Transform(sweep_e[10],Line(mps[3].get_right(),sweep_e[10].end)),
                Transform(sweep_e[8],Line(mps[2].get_right(),sweep_e[8].end)),
                Transform(sweep_e[9],Line(mps[1].get_right(),sweep_e[9].end)),
            )
            self.slide_break()


            self.play(sweep_l.animate.shift(1.125*RIGHT))
            self.slide_break()
            self.play(
                Uncreate(sweep_e[10]),
                Uncreate(sweep_e[8]),
                Uncreate(sweep_e[9]),
                Transform(mps,Circle(0.25,color=WHITE).set_fill(TEN_PURPLE,opacity=1).move_to(mps[2])),
                FadeOut(sweep_t[6],target_position=mps[1]),
            )
            self.slide_break()

            self.play(FadeOut(sweep_l,shift=0.5*RIGHT),mps.animate.move_to(DOWN/2))
            self.slide_break()
            self.remove(sweep_l)

            self.play(FadeOut(mps))
            self.slide_break()

        if subsec==7 or subsec==-1:
            pass
        if subsec==8 or subsec==-1:
            pass
        if subsec==9 or subsec==-1:
            pass
        if subsec==10 or subsec==-1:
            pass

        self.play(Restore(toc))

class Lec3_2(SlideScene):
    def construct(self):
        tocindex=(2,2)
        toc.set_opacity(0.25)
        toc[tocindex[0]].set_opacity(1)
        toc.save_state()
        heading = toc[tocindex[0]][tocindex[1]]
        self.add(toc,footer)
        self.play(
            toc.animate.set_opacity(0),
            heading.animate.scale(2).to_corner(UP).set_x(0),
        )
        heading.set_opacity(1)
        self.slide_break()

        subsec = -1
        # 1     ?
        # 2     ?
        # 3     ?
        # 4     ?
        # 5     ?
        # 6     ?
        # 7     ?
        # 8     ?
        # 9     ?
        # 10    ?

        if subsec==1 or subsec==-1:
            peps=VGroup(
                *[Line(2*LEFT,2*RIGHT).shift(i*UP) for i in range(-2,3)],
                *[Line(2*UP,2*DOWN).shift(i*RIGHT) for i in range(-2,3)],
                *[Line(ORIGIN,IN).shift(i*UP+j*RIGHT) for i in range(-2,3) for j in range(-2,3)],
                *[Cube(1/3,stroke_color=WHITE,fill_opacity=1,fill_color=BLUE).move_to(i*RIGHT+j*UP) for i in range(-2,3) for j in range(-2,3)]
            )
            peps.rotate(TAU/4,axis=RIGHT)

            peps.save_state()
            peps.set_color(BG)
            self.play(Restore(peps))
            self.slide_break()
            # self.play(Rotate(peps,angle=TAU/4,axis=RIGHT))
            self.play(Rotate(peps,angle=0.75,axis=RIGHT+DOWN/2))
            self.slide_break()
            self.play(Rotate(peps,angle=-0.75,axis=RIGHT+DOWN/2))
            self.play(Rotate(peps,angle=-TAU/4,axis=RIGHT))

            wave=Axes(
                x_range=[0, 2*TAU, 1],
                y_range=[-1.5, 1.5, 1]
            ).plot(lambda x: 0.5*np.sin(x))
            wave.width=.5
            wave.rotate(TAU/8)

            peps2=VGroup(
                *[Line(2*LEFT,2*RIGHT).shift(i*UP) for i in range(-2,3)],
                *[Line(2*UP,2*DOWN).shift(i*RIGHT) for i in range(-2,3)],
                *[Square(1/3,stroke_color=WHITE,fill_opacity=1,fill_color=BLUE).move_to(i*RIGHT+j*UP) for i in range(-2,3) for j in range(-2,3)],
                *[Line(ORIGIN,IN).shift(i*UP+j*RIGHT) for i in range(-2,3) for j in range(-2,3)],
            )


            peps3=VGroup(
                *[Line(2*LEFT,2*RIGHT).shift(i*UP) for i in range(-2,3)],
                *[Line(2*UP,2*DOWN).shift(i*RIGHT) for i in range(-2,3)],
                *[Square(1/3,stroke_color=WHITE,fill_opacity=1,fill_color=BLUE).move_to(i*RIGHT+j*UP) for i in range(-2,3) for j in range(-2,3)],
                *[wave.move_to(UR/4).copy().shift(i*UP+j*RIGHT) for i in range(-2,3) for j in range(-2,3)],
            )
            self.play(FadeTransform(peps,peps2))
            self.play(ReplacementTransform(peps2,peps3))
            self.slide_break()
            self.play(peps3.animate.set_color(BG))
            self.remove(peps3)
            self.slide_break()

        if subsec==2 or subsec==-1:

            a=1.5
            pepstebd=VGroup(
                *[Line(ORIGIN,UR).shift(i*a*RIGHT+j*a*UP) for i in range(3) for j in range(3)],
                VGroup(
                    *[Line(i*a*UP,2*a*RIGHT+i*a*UP) for i in range(3)],
                    *[Line(i*a*RIGHT,2*a*UP+i*a*RIGHT) for i in range(3)],
                    *[Square(1/4,color=WHITE,fill_opacity=1,fill_color=TEN_BLUE).shift(i*a*RIGHT+j*a*UP) for i in range(3) for j in range(3)],
                ),
                VGroup(
                    *[Line(i*a*UP,2*a*RIGHT+i*a*UP) for i in range(3)],
                    *[Line(i*a*RIGHT,2*a*UP+i*a*RIGHT) for i in range(3)],
                    *[Square(1/4,color=WHITE,fill_opacity=1,fill_color=TEN_RED).shift(i*a*RIGHT+j*a*UP) for i in range(3) for j in range(3)],
                ).shift(UR/3),
                VGroup(
                    *[Line(i*a*UP,2*a*RIGHT+i*a*UP) for i in range(3)],
                    *[Line(i*a*RIGHT,2*a*UP+i*a*RIGHT) for i in range(3)],
                    *[Square(1/4,color=WHITE,fill_opacity=1,fill_color=TEN_RED).shift(i*a*RIGHT+j*a*UP) for i in range(3) for j in range(3)],
                ).shift(UR*2/3),
            ).move_to(ORIGIN)
            self.play(FadeIn(pepstebd))
            self.slide_break()

            util=Group(
                ImageMobject("utility.png"),
                ImageMobject("utility2.png"),
            )
            util[0].set_height(3.5)
            util[1].set_height(3.5)
            util.arrange(RIGHT,buff=0.5)
            self.play(FadeIn(util[0]))
            self.play(FadeIn(util[1]))
            self.slide_break()

            self.play(FadeOut(util))
            ibm=Group(
                ImageMobject("ibm1.png"),
                ImageMobject("ibm2.png"),
            )
            ibm[0].set_height(5)
            ibm[1].set_height(5)
            ibm.arrange(RIGHT,buff=0.5)
            self.play(FadeIn(ibm[0]))
            self.play(FadeIn(ibm[1]))
            self.slide_break()

            self.play(*[FadeOut(mob) for mob in self.mobjects if mob!=toc and mob!=footer])

        if subsec==3 or subsec==-1:
            pass
        if subsec==4 or subsec==-1:
            pass
        if subsec==5 or subsec==-1:
            pass
        if subsec==6 or subsec==-1:
            pass
        if subsec==7 or subsec==-1:
            pass
        if subsec==8 or subsec==-1:
            pass
        if subsec==9 or subsec==-1:
            pass
        if subsec==10 or subsec==-1:
            pass

        self.play(Restore(toc))
