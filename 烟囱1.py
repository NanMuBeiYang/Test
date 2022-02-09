from pyp3d import *
# 定义参数化模型
class 烟囱(Component):
    # 定义各个参数及其默认值
    def __init__(self):
        Component.__init__(self)
        self['底座高度'] = Attr(2000.0, obvious=True)
        self['底座边长'] = Attr(1228.0, obvious=True)
        self['底部倾斜角度'] = Attr(30,obvious = True)

        self['顶部高度'] = Attr(1500, obvious=True)
        self['顶部边长'] = Attr(1128,obvious = True)
        self['棱角缩进'] = Attr(215, obvious=True)


        self['烟管外半径 '] = Attr(150, obvious=True)
        self['烟管内半径 '] = Attr(110, obvious=True)
        

       
        self['烟囱'] = Attr(None, show=True)
      
        self.replace()
    @export
    # 开始写模型
    def replace(self):
        # 设置变量，同时调用参数(简化书写过程)
        High_B = self['底座高度']
        Edge_B = self['底座边长']
        angle = self['底部倾斜角度']

        High_T = self['顶部高度']
        Edge_T = self['顶部边长']
        SJ = self['棱角缩进']

        YG_R_Out = self['烟管外半径 ']
        YG_R_In = self['烟管内半径 ']
        
  
        # 绘制模型

        bottom_cube = scale(Edge_B,Edge_B,High_B)*Cube()

        top_cube = translate(0,0,High_B)*scale(Edge_T,Edge_T,High_T)*Cube()

        cube_minus_B = rotate(Vec3(0,-1,0),angle*pi/180)*translate(-5000,-5000,-10000)*scale(10000,10000,10000)*Cube()

        cube_minus_T = translate(Edge_T/2-SJ,Edge_T/2-SJ,High_B)*scale(SJ,SJ,High_T)*Cube()

        # 底部斜面

        bottom_model = bottom_cube - cube_minus_B

        # 数组实现四个棱角缩进

       
        line = combine()
        for i in linspace(0,2*pi,5):
            line.append(rotate(i)*cube_minus_T)


        #位移至中点

        bottom_center = translate(-Edge_B/2,-Edge_B/2)*bottom_model
        
        top_center = translate(-Edge_T/2,-Edge_T/2)*top_cube

        mojor_model = top_center + bottom_center - line

        # 上色

        color_mojor = mojor_model.color(178/255,34/255,34/255,1)

        

        # 管道装饰
          #第一部分
        arc_1 = translate(-120,0)*scale(120,350)*Arc(0.5*pi)
        arc_2 = translate(-130,350)*translate(-35,0)*scale(35,35)*Arc(0.5*pi)
        arc_3 = translate(-165,420)*rotate(1.5*pi)*rotate(Vec3(1,0,0),pi)*scale(35,35)*Arc(0.5*pi)

       

        sect_A_0 = Section(arc_1,arc_2,arc_3,Vec2(-200,420),Vec2(-200,440),Vec2(-120,460),Vec2(0,460),Vec2(0,0))

        sect_A_1 = translate(-Edge_T/2,-Edge_T/2)*rotate(0.25*pi)*rotate(Vec3(-1,0,0),1.5*pi) *sect_A_0
        sect_A_2 = rotate(0.5*pi)*sect_A_1
        sect_A_3 = rotate(0.5*pi)*sect_A_2
        sect_A_4 = rotate(0.5*pi)*sect_A_3

        ZS_1 =translate(0,0,High_B+High_T-460)* Loft(translate(0,SJ)*sect_A_1,translate(SJ,SJ)*sect_A_1,translate(SJ,0)*sect_A_1,translate(-SJ,0)*sect_A_2,translate(-SJ,SJ)*sect_A_2,translate(0,SJ)*sect_A_2,translate(0,-SJ)*sect_A_3,translate(-SJ,-SJ)*sect_A_3,translate(-SJ,0)*sect_A_3,translate(SJ,0)*sect_A_4,translate(SJ,-SJ)*sect_A_4,translate(0,-SJ)*sect_A_4,translate(0,SJ)*sect_A_1).color(255/255,250/255,205/255,1)#ZS 装饰
        
          #第二部分

        arc_1 = translate(-45,0)*scale(35,35)*Arc(0.5*pi)
        arc_2 = translate(-45,70)*rotate(1.5*pi)*rotate(Vec3(1,0,0),pi)*scale(35,35)*Arc(0.5*pi)

       

        sect_B_0 = Section(arc_1,arc_2,Vec2(-120,70),Vec2(-120,90),Vec2(0,110),Vec2(0,0))

        sect_B_1 = translate(-Edge_T/2,-Edge_T/2)*rotate(0.25*pi)*rotate(Vec3(-1,0,0),1.5*pi) *sect_B_0
        sect_B_2 = rotate(0.5*pi)*sect_B_1
        sect_B_3 = rotate(0.5*pi)*sect_B_2
        sect_B_4 = rotate(0.5*pi)*sect_B_3

        ZS_2 =translate(0,0,High_T/2+High_B)* Loft(translate(0,SJ)*sect_B_1,translate(SJ,SJ)*sect_B_1,translate(SJ,0)*sect_B_1,translate(-SJ,0)*sect_B_2,translate(-SJ,SJ)*sect_B_2,translate(0,SJ)*sect_B_2,translate(0,-SJ)*sect_B_3,translate(-SJ,-SJ)*sect_B_3,translate(-SJ,0)*sect_B_3,translate(SJ,0)*sect_B_4,translate(SJ,-SJ)*sect_B_4,translate(0,-SJ)*sect_B_4,translate(0,SJ)*sect_B_1).color(255/255,250/255,205/255,1)#ZS 装饰
         

          #第三部分
        
        
        sect_C_0 = Section(Vec2(-50,0),Vec2(0,50))

        sect_C_1 = translate(-Edge_T/2,-Edge_T/2)*rotate(0.25*pi)*rotate(Vec3(-1,0,0),1.5*pi) *sect_C_0
        sect_C_2 = rotate(0.5*pi)*sect_C_1
        sect_C_3 = rotate(0.5*pi)*sect_C_2
        sect_C_4 = rotate(0.5*pi)*sect_C_3

        ZS_3 =translate(0,0,High_B)* Loft(translate(0,SJ)*sect_C_1,translate(SJ,SJ)*sect_C_1,translate(SJ,0)*sect_C_1,translate(-SJ,0)*sect_C_2,translate(-SJ,SJ)*sect_C_2,translate(0,SJ)*sect_C_2,translate(0,-SJ)*sect_C_3,translate(-SJ,-SJ)*sect_C_3,translate(-SJ,0)*sect_C_3,translate(SJ,0)*sect_C_4,translate(SJ,-SJ)*sect_C_4,translate(0,-SJ)*sect_C_4,translate(0,SJ)*sect_C_1).color(255/255,250/255,205/255,1)#ZS 装饰
        


        #烟管1
        sect_D_1 = Section(scale(YG_R_Out,YG_R_Out)*Arc())
        sect_D_2 = Section(scale(YG_R_In,YG_R_In)*Arc())
        sect_D_3 = Section(scale(YG_R_Out+70,YG_R_Out+70)*Arc())

        YG_A_surface = Loft(sect_D_1,translate(0,0,565)*sect_D_1)

        YG_A_inner = Loft(sect_D_2,translate(0,0,565)*sect_D_2)

        YG_A_top_0 = Loft(translate(0,0,515)*sect_D_3,translate(0,0,565)*sect_D_3)

        YG_A_top_1 = YG_A_top_0 -YG_A_surface

        major_YG_A = YG_A_surface - YG_A_inner +YG_A_top_1

        color_YG_A =translate(0,242,High_B+High_T)*major_YG_A.color(255/255,250/255,205/255,1)

        #烟管2
        sect_E_1 = Section(scale(YG_R_Out,YG_R_Out)*Arc())
        sect_E_2 = Section(scale(YG_R_In,YG_R_In)*Arc())
        sect_E_3 = Section(scale(YG_R_Out+70,YG_R_Out+70)*Arc())

        YG_B_surface = Loft(sect_E_1,translate(0,0,565)*sect_E_1)

        YG_B_inner = Loft(sect_E_2,translate(0,0,565)*sect_E_2)

        YG_B_top_0 = Loft(translate(0,0,515)*sect_E_3,translate(0,0,565)*sect_E_3)

        YG_B_top_1 = YG_B_top_0 -YG_B_surface

        major_YG_B = YG_B_surface - YG_B_inner +YG_B_top_1

        color_YG_B =translate(0,-242,High_B+High_T)*major_YG_B.color(255/255,250/255,205/255,1)



        #组合
        
        self['烟囱'] =Combine(color_mojor,ZS_1,ZS_2,ZS_3,color_YG_A,color_YG_B)

 
# 输出模型
if __name__ == "__main__":
    FinalGeometry = 烟囱()
    place(FinalGeometry)

