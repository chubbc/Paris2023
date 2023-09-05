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
        MyTex(r"3.1:~PEPS"),
        MyTex(r"3.2:~Higher-dim TEBD"),
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
            self.play(FadeOut(trunc8))
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
                    MyMathTex(r"\ket\Lambda \approx \min_{\psi} \braopket{\psi}{H}{\psi}"),
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
                r"\min_{\psi}",r"&~~~\braopket \psi H \psi\\~\\",
                r"\text{where}",r"&~~~\braket\psi\psi",r"=1,\\",
                r"&~~~\text{BD}(\ket \psi)\leq \chi",
            )
            rayleigh2=MyMathTex(
                r"\min_{\psi}",r"&~~~{\braopket \psi H \psi ", r"\over", r"\braket\psi\psi}\\~\\",
                r"\text{where}",r"&~~~\text{BD}(\ket \psi)\leq \chi",
            )

            # i=3
            # self.add(rayleigh2[i])
            # self.add(index_labels(rayleigh2[i]))


            # return

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

            n=6
            k=2
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

            env1.move_to(ORIGIN)
            env2.move_to(ORIGIN)

            self.play(FadeIn(env1))
            self.slide_break()
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
